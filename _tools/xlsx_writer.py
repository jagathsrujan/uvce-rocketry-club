#!/usr/bin/env python3
"""
Minimal, dependency-free XLSX writer for the UVCE Rocketry workspace.

XLSX is an OPC (Open Packaging Conventions) ZIP containing XML parts, so it can be
written with nothing but the standard library. Avoids needing openpyxl, which is
unavailable in this environment.

Supports: multiple sheets, shared strings, formulas, column widths, bold/italic fonts,
fills, number formats, cell alignment, freeze panes, and autofilter.
"""

import re
import zipfile
from xml.sax.saxutils import escape

# ----------------------------------------------------------------------------- styles

FONTS = [
    {},                                                                   # 0 default
    {"b": True, "sz": 11},                                                # 1 bold
    {"b": True, "sz": 14},                                                # 2 title
    {"sz": 9, "i": True, "color": "FF666666"},                            # 3 note/italic grey
    {"b": True, "sz": 11, "color": "FFFFFFFF"},                           # 4 bold white
    {"b": True, "sz": 12, "color": "FF1F3864"},                           # 5 section header
]

FILLS = [
    {},                                                                   # 0 none
    {"fg": "FF1F3864"},                                                   # 1 dark blue
    {"fg": "FFD9E1F2"},                                                   # 2 light blue
    {"fg": "FFFFF2CC"},                                                   # 3 light amber (input)
    {"fg": "FFFCE4D6"},                                                   # 4 light orange (warning)
    {"fg": "FFE2EFDA"},                                                   # 5 light green (good)
]

BORDERS = [
    {},                                                                   # 0 none
    {"bottom": True},                                                     # 1 bottom hairline
]

NUMFMT = {
    "general": 0,
    "0.00": 2,
    "0.000": 3,
    "0.0%": 10,
    "#,##0": 3,
    "#,##0.00": 4,
}


def _col(n):
    """0-based column index -> spreadsheet letters."""
    s = ""
    n += 1
    while n:
        n, r = divmod(n - 1, 26)
        s = chr(65 + r) + s
    return s


class Sheet:
    def __init__(self, name, widths=None, freeze=None, autofilter=None):
        self.name = name
        self.rows = []          # list of list of cell dicts
        self.widths = widths or {}
        self.freeze = freeze
        self.autofilter = autofilter

    # -- writing -------------------------------------------------------------
    def add(self, cells):
        """cells: list of values, or dicts for styled cells."""
        row = []
        for c in cells:
            if isinstance(c, dict):
                row.append(c)
            else:
                row.append({"v": c})
        self.rows.append(row)

    def blank(self, n=1):
        for _ in range(n):
            self.rows.append([])

    # -- serialisation -------------------------------------------------------
    def _cell_xml(self, ref, cell):
        v = cell.get("v")
        f = cell.get("f")
        style = cell.get("s", 0)
        t = cell.get("t")

        attrs = f' r="{ref}"'
        if style:
            attrs += f' s="{style}"'

        if f:
            attrs += " t=\"str\"" if t == "str" else ""
            inner = f"<f>{escape(str(f))}</f>"
            if v is not None and not isinstance(v, str):
                inner += f"<v>{v}</v>"
            elif isinstance(v, str):
                inner += f"<v>{escape(v)}</v>"
            return f"<c{attrs}>{inner}</c>"

        if v is None or v == "":
            return f"<c{attrs}/>" if style else ""

        if isinstance(v, bool):
            return f'<c{attrs} t="b"><v>{1 if v else 0}</v></c>'
        if isinstance(v, (int, float)):
            return f"<c{attrs}><v>{v}</v></c>"

        # inline string (avoids shared-string table entirely)
        return f'<c{attrs} t="inlineStr"><is><t xml:space="preserve">{escape(str(v))}</t></is></c>'

    def xml(self):
        out = [
            '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>',
            '<worksheet xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main">',
        ]

        if self.widths:
            out.append("<cols>")
            for idx, w in sorted(self.widths.items()):
                out.append(f'<col min="{idx+1}" max="{idx+1}" width="{w}" customWidth="1"/>')
            out.append("</cols>")

        out.append("<sheetData>")
        for ri, row in enumerate(self.rows, start=1):
            if not row:
                continue
            out.append(f'<row r="{ri}">')
            for ci, cell in enumerate(row):
                if cell:
                    out.append(self._cell_xml(f"{_col(ci)}{ri}", cell))
            out.append("</row>")
        out.append("</sheetData>")

        if self.autofilter:
            out.append(f'<autoFilter ref="{self.autofilter}"/>')

        if self.freeze:
            # freeze panes: split at given cell
            pane = self.freeze
            col = re.match(r"([A-Z]+)", pane).group(1)
            row = int(re.search(r"(\d+)", pane).group(1))
            xsplit = sum((ord(ch) - 64) * (26 ** i) for i, ch in enumerate(reversed(col)))
            ysplit = row - 1
            out.append(
                "<sheetViews><sheetView workbookViewId=\"0\">"
                f'<pane xSplit="{xsplit}" ySplit="{ysplit}" topLeftCell="{pane}" activePane="bottomRight" state="frozen"/>'
                "</sheetView></sheetViews>"
            )

        out.append("</worksheet>")
        return "".join(out)


def write_xlsx(path, sheets):
    """sheets: list of Sheet objects."""
    n = len(sheets)

    def styles_xml():
        fonts = []
        for f in FONTS:
            a = []
            if f.get("b"):
                a.append('<b/>')
            if f.get("i"):
                a.append('<i/>')
            if f.get("sz"):
                a.append(f'<sz val="{f["sz"]}"/>')
            if f.get("color"):
                a.append(f'<color rgb="{f["color"]}"/>')
            fonts.append(f'<font>{"".join(a)}</font>')
        if not fonts:
            fonts = ["<font/>"]

        fills = ['<fill><patternFill patternType="none"/></fill>',
                 '<fill><patternFill patternType="gray125"/></fill>']
        for fl in FILLS[1:]:
            fills.append(
                f'<fill><patternFill patternType="solid">'
                f'<fgColor rgb="{fl["fg"]}"/><bgColor indexed="64"/>'
                f'</patternFill></fill>'
            )

        borders = ['<border><left/><right/><top/><bottom/><diagonal/></border>']
        for b in BORDERS[1:]:
            bottom = '<bottom style="thin"><color rgb="FFBFBFBF"/></bottom>' if b.get("bottom") else "<bottom/>"
            borders.append(f"<border><left/><right/><top/>{bottom}<diagonal/></border>")

        nf = ['<numFmt numFmtId="164" formatCode="#,##0.00"/>',
              '<numFmt numFmtId="165" formatCode="0.000"/>']
        cellxfs = ['<xf numFmtId="0" fontId="0" fillId="0" borderId="0" xfId="0"/>']
        # style ids must match the `s=` values used by the caller
        # (numFmtId, fontId, fillId, borderId, align?)
        combos = [
            (0,   0, 0, 0),                 # 0 default
            (0,   1, 0, 0),                 # 1 bold
            (0,   2, 0, 0),                 # 2 title
            (0,   3, 0, 0),                 # 3 italic grey
            (0,   4, 1, 0),                 # 4 bold white on dark blue (header row)
            (0,   5, 0, 0),                 # 5 section header (blue text)
            (0,   0, 0, 1),                 # 6 bottom border
            (164, 0, 0, 0),                 # 7 number 2dp
            (165, 0, 0, 0),                 # 8 number 3dp
            (0,   1, 2, 0, "left"),         # 9 bold on light blue, left
            (0,   0, 3, 0, "left"),         # 10 amber = INPUT cell
            (0,   0, 4, 0, "left"),         # 11 orange = warning
            (0,   0, 5, 0, "left"),         # 12 green = good
            (0,   0, 0, 0, "left"),         # 13 plain left
            (0,   0, 0, 0, "center"),       # 14 plain center
        ]
        for c in combos:
            numfmt, font, fill, border = c[0], c[1], c[2], c[3]
            align = ""
            if len(c) > 4:
                align = f'<alignment horizontal="{c[4]}"/>'
            cellxfs.append(
                f'<xf numFmtId="{numfmt}" fontId="{font}" fillId="{fill}" borderId="{border}" xfId="0"'
                f' applyFont="1" applyFill="1" applyBorder="1" applyNumberFormat="1">{align}</xf>'
            )

        return (
            '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
            '<styleSheet xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main">'
            f'<numFmts count="{len(nf)}">{"".join(nf)}</numFmts>'
            f'<fonts count="{len(fonts)}">{"".join(fonts)}</fonts>'
            f'<fills count="{len(fills)}">{"".join(fills)}</fills>'
            f'<borders count="{len(borders)}">{"".join(borders)}</borders>'
            '<cellStyleXfs count="1"><xf numFmtId="0" fontId="0" fillId="0" borderId="0"/></cellStyleXfs>'
            f'<cellXfs count="{len(cellxfs)}">{"".join(cellxfs)}</cellXfs>'
            "</styleSheet>"
        )

    def workbook_xml():
        parts = []
        for i, s in enumerate(sheets, start=1):
            parts.append(f'<sheet name="{escape(s.name)}" sheetId="{i}" r:id="rId{i}"/>')
        return (
            '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
            '<workbook xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main" '
            'xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships">'
            f'<sheets>{"".join(parts)}</sheets>'
            "</workbook>"
        )

    def content_types():
        over = "".join(
            f'<Override PartName="/xl/worksheets/sheet{i}.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.worksheet+xml"/>'
            for i in range(1, n + 1)
        )
        return (
            '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
            '<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">'
            '<Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>'
            '<Default Extension="xml" ContentType="application/xml"/>'
            '<Override PartName="/xl/workbook.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet.main+xml"/>'
            '<Override PartName="/xl/styles.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.styles+xml"/>'
            f"{over}</Types>"
        )

    def root_rels():
        return (
            '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
            '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
            '<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="xl/workbook.xml"/>'
            "</Relationships>"
        )

    def wb_rels():
        rels = "".join(
            f'<Relationship Id="rId{i}" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/worksheet" Target="worksheets/sheet{i}.xml"/>'
            for i in range(1, n + 1)
        )
        rels += (
            f'<Relationship Id="rId{n+1}" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/styles" Target="styles.xml"/>'
        )
        return (
            '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
            '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
            f"{rels}</Relationships>"
        )

    with zipfile.ZipFile(path, "w", zipfile.ZIP_DEFLATED) as z:
        z.writestr("[Content_Types].xml", content_types())
        z.writestr("_rels/.rels", root_rels())
        z.writestr("xl/workbook.xml", workbook_xml())
        z.writestr("xl/_rels/workbook.xml.rels", wb_rels())
        z.writestr("xl/styles.xml", styles_xml())
        for i, s in enumerate(sheets, start=1):
            z.writestr(f"xl/worksheets/sheet{i}.xml", s.xml())
    return path

"""Rasterize every printed page and report print geometry, fonts and sparse pages."""
import argparse
import json
from pathlib import Path
from PIL import Image
from pypdf import PdfReader
from extract import render


def main():
    cli = argparse.ArgumentParser(description=__doc__)
    cli.add_argument("pdf", type=Path)
    cli.add_argument("out", type=Path)
    cli.add_argument("--dpi", type=int, default=144)
    args = cli.parse_args()
    args.out.mkdir(parents=True, exist_ok=True)
    reports = []
    for n, page in enumerate(PdfReader(args.pdf).pages, 1):
        path = render(args.pdf, n, args.out / f"page-{n:04}", args.dpi)
        width, height = float(page.mediabox.width), float(page.mediabox.height)
        warnings = []
        if abs(width - 595.3) > 2 or abs(height - 841.9) > 2:
            warnings.append("Check A4 geometry")
        fonts = {}
        resources = page["/Resources"].get_object()
        font_map = resources["/Font"].get_object() if "/Font" in resources else {}
        for ref in font_map.values():
            font = ref.get_object()
            face = font["/DescendantFonts"][0].get_object() if "/DescendantFonts" in font else font
            descriptor = face.get("/FontDescriptor")
            embedded = bool(descriptor and any(k in descriptor.get_object() for k in ("/FontFile","/FontFile2","/FontFile3"))) or face.get("/Subtype") == "/Type3"
            fonts[str(font.get("/BaseFont", "?"))] = embedded
        if not fonts or not all(fonts.values()):
            warnings.append("Inspect missing text or unembedded fonts")
        with Image.open(path) as im:
            gray = im.convert("L")
            body = gray.crop((0, round(gray.height * .064), gray.width, round(gray.height * .94)))
            ink = body.point(lambda x: 255 if x < 175 else 0)
            rows = ink.getbbox()
            extent = round(rows[3] / body.height, 3) if rows else 0
        if extent < .58:
            warnings.append("Check unused lower page or an orphaned ending")
        reports.append(dict(page=n, png=path.name, size_pt=[width, height], embedded_fonts=fonts,
                            last_body_ink_fraction=extent, warnings=warnings))
    (args.out / "review.json").write_text(json.dumps(reports, ensure_ascii=False, indent=2), encoding="utf-8")
    for entry in reports:
        print(entry["page"], entry["warnings"])


if __name__ == "__main__":
    main()

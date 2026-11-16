"""Extract source text and page images, or crop a figure from a source page."""
import argparse
from pathlib import Path
import subprocess

from PIL import Image
from pypdf import PdfReader


def render(source, page, prefix, dpi):
    subprocess.run(["pdftoppm", "-f", str(page), "-l", str(page), "-r", str(dpi),
                    "-singlefile", "-png", str(source), str(prefix)], check=True)
    return prefix.with_suffix(".png")


def main():
    cli = argparse.ArgumentParser(description=__doc__)
    cli.add_argument("source", type=Path)
    cli.add_argument("out", type=Path)
    cli.add_argument("--first", type=int, default=1)
    cli.add_argument("--last", type=int)
    cli.add_argument("--dpi", type=int, default=135)
    cli.add_argument("--crop", type=float, nargs=4, metavar=("LEFT", "TOP", "RIGHT", "BOTTOM"),
                     help="One page only. Coordinates are fractions of the rendered page.")
    args = cli.parse_args()
    pdf = PdfReader(args.source)
    last = len(pdf.pages) if args.last is None else args.last
    if not (1 <= args.first <= last <= len(pdf.pages)) or args.dpi <= 0:
        cli.error("Check page range and positive DPI.")
    if args.crop:
        left, top, right, bottom = args.crop
        if args.first != last or not (0 <= left < right <= 1 and 0 <= top < bottom <= 1):
            cli.error("Cropping needs one page and an ordered rectangle within [0, 1].")
    args.out.mkdir(parents=True, exist_ok=True)
    for number in range(args.first, last + 1):
        prefix = args.out / f"page-{number:04}"
        text = pdf.pages[number - 1].extract_text() or ""
        prefix.with_suffix(".txt").write_text(text, encoding="utf-8")
        path = render(args.source, number, prefix, args.dpi)
        if args.crop:
            with Image.open(path) as im:
                bounds = [round(v * dim) for v, dim in zip(args.crop, (im.width, im.height) * 2)]
                im.crop(bounds).save(args.out / f"figure-{number:04}.png")
        if len(text.strip()) < 25:
            print(f"Page {number}: inspect raster for scanned or image-only text.")


if __name__ == "__main__":
    main()

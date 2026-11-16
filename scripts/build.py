"""Print a local teaching handout with Chromium and check browser layout."""
import argparse
import html
import json
from pathlib import Path
import os
import tempfile

from playwright.sync_api import sync_playwright


def main():
    cli = argparse.ArgumentParser(description=__doc__)
    cli.add_argument("source", type=Path)
    cli.add_argument("pdf", type=Path)
    cli.add_argument("--browser", help="Installed Chrome/Chromium executable")
    args = cli.parse_args()
    source = args.source.resolve(strict=True)
    dest = args.pdf.resolve()
    if dest.suffix.lower() != ".pdf" or source == dest:
        cli.error("Choose a separate PDF destination.")
    dest.parent.mkdir(parents=True, exist_ok=True)
    with sync_playwright() as pw:
        browser = pw.chromium.launch(executable_path=args.browser)
        page = browser.new_page(viewport={"width": 673, "height": 980})
        failures = []
        page.on("requestfailed", lambda req: failures.append(req.url))
        page.on("pageerror", lambda error: failures.append(str(error)))
        page.emulate_media(media="print")
        page.goto(source.as_uri(), wait_until="networkidle")
        digit_rules = Path(__file__).with_name("persian-digits.js").read_text(encoding="utf-8")
        page.evaluate(digit_rules)
        page.evaluate("document.fonts.ready")
        issues = page.evaluate("""() => {
          const issues = [];
          const body = document.body.getBoundingClientRect();
          for (const el of document.querySelectorAll('main *, article *, img')) {
            const rect = el.getBoundingClientRect();
            if (!rect.width) continue;
            if (rect.right > body.right + 2 || rect.left < body.left - 2 ||
                (el.clientWidth && el.scrollWidth > el.clientWidth + 2))
              issues.push('Horizontal overflow: ' + el.tagName + ' ' + el.textContent.slice(0,45));
            if (el.tagName === 'IMG' && !el.naturalWidth) issues.push('Missing image: ' + el.src);
          }
          return issues;
        }""")
        if failures or issues:
            raise SystemExit("\n".join(failures + issues))
        direction = "rtl" if page.locator("html").get_attribute("dir") == "rtl" else "ltr"
        title = html.escape(page.title())
        bar = f'width:100%;margin:0 16mm;font:8px Tahoma, sans-serif;color:#46605d;direction:{direction};'
        header = f'<div style="{bar}">{title}</div>'
        footer = f'<div style="{bar}text-align:end"><span dir="ltr"><span class="pageNumber"></span> / <span class="totalPages"></span></span></div>'
        # Page margin boxes share the document's web fonts in Chromium 131+.
        use_margin_boxes = int(browser.version.split(".")[0]) >= 131
        if use_margin_boxes:
            start, end = ("right", "left") if direction == "rtl" else ("left", "right")
            family = page.locator("body").evaluate("(el) => getComputedStyle(el).fontFamily")
            style = f"font: 8pt {family}; color: #46605d;"
            page_title = json.dumps(page.title(), ensure_ascii=False)
            margin_css = f"""@page {{
                @top-{start} {{ content: {page_title}; {style} direction: {direction}; }}
                @bottom-{end} {{ content: counter(page) ' / ' counter(pages); {style} direction: ltr; }}
            }}"""
            page.add_style_tag(content=margin_css)
        with tempfile.NamedTemporaryFile(dir=dest.parent, suffix=".pdf", delete=False) as tmp:
            staging = Path(tmp.name)
        try:
            page.pdf(path=staging, format="A4", prefer_css_page_size=True, print_background=True,
                     display_header_footer=not use_margin_boxes, header_template=header, footer_template=footer,
                     margin={"top":"19mm","bottom":"18mm","left":"16mm","right":"16mm"})
            os.replace(staging, dest)
        finally:
            staging.unlink(missing_ok=True)
        browser.close()


if __name__ == "__main__":
    main()

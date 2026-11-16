# Install and run

Place the whole persian-educational-designer directory under ~/.agents/skills/ on the user account. Start a new chat in any project, attach or identify the raw source and, if available, the style reference. Invoke `$persian-educational-designer` or ask for a lecture handout in natural language. With no reference or explicit language instruction the raw source language determines the output.

Use Python 3.10+, install the packages in requirements.txt with that interpreter, and install Poppler with pdftoppm on PATH. Use `python -m playwright install chromium` or pass an existing Chromium/Chrome path with --browser. A local font covering the target script is required. Persian uses the bundled Vazirmatn v33.003 Regular and Bold (SIL OFL, license in templates/fonts/OFL.txt); use a local math font for MathML. Avoid remote fonts and remote diagrams.

PowerShell example, run from a new course project:

```powershell
$skill = Join-Path $env:USERPROFILE '.agents/skills/persian-educational-designer'
python -m pip install -r "$skill/requirements.txt"
python -m playwright install chromium
python "$skill/scripts/extract.py" slides.pdf work/source
Copy-Item -Recurse "$skill/templates" work/lesson
# Author work/lesson/lesson.html, set lang/dir and adapt the copied CSS.
python "$skill/scripts/build.py" work/lesson/lesson.html handout.pdf
python "$skill/scripts/review.py" handout.pdf work/review
```

The same scripts accept POSIX paths. For a selected range use --first 5 --last 8. To reuse a diagram crop from the actual page at high resolution, use --first 5 --last 5 --dpi 240 --crop 0.2 0.15 0.85 0.72. Fractions run from the top left of the rendered page. Preserve its legend and units. For vector redraws retain values, labels, topology and source page, and mark simplified examples. Use separate working directories per input/run.

## Engineering choices

pypdf reads the text layer, Poppler independently rasterizes source and final pages, Pillow handles crops and print diagnostics. Chromium via Playwright shapes complex scripts, isolates bidirectional runs, prints SVG and native MathML and paginates flowing HTML. ReportLab would require more custom flow and script handling. PyMuPDF or pdfplumber can help recover difficult layouts but are optional; the rendered source is the authority for visual information. The language/content transformation is performed by the invoking agent, with no model API dependency.
Adapt snippets from templates/components.html for semantic tables, native MathML, SVG and callouts. It is a fragment library; print the authored lesson.html.

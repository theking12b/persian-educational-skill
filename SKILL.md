---
name: persian-educational-designer
description: Transform academic slides or lecture PDFs into source-grounded teaching handouts in the reference handout's language, with special support for Persian RTL, worked examples, A4 layout and visual PDF review. Use for course notes, slide-to-handout conversion, and Persian requests such as تبدیل اسلاید به جزوه.
---

# Educational handout design

Resolve package paths relative to this skill. Write working files in the user's project and preserve inputs.

1. Identify the raw subject source, style reference and page scope. Use the user's requested language first, otherwise the designated reference handout's main language, otherwise the raw source language. With mixed references use the one closest to the assignment; record the choice. Identify the script direction independently. For Persian follow the mixed-script typography rules below.
2. Run `scripts/extract.py` on the raw PDF. For native slides first export slides and any relevant speaker notes using the presentation application. Read extracted text alongside page images, especially cumulative diagrams, equations and tables.
3. Follow [teaching.md](references/teaching.md) to map source coverage and teach a beginner. The reference models teaching and design; scientific claims come from the course source or clearly identified derivations.
4. Apply [design-system.md](references/design-system.md). Copy the starter HTML, CSS and adjacent fonts directory into the project, set document language, direction and title, and author the lesson. Typeset mathematical quotients as stacked fractions, including inline math and numerical substitutions. See [usage.md](references/usage.md) for commands.
5. Print with `scripts/build.py`, rasterize **every output page** with `scripts/review.py`, then follow [quality.md](references/quality.md). Correct the source and repeat the print/review cycle. Deliver the verified PDF, coverage summary and any unresolved source ambiguity.

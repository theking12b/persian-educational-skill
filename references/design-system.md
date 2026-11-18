# Design system derived from the reference handouts

## Evidence

Six Opus handouts, all from a data structures course, supplied the style evidence. Eight separate landscape decks supplied raw material. Five rendered positions per file (opening three pages, middle, final page) were juxtaposed. Inspecting page 3 of reference 03 at reading size clarified the spacing and example structure. This is one course family; use its principles across subjects and adapt diagrams to the discipline.

| Handout | Pages | Specific evidence and transferable decision |
|---|---:|---|
| 03 Data Structures and Memory | 23 | Page 3 moves from a plain definition through a 500-book analogy to labeled memory cells. Map familiar objects onto technical roles, then show the real representation. |
| 04 Asymptotic Analysis | 19 | Page 9 uses notation, a comparison table and an interval graphic. Read a symbol aloud and attach its conditions. |
| 05 Algorithm Analysis | 26 | Page 13 pairs code and a colored computation grid. Show the intermediate state a reader needs to understand the code. |
| 06 Lists, Stacks, Queues, Deques | 50 | Page 2 uses two contents columns. Page 25 combines code and a compact comparison. A short summary fragment spills onto page 50. Inspect chapter endings after print. |
| 07 Sorting, Insertion and Bubble | 25 | Pages 3 and 12 combine small comparable inputs, steps and implementation. Hold the input constant across alternatives. |
| 08 Merge Sort and Quick Sort | 32 | Page 3 shows successive arrays; page 16 groups practice around the operation. Explain why each state changes. |

Raw inventory (filename, topic, page count): C11 mathematical review 46; C12 C++ 81; C13 induction 43; C21 structures 41; C22 asymptotics 52; C3 algorithm analysis 97; C4 lists 234; C5 sorting 101. Repeated slide navigation, logos and progressive animation states are presentation furniture. Preserve the changes across animation states when they carry information.

## Composition and type

The recurring sequence is a subject-specific cover illustration, a contents page, numbered sections, one-column teaching pages and an exam review. Scale this to the lesson. Open a short unit with its motivating question. For long notes provide navigable contents or verified final page references. Recap the conditions that change an answer; connect the conclusion of a section to the next question.

The body on reference 03 page 3 spans about 86% of the page width. Body copy is dark on white, with approximately two glyph heights between baselines. Reference PDF font resources include Vazirmatn, JetBrains Mono and KaTeX faces. Raw PDF font operands are transformed and are not final print point sizes. The starter uses **adapted print tokens**: A4, 16 mm sides, 11.2 pt body at 1.8 line height, 23/16/13 pt title/section/subsection, 9 pt captions. Use regular body weight and bold only the operative term. Keep heading-to-text spacing smaller than spacing between concepts.

## Semantic components

Teal section headings and thin rules orient the reader. Use a light interior and an inline-start accent for a definition (blue), worked example (green), condition (amber) or misconception (red). Use a subtle 2.5 mm radius for instructional callouts. Apply the panel class selectively to an intentionally framed diagram. Keep tables and their cell grid rectangular with square outer corners. Give each a textual label in the output language. Keep ordinary explanation on white. Reserve tables for comparison on a common axis, with units, meaningful row/column headers and aligned values. Use vector traces for state changes, plots with named axes for quantitative relations and aligned lines of reasoning for proofs. Place captions beside their figures in reading order; state what to notice.

## Language-sensitive typography

Set HTML lang and dir for the output language. Use CSS logical edges. Use the bundled Vazirmatn Regular and Bold for Persian prose, headings, captions, and labels. Keep the fonts directory beside print.css. Inspect the PDF font list for both used weights. Optional licensed fonts may be supplied with local @font-face URLs. Use real Persian ی and ک and preserve lexical ZWNJ (می‌شود). Introduce an English term once and wrap it and its internal punctuation in an LTR bdi. Keep code, addresses, mathematical operands and array indices LTR even within RTL tables. Decide column order according to meaning. Use native MathML with an appropriate installed math face, or a verified local vector equation. A surrounding Persian sentence explains variables and direction. Use Persian digits (۰۱۲۳۴۵۶۷۸۹) in Persian prose, headings, captions and source-page references. Use ASCII digits (0123456789) in equations (including inline math), table cells, diagram labels, code and technical identifiers. Mark inline expressions with math or an LTR bdi so the printer can distinguish «۱۲ رأس» from n = 12. Table captions follow the prose rule. Mark a verbatim literal whose exact Unicode spelling matters with data-digits="preserve". For LTR lessons use the language's normal prose face, line height and punctuation; keep semantic accents on the start edge.

## Fractions and numerical substitution

Typeset every mathematical quotient as a stacked fraction with a horizontal bar, including inline expressions, table equations and worked numerical substitutions. Use MathML mfrac or LaTeX frac in a supported local math renderer. For example, (105 - 120)/15 becomes an mfrac with the entire difference in its numerator and 15 in its denominator. Keep decimal numbers as decimals and code operators faithful to executable syntax. Group numerator and denominator explicitly before rendering; preserve signs and operator precedence. Inspect inline fractions for baseline alignment and adequate line spacing.

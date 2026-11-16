# Review the printed artifact

Record output version, page count, page-to-section mapping, scientific checks, visual findings, repairs and the final rerun. Verify that the actual PDF opens. A successful print or a clean JSON report is only the start.

1. Check every in-scope source page against the coverage ledger. Verify each copied value, graph edge, axis, table unit and equation independently. Document additions and source ambiguities.
2. Inspect review.json for A4 geometry, empty or lightly occupied pages and embedded fonts. Compare actual embedded face names with the intended body, math and code faces. Unexpected fallback needs review even when embedded. Confirm header, page number and last line on every raster.
3. Open every page at reading resolution. Check Persian joining, ZWNJ, punctuation and mixed terms, code indentation, minus signs, exponents and fractions. Inspect arrows and labels at full size. Verify each caption follows the right figure and repeated table headers retain their columns.
4. Compare adjacent pages at thumbnail scale for hierarchy, continuity and empty lower areas. Keep short figures and callouts intact. Split a long callout or table at a semantic boundary; repeat table headers. Move headings with the first paragraph. Avoid fixed-height clipping and blanket page breaks. Rebalance a near-empty ending before reducing body size.
5. Correct HTML/CSS or content, print again and rasterize the new PDF into a fresh directory. Review all changed pages and neighbors, and verify total pages and coverage again. Record any item whose correctness could not be resolved from the source.

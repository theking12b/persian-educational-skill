// Shape visible digits for print without modifying links, SVG geometry or markup.
() => {
  if (!document.documentElement.matches(":lang(fa)")) return;
  const technical = "td, th, math, .math, .equation, .ltr, [dir=ltr], code, pre, kbd, samp, svg, [data-digits=latin]";
  const walker = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT);
  while (walker.nextNode()) {
    const node = walker.currentNode;
    const parent = node.parentElement;
    if (!parent || !parent.matches(":lang(fa)") ||
        parent.closest("script, style, textarea, [data-digits=preserve]")) continue;
    const digits = parent.closest(technical) ? "0123456789" : "۰۱۲۳۴۵۶۷۸۹";
    node.data = node.data.replace(/[0-9۰-۹٠-٩]/g, ch =>
      digits[ch.charCodeAt(0) & 15]);
  }
}

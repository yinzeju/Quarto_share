// Run with playwright-cli run-code --filename after opening this template's slides.
async (page) => {
  const failures = [];
  page.on('pageerror', error => failures.push(error.message));
  await page.route(/^https?:\/\/(?!127\.0\.0\.1|localhost)/, route => route.abort());
  await page.reload();
  await page.waitForFunction(() => window.Reveal && Reveal.isReady());
  await page.waitForFunction(() => window.mathReady === true);
  const math = await page.evaluate(() => ({total:document.querySelectorAll('span.math').length, rendered:document.querySelectorAll('span.math .katex').length}));
  if (math.total === 0 || math.total !== math.rendered) throw new Error('Mathematics did not render completely');
  await page.evaluate(() => document.fonts.ready);
  await page.setViewportSize({width:1280, height:720});
  const slides = await page.evaluate(() => Reveal.getSlides().map((slide,index) => ({
    index, id:slide.id, title:slide.querySelector('h2')?.textContent,
    scroll:slide.classList.contains('long-derivation')
  })));
  if (slides.length !== 13 || slides.some(slide => !slide.title)) throw new Error('Unexpected logical slide structure');
  const pages = [];
  let gifChanged = false;
  for (const slide of slides) {
    await page.evaluate(index => Reveal.slide(index), slide.index);
    await page.evaluate(() => new Promise(resolve => requestAnimationFrame(() => requestAnimationFrame(resolve))));
    await page.waitForFunction(() => [...document.querySelectorAll('.present img')].every(image => image.complete && image.naturalWidth > 0));
    const metrics = await page.evaluate(() => {
      const slide = Reveal.getCurrentSlide();
      const bounds = slide.getBoundingClientRect();
      const source = slide.querySelector('.source')?.getBoundingClientRect();
      const content = [...slide.querySelectorAll('p,table,.katex-display,img,pre')].filter(node => !node.closest('.source,.notes'));
      const bottom = Math.max(...content.map(node => node.getBoundingClientRect().bottom));
      const wideMath = [...slide.querySelectorAll('.katex-display .katex')].filter(node => node.getBoundingClientRect().right > bounds.right - 12).length;
      return {height:slide.clientHeight, scrollHeight:slide.scrollHeight,
        contentPastFooter:source ? bottom > source.top - 6 : bottom > bounds.bottom - 13,
        wideMath, mathErrors:slide.querySelectorAll('.katex-error').length};
    });
    const number = String(slide.index+1).padStart(2,'0');
    await page.screenshot({path:'output/playwright/weekly-'+number+'.png'});
    if (slide.scroll) {
      await page.evaluate(() => {const slide=Reveal.getCurrentSlide(); slide.scrollTop=slide.scrollHeight;});
      await page.screenshot({path:'output/playwright/weekly-'+number+'-bottom.png'});
      await page.evaluate(() => {Reveal.getCurrentSlide().scrollTop=0;});
    }
    if (slide.id === 'gif-and-image') {
      const image = page.locator('.present img').first();
      const first = await image.screenshot();
      await page.waitForTimeout(300);
      gifChanged = !first.equals(await image.screenshot());
    }
    pages.push({...slide, ...metrics});
  }
  await page.evaluate(() => Reveal.slide(0));
  return {logicalSlides:slides.length, math, pages, gifChanged, pageErrors:failures};
}

-- Keep TeX intact for the locally embedded KaTeX runtime after cross-references.
function Math(el)
  if FORMAT:match('html') or FORMAT:match('revealjs') then
    local mode = el.mathtype == 'DisplayMath' and 'display' or 'inline'
    local tex = el.text:gsub('&', '&amp;'):gsub('<', '&lt;'):gsub('>', '&gt;')
    return pandoc.RawInline('html', '<span class="math ' .. mode .. '">' .. tex .. '</span>')
  end
end

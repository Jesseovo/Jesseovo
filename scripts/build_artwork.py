"""Maintain the profile typing animation, compact link cards and pixel still life.

The cat animation is built separately by animate_cat.py.
"""
from pathlib import Path
from html import escape
ROOT = Path(__file__).resolve().parents[1]

TYPING = r'''<svg xmlns="http://www.w3.org/2000/svg" width="600" height="48" viewBox="0 0 600 48" role="img" aria-labelledby="title">
<title id="title">Welcome to my little corner of GitHub</title>
<style>text{font-family:'SFMono-Regular',Consolas,'Liberation Mono',monospace}
.line{opacity:0;animation:show 20s steps(1,end) infinite}
.line-0{opacity:1}.line-1{animation-delay:5s}.line-2{animation-delay:10s}.line-3{animation-delay:15s}
.reveal{animation:type 20s steps(36,end) infinite;transform-box:fill-box;transform-origin:left}
.reveal-1{animation-delay:5s}.reveal-2{animation-delay:10s}.reveal-3{animation-delay:15s}
@keyframes show{0%,24.99%{opacity:1}25%,100%{opacity:0}}
@keyframes type{0%{transform:scaleX(0)}12%,20.25%{transform:scaleX(1)}25%,100%{transform:scaleX(0)}}
@media(prefers-reduced-motion:reduce){.line,.reveal{animation:none}.line{opacity:0}.line-0{opacity:1}}
</style>
<g class="line line-0">
<clipPath id="reveal-0"><rect class="reveal reveal-0" x="111.0" y="0" width="388" height="48"/></clipPath>
<text x="111.0" y="30" font-size="16" letter-spacing=".2" fill="#58a6ff" clip-path="url(#reveal-0)">Welcome to my little corner of GitHub.</text>
</g>
<g class="line line-1">
<clipPath id="reveal-1"><rect class="reveal reveal-1" x="96.0" y="0" width="418" height="48"/></clipPath>
<text x="96.0" y="30" font-size="16" letter-spacing=".2" fill="#58a6ff" clip-path="url(#reveal-1)">Making useful things. Keeping it playful.</text>
</g>
<g class="line line-2">
<clipPath id="reveal-2"><rect class="reveal reveal-2" x="126.0" y="0" width="358" height="48"/></clipPath>
<text x="126.0" y="30" font-size="16" letter-spacing=".2" fill="#58a6ff" clip-path="url(#reveal-2)">A little curiosity goes a long way.</text>
</g>
<g class="line line-3">
<clipPath id="reveal-3"><rect class="reveal reveal-3" x="94.2" y="0" width="420" height="48"/></clipPath>
<text x="94.2" y="30" font-size="16" letter-spacing=".2" fill="#58a6ff" clip-path="url(#reveal-3)">Aware of my shortcomings, I keep striving.</text>
</g>
</svg>
'''

CORNER_LIGHT = r'''<svg xmlns="http://www.w3.org/2000/svg" width="880" height="168" viewBox="0 0 880 168" role="img" aria-labelledby="title">
<title id="title">A quiet pixel corner with plants, books, coffee and a candle</title>
<style>text{font-family:'SFMono-Regular',Consolas,'Liberation Mono',monospace}
.plant{transform-origin:264px 131px;animation:sway 8s ease-in-out infinite}
.flower{transform-origin:508px 131px;animation:sway 7s ease-in-out -3s infinite}
.steam{animation:steam 4s ease-in-out infinite}
.sparkle{animation:twinkle 5s ease-in-out infinite}
.flame{transform-origin:590px 103px;animation:flicker 2s steps(2,end) infinite}
@keyframes sway{0%,100%{transform:rotate(-1deg)}50%{transform:rotate(1deg)}}
@keyframes steam{0%,100%{opacity:.25;transform:translateY(2px)}50%{opacity:.8;transform:translateY(-3px)}}
@keyframes twinkle{0%,100%{opacity:.35}50%{opacity:1}}
@keyframes flicker{0%,100%{transform:scale(1,1)}50%{transform:scale(.8,1.12)}}
@media(prefers-reduced-motion:reduce){.plant,.flower,.steam,.sparkle,.flame{animation:none}}
</style>

<g shape-rendering="crispEdges">
  <path d="M194 131h492v4H194zM210 135h460v5H210z" fill="#f2eee7"/>
  <path d="M210 140h460v2H210zM228 146h55v2h-55zM616 146h37v2h-37z" fill="#f8f6f2"/>
  <g class="plant">
    <path d="M247 104h34v6h-34zM251 110h26v21h-26z" fill="#c7866f"/>
    <path d="M251 110h7v21h-7z" fill="#dca58b"/>
    <path d="M262 70h4v34h-4z" fill="#67876f"/>
    <path d="M248 65h12v4h4v12h-12v-4h-4zM268 77h16v4h4v9h-16v-4h-4z" fill="#87a78f"/>
    <path d="M248 87h11v4h5v9h-12v-4h-4zM266 56h9v4h5v10h-10v4h-4z" fill="#b4c6a4"/>
  </g>
  <g>
    <path d="M312 119h47v12h-47z" fill="#a3bdce"/>
    <path d="M317 122h39v5h-39z" fill="#f0e6d5"/>
    <path d="M319 107h43v11h-43z" fill="#d4a28e"/>
    <path d="M324 110h35v4h-35z" fill="#f0e6d5"/>
    <path d="M326 101h28v6h-28z" fill="#f0e6d5"/>
  </g>
  <g>
    <path d="M402 103h34v24h-4v4h-26v-4h-4z" fill="#e2ebee"/>
    <path d="M436 107h10v16h-10v-4h6v-8h-6z" fill="#a3bdce"/>
    <path d="M406 103h26v4h-26z" fill="#7d6354"/>
    <path d="M398 131h43v3h-43z" fill="#e5dfd5"/>
    <g class="steam" fill="#e5dfd5">
      <path d="M410 91h3v7h-3zM407 85h3v6h-3zM410 79h3v6h-3z"/>
      <path d="M424 87h3v8h-3zM427 81h3v6h-3zM424 75h3v6h-3z"/>
    </g>
  </g>
  <g class="flower">
    <path d="M506 81h3v29h-3zM496 93h10v4h-10zM509 100h9v4h-9z" fill="#67876f"/>
    <path d="M503 67h9v8h-9zM503 83h9v7h-9zM495 75h8v8h-8zM512 75h8v8h-8z" fill="#efd6c4"/>
    <path d="M503 75h9v8h-9z" fill="#d6b36e"/>
    <path d="M494 110h27v5h-27zM498 115h19v16h-19z" fill="#f0e6d5"/>
    <path d="M498 115h5v16h-5z" fill="#c5bba9"/>
  </g>
  <g>
    <path d="M582 113h17v18h-17zM585 108h11v5h-11z" fill="#d5bfa3"/>
    <path d="M588 102h3v6h-3z" fill="#897a6a"/>
    <path class="flame" d="M588 91h4v5h3v6h-9v-6h2z" fill="#d9aa68"/>
    <path d="M576 131h29v3h-29z" fill="#e5dfd5"/>
  </g>
  <g class="sparkle" fill="#d3c3a5">
    <path d="M218 59h2v5h5v2h-5v5h-2v-5h-5v-2h5z"/>
    <path d="M629 69h2v4h4v2h-4v4h-2v-4h-4v-2h4z"/>
  </g>
  <path d="M338 73h3v3h-3zM568 58h3v3h-3zM649 109h3v3h-3z" fill="#e5dfd5"/>
</g>

</svg>
'''

CORNER_DARK = r'''<svg xmlns="http://www.w3.org/2000/svg" width="880" height="168" viewBox="0 0 880 168" role="img" aria-labelledby="title">
<title id="title">A quiet pixel corner with plants, books, coffee and a candle</title>
<style>text{font-family:'SFMono-Regular',Consolas,'Liberation Mono',monospace}
.plant{transform-origin:264px 131px;animation:sway 8s ease-in-out infinite}
.flower{transform-origin:508px 131px;animation:sway 7s ease-in-out -3s infinite}
.steam{animation:steam 4s ease-in-out infinite}
.sparkle{animation:twinkle 5s ease-in-out infinite}
.flame{transform-origin:590px 103px;animation:flicker 2s steps(2,end) infinite}
@keyframes sway{0%,100%{transform:rotate(-1deg)}50%{transform:rotate(1deg)}}
@keyframes steam{0%,100%{opacity:.25;transform:translateY(2px)}50%{opacity:.8;transform:translateY(-3px)}}
@keyframes twinkle{0%,100%{opacity:.35}50%{opacity:1}}
@keyframes flicker{0%,100%{transform:scale(1,1)}50%{transform:scale(.8,1.12)}}
@media(prefers-reduced-motion:reduce){.plant,.flower,.steam,.sparkle,.flame{animation:none}}
</style>

<g shape-rendering="crispEdges">
  <path d="M194 131h492v4H194zM210 135h460v5H210z" fill="#242b34"/>
  <path d="M210 140h460v2H210zM228 146h55v2h-55zM616 146h37v2h-37z" fill="#161c24"/>
  <g class="plant">
    <path d="M247 104h34v6h-34zM251 110h26v21h-26z" fill="#c7866f"/>
    <path d="M251 110h7v21h-7z" fill="#dca58b"/>
    <path d="M262 70h4v34h-4z" fill="#577a61"/>
    <path d="M248 65h12v4h4v12h-12v-4h-4zM268 77h16v4h4v9h-16v-4h-4z" fill="#8eb39a"/>
    <path d="M248 87h11v4h5v9h-12v-4h-4zM266 56h9v4h5v10h-10v4h-4z" fill="#b6d0ac"/>
  </g>
  <g>
    <path d="M312 119h47v12h-47z" fill="#7396b3"/>
    <path d="M317 122h39v5h-39z" fill="#d5c8b5"/>
    <path d="M319 107h43v11h-43z" fill="#d4a28e"/>
    <path d="M324 110h35v4h-35z" fill="#d5c8b5"/>
    <path d="M326 101h28v6h-28z" fill="#d5c8b5"/>
  </g>
  <g>
    <path d="M402 103h34v24h-4v4h-26v-4h-4z" fill="#becbd5"/>
    <path d="M436 107h10v16h-10v-4h6v-8h-6z" fill="#7396b3"/>
    <path d="M406 103h26v4h-26z" fill="#7d6354"/>
    <path d="M398 131h43v3h-43z" fill="#3b424b"/>
    <g class="steam" fill="#3b424b">
      <path d="M410 91h3v7h-3zM407 85h3v6h-3zM410 79h3v6h-3z"/>
      <path d="M424 87h3v8h-3zM427 81h3v6h-3zM424 75h3v6h-3z"/>
    </g>
  </g>
  <g class="flower">
    <path d="M506 81h3v29h-3zM496 93h10v4h-10zM509 100h9v4h-9z" fill="#577a61"/>
    <path d="M503 67h9v8h-9zM503 83h9v7h-9zM495 75h8v8h-8zM512 75h8v8h-8z" fill="#eac8b5"/>
    <path d="M503 75h9v8h-9z" fill="#d6b36e"/>
    <path d="M494 110h27v5h-27zM498 115h19v16h-19z" fill="#d5c8b5"/>
    <path d="M498 115h5v16h-5z" fill="#c5bba9"/>
  </g>
  <g>
    <path d="M582 113h17v18h-17zM585 108h11v5h-11z" fill="#d5bfa3"/>
    <path d="M588 102h3v6h-3z" fill="#897a6a"/>
    <path class="flame" d="M588 91h4v5h3v6h-9v-6h2z" fill="#d9aa68"/>
    <path d="M576 131h29v3h-29z" fill="#3b424b"/>
  </g>
  <g class="sparkle" fill="#d4b27d">
    <path d="M218 59h2v5h5v2h-5v5h-2v-5h-5v-2h5z"/>
    <path d="M629 69h2v4h4v2h-4v4h-2v-4h-4v-2h4z"/>
  </g>
  <path d="M338 73h3v3h-3zM568 58h3v3h-3zM649 109h3v3h-3z" fill="#3b424b"/>
</g>

</svg>
'''

PROJECTS = [
    ("last30days", "last30days-skill-cn", "Web research"),
    ("papercash", "PaperCash", "Papers & citations"),
]

CONTACTS = [
    ("email", "Email", "Jesseovo1219@gmail.com"),
    ("website", "Website", "jesseovo.qzz.io"),
]


def compact_card(item, theme, icon_builder):
    slug, name, description = item
    dark = theme == "dark"
    # Trim unused trailing space in the shorter right column so the visible
    # artwork and text, rather than the image canvases, sit around the centre.
    width = 176 if slug in ("papercash", "website") else 208
    ink, muted = ("#d4ded9", "#8b9f95") if dark else ("#36463e", "#7a887f")
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="60" viewBox="0 0 {width} 60" role="img" aria-labelledby="title desc">
<title id="title">{escape(name)}</title>
<desc id="desc">{escape(description)}</desc>
{icon_builder(slug,dark)}
<g font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Arial, sans-serif">
<text x="80" y="26" font-size="12.5" font-weight="500" fill="{ink}">{escape(name)}</text>
<text x="80" y="43" font-size="10.5" fill="{muted}">{escape(description)}</text>
</g>
</svg>
'''


def project_icon(slug, dark=False):
    """Small transparent pixel vignettes for the compact project links."""
    outline = "#829e97" if dark else "#78918a"
    paper = "#e9dfc8" if dark else "#eee7d5"
    if slug == "last30days":
        icon = f'''
<path d="M5 4h20v2h2v13H3V6h2z" fill="{outline}"/>
<path d="M5 6h20v11H5z" fill="#d0dfd6"/>
<path d="M6 7h18v9H6z" fill="#30484d"/>
<path d="M8 9h12v1H8zM8 12h2v2H8z" fill="#c0d4ca"/>
<path d="M12 12h9v1h-9zM12 14h6v1h-6z" fill="#96b3bb"/>
<path d="M13 19h4v3h-4zM9 22h12v2H9z" fill="{outline}"/>
<path d="M24 16h5v1h1v5h-1v1h-5v-1h-1v-5h1zM29 22h2v2h-2zM31 24h1v2h-1z" fill="#819c7c"/>
<path d="M25 17h3v1h1v3h-1v1h-3v-1h-1v-3h1z" fill="#d9e6d3"/>
<path d="M25 18h2v1h-2z" fill="#f4f6e9"/>
<path d="M1 19h3v4H1z" fill="#d6a79a"/>
'''
    else:
        icon = f'''
<path d="M11 1h10v12H11z" fill="#b6a99a"/>
<path d="M12 2h8v10h-8z" fill="{paper}"/>
<path d="M14 4h4v1h-4zM14 7h4v1h-4z" fill="#b6a99a"/>
<path d="M22 5h6v2h2v10h-8z" fill="#9bb0a5"/>
<path d="M23 6h3v3h3v7h-6z" fill="#d6e2d5"/>
<path d="M2 13h4v-1h7v2h3v2h1v9h-3v-1H5v-2H2zM32 13h-4v-1h-7v2h-3v2h-1v9h3v-1h9v-2h3z" fill="#8da4b1"/>
<path d="M5 14h7v1h3v8h-3v-1H5zM29 14h-7v1h-3v8h3v-1h7z" fill="{paper}"/>
<path d="M7 16h5v1H7zM7 19h6v1H7zM22 16h5v1h-5zM21 19h6v1h-6z" fill="#bbb49e"/>
<path d="M23 21h2v5h-1v-1h-1z" fill="#98ad90"/>
'''
    offset_x = 6 if slug == "last30days" else 4
    return f'<g transform="translate({offset_x} 4) scale(2)" shape-rendering="crispEdges">'+icon+'</g>'


def contact_icon(slug, dark=False):
    """Contact illustrations on the same grid and palette as the projects."""
    sage = "#92aa9b" if dark else "#91a595"
    paper = "#dfd7c3" if dark else "#eee7d5"
    blue = "#9bb4c2" if dark else "#97aebc"
    if slug == "email":
        icon = f'''
<path d="M5 6h22v2h2v15H3V8h2z" fill="{sage}"/>
<path d="M5 8h22v13H5z" fill="{paper}"/>
<path d="M5 8h3v2h3v2h3v2h4v-2h3v-2h3V8h3v3h-3v2h-3v2h-3v2h-4v-2h-3v-2H8v-2H5z" fill="#c7baa3"/>
<path d="M5 20h3v-2h3v-2h2v2h-2v2H8v1H5zM27 20h-3v-2h-3v-2h-2v2h2v2h3v1h3z" fill="#d9cdb6"/>
<path d="M14 13h4v1h1v3h-1v1h-4v-1h-1v-3h1z" fill="#d2a095"/>
<path d="M15 14h2v2h-2z" fill="#e9bdb0"/>
<path d="M25 3h2v2h-2zM29 5h2v1h-2z" fill="{blue}"/>
'''
    else:
        icon = f'''
<path d="M5 4h23v2h2v17H3V6h2z" fill="{blue}"/>
<path d="M5 6h23v4H5z" fill="#d7e3df"/>
<path d="M5 11h23v10H5z" fill="{paper}"/>
<path d="M6 7h1v1H6zM9 7h1v1H9zM12 7h1v1h-1z" fill="#a9b7af"/>
<path d="M16 7h10v1H16z" fill="#f3f1e7"/>
<path d="M8 13h6v2H8zM8 17h12v1H8zM8 19h9v1H8z" fill="{sage}"/>
<path d="M24 15h2v2h2v2h2v2h-3v3h-2v-3h-1z" fill="#bca28c"/>
<path d="M25 17h1v2h2v1h-3z" fill="#eee0cb"/>
'''
    offset_y = 10 if slug == "email" else 8
    return f'<g transform="translate(2 {offset_y}) scale(2)" shape-rendering="crispEdges">'+icon+'</g>'


if __name__ == "__main__":
    assets=ROOT / "assets"
    assets.mkdir(exist_ok=True)
    for name,artwork in [("typing.svg",TYPING),("little-corner-light.svg",CORNER_LIGHT),("little-corner-dark.svg",CORNER_DARK)]:
        (assets/name).write_text(artwork,encoding="utf-8")
    for prefix, items, icon_builder in (
        ("project", PROJECTS, project_icon), ("contact", CONTACTS, contact_icon)
    ):
        for item in items:
            for theme in ("light", "dark"):
                (assets/f"{prefix}-{item[0]}-{theme}.svg").write_text(
                    compact_card(item,theme,icon_builder),encoding="utf-8")

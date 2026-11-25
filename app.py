
import base64
import html
import json
from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

import data as D

ROOT = Path(__file__).parent

st.set_page_config(
    page_title=f"{D.NAME} | {D.TITLE.split(' · ')[0]}",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed",
    menu_items={"About": f"{D.NAME}: {D.TAGLINE}"}
)

esc = html.escape


@st.cache_data
def uri(rel):
    p = ROOT / rel
    if not rel or not p.exists():
        return ""

    mime = {
        ".png": "image/png",
        ".webp": "image/webp"
    }.get(p.suffix.lower(), "image/jpeg")

    return f"data:{mime};base64," + base64.b64encode(
        p.read_bytes()
    ).decode()


RESUME = ROOT / D.RESUME_FILE
RESUME_BYTES = RESUME.read_bytes() if RESUME.exists() else None

PALETTES = {
    False: dict(
        bg="#fbfbfd",
        surface="#ffffff",
        ink="#0b1220",
        muted="#5b6478",
        line="#e3e7f0",
        accent="#1747ff",
        soft="#eaf0ff",
        on="#ffffff",
        nav="rgba(251,251,253,.96)"
    ),
    True: dict(
        bg="#080d1a",
        surface="#0f1730",
        ink="#f1f4ff",
        muted="#9ba6c4",
        line="#1f2944",
        accent="#7b9bff",
        soft="#15204a",
        on="#080d1a",
        nav="rgba(8,13,26,.96)"
    ),
}

P = PALETTES[bool(st.session_state.get("dark", False))]
root_vars = ":root{" + "".join(
    f"--{k}:{v};" for k, v in P.items()
) + "}"


CSS = """
@import url('https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,600;12..96,800&family=Instrument+Sans:wght@400;500&display=swap');

html,[data-testid="stMain"]{scroll-behavior:smooth}
.stApp,[data-testid="stAppViewContainer"],[data-testid="stMain"]{background:var(--bg)!important;color:var(--ink)}
[data-testid="stHeader"],footer,#MainMenu{display:none!important}
.block-container{max-width:1080px;padding:0 1.5rem 3rem!important}
html,body,[class*="st-"],.stMarkdown{font-family:'Instrument Sans',system-ui,sans-serif}
h1,h2,h3,h4{font-family:'Bricolage Grotesque',system-ui,sans-serif!important;letter-spacing:-.03em;color:var(--ink)!important;margin:0;padding:0}
.stMarkdown p,.stMarkdown li{color:var(--ink)}
.muted,.stMarkdown p.muted{color:var(--muted)}
a{color:var(--accent)}
:focus-visible{outline:3px solid var(--accent);outline-offset:3px}

.st-key-topbar{position:sticky;top:0;z-index:999;background:var(--nav);backdrop-filter:blur(12px);border-bottom:1px solid var(--line);padding:.35rem 0;margin-bottom:1rem}
.st-key-topbar [data-testid="stHorizontalBlock"]{flex-wrap:nowrap!important;gap:.6rem}
.st-key-topbar [data-testid="stColumn"]{min-width:0!important}
.pf-nav{display:flex;align-items:center;gap:22px;overflow-x:auto;white-space:nowrap;scrollbar-width:none}
.pf-nav .brand{font:800 18px 'Bricolage Grotesque',sans-serif;color:var(--ink);text-decoration:none;margin-right:8px}
.pf-nav a.nl{color:var(--muted);text-decoration:none;font-size:15px;padding:6px 2px;border-bottom:2px solid transparent;transition:color .2s,border-color .2s}
.pf-nav a.nl:hover,.pf-nav a.nl.active{color:var(--accent);border-color:var(--accent)}

.anchor{scroll-margin-top:84px;height:0}
.reveal{transition:opacity .6s ease,transform .6s ease}
.has-js .reveal:not(.in){opacity:0;transform:translateY(14px)}

.hero{padding:40px 0 8px;animation:rise .8s ease both}
@keyframes rise{from{opacity:0;transform:translateY(16px)}to{opacity:1;transform:none}}
.open{display:inline-flex;align-items:center;gap:9px;font-size:14.5px;font-weight:500;background:var(--surface);border:1px solid var(--line);padding:6px 14px;border-radius:999px;margin-bottom:22px;color:var(--ink)}
.open::before{content:"";width:8px;height:8px;border-radius:50%;background:#18a957}
.hero h1{font-size:clamp(34px,5vw,60px);font-weight:800;line-height:1.05}
.hero .tag{font:600 clamp(18px,2.4vw,26px) 'Bricolage Grotesque',sans-serif;color:var(--accent)!important;margin:14px 0 16px}
.hero .lead{color:var(--muted);max-width:56ch;font-size:18px;margin:0 0 20px}

.btn{display:inline-block;padding:11px 22px;border-radius:999px;font-weight:500;text-decoration:none!important;border:1.5px solid var(--accent);color:var(--accent)!important;transition:transform .15s,background .15s}
.btn.p{background:var(--accent);color:var(--on)!important}
.btn:hover{transform:translateY(-2px)}

.socials{display:flex;flex-wrap:wrap;gap:10px;margin-top:6px}
.socials a{border:1px solid var(--line);background:var(--surface);color:var(--ink)!important;text-decoration:none!important;padding:7px 16px;border-radius:999px;font-size:14.5px}
.socials a:hover{border-color:var(--accent);color:var(--accent)!important}

.avatar{width:min(300px,70%);aspect-ratio:1;border-radius:28px;margin:0 auto;display:flex;align-items:center;justify-content:center;background:var(--soft);border:1px solid var(--line);font:800 84px 'Bricolage Grotesque',sans-serif;color:var(--accent);object-fit:cover}

.sec{padding:72px 0 8px}
.sec h2{font-size:clamp(28px,4vw,42px);font-weight:800}
.sec p.sub{color:var(--muted);margin:10px 0 0;max-width:60ch}

.chip{display:inline-block;background:var(--soft);color:var(--accent);font-size:13.5px;font-weight:500;padding:4px 12px;border-radius:999px;margin:0 8px 8px 0}

.panel{background:var(--surface);border:1px solid var(--line);border-radius:18px;padding:22px 24px;margin-bottom:16px}
.panel h3{font-size:18px;margin-bottom:12px}
.panel ul{margin:0;padding-left:18px;color:var(--muted)}
.panel p{margin:0;color:var(--muted)}

.skills{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:16px}
.skills .panel{margin:0}
.skills h3::before,.dot::before{content:"";display:inline-block;width:10px;height:10px;border-radius:3px;background:var(--accent);margin-right:10px}

[class*="st-key-card_"]{background:var(--surface);border:1px solid var(--line)!important;border-radius:20px;padding:14px 14px 10px!important}
.thumb{height:190px;border-radius:12px;background:var(--soft);display:flex;align-items:center;justify-content:center;overflow:hidden;margin-bottom:14px}
.thumb img{width:100%;height:100%;object-fit:contain;background:#fff}
.thumb span{font:800 30px 'Bricolage Grotesque',sans-serif;color:var(--accent);text-align:center;padding:0 16px}

.pc h3{font-size:22px;font-weight:800;margin:8px 0 6px}
.pc p{color:var(--muted);margin:0 0 12px}
.pc .when{font-size:14px;margin-bottom:10px}

.tl{border-left:2px solid var(--line);margin-left:6px}
.tl .it{position:relative;padding:0 0 26px 26px}
.tl .it::before{content:"";position:absolute;left:-7px;top:6px;width:12px;height:12px;border-radius:50%;background:var(--accent)}
.tl h3{font-size:20px}
.tl .meta{color:var(--muted);font-size:15px;margin:2px 0 8px}
.tl ul{margin:0;padding-left:18px;color:var(--muted)}

.contact{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:16px}
.contact a{display:block;background:var(--surface);border:1px solid var(--line);border-radius:18px;padding:22px;text-decoration:none!important;color:var(--ink)!important;transition:transform .15s,border-color .15s}
.contact a:hover{transform:translateY(-3px);border-color:var(--accent)}
.contact b{display:block;font:800 20px 'Bricolage Grotesque',sans-serif;color:var(--accent)}
.contact span{color:var(--muted);font-size:15px;word-break:break-all}

.footer{margin-top:72px;padding:30px 0 10px;border-top:1px solid var(--line);display:flex;flex-wrap:wrap;gap:20px;justify-content:space-between;color:var(--muted);font-size:14.5px}
.footer b{font:800 18px 'Bricolage Grotesque',sans-serif;color:var(--ink);display:block}
.footer a{color:var(--muted)!important;text-decoration:none;margin-right:14px}
.footer a:hover{color:var(--accent)!important}

.totop{position:fixed;right:20px;bottom:20px;width:44px;height:44px;border-radius:50%;background:var(--accent);color:var(--on)!important;display:flex;align-items:center;justify-content:center;text-decoration:none!important;font-size:20px;z-index:998;box-shadow:0 8px 24px -8px var(--accent)}

.stButton button,.stDownloadButton button,.stLinkButton a{border-radius:999px!important;border:1.5px solid var(--accent)!important;background:transparent!important;font-weight:500}
.stButton button p,.stDownloadButton button p,.stLinkButton a p{color:var(--accent)!important}
[data-testid="stBaseButton-primary"]{background:var(--accent)!important}
[data-testid="stBaseButton-primary"] p{color:var(--on)!important}
[data-testid="stToggle"] p,[data-testid="stWidgetLabel"] p{color:var(--ink)!important;font-size:14px}
[data-testid="stSegmentedControl"] button p{color:var(--ink)!important}
div[data-testid="stDialog"] div[role="dialog"]{background:var(--surface)!important;color:var(--ink)}

.cs h4{font-size:15px;color:var(--accent)!important;margin:20px 0 6px}
.cs p,.cs li{color:var(--muted);margin:0 0 6px}
.cs ul,.cs ol{margin:0;padding-left:20px}

.process-steps{display:grid;gap:12px;margin:8px 0 4px}
.process-step{display:grid;grid-template-columns:38px minmax(0,1fr);gap:12px;align-items:start;padding:14px 16px;background:var(--soft);border:1px solid var(--line);border-radius:12px}
.process-number{width:34px;height:34px;display:flex;align-items:center;justify-content:center;border-radius:9px;background:var(--surface);color:var(--accent);font:800 14px 'Bricolage Grotesque',sans-serif}
.process-step b{display:block;color:var(--ink);margin:1px 0 4px}
.process-step p{margin:0!important;color:var(--muted)!important;font-size:14px;line-height:1.55}

.metrics{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:12px;margin-top:6px}
.metrics div{background:var(--soft);border-radius:14px;padding:14px}
.metrics b{display:block;font:800 26px 'Bricolage Grotesque',sans-serif;color:var(--accent)}
.metrics span{font-size:13.5px;color:var(--muted)}

.fig{margin:14px 0}
.fig img{width:100%;border-radius:12px;border:1px solid var(--line);background:#fff}
.fig figcaption{font-size:13.5px;color:var(--muted);margin-top:6px}

@media (max-width:700px){
    .sec{padding-top:52px}
    .hero{padding-top:12px}
    .totop{right:14px;bottom:14px}
}

@media (prefers-reduced-motion:reduce){
    *,html,[data-testid="stMain"]{animation:none!important;transition:none!important;scroll-behavior:auto!important}
    .has-js .reveal:not(.in){opacity:1;transform:none}
}
"""


CSS2 = """
[data-testid="stMain"]{background:radial-gradient(900px 340px at 88% -80px,var(--soft),transparent 72%) no-repeat local,var(--bg)!important}
.stApp{transition:background-color .3s}
.skip{position:absolute;left:-9999px;top:6px;background:var(--accent);color:var(--on)!important;padding:8px 14px;border-radius:8px;z-index:1000;text-decoration:none}
.skip:focus{left:12px}

.st-key-topbar [data-testid="stHorizontalBlock"]{display:grid!important;grid-template-columns:auto minmax(0,1fr) auto auto;align-items:center;gap:.4rem 1rem}
.st-key-topbar [data-testid="stColumn"]{width:auto!important;min-width:0!important;flex:none!important}
.st-key-topbar .stDownloadButton button{min-height:40px;padding:0 18px}
.pf-nav .brand{margin-right:0}

.stDownloadButton button,.stButton button,.stLinkButton a{min-height:46px;transition:transform .15s,background .15s}
.stDownloadButton button:hover,.stButton button:hover,.stLinkButton a:hover{transform:translateY(-2px);background:var(--soft)!important}
[data-testid="stBaseButton-primary"]:hover{background:var(--accent)!important;filter:brightness(1.08)}
.stDownloadButton button p,.stButton button p,.stLinkButton a p{font-size:16px;font-weight:500}

.btn{min-height:46px;display:inline-flex;align-items:center;font-size:16px}
.tlink{color:var(--accent)!important;font-weight:500;text-decoration:none!important;display:inline-block;padding:10px 4px}
.tlink:hover{text-decoration:underline!important}

.sec h2::after{content:"";display:block;width:44px;height:4px;border-radius:4px;background:var(--accent);margin-top:14px}
.avatar{width:min(280px,72%);box-shadow:0 30px 60px -34px var(--accent);outline:1px solid var(--line);outline-offset:10px}

.totop{opacity:0;pointer-events:none;transform:translateY(8px);transition:opacity .25s,transform .25s}
.totop.show{opacity:1;pointer-events:auto;transform:none}

[class*="st-key-card_"]{transition:transform .2s,box-shadow .2s,border-color .2s}
[class*="st-key-card_"]:hover{transform:translateY(-4px);border-color:var(--accent)!important;box-shadow:0 22px 40px -28px var(--accent)}
.thumb{align-items:stretch}
.thumb img{transition:transform .5s;align-self:center}
[class*="st-key-card_"]:hover .thumb img{transform:scale(1.03)}

.tile{width:100%;padding:18px 20px;display:flex;flex-direction:column;justify-content:space-between;border-left:4px solid var(--accent);text-align:left}
.tile small{color:var(--accent);font-weight:500;font-size:14px}
.tile b{font:800 28px/1.05 'Bricolage Grotesque',sans-serif;color:var(--ink)}
.tile i{font-style:normal;color:var(--muted);font-size:13.5px}
.pc h3{font-size:21px}

div:has(> .st-key-topbar){position:sticky;top:0;z-index:999}
.st-key-topbar{position:relative;top:auto;margin-bottom:0}
#top.anchor{scroll-margin-top:240px}

.st-key-cat button[role="radio"]{background:var(--surface)!important;border-color:var(--line)!important;min-height:40px}
.st-key-cat button[role="radio"] *{color:var(--ink)!important}
.st-key-cat button[role="radio"][aria-checked="true"]{background:var(--accent)!important;border-color:var(--accent)!important}
.st-key-cat button[role="radio"][aria-checked="true"] *{color:var(--on)!important}

.footer>div{min-width:0}
.footer a{display:inline-block;margin-bottom:6px}
.rprev img{width:100%;height:auto;border-radius:12px;border:1px solid var(--line);box-shadow:0 24px 50px -36px var(--ink)}
.rprev p{font-size:13.5px;color:var(--muted);margin-top:8px}

@media (max-width:760px){
    .st-key-topbar [data-testid="stHorizontalBlock"]{grid-template-columns:minmax(0,1fr) auto auto;gap:.2rem .6rem}
    .st-key-topbar [data-testid="stColumn"]:nth-child(2){grid-row:2;grid-column:1/-1}
    .avatar{width:min(170px,48%);font-size:54px;border-radius:22px;outline-offset:8px}
    .hero .lead{font-size:17px}
    .skills{grid-template-columns:1fr}
    .metrics{grid-template-columns:1fr 1fr}
}
"""

st.markdown(
    f"<style>{root_vars}{CSS}{CSS2}</style>",
    unsafe_allow_html=True
)


def chips(items):
    return "".join(
        f'<span class="chip">{esc(i)}</span>' for i in items
    )


def section(anchor, title, sub=""):
    sub_html = f'<p class="sub">{esc(sub)}</p>' if sub else ""

    st.markdown(
        f'<div id="{anchor}" class="anchor"></div>'
        f'<div class="sec reveal"><h2>{esc(title)}</h2>{sub_html}</div>',
        unsafe_allow_html=True
    )


def ul(items):
    return (
        "<ul>" + "".join(f"<li>{esc(i)}</li>" for i in items) + "</ul>"
        if items else ""
    )


# ---------------- navigation ----------------

has_certs = bool(
    D.CERTIFICATIONS or any(D.ACHIEVEMENTS.values())
)

NAV = [
    ("Home", "top"),
    ("About", "about"),
    ("Skills", "skills"),
    ("Projects", "projects"),
    ("Education", "education")
]

if has_certs:
    NAV.append(("Certifications", "certifications"))

NAV += [
    ("Resume", "resume"),
    ("Contact", "contact")
]

with st.container(key="topbar"):
    c0, c1, c2, c3 = st.columns(
        [1, 6, 1, 1],
        vertical_alignment="center"
    )

    links = "".join(
        f'<a class="nl" href="#{a}" target="_self">{n}</a>'
        for n, a in NAV[1:]
    )

    c0.markdown(
        f'<a class="skip" href="#about" target="_self">Skip to content</a>'
        f'<nav class="pf-nav" aria-label="Brand">'
        f'<a class="brand" href="#top" target="_self">{esc(D.NAME)}</a>'
        f'</nav>',
        unsafe_allow_html=True
    )

    c1.markdown(
        f'<nav class="pf-nav" aria-label="Main">'
        f'<a class="nl" href="#top" target="_self">Home</a>{links}'
        f'</nav>',
        unsafe_allow_html=True
    )

    c2.toggle("Dark", key="dark")

    if RESUME_BYTES:
        c3.download_button(
            "Resume",
            RESUME_BYTES,
            file_name=f"{D.NAME.replace(' ', '_')}_Resume.pdf",
            mime="application/pdf",
            type="primary",
            key="dl_top"
        )


# ---------------- hero ----------------

st.markdown(
    '<div id="top" class="anchor"></div>',
    unsafe_allow_html=True
)

left, right = st.columns(
    [1.5, 1],
    gap="large",
    vertical_alignment="center"
)

with left:
    st.markdown(
        f'<div class="hero">'
        f'<span class="open">{esc(D.OPEN_TO)}</span>'
        f'<h1>{esc(D.NAME)}</h1>'
        f'<p class="tag">{esc(D.TITLE)}</p>'
        f'<p class="lead">{esc(D.INTRO)}</p>'
        f'</div>',
        unsafe_allow_html=True
    )

    b1, b2, b3 = st.columns(
        [1, 1.25, 1],
        vertical_alignment="center"
    )

    b1.markdown(
        '<a class="btn p" href="#projects" target="_self">View my work</a>',
        unsafe_allow_html=True
    )

    if RESUME_BYTES:
        b2.download_button(
            "Download resume",
            RESUME_BYTES,
            file_name=f"{D.NAME.replace(' ', '_')}_Resume.pdf",
            mime="application/pdf",
            key="dl_hero",
            use_container_width=True
        )

    b3.markdown(
        '<a class="tlink" href="#contact" target="_self">Contact me →</a>',
        unsafe_allow_html=True
    )

    st.markdown(
        f'<div class="socials">'
        f'<a href="{esc(D.GITHUB)}" target="_blank" rel="noopener">GitHub ↗</a>'
        f'<a href="{esc(D.LINKEDIN)}" target="_blank" rel="noopener">LinkedIn ↗</a>'
        f'<a href="mailto:{esc(D.EMAIL)}">Email</a>'
        f'</div>',
        unsafe_allow_html=True
    )

with right:
    photo = uri(D.PROFILE_IMAGE)

    st.markdown(
        f'<img class="avatar" src="{photo}" alt="Portrait of {esc(D.NAME)}">'
        if photo else
        f'<div class="avatar" role="img" aria-label="Initials of {esc(D.NAME)}">'
        f'{esc(D.INITIALS)}</div>',
        unsafe_allow_html=True
    )


# ---------------- about ----------------

section("about", "About me")

a1, a2 = st.columns([1.2, 1], gap="large")

with a1:
    st.markdown(
        "".join(
            f"<p>{esc(t)}</p>" for t in D.ABOUT["paragraphs"]
        ),
        unsafe_allow_html=True
    )

    st.markdown(
        f'<div class="panel">'
        f'<h3 class="dot">Career objective</h3>'
        f'<p>{esc(D.ABOUT["objective"])}</p>'
        f'</div>'
        f'<div class="panel">'
        f'<h3 class="dot">How I approach problems</h3>'
        f'<p>{esc(D.ABOUT["approach"])}</p>'
        f'</div>',
        unsafe_allow_html=True
    )

with a2:
    st.markdown(
        f'<div class="panel"><h3 class="dot">Strengths</h3>'
        f'{ul(D.ABOUT["strengths"])}</div>'
        f'<div class="panel"><h3 class="dot">Interests</h3>'
        f'{ul(D.ABOUT["interests"])}</div>'
        + (
            f'<div class="panel"><h3 class="dot">Currently learning</h3>'
            f'{ul(D.ABOUT["learning"])}</div>'
            if D.ABOUT["learning"] else ""
        ),
        unsafe_allow_html=True
    )


# ---------------- skills ----------------

section("skills", "Skills and technologies")

st.markdown(
    '<div class="skills">' +
    "".join(
        f'<div class="panel reveal">'
        f'<h3 class="dot">{esc(g)}</h3>{chips(i)}</div>'
        for g, i in D.SKILLS.items()
    ) +
    "</div>",
    unsafe_allow_html=True
)


# ---------------- projects ----------------

def block(title, body):
    return f'<h4>{title}</h4>{body}' if body else ""


@st.dialog("Project case study", width="large")
def case_study(p):
    img = uri(p.get("image", ""))

    fig = (
        f'<figure class="fig">'
        f'<img loading="lazy" decoding="async" src="{img}" '
        f'alt="{esc(p["title"])} results">'
        f'<figcaption>{esc(p.get("caption", ""))}</figcaption>'
        f'</figure>'
        if img else ""
    )

    metrics = (
        '<div class="metrics">' +
        "".join(
            f"<div><b>{esc(v)}</b><span>{esc(l)}</span></div>"
            for v, l in p.get("metrics", [])
        ) +
        "</div>"
        if p.get("metrics") else ""
    )

    process = (
        '<div class="process-steps">' +
        "".join(
            f'<div class="process-step">'
            f'<span class="process-number">{i:02d}</span>'
            f'<div><b>{esc(t)}</b><p>{esc(x)}</p></div>'
            f'</div>'
            for i, (t, x) in enumerate(p.get("process", []), 1)
        ) +
        "</div>"
        if p.get("process") else ""
    )

    ch = ""

    if p.get("challenges"):
        ch = "<ul>" + "".join(
            f"<li>{esc(c)}" +
            (f"<br><b>Solution:</b> {esc(s)}" if s else "") +
            "</li>"
            for c, s in p["challenges"]
        ) + "</ul>"

    para = lambda k: f"<p>{esc(p[k])}</p>" if p.get(k) else ""

    st.markdown(
        f'<div class="cs">'
        f'<span class="chip">{esc(p["category"])}</span>'
        f'<h3 style="font-size:26px">{esc(p["title"])}</h3>'
        f'<p class="muted">{esc(p["dates"])}</p>{fig}'
        + block("Overview", para("overview"))
        + block("Problem statement", para("problem"))
        + block("Objective", para("objective"))
        + block("Proposed solution", para("solution"))
        + block("My role and contribution", para("role"))
        + block("Technologies used", chips(p.get("stack", [])))
        + block("Key features", ul(p.get("features", [])))
        + block("Development process", process)
        + block("Challenges and solutions", ch)
        + block("Results", metrics + ul(p.get("results", [])))
        + block("Limitations", ul(p.get("limitations", [])))
        + "</div>",
        unsafe_allow_html=True
    )

    if p.get("github") or p.get("demo"):
        cols = st.columns(2)

        if p.get("github"):
            cols[0].link_button(
                "Source code on GitHub ↗",
                p["github"],
                use_container_width=True
            )

        if p.get("demo"):
            cols[1].link_button(
                "Live demo ↗",
                p["demo"],
                use_container_width=True
            )


section(
    "projects",
    "Featured projects",
    "Select a project to read the full case study."
)

cats = ["All"] + sorted({
    p["category"] for p in D.PROJECTS
})

sel = st.segmented_control(
    "Filter projects",
    cats,
    default="All",
    key="cat",
    label_visibility="collapsed"
) or "All"

shown = [
    p for p in D.PROJECTS
    if sel in ("All", p["category"])
]

for row in range(0, len(shown), 2):
    cols = st.columns(2, gap="medium")

    for col, p in zip(cols, shown[row:row + 2]):
        with col, st.container(key=f"card_{p['id']}"):
            img = uri(p.get("image", ""))

            short_title = p.get("short") or p.get("title", "Project")

            thumb = (
                f'<img loading="lazy" decoding="async" '
                f'src="{img}" alt="{esc(p["title"])} results">'
                if img else
                f'<div class="tile" role="img" '
                f'aria-label="{esc(p["title"])}">'
                f'<small>Case study</small>'
                f'<b>{esc(short_title)}</b>'
                f'<i>{esc(" · ".join(p.get("stack", [])[:3]))}</i>'
                f'</div>'
            )

            st.markdown(
                f'<div class="pc">'
                f'<div class="thumb">{thumb}</div>'
                f'<span class="chip">{esc(p["category"])}</span>'
                f'<h3>{esc(p["title"])}</h3>'
                f'<p class="when">{esc(p["dates"])}</p>'
                f'<p>{esc(p["summary"])}</p>'
                f'{chips(p.get("stack", [])[:5])}'
                f'</div>',
                unsafe_allow_html=True
            )

            b = st.columns(2)

            if b[0].button(
                "View case study",
                key=f"v_{p['id']}",
                use_container_width=True
            ):
                case_study(p)

            if p.get("github"):
                b[1].link_button(
                    "GitHub ↗",
                    p["github"],
                    use_container_width=True
                )


# ---------------- education ----------------

section("education", "Education")

items = ""

for e in D.EDUCATION:
    meta = " · ".join(
        x for x in [
            e["institution"],
            e["location"],
            f'{e["start"]} – {e["end"]}',
            e["status"]
        ]
        if x
    )

    items += (
        f'<div class="it reveal">'
        f'<h3>{esc(e["degree"])}</h3>'
        f'<div class="meta">{esc(meta)}</div>'
        f'{ul(e["details"])}'
        f'</div>'
    )

st.markdown(
    f'<div class="tl">{items}</div>',
    unsafe_allow_html=True
)


# ---------------- certifications and achievements ----------------

if has_certs:
    section(
        "certifications",
        "Certifications and achievements"
    )

    cards = ""

    for c in D.CERTIFICATIONS:
        img = uri(c.get("image", ""))

        cards += (
            f'<div class="panel reveal">' +
            (
                f'<div class="fig">'
                f'<img loading="lazy" decoding="async" src="{img}" '
                f'alt="{esc(c["name"])} certificate"></div>'
                if img else ""
            )
            +
            f'<h3>{esc(c["name"])}</h3>'
            f'<p>{esc(c["issuer"])} · {esc(c["date"])}</p>'
            +
            (
                f'<p>Credential ID: {esc(c["credential_id"])}</p>'
                if c.get("credential_id") else ""
            )
            +
            (
                f'<p><a href="{esc(c["url"])}" target="_blank" '
                f'rel="noopener">Verify ↗</a></p>'
                if c.get("url") else ""
            )
            +
            "</div>"
        )

    for cat, rows in D.ACHIEVEMENTS.items():
        for r in rows:
            cards += (
                f'<div class="panel reveal">'
                f'<span class="chip">{esc(cat)}</span>'
                f'<h3>{esc(r["title"])}</h3>'
                f'<p>{esc(r.get("detail", ""))}</p>'
                +
                (
                    f'<p><a href="{esc(r["url"])}" target="_blank" '
                    f'rel="noopener">Learn more ↗</a></p>'
                    if r.get("url") else ""
                )
                +
                "</div>"
            )

    st.markdown(
        f'<div class="skills">{cards}</div>',
        unsafe_allow_html=True
    )


# ---------------- resume ----------------

section("resume", "Resume")

r1, r2 = st.columns(
    [1, 1],
    gap="large",
    vertical_alignment="center"
)

with r1:
    prev = ROOT / D.RESUME_PREVIEW

    if prev.exists():
        st.markdown(
            f'<div class="rprev">'
            f'<img src="{uri(D.RESUME_PREVIEW)}" '
            f'alt="Preview of the first page of the resume" '
            f'loading="lazy" decoding="async">'
            f'<p>Preview of page 1</p>'
            f'</div>',
            unsafe_allow_html=True
        )

with r2:
    st.markdown(
        f'<div class="panel">'
        f'<h3 class="dot">Download my resume</h3>'
        f'<p>The same PDF I send with job applications.</p>'
        f'<p class="muted" style="margin-top:10px">'
        f'Last updated: {esc(D.RESUME_UPDATED)}</p>'
        f'</div>',
        unsafe_allow_html=True
    )

    if RESUME_BYTES:
        st.download_button(
            "Download resume (PDF)",
            RESUME_BYTES,
            file_name=f"{D.NAME.replace(' ', '_')}_Resume.pdf",
            mime="application/pdf",
            type="primary",
            key="dl_resume"
        )


# ---------------- contact ----------------

section(
    "contact",
    "Let’s talk",
    "I’m open to data science and machine learning roles. "
    "The fastest way to reach me is by email."
)

st.markdown(
    f'<div class="contact">'
    f'<a href="mailto:{esc(D.EMAIL)}">'
    f'<b>Email</b><span>{esc(D.EMAIL)}</span></a>'
    f'<a href="{esc(D.LINKEDIN)}" target="_blank" rel="noopener">'
    f'<b>LinkedIn</b>'
    f'<span>{esc(D.LINKEDIN.replace("https://www.", ""))}</span></a>'
    f'<a href="{esc(D.GITHUB)}" target="_blank" rel="noopener">'
    f'<b>GitHub</b>'
    f'<span>{esc(D.GITHUB.replace("https://", ""))}</span></a>'
    f'<a href="tel:{esc(D.PHONE.replace(" ", ""))}">'
    f'<b>Phone</b><span>{esc(D.PHONE)}</span></a>'
    f'</div>',
    unsafe_allow_html=True
)


# ---------------- footer ----------------

quick = "".join(
    f'<a href="#{a}" target="_self">{n}</a>'
    for n, a in NAV[1:]
)

st.markdown(
    f'<div class="footer">'
    f'<div><b>{esc(D.NAME)}</b>{esc(D.TAGLINE)}</div>'
    f'<div>{quick}</div>'
    f'<div>'
    f'<a href="{esc(D.GITHUB)}" target="_blank" rel="noopener">GitHub</a>'
    f'<a href="{esc(D.LINKEDIN)}" target="_blank" rel="noopener">LinkedIn</a>'
    f'</div>'
    f'<div style="width:100%">© 2026 {esc(D.NAME)}</div>'
    f'</div>'
    f'<a class="totop" href="#top" target="_self" '
    f'aria-label="Back to top">↑</a>',
    unsafe_allow_html=True
)


# ---------------- scroll behavior ----------------

SCROLL_JS = """
<script>
(function(){try{
const d=window.parent.document;
d.body.classList.add('has-js');

const TITLE=__TITLE__,DESC=__DESC__;
d.title=TITLE;

function meta(attr,key,val){
    let m=d.head.querySelector('meta['+attr+'="'+key+'"]');
    if(!m){
        m=d.createElement('meta');
        m.setAttribute(attr,key);
        d.head.appendChild(m);
    }
    m.setAttribute('content',val);
}

meta('name','description',DESC);
meta('property','og:title',TITLE);
meta('property','og:description',DESC);
meta('property','og:type','website');
meta('name','theme-color','#1747ff');

const main=d.querySelector('[data-testid="stMain"]')||d.scrollingElement;

function update(){
    const links=[...d.querySelectorAll('.pf-nav a.nl')];
    let cur=null;

    d.querySelectorAll('.anchor').forEach(a=>{
        if(a.getBoundingClientRect().top<=140)cur=a.id;
    });

    const an=d.querySelectorAll('.anchor');

    if(an.length&&main.scrollTop+main.clientHeight>=main.scrollHeight-8){
        cur=an[an.length-1].id;
    }

    links.forEach(l=>{
        const on=l.getAttribute('href')==='#'+cur;
        l.classList.toggle('active',on);

        if(on)l.setAttribute('aria-current','true');
        else l.removeAttribute('aria-current');
    });

    const tt=d.querySelector('.totop');

    if(tt)tt.classList.toggle('show',main.scrollTop>500);
}

let t=false;

main.addEventListener('scroll',()=>{
    if(!t){
        t=true;
        requestAnimationFrame(()=>{
            update();
            t=false;
        });
    }
});

update();

const io=new IntersectionObserver(es=>es.forEach(e=>{
    if(e.isIntersecting){
        e.target.classList.add('in');
        io.unobserve(e.target);
    }
}),{threshold:.05});

function scan(){
    d.querySelectorAll('.reveal:not(.in):not([data-o])').forEach(el=>{
        el.setAttribute('data-o','1');
        io.observe(el);
    });
    update();
}

scan();

new MutationObserver(scan).observe(
    d.body,
    {childList:true,subtree:true}
);

}catch(e){} })();
</script>
""".replace(
    "__TITLE__",
    json.dumps(f"{D.NAME} | {D.TITLE}")
).replace(
    "__DESC__",
    json.dumps(f"{D.NAME}: {D.TITLE}. {D.INTRO}")
)

if hasattr(st, "iframe"):
    st.iframe(SCROLL_JS, height=1)
else:
    components.html(SCROLL_JS, height=0)

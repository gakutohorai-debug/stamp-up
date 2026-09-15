
import streamlit as st
from pathlib import Path
import pandas as pd
import pydeck as pdk

st.set_page_config(
    page_title="HIGH HOPE! | Experience Passport",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="collapsed",
)

ASSET = Path(__file__).parent / "assets" / "passport_cover.png"

st.markdown("""
<style>
    .stApp {
        background:
            radial-gradient(circle at 8% 8%, rgba(255,213,79,.20), transparent 24%),
            radial-gradient(circle at 92% 8%, rgba(66,165,245,.14), transparent 28%),
            linear-gradient(180deg, #fffdf7 0%, #f7fbff 52%, #ffffff 100%);
        color: #12355b;
    }
    .block-container {
        max-width: 1180px;
        padding-top: 2.2rem;
        padding-bottom: 4rem;
    }
    h1, h2, h3 { color: #123f73; letter-spacing: -0.02em; }
    .hero-kicker {
        display:inline-block;
        padding:.45rem .8rem;
        border-radius:999px;
        background:#e9f4ff;
        color:#0b5fa5;
        font-weight:800;
        margin-bottom:.7rem;
    }
    .hero-title {
        font-size: clamp(3rem, 7vw, 6.8rem);
        line-height:.92;
        font-weight:1000;
        letter-spacing:-.07em;
        margin:.2rem 0 1rem;
        color:#0d3b66;
    }
    .hero-title span:nth-child(2){color:#f72585;}
    .hero-title span:nth-child(3){color:#ff8c1a;}
    .hero-sub {
        font-size:1.25rem;
        line-height:1.7;
        color:#355a7c;
        max-width:760px;
    }
    .pill-row { margin: 1.2rem 0 1.6rem; }
    .pill {
        display:inline-block;
        margin:.25rem .35rem .25rem 0;
        padding:.5rem .8rem;
        border-radius:999px;
        background:white;
        border:1px solid #dce8f3;
        box-shadow:0 4px 14px rgba(33,79,122,.06);
        font-weight:700;
    }
    .card {
        background:rgba(255,255,255,.93);
        border:1px solid #e0eaf2;
        border-radius:24px;
        padding:1.25rem 1.3rem;
        box-shadow:0 10px 30px rgba(23,62,98,.07);
        height:100%;
    }
    .step {
        border-left:5px solid #f7b500;
        padding-left:1rem;
    }
    .step-num {
        font-weight:900;
        color:#f39c12;
        font-size:.85rem;
        text-transform:uppercase;
        letter-spacing:.08em;
    }
    .big-quote {
        background:#0e4d82;
        color:white;
        border-radius:26px;
        padding:1.7rem 1.8rem;
        font-size:1.45rem;
        font-weight:800;
        line-height:1.5;
        text-align:center;
        margin:1rem 0 2rem;
    }
    .unlock {
        background:linear-gradient(135deg,#fff3c4,#fffdf5);
        border:1px solid #f4d26e;
        border-radius:24px;
        padding:1.3rem;
        box-shadow:0 10px 28px rgba(197,140,0,.08);
    }
    .footer-note {
        color:#6b7f93;
        font-size:.9rem;
        text-align:center;
        margin-top:3rem;
    }
    .metric-box {
        text-align:center;
        padding:1.1rem .6rem;
        border-radius:20px;
        background:white;
        border:1px solid #e3edf4;
    }
    .metric-box b {
        display:block;
        font-size:2rem;
        color:#0d5798;
    }
    .small { color:#5a7087; font-size:.95rem; }
</style>
""", unsafe_allow_html=True)

# HERO
left, right = st.columns([1.25, .75], gap="large")

with left:
    st.markdown('<div class="hero-kicker">Barangay-based youth experience program</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="hero-title"><span>HIGH</span> <span>HOPE</span><span>!</span></div>',
        unsafe_allow_html=True
    )
    st.markdown(
        '<div class="hero-sub">'
        'This project gives children opportunities to experience things they would not normally have the chance to try, '
        'helping them discover their interests, strengths, and potential. It goes beyond career experiences and allows '
        'children to collect a wide variety of experiences, including creativity, sports, leadership, and connections '
        'with the local community.'
        '</div>',
        unsafe_allow_html=True,
    )
    st.markdown(
        '<div class="pill-row">'
        '<span class="pill">🌱 Explore</span>'
        '<span class="pill">🔎 Discover</span>'
        '<span class="pill">🔓 Unlock</span>'
        '<span class="pill">🚀 Expand</span>'
        '</div>',
        unsafe_allow_html=True,
    )
    st.markdown(
        '<div class="big-quote">Collect experiences, not stamp.</div>',
        unsafe_allow_html=True,
    )

with right:
    if ASSET.exists():
        st.image(str(ASSET), caption="HIGH HOPE! Experience Passport", use_container_width=True)
    else:
        st.info("Passport cover image can be placed at assets/passport_cover.png")

st.divider()

# WHY
st.header("Why HIGH HOPE!?")
c1, c2, c3 = st.columns(3, gap="medium")
with c1:
    st.markdown("""<div class="card">
    <h3>🎁 More than rewards</h3>
    <p>Instead of motivating children with coins or prizes, HIGH HOPE! uses curiosity itself — “What can I experience next?” — as the motivation.</p>
    </div>""", unsafe_allow_html=True)
with c2:
    st.markdown("""<div class="card">
    <h3>✨ Create opportunities to discover</h3>
    <p>The program is not only for children who are already talented. New experiences help them discover unexpected interests and strengths.</p>
    </div>""", unsafe_allow_html=True)
with c3:
    st.markdown("""<div class="card">
    <h3>🤝 The whole community is the stage</h3>
    <p>The whole community becomes an Experience Field — including the Barangay Hall, companies, universities, shops, creators, and sports facilities.</p>
    </div>""", unsafe_allow_html=True)

st.divider()

# HOW IT WORKS
st.header("How it works")
steps = [
    ("01", "EXPERIENCE", "Try something you normally cannot experience", "Explore behind the scenes of a hotel, create a video, host an event, or develop ideas with a team."),
    ("02", "STAMP", "Record it in your Passport", "Collect stamps as a record of participation and note what you enjoyed or became interested in."),
    ("03", "DISCOVER", "Discover yourself", "Discover things about yourself, such as “I like talking with people,” “I enjoy creating,” or “I like solving problems.”"),
    ("04", "UNLOCK", "Unlock the next special experience", "After completing a certain number of experiences, new places, challenges, and roles are unlocked."),
]
cols = st.columns(4, gap="small")
for col, (n, title, jp, desc) in zip(cols, steps):
    with col:
        st.markdown(f"""<div class="card step">
        <div class="step-num">{n} · {title}</div>
        <h3>{jp}</h3>
        <p>{desc}</p>
        </div>""", unsafe_allow_html=True)

st.divider()

# EXPERIENCE CATEGORIES
st.header("Not just career experience")
st.caption("HIGH HOPE! is not only about learning about jobs. It is an Experience Program designed to expand a child’s world.")

cats = [
    ("🎨", "CREATE", "Art / Music / Cooking / Making"),
    ("🎤", "LEAD", "MC / Presentation / Junior Leader"),
    ("📷", "EXPRESS", "Photo / Video / Storytelling"),
    ("🏀", "CHALLENGE", "Sports / Team mission / New challenge"),
    ("🏢", "EXPLORE", "Company / Hotel / University / Behind the scenes"),
    ("🤝", "CONNECT", "Meet local people / students / professionals"),
    ("💡", "IMAGINE", "Create ideas for the barangay"),
    ("🌟", "DISCOVER", "Design your own experience"),
]
rows = [cats[:4], cats[4:]]
for row in rows:
    cols = st.columns(4, gap="small")
    for col, (icon, title, detail) in zip(cols, row):
        with col:
            st.markdown(f"""<div class="card">
            <div style="font-size:2rem">{icon}</div>
            <h3>{title}</h3>
            <p class="small">{detail}</p>
            </div>""", unsafe_allow_html=True)

st.divider()

# INTERACTIVE UNLOCK DEMO

st.divider()

# EXPERIENCE MAP
st.header("Experience Map — Lahug")
st.write(
    "Lahug Barangay Hall is set as **HOME**, with nearby locations shown as Potential Experience Spots. "
    "Locations that are not confirmed partners are clearly presented as possible future experience sites."
)

experience_spots = pd.DataFrame([
    {
        "name": "Lahug Barangay Hall",
        "lat": 10.32424,
        "lon": 123.89854,
        "category": "HOME",
        "experience": "The starting point of HIGH HOPE!: Passport distribution, orientation, and Unlock check.",
        "status": "HOME",
        "color": [247, 181, 0],
        "radius": 130,
    },
    {
        "name": "University of the Philippines Cebu",
        "lat": 10.31806,
        "lon": 123.89778,
        "category": "EXPLORE / CREATE",
        "experience": "Explore a university campus, meet students, and experience research, art, and idea creation.",
        "status": "Potential Experience Spot",
        "color": [40, 167, 69],
        "radius": 90,
    },
    {
        "name": "Waterfront Cebu City Hotel",
        "lat": 10.32524,
        "lon": 123.90486,
        "category": "BEHIND THE SCENES",
        "experience": "A potential special experience to explore hotel operations, service, and event management behind the scenes.",
        "status": "Potential Experience Spot",
        "color": [111, 66, 193],
        "radius": 90,
    },
    {
        "name": "Cebu IT Park",
        "lat": 10.32970,
        "lon": 123.90720,
        "category": "TECH / INNOVATION",
        "experience": "A potential experience involving technology, design, English communication, and team-based idea creation.",
        "status": "Potential Experience Area",
        "color": [13, 110, 253],
        "radius": 95,
    },
    {
        "name": "JY Square Mall",
        "lat": 10.33035,
        "lon": 123.89812,
        "category": "COMMUNITY / BUSINESS",
        "experience": "A potential experience to learn about local business through shops, services, customer interaction, and product creation.",
        "status": "Potential Experience Spot",
        "color": [253, 126, 20],
        "radius": 85,
    },
])

home = experience_spots.iloc[0]

map_col, info_col = st.columns([1.45, .55], gap="large")

with map_col:
    view_state = pdk.ViewState(
        latitude=10.3255,
        longitude=123.9018,
        zoom=14.2,
        pitch=0,
    )

    scatter = pdk.Layer(
        "ScatterplotLayer",
        data=experience_spots,
        get_position="[lon, lat]",
        get_fill_color="color",
        get_radius="radius",
        pickable=True,
        stroked=True,
        get_line_color=[255, 255, 255],
        line_width_min_pixels=2,
    )

    labels = pdk.Layer(
        "TextLayer",
        data=experience_spots,
        get_position="[lon, lat]",
        get_text="name",
        get_size=13,
        get_color=[20, 55, 90],
        get_angle=0,
        get_text_anchor="'middle'",
        get_alignment_baseline="'bottom'",
        get_pixel_offset=[0, -12],
        pickable=False,
    )

    deck = pdk.Deck(
        map_style="https://basemaps.cartocdn.com/gl/positron-gl-style/style.json",
        initial_view_state=view_state,
        layers=[scatter, labels],
        tooltip={
            "html": """
                <div style="font-family:Arial; max-width:290px">
                <b style="font-size:15px">{name}</b><br/>
                <span style="color:#777">{status}</span><br/><br/>
                <b>{category}</b><br/>
                {experience}
                </div>
            """,
            "style": {"backgroundColor": "white", "color": "#12355b"},
        },
    )
    st.pydeck_chart(deck, use_container_width=True)

    st.caption(
        "🟡 HOME = Lahug Barangay Hall　 🟢/🟣/🔵/🟠 = Potential Experience Spots"
    )

with info_col:
    st.markdown("""
    <div class="card">
      <h3>🏠 HOME</h3>
      <p><b>Lahug Barangay Hall</b></p>
      <p>Every child starts here.</p>
      <p>① Receive your Passport<br>
      ② Choose an Experience<br>
      ③ Go out into the community<br>
      ④ Return and record your discovery<br>
      ⑤ Unlock the next Experience</p>
    </div>
    """, unsafe_allow_html=True)

    selected = st.selectbox(
        "Experience spot",
        experience_spots["name"].tolist(),
        index=0,
    )
    row = experience_spots.loc[experience_spots["name"] == selected].iloc[0]
    st.markdown(f"**{row['category']}**")
    st.write(row["experience"])

st.markdown("#### Experience journey")
st.markdown(
    """
    **🏠 HOME — Lahug Barangay Hall**  
    ↓ *Choose an experience*  
    **📍 Go to an Experience Spot**  
    ↓ *Try something new*  
    **✨ Discover something about yourself**  
    ↓ *Return / record it in the Passport*  
    **🔓 Unlock the next experience**
    """
)


st.header("Try the Unlock demo")
st.write("This demo shows how new experiences can be unlocked based on the number of completed experiences in the Passport.")

completed = st.slider("Completed experiences", 0, 10, 3)

if completed < 3:
    next_unlock = 3
    label = "🔒 Special Experience"
elif completed < 5:
    next_unlock = 5
    label = "🔒 Behind-the-Scenes Experience"
elif completed < 8:
    next_unlock = 8
    label = "🔒 Leadership Challenge"
else:
    next_unlock = 10
    label = "🔒 Create Your Own Experience"

m1, m2, m3 = st.columns(3)
with m1:
    st.markdown(f'<div class="metric-box"><b>{completed}</b>Experiences completed</div>', unsafe_allow_html=True)
with m2:
    st.markdown(f'<div class="metric-box"><b>{max(0, next_unlock-completed)}</b>Until next Unlock</div>', unsafe_allow_html=True)
with m3:
    st.markdown(f'<div class="metric-box"><b>{"OPEN" if completed >= 3 else "LOCKED"}</b>Unlock status</div>', unsafe_allow_html=True)

st.progress(completed / 10)

if completed >= 8:
    st.success("🌟 UNLOCKED: Create Your Own Experience — Propose your own idea for the next experience you want to try.")
elif completed >= 5:
    st.success("🎤 UNLOCKED: Leadership Challenge — Try hosting, public speaking, event support, and other leadership challenges.")
elif completed >= 3:
    st.success("🏢 UNLOCKED: Special Experience — Access special programs and places children would not normally be able to experience.")
else:
    st.info(f"{label} — {3-completed} more Experience(s) needed")

st.divider()

# GROWTH LOOP
st.header("How the project grows")
g1, g2 = st.columns([1,1], gap="large")
with g1:
    st.markdown("""<div class="unlock">
    <h3>👧 Child Unlock</h3>
    <p>The more experiences a child completes, the more special experiences and roles are unlocked.</p>
    <hr>
    <h3>🏘️ Community Unlock</h3>
    <p>As participation grows, new companies, universities, and community partners can join, unlocking entirely new experiences.</p>
    </div>""", unsafe_allow_html=True)
with g2:
    st.markdown("""<div class="card">
    <h3>Growth Loop</h3>
    <p><b>Experience</b> → Stamp → Discover → Unlock → Share → New Partner → New Experience</p>
    <p>The more children explore, the more opportunities the community creates.</p>
    <p><b>The more children explore, the more opportunities the community unlocks.</b></p>
    </div>""", unsafe_allow_html=True)

st.divider()

# PARTNER CTA
st.header("For partners")
st.write("Instead of asking companies or local partners for a large sponsorship, HIGH HOPE! starts with one simple request: “Can you unlock one new experience for our children?”")
st.markdown("""
<div class="big-quote">
Can you unlock one new experience for our children?
</div>
""", unsafe_allow_html=True)

p1, p2, p3 = st.columns(3)
with p1:
    st.markdown("""<div class="card"><h3>🏢 Company</h3><p>Office visits, team challenges, conversations with employees, and more.</p></div>""", unsafe_allow_html=True)
with p2:
    st.markdown("""<div class="card"><h3>🎓 University</h3><p>Laboratory visits, campus exploration, workshops with students, and more.</p></div>""", unsafe_allow_html=True)
with p3:
    st.markdown("""<div class="card"><h3>🏘️ Barangay</h3><p>Turn local places, people, and community events into opportunities for meaningful experiences.</p></div>""", unsafe_allow_html=True)

st.markdown('<div class="footer-note">HIGH HOPE! demo concept • Experience Passport / Unlock System</div>', unsafe_allow_html=True)

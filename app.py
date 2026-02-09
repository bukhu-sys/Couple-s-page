import streamlit as st
import random
import time
from datetime import date
import streamlit.components.v1 as components

st.set_page_config(
    layout="wide",
    page_title="Our Cute App 💕",
    initial_sidebar_state="collapsed"
)

# =========================
# 💌 VALENTINE GATE STATE
# =========================
if "accepted" not in st.session_state:
    st.session_state.accepted = False

# =========================
# 💌 VALENTINE GATE
# =========================
if not st.session_state.accepted:

    gate_html = """
<div style="
    position:fixed; inset:0;
    background:linear-gradient(135deg,#ffc2db,#ffd6e7,#fff0f5);
    display:flex; justify-content:center; align-items:center;
    font-family:sans-serif;
">
  <div style="
        background:white;
        padding:40px;
        border-radius:30px;
        text-align:center;
        box-shadow:0 10px 40px rgba(0,0,0,0.15);
        width:360px;
  ">
    <h1>Will you be my Valentine? 💌</h1>
    <p>I made something cute for you… but first answer 🥺</p>

    <div id="btnRow" style="
        display:flex;
        justify-content:center;
        gap:18px;
        position:relative;
    ">
      <a href="?yes=1">
        <button style="
            background:#ff4d8d;color:white;border:none;
            padding:16px 26px;border-radius:999px;
            font-size:18px;cursor:pointer;">
            YES 💖
        </button>
      </a>

      <button id="noBtn" style="
            background:#eee;border:none;
            padding:16px 26px;border-radius:999px;
            font-size:18px;cursor:pointer;
            position:relative;
            transition: transform .25s ease;">
            No 🙈
      </button>
    </div>
  </div>
</div>

<script>
const btn = document.getElementById("noBtn");

function moveBtn(){
  const dx = (Math.random()*120) - 60;
  const dy = (Math.random()*80) - 40;
  btn.style.transform = `translate(${dx}px, ${dy}px)`;
}

btn.onclick = moveBtn;
btn.onmouseenter = moveBtn;
btn.ontouchstart = moveBtn;
</script>
"""

    components.html(gate_html, height=900)

    if "yes" in st.query_params:
        st.session_state.accepted = True
        st.query_params.clear()
        st.rerun()

    st.stop()

# =========================
# 🎀 THEME + FULLSCREEN FIX
# =========================
st.markdown("""
<style>

#MainMenu, header, footer {visibility:hidden;}
[data-testid="stToolbar"] {display:none;}

html, body, [data-testid="stAppViewContainer"] {
    background: linear-gradient(135deg,#ffb6d9,#ffd6ec) !important;
    color:#6b003a;
}

/* Hide the Streamlit Toolbar (the 'Deploy', 'View Source', etc. buttons) */
header {visibility: hidden;}

/* Hide the Main Menu (Hamburger icon) */
#MainMenu {visibility: hidden;}

/* Hide the footer (made with streamlit) */
footer {visibility: hidden;}

.block-container {
    max-width: 100vw !important;
    padding-top: 0rem !important;
    padding-left: 2rem !important;
    padding-right: 2rem !important;
}
section.main > div {
    max-width: 100vw !important;
}

.card {
    background: rgba(255,255,255,0.95);
    border-radius:20px;
    padding:22px;
    box-shadow:0 8px 24px rgba(0,0,0,0.12);
    text-align:center;
    margin-bottom:22px;   
}
            
@media (max-width:600px){
    .block-container {
        padding-left: 0.5rem !important;
        padding-right: 0.5rem !important;
    }
}

.stButton button {
    background: linear-gradient(135deg,#ff6fa3,#ff3d7a) !important;
    color:white !important;
    border-radius:25px !important;
    font-weight:700 !important;
    width:100%;
    border:none !important;
}

.badge {
    display:inline-block;
    background:#ff4f8b;
    color:white;
    padding:6px 12px;
    border-radius:15px;
    margin:4px;
    font-weight:600;
}

@keyframes floatUp {
0% { transform:translateY(0); }
100% { transform:translateY(-120vh); }
}

@keyframes pop {
from {transform:scale(.8);opacity:0;}
to {transform:scale(1);opacity:1;}
}

</style>
""", unsafe_allow_html=True)

# =========================
# 🔊 SOUND ENGINE (ADDED — nothing removed)
# =========================
components.html("""
<script>
const sounds = {
 spin: new Audio("https://assets.mixkit.co/active_storage/sfx/2003/2003-preview.mp3"),
 win: new Audio("https://assets.mixkit.co/active_storage/sfx/2018/2018-preview.mp3"),
 redeem: new Audio("https://assets.mixkit.co/active_storage/sfx/1114/1114-preview.mp3"),
 reason: new Audio("https://assets.mixkit.co/active_storage/sfx/2571/2571-preview.mp3")
};
function playSound(n){
 if(sounds[n]){sounds[n].currentTime=0;sounds[n].play();}
}
</script>
""", height=0)

# =========================
# 💗 FLOATING HEARTS BG
# =========================
if "bg_hearts" not in st.session_state:
    st.session_state.bg_hearts = [
        (random.randint(0,100),
         random.randint(16,36),
         random.uniform(10,22),
         random.uniform(0,12),
         random.choice(["💖","💕","💗","💓","💞"]))
        for _ in range(60)
    ]

for l,s,dur,dly,e in st.session_state.bg_hearts:
    st.markdown(
        f"<div style='position:fixed;bottom:-40px;left:{l}%;font-size:{s}px;opacity:.25;pointer-events:none;animation:floatUp {dur}s linear {dly}s infinite'>{e}</div>",
        unsafe_allow_html=True
    )

# =========================
# ❤️ HEART BURST
# =========================
def heart_burst(n=25):
    html=""
    for _ in range(n):
        html += f"<div style='position:fixed;left:{random.randint(0,100)}%;bottom:-20px;font-size:{random.randint(20,42)}px;animation:floatUp {random.uniform(2,4)}s linear'>{random.choice(['💖','💗','💓','💞'])}</div>"
    st.markdown(html, unsafe_allow_html=True)

# =========================
# HERO INTRO (YES CELEBRATION)
# =========================
st.markdown("""
<div style="height:420px;display:flex;flex-direction:column;
justify-content:center;align-items:center;text-align:center;
animation: pop .6s ease;">
<h1 style="font-size:54px;">Yaaay you said YES!! 💖🥹💞</h1>
<p style="font-size:22px;opacity:.9;">
Welcome to our little love space ✨<br>
Scroll down for surprises ↓
</p>
<div style="font-size:34px;margin-top:18px;">
💗 💓 💕 💞 💖
</div>
</div>
""", unsafe_allow_html=True)

# =========================
# STATE
# =========================
if "used" not in st.session_state: st.session_state.used=[]
if "spin_result" not in st.session_state: st.session_state.spin_result=None
if "wheel_wins" not in st.session_state: st.session_state.wheel_wins=[]

# =========================
# COUNTER
# =========================
anniversary=date(2025,10,17)
days=(date.today()-anniversary).days

c1,c2,c3=st.columns(3)
c1.markdown(f"<div class='card'><h2>{days}</h2>Days</div>",unsafe_allow_html=True)
c2.markdown(f"<div class='card'><h2>{round(days/30.4,1)}</h2>Months</div>",unsafe_allow_html=True)
c3.markdown(f"<div class='card'><h2>{round(days/365,2)}</h2>Years</div>",unsafe_allow_html=True)

# =========================
# COUPONS
# =========================
st.markdown("## 🎟 Love Coupons")

available=[
"Vent Pass 🗣️","Photo Session 📸","Snack Delivery 🍟",
"Win Argument 🏆","Pick Outfit 👕","No Chores Day 🛋️"
]

remaining=max(0,3-len(st.session_state.used))

pick=st.multiselect(f"Pick rewards ({remaining} left)",available,disabled=remaining==0)

if st.button("Redeem 💝"):
    components.html("<script>playSound('redeem')</script>", height=0)
    for p in pick[:remaining]:
        if p not in st.session_state.used:
            st.session_state.used.append(p)
    heart_burst()
    st.rerun()

# =========================
# 🎡 Love Wheel
# =========================
st.markdown("## 🎡 Love Wheel")

spins_left = 3 - len(st.session_state.wheel_wins)
st.caption(f"🎯 Unique rewards left: {max(spins_left,0)}")

wheel_items=[
("💋","Kiss"),("🎬","Movie"),("💆","Massage"),
("🍫","Snack"),("🤗","Hug"),("✅","Yes Day")
]

slice_colors=[
"#ff4f8b","#ffd6ec",
"#ff7ab6","#ffe4f1",
"#ff6fa3","#ffc2da"
]

deg=360/len(wheel_items)

if "spin_target" not in st.session_state:
    st.session_state.spin_target=0

if st.button("Spin 💗"):

    components.html("<script>playSound('spin')</script>", height=0)

    idx = random.randint(0, len(wheel_items)-1)
    label = f"{wheel_items[idx][1]} {wheel_items[idx][0]}"

    stop = -(idx*deg + deg/2)
    st.session_state.spin_target = 360*5 + stop
    st.session_state.spin_result = label

    if label not in st.session_state.wheel_wins and len(st.session_state.wheel_wins) < 3:
        st.session_state.wheel_wins.append(label)
        if label not in st.session_state.used:
            st.session_state.used.append(label)

    heart_burst()
    st.rerun()

grad=""
cur=0
for c in slice_colors:
    grad+=f"{c} {cur}deg {cur+deg}deg,"
    cur+=deg
grad=grad.rstrip(",")

emoji_html=""
for i,(emoji,_) in enumerate(wheel_items):
    angle=i*deg+deg/2
    emoji_html+=f"""
    <div style="position:absolute;left:50%;top:50%;
    transform:translate(-50%,-50%) rotate({angle}deg)
    translateY(-110px) rotate(-{angle}deg);
    font-size:30px;">{emoji}</div>
    """

wheel_html=f"""
<div style="position:relative;width:min(92vw,300px);height:min(92vw,300px);margin:auto;">
<div style="position:absolute;top:-26px;left:50%;
transform:translateX(-50%);font-size:30px;">▼</div>

<div style="
width:100%;height:100%;
border-radius:50%;
border:10px solid white;
animation:spin 3.2s cubic-bezier(.15,0,.15,1) forwards;
background:conic-gradient({grad});
position:relative;">
{emoji_html}
</div></div>

<style>
@keyframes spin {{
to {{transform:rotate({st.session_state.spin_target}deg);}}
}}
</style>
"""

components.html(wheel_html,height=340)

if st.session_state.spin_result:
    time.sleep(3.2)
    components.html("<script>playSound('win')</script>", height=0)
    st.success(f"🎉 You got: {st.session_state.spin_result}")

# =========================
# 💌 COLLECTION — CARD STYLE (OLD ONE)
# =========================
if st.session_state.used:
    st.markdown("## 💌 Your Collection")
    st.caption("📸 Send me the screenshot of your collection 💌")


    cols = st.columns(3)
    for i, item in enumerate(st.session_state.used):
        cols[i % 3].markdown(f"""
        <div class='card' style="animation:pop .35s ease;">
            <h3>✓</h3>
            <p style="font-size:18px;font-weight:600;">{item}</p>
        </div>
        """, unsafe_allow_html=True)

# =========================
# WHY
# =========================
st.markdown("## 💖 Why I Love You")

reasons=[
"Your smile fixes everything",
"Your laugh is my favorite sound",
"You feel like home",
"Life is better with you"
]

if st.button("Tell Me Why 💗"):
    components.html("<script>playSound('reason')</script>", height=0)
    heart_burst()
    st.markdown(f"<div class='card' style='animation:pop .4s ease'>{random.choice(reasons)}</div>",
    unsafe_allow_html=True)

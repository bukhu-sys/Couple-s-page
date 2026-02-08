import streamlit as st
import random
import time
from datetime import date
import streamlit.components.v1 as components

st.set_page_config(layout="centered", page_title="Our Cute App")

# ---------- THEME ----------
st.markdown("""
<style>
html, body, [data-testid="stAppViewContainer"] {
    background: linear-gradient(135deg,#ffb6d9,#ffd6ec) !important;
    color:#6b003a;
}

.block-container { padding-top:0rem; }

.big-intro {
    height:520px;
    display:flex;
    flex-direction:column;
    justify-content:center;
    align-items:center;
    text-align:center;
}

.card {
    background: rgba(255,255,255,0.9);
    border-radius:20px;
    padding:18px;
    box-shadow:0 4px 15px rgba(0,0,0,0.1);
    text-align:center;
}

.stButton button {
    background: linear-gradient(135deg,#ff6fa3,#ff3d7a) !important;
    color:white !important;
    border-radius:25px !important;
    font-weight:700 !important;
    width:100%;
}

.badge {
    display:inline-block;
    background:#ff4f8b;
    color:white;
    padding:6px 12px;
    border-radius:15px;
    margin:4px;
}

.heart-bg {
    position: fixed;
    bottom:-40px;
    opacity:.35;
    pointer-events:none;
}

@keyframes floatUp {
0% { transform:translateY(0); }
100% { transform:translateY(-120vh); }
}
</style>
""", unsafe_allow_html=True)

# ---------- FLOATING HEARTS ----------
if "bg_hearts" not in st.session_state:
    st.session_state.bg_hearts = [
        (random.randint(0,100),
         random.randint(18,34),
         random.uniform(8,18),
         random.uniform(0,10),
         random.choice(["💖","💕","💗","💓"]))
        for _ in range(45)
    ]

for l,s,dur,dly,e in st.session_state.bg_hearts:
    st.markdown(
        f"<div class='heart-bg' style='left:{l}%;font-size:{s}px;animation:floatUp {dur}s linear {dly}s infinite'>{e}</div>",
        unsafe_allow_html=True
    )

# ---------- INTRO SECTION ----------
st.markdown("""
<div class="big-intro">
<h1>💝 Our Cute App 💝</h1>
<p>Scroll down for surprises ↓</p>
</div>
""", unsafe_allow_html=True)

# ---------- HEART BURST ----------
def heart_burst():
    html=""
    for _ in range(25):
        html+=f"<div class='heart-bg' style='left:{random.randint(0,100)}%;font-size:{random.randint(20,45)}px;animation:floatUp {random.uniform(2,4)}s ease-out'>{random.choice(['💖','💗','💓'])}</div>"
    st.markdown(html, unsafe_allow_html=True)

# ---------- STATE ----------
if "used" not in st.session_state: st.session_state.used=[]
if "wheel_saved" not in st.session_state: st.session_state.wheel_saved=False
if "spin_target" not in st.session_state: st.session_state.spin_target=0
if "spin_result" not in st.session_state: st.session_state.spin_result=None

# ---------- COUNTER ----------
anniversary=date(2025,10,17)
days=(date.today()-anniversary).days
c1,c2,c3=st.columns(3)
c1.markdown(f"<div class='card'><h2>{days}</h2>Days since we met</div>",unsafe_allow_html=True)
c2.markdown(f"<div class='card'><h2>{round(days/30.4,1)}</h2>Months since we met</div>",unsafe_allow_html=True)
c3.markdown(f"<div class='card'><h2>{round(days/365,2)}</h2>Years since we met</div>",unsafe_allow_html=True)

# ---------- FIRSTS ----------
st.markdown("## 💌 Our Firsts")
f1,f2,f3=st.columns(3)
f1.markdown("<div class='card'>💋 First Kiss</div>",unsafe_allow_html=True)
f2.markdown("<div class='card'>🤝 First Met</div>",unsafe_allow_html=True)
f3.markdown("<div class='card'>💕 First Love</div>",unsafe_allow_html=True)

# ---------- COUPONS (LIMIT 3) ----------
st.markdown("## 🎟 Love Coupons")

available=[
"Vent Pass 🗣️","Photo Session 📸","Snack Delivery 🍟",
"Win Argument 🏆","Pick Outfit 👕","No Chores Day 🛋️"
]

coupon_used=[x for x in st.session_state.used if not x.startswith("Wheel:")]
remaining=max(0,3-len(coupon_used))

pick=st.multiselect(
f"Pick rewards (Remaining {remaining}/3)",
available,
disabled=remaining==0
)

if st.button("Redeem 💝", disabled=remaining==0):
    for p in pick[:remaining]:
        if p not in st.session_state.used:
            st.session_state.used.append(p)
    if pick:
        heart_burst()
        st.rerun()

# ---------- COLOR SEGMENT WHEEL ----------
st.markdown("## 🎡 Love Wheel")

wheel_items=[
("💋","Kiss"),("🎬","Movie"),("💆","Massage"),
("🍫","Snack"),("🤗","Hug"),("✅","Yes Day")
]

# alternating strong slice colors
slice_colors=[
"#ff4f8b","#ffd6ec",
"#ff7ab6","#ffe4f1",
"#ff6fa3","#ffc2da"
]

deg=360/len(wheel_items)

if st.button("Spin 💗"):
    idx=random.randint(0,len(wheel_items)-1)
    stop=-(idx*deg+deg/2)
    st.session_state.spin_target=360*5+stop
    result=f"Wheel: {wheel_items[idx][1]} {wheel_items[idx][0]}"
    st.session_state.spin_result=result
    if not st.session_state.wheel_saved:
        st.session_state.used.append(result)
        st.session_state.wheel_saved=True
    st.rerun()

# build conic gradient slices
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
    translateY(-92px) rotate(-{angle}deg);
    font-size:28px;">{emoji}</div>
    """

wheel_html=f"""
<div style="position:relative;width:260px;height:260px;margin:auto;">
<div style="position:absolute;top:-22px;left:50%;
transform:translateX(-50%);font-size:28px;">▼</div>

<div style="
width:100%;height:100%;
border-radius:50%;
border:8px solid white;
animation:spin 3s cubic-bezier(.15,0,.15,1) forwards;
background:conic-gradient({grad});
position:relative;">
{emoji_html}
</div></div>

<style>
@keyframes spin {{
from {{transform:rotate(0deg);}}
to {{transform:rotate({st.session_state.spin_target}deg);}}
}}
</style>
"""

components.html(wheel_html,height=300)

if st.session_state.spin_result:
    time.sleep(3.1)
    heart_burst()
    st.success(st.session_state.spin_result)

# ---------- COLLECTION ----------
if st.session_state.used:
    st.markdown("## 💌 Your Collection")

    badges_html = " ".join(
        [f"<span class='badge'>✓ {c}</span>" for c in st.session_state.used]
    )

    st.markdown(f"""
    <div id="collection-box"
         style="background:rgba(255,255,255,0.9);
                padding:18px;
                border-radius:20px;
                text-align:center;">
        {badges_html}
    </div>
    """, unsafe_allow_html=True)

    # screenshot button (no change to your state)
    components.html("""
    <script src="https://html2canvas.hertzen.com/dist/html2canvas.min.js"></script>
    <button onclick="
        html2canvas(document.querySelector('#collection-box')).then(canvas => {
            const link = document.createElement('a');
            link.download = 'my-love-collection.png';
            link.href = canvas.toDataURL();
            link.click();
        });
    "
    style="
        margin-top:12px;
        padding:10px 18px;
        border:none;
        border-radius:20px;
        background:#ff4f8b;
        color:white;
        font-weight:700;
        cursor:pointer;
        width:100%;">
    📸 Send me the screenshot
    </button>
    """, height=70)


# ---------- WHY ----------
st.markdown("## 💖 Why I Love You")

reasons=[
"Your smile fixes everything",
"Your laugh is my favorite sound",
"You feel like home",
"Life is better with you"
]

if st.button("Tell Me Why 💗"):
    heart_burst()
    st.markdown(f"<div class='card'>{random.choice(reasons)}</div>",
    unsafe_allow_html=True)
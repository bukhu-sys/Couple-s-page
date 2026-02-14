import streamlit as st
import random
import time
from datetime import date
import streamlit.components.v1 as components

st.set_page_config(
    layout="wide",
    page_title="💕Will you be my valentine?💕",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0">
""", unsafe_allow_html=True)

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
        width:min(90vw, 360px);
  ">
    <h1>Will you be my Valentine? 💌</h1>
    <p>Би чамд нэг хөөрхөн зүйл бэлдсээн… гэхдээ эхлээд хариулаарай 🥺</p>

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
            Тэгье 💖
        </button>
      </a>

      <button id="noBtn" style="
            background:#eee;border:none;
            padding:16px 26px;border-radius:999px;
            font-size:18px;cursor:pointer;
            position:relative;
            transition: transform .25s ease;">
            Үгүй эээ 🙈
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
    overflow-x:hidden !important;
}

/* Make everything responsive */
.block-container {
    max-width: 100vw !important;
    padding-top: 1rem !important;
    padding-left: 1rem !important;
    padding-right: 1rem !important;
}

/* Remove weird negative spacing */
.block-container > div:first-child {
    margin-top: 0 !important;
}

/* CARD STYLE */
.card {
    background: rgba(255,255,255,0.95);
    border-radius:20px;
    padding:20px;
    box-shadow:0 6px 18px rgba(0,0,0,0.12);
    text-align:center;
    margin-bottom:18px;
}

/* Buttons */
.stButton button {
    background: linear-gradient(135deg,#ff6fa3,#ff3d7a) !important;
    color:white !important;
    border-radius:30px !important;
    font-weight:700 !important;
    width:100%;
    padding:16px !important;
    font-size:18px !important;
    border:none !important;
}

/* HERO TEXT RESPONSIVE */
.hero-title {
    font-size: clamp(32px, 7vw, 56px);
    text-align:center;
}

.hero-sub {
    font-size: clamp(16px, 4.5vw, 22px);
    text-align:center;
}

/* Make columns stack nicely on mobile */
@media (max-width: 768px) {

    .block-container {
        padding-left: 0.7rem !important;
        padding-right: 0.7rem !important;
    }

    h1, h2, h3 {
        text-align:center;
    }

    .stColumns {
        flex-direction: column !important;
        gap: 12px !important;
    }

}

@keyframes floatUp {
0% {
    transform: translateY(0) scale(0.8);
    opacity: 0;
}
10% {
    opacity: 0.4;
}
50% {
    transform: translateY(-60vh) translateX(10px) scale(1);
    opacity: 0.7;
}
100% {
    transform: translateY(-120vh) translateX(-10px) scale(1.2);
    opacity: 0;
}
}


@keyframes pop {
from {transform:scale(.9);opacity:0;}
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
    f"<div style='position:fixed;bottom:-40px;left:{l}%;font-size:{s}px;opacity:.35;pointer-events:none;animation:floatUp {dur}s ease-in-out {dly}s infinite'>{e}</div>",
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
# HERO INTRO — TOP (NO EMPTY SPACE)
# =========================
st.markdown("""
<div style="
display:flex;
flex-direction:column;
align-items:center;
text-align:center;
animation: pop .6s ease;
padding-top:20px;
">

<h1 class="hero-title">
Yaaay чи зөвшөөрчихлөө!! 💖🥹💞
</h1>

<p class="hero-sub">
Бидний бяцхан хайрын орчинп тавтай морил ✨<br>
Доош нь гүйлгээрэй surprise байгаа шүү ↓
</p>

<div style="font-size:clamp(24px,6vw,36px);margin-top:15px;">
💗 💓 💕 💞 💖
</div>

</div>
""", unsafe_allow_html=True)

# ===== SCROLL SPACER AFTER HERO =====
st.markdown("<div style='height:100vh'></div>", unsafe_allow_html=True)

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
c1.markdown(f"<div class='card'><h2>{days}</h2>Өдөр бодолд минь зөвхөн чи лл байлаа</div>",unsafe_allow_html=True)
c2.markdown(f"<div class='card'><h2>{round(days/30.4,1)}</h2>Сар хамгийн аз жаргалтайгаараа байлаа</div>",unsafe_allow_html=True)
c3.markdown(f"<div class='card'><h2>{round(days/365,2)}</h2>Жил надтай хамт байсанд баярлалаа</div>",unsafe_allow_html=True)

# =========================
# COUPONS
# =========================
st.markdown("## 🎟 Хайрын купон")

available=[
    "Хувийн Paparazzo 📸 (Таалагдсан зурагтай болтол чинь амаа татаад дарах болно)",
    "Movie night 🎬 (Мэдээж кино нь чиний сонголт байх болно)",
    "Амттан хүргэлт 🍟 (Хаана ч, хэзээ ч)",
    "TikTok хамтрагч (Би хүссэн бүжгийг чинь сураад цуг бүжиглэе)",
    "Style My Hair 💇‍♂️ (Миний дараагийн үсний засалт чиний гарт)",
    "Бидний playlist 🎵 (Хамтдаа хоюулаа сонсож болох playlist хийе)",
    "'Тийм' өдөр ✅ (Би 1 өдрийн туршид бүх зүйлд тийм гэх болно!)",
    "3 хүсэл (100 хүсэл гэсэн хүсэл байж болохгүй шүү хх)"
]

remaining=max(0,3-len(st.session_state.used))

pick=st.multiselect(f"Pick rewards ({remaining} left)",available,disabled=remaining==0)

if st.button("Баталгаажуулах 💝"):
    components.html("<script>playSound('redeem')</script>", height=0)
    for p in pick[:remaining]:
        if p not in st.session_state.used:
            st.session_state.used.append(p)
    heart_burst()
    st.rerun()

# =========================
# 🎡 Love Wheel
# =========================
st.markdown("## 🎡 Хайрын хүрд")

spins_left = 3 - len(st.session_state.wheel_wins)
st.caption(f"🎯 {max(spins_left,0)} боломж байгаа жү хөөрхнөө❤️")

wheel_items=[
    ("💋", "Үнсэлт"),
    ("🎬", "Movie Pick"),
    ("💆", "10-минутын Massage"),
    ("🍫", "Дуртай амттан"),
    ("🤗", "Удаан тэврэлт (1-2 min)"),
    ("✨", "Surprise Gift") 
]

slice_colors=[
"#ff4f8b","#ffd6ec",
"#ff7ab6","#ffe4f1",
"#ff6fa3","#ffc2da"
]

deg=360/len(wheel_items)

if "spin_target" not in st.session_state:
    st.session_state.spin_target=0

if st.button("Эргүүлэх 💗"):

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
<div style="position:relative;width:min(95vw,360px);height:min(95vw,360px);margin:auto;">
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
    st.markdown("## 💌 Цуглуулга")
    st.caption("📸 Screenshot хийгээд над руу явуулаарай 💌")

    for item in st.session_state.used:
        st.markdown(f"""
        <div class='card' style="animation:pop .35s ease;">
            <h3>✓</h3>
            <p style="font-size:18px;font-weight:600;">{item}</p>
        </div>
        """, unsafe_allow_html=True)

# =========================
# WHY
# =========================
st.markdown("## 💖 Би чамд хайртай 💖")

reasons = [
    "❤️Чамтай байхдаа би 100% өөрийнхөөрөө байж чаддаг.❤️",
    "❤️Жинхэнэ хайр, халамж гэж юу байдгийг чи л надад мэдрүүлсэн.❤️",
    "❤️Миний хэцүү үеийг тэвчээртэйгээр хуваалцдагт чинь.❤️",
    "❤️Чиний ачаар би өдөр бүр илүү дээр хүн болж өөрчлөгдөж байгаа.❤️",
    "❤️Чи бол миний амьдралын хэзээ ч алдаж болохгүй тэр нэгэн эрдэнэ.❤️",
    "❤️Чиний инээмсэглэл миний сэтгэл санааг хормын дотор засаж чаддаг.❤️",
    "❤️Гар чинь минийхтэй яг л таарч байгаа тэр мэдрэмж.❤️",
    "❤️Уулзах болгондоо яг л анхных шигээ догдолдог.❤️",
    "❤️Чиний дуу хоолой бол миний хамгийн сонсох дуртай аялгуу.❤️",
    "❤️Зөвхөн над руу л хардаг тэр нэгэн харц.❤️",
    "❤️Чимээгүй хамт суусан ч чиний дэргэд л хамгийн тухтай байдагт.❤️",
    "❤️Насан туршдаа зөвхөн чамайг л өдөж, ядаргаа болж амьдармаар байна.❤️",
    "❤️Миний уур, баяр хоёрыг чи л хамгийн сайн зохицуулдаг.❤️",
    "❤️Чамтай учрахаас өмнөх амьдрал 5/10 байсан бол одоо 11/10.❤️",
    "❤️Ирээдүйгээ харах болгонд хамгийн түрүүнд чи л харагддаг.❤️",
    "❤️Бидний цугтаа бүтээх ирээдүйг тэсэн ядан хүлээж байна.❤️",
]

if "love_index" not in st.session_state:
    st.session_state.love_index = 0

next_texts = [
    "Байжий дахиад байгаа 👀",
    "Дахиад нэг 😳",
]


if st.button("Яагаад гэвэл💗🙊"):
    st.session_state.love_index = 1
    components.html("<script>playSound('reason')</script>", height=0)
    heart_burst()

if st.session_state.love_index > 0:

    st.markdown(
        f"<div class='card' style='animation:pop .4s ease'>{reasons[st.session_state.love_index - 1]}</div>",
        unsafe_allow_html=True
    )

    if st.session_state.love_index < len(reasons):

        btn_text = next_texts[
            min(st.session_state.love_index - 1, len(next_texts) - 1)
        ]

        if st.button(btn_text):
            st.session_state.love_index += 1
            components.html("<script>playSound('reason')</script>", height=0)
            heart_burst()
            st.rerun()
    else:
        heart_burst()
        components.html("<script>playSound('reason')</script>", height=0)
        st.success("That’s not even all of it… I just ran out of space 🥹❤️")

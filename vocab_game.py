import time
import streamlit as st

st.title("⏱️ เกมเติมศัพท์จับเวลา")

for key in ["ans1_val", "ans2_val", "ans3_val", "ans4_val"]:
    if key not in st.session_state:
        st.session_state[key] = ""


def reset_game():
    st.session_state.ans1_val = ""
    st.session_state.ans2_val = ""
    st.session_state.ans3_val = ""
    st.session_state.ans4_val = ""
    st.session_state.start = time.time()
    st.session_state.is_ended = False


@st.dialog("📊 สรุปผลการเล่นเกม")
def show_result_dialog(ans1, ans2, ans3, ans4):
    st.balloons()
    score = 0
    answers = [ans1, ans2, ans3, ans4]
    correct = ["apple", "fish", "dog", "bird"]

    for i, (ans, correct_ans) in enumerate(zip(answers, correct), 1):
        u_ans = ans.strip().lower()
        if u_ans == correct_ans:
            st.success(f"✅ ข้อ {i}: ถูกต้อง")
            score += 1
        else:
            st.error(f"❌ ข้อ {i}: ยังไม่ถูกต้อง (คุณตอบ '{u_ans}')")

    st.info(f"🏆 ได้คะแนนรวม: {score} คะแนน")
    if score == 4:
        st.success("🎉 You win!")
    else:
        st.error("💀 You lose!")


st.button("🎮 เริ่มเล่นเกม", on_click=reset_game)

if "start" in st.session_state and not st.session_state.get("is_ended", False):
    time_left = int(30 - (time.time() - st.session_state.start))
    if time_left > 0:
        st.error(f"⏳ เหลือเวลา: {time_left} วินาที")
    else:
        st.session_state.is_ended = True
        st.rerun()

st.divider()

ans1 = st.text_input(
    "ข้อ 1: An `a _ _ l e` a day keeps the doctor away. 🍎",
    value=st.session_state.ans1_val,
)
ans2 = st.text_input(
    "ข้อ 2: Cats love to eat `f _ s h`. 🐟",
    value=st.session_state.ans2_val,
)
ans3 = st.text_input(
    "ข้อ 3: A `d _ g` is a man's best friend. 🐶",
    value=st.session_state.ans3_val,
)
ans4 = st.text_input(
    "ข้อ 4: A `b _ r d` can fly in the sky. 🐦",
    value=st.session_state.ans4_val,
)

st.session_state.ans1_val = ans1
st.session_state.ans2_val = ans2
st.session_state.ans3_val = ans3
st.session_state.ans4_val = ans4

if "start" in st.session_state and not st.session_state.get("is_ended", False):
    if st.button("📥 ส่งคำตอบ"):
        st.session_state.is_ended = True
        st.rerun()
    time.sleep(1)
    st.rerun()

if st.session_state.get("is_ended", False):
    show_result_dialog(ans1, ans2, ans3, ans4)

st.divider()
st.write("นางสาวดีใจ ยิ้มแย้ม เลขที่ 5 ม.4/5")

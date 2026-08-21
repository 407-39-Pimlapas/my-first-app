import streamlit as st
import time

st.title("⏱️ เกมเติมศัพท์จับเวลา")

# ----------------------------------------------------
# 1. กำหนดค่าเริ่มต้นใน session_state
# ----------------------------------------------------
if "ans1_val" not in st.session_state:
    st.session_state.ans1_val = ""

if "ans2_val" not in st.session_state:
    st.session_state.ans2_val = ""

if "ans3_val" not in st.session_state:
    st.session_state.ans3_val = ""

if "ans4_val" not in st.session_state:
    st.session_state.ans4_val = ""

if "start" not in st.session_state:
    st.session_state.start = None

if "is_ended" not in st.session_state:
    st.session_state.is_ended = False


# ----------------------------------------------------
# 2. ฟังก์ชันเริ่มเกมใหม่
# ----------------------------------------------------
def reset_game():
    st.session_state.ans1_val = ""
    st.session_state.ans2_val = ""
    st.session_state.ans3_val = ""
    st.session_state.ans4_val = ""

    st.session_state.start = time.time()
    st.session_state.is_ended = False


# ----------------------------------------------------
# 3. ฟังก์ชันแสดงผลคะแนน
# ----------------------------------------------------
@st.dialog("📊 สรุปผลการเล่นเกม")
def show_result_dialog(ans1, ans2, ans3, ans4):

    st.balloons()

    score = 0

    u_ans1 = ans1.strip().lower()
    u_ans2 = ans2.strip().lower()
    u_ans3 = ans3.strip().lower()
    u_ans4 = ans4.strip().lower()

    # ข้อ 1
    if u_ans1 == "apple":
        st.success("✅ ข้อ 1: ถูกต้อง")
        score += 1
    else:
        st.error(f"❌ ข้อ 1: ยังไม่ถูกต้อง (คุณตอบ '{u_ans1}')")

    # ข้อ 2
    if u_ans2 == "fish":
        st.success("✅ ข้อ 2: ถูกต้อง")
        score += 1
    else:
        st.error(f"❌ ข้อ 2: ยังไม่ถูกต้อง (คุณตอบ '{u_ans2}')")

    # ข้อ 3
    if u_ans3 == "pencil":
        st.success("✅ ข้อ 3: ถูกต้อง")
        score += 1
    else:
        st.error(f"❌ ข้อ 3: ยังไม่ถูกต้อง (คุณตอบ '{u_ans3}')")

    # ข้อ 4
    if u_ans4 == "banana":
        st.success("✅ ข้อ 4: ถูกต้อง")
        score += 1
    else:
        st.error(f"❌ ข้อ 4: ยังไม่ถูกต้อง (คุณตอบ '{u_ans4}')")

    # คะแนนรวม
    st.info(f"🏆 ได้คะแนนรวม: {score} / 4 คะแนน")

    if score == 4:
        st.success("🎉 You win!")
    else:
        st.error("💀 You lose!")


# ----------------------------------------------------
# 4. ปุ่มเริ่มเกม
# ----------------------------------------------------
st.button(
    "🎮 เริ่มเล่นเกม",
    on_click=reset_game
)


# ----------------------------------------------------
# 5. แสดงเวลานับถอยหลัง
# ----------------------------------------------------
if (
    st.session_state.start is not None
    and not st.session_state.is_ended
):

    time_left = int(
        30 - (time.time() - st.session_state.start)
    )

    if time_left > 0:
        st.error(f"⏳ เหลือเวลา: {time_left} วินาที")
    else:
        st.session_state.is_ended = True
        st.rerun()


st.divider()


# ----------------------------------------------------
# 6. ช่องกรอกคำตอบ
# ----------------------------------------------------
ans1 = st.text_input(
    "ข้อ 1: An `a _ _ l e` a day keeps the doctor away. 🍎",
    value=st.session_state.ans1_val
)

ans2 = st.text_input(
    "ข้อ 2: Cats love to eat `f _ s h`. 🐟",
    value=st.session_state.ans2_val
)

ans3 = st.text_input(
    "ข้อ 3: Student use to write `p _ n _ i l`. ✏️",
    value=st.session_state.ans3_val
)

ans4 = st.text_input(
    "ข้อ 4: Monkey love to eat `b _ n _ n _`. 🍌",
    value=st.session_state.ans4_val
)


# ----------------------------------------------------
# 7. บันทึกคำตอบ
# ----------------------------------------------------
st.session_state.ans1_val = ans1
st.session_state.ans2_val = ans2
st.session_state.ans3_val = ans3
st.session_state.ans4_val = ans4


# ----------------------------------------------------
# 8. ปุ่มส่งคำตอบ
# ----------------------------------------------------
if (
    st.session_state.start is not None
    and not st.session_state.is_ended
):

    if st.button("📥 ส่งคำตอบ"):

        st.session_state.is_ended = True
        st.rerun()

    # ทำให้เวลานับทุก 1 วินาที
    time.sleep(1)
    st.rerun()


# ----------------------------------------------------
# 9. แสดงผลลัพธ์
# ----------------------------------------------------
if st.session_state.is_ended:

    show_result_dialog(
        st.session_state.ans1_val,
        st.session_state.ans2_val,
        st.session_state.ans3_val,
        st.session_state.ans4_val
    )


st.divider()

st.write(
    "นางสาวพิมพ์ลภัส สายวงค์เปี้ย เลขที่ 39 ม.4/7"
)

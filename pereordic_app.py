import streamlit as st
import time

st.title("ทายชื่อธาตุจากสัญลักษณ์ธาตุ   หมู่ 1A-8A")

# ----------------------------------------------------
# 1. กำหนดค่าเริ่มต้นใน session_state
# ----------------------------------------------------
if "ans1_val" not in st.session_state:
    st.session_state.ans1_val = ""

if "ans2_val" not in st.session_state:
    st.session_state.ans2_val = ""

if "ans3_val" not in st.session_state:
    st.session_state.ans3_val = ""

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


    st.session_state.start = time.time()
    st.session_state.is_ended = False


# ----------------------------------------------------
# 3. ฟังก์ชันแสดงผลคะแนน
# ----------------------------------------------------
@st.dialog("📊 สรุปผลการเล่นเกม")
def show_result_dialog(ans1, ans2):

    st.balloons()

    score = 0

    u_ans1 = ans1.strip().lower()
    u_ans2 = ans2.strip().lower()
    u_ans3 = ans3.strip().lower()


# ข้อ 1
    if u_ans1 == "ลิเทียม":
        st.success("✅ ข้อ 1: ถูกต้อง")
        score += 1
    else:
        st.error(f"❌ ข้อ 1: ยังไม่ถูกต้อง (คุณตอบ '{u_ans1}')")

    # ข้อ 2
    if u_ans2 == "โซเดียม":
        st.success("✅ ข้อ 2: ถูกต้อง")
        score += 1
    else:
        st.error(f"❌ ข้อ 2: ยังไม่ถูกต้อง (คุณตอบ '{u_ans2}')")
# ข้อ 3
    if u_ans3 == "แคลเซียม":
        st.success("✅ ข้อ 3: ถูกต้อง")
        score += 1
    else:
        st.error(f"❌ ข้อ 3: ยังไม่ถูกต้อง (คุณตอบ '{u_ans3}')")

score = 3

if score == 3:
    st.success("🎉 ว้าววว คุณเก่งมาก")
elif 1 <= score <= 2:
    st.info("🎈 คุณพยายามอีกนิดนะ")
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
    "ข้อ 1: Li",
    value=st.session_state.ans1_val
)

ans2 = st.text_input(
    "ข้อ 2: Na",
    value=st.session_state.ans2_val
)
ans3 = st.text_input(
    "ข้อ 3: Ca",
    value=st.session_state.ans3_val
)


# ----------------------------------------------------
# 7. เก็บคำตอบลง session_state
# ----------------------------------------------------
st.session_state.ans1_val = ans1
st.session_state.ans2_val = ans2
st.session_state.ans3_val = ans3


# ----------------------------------------------------
# 8. ปุ่มส่งคำตอบ + Timer
# ----------------------------------------------------
if (
    st.session_state.start is not None
    and not st.session_state.is_ended
):

    if st.button("📥 ส่งคำตอบ", key="submit_answer"):

        st.session_state.is_ended = True
        st.rerun()

    # ทำให้เวลานับทุก 1 วินาที
    time.sleep(1)

    # ตรวจสอบอีกครั้งก่อน rerun
    if not st.session_state.is_ended:
        st.rerun()


# ----------------------------------------------------
# 9. แสดงผลลัพธ์
# ----------------------------------------------------
if st.session_state.is_ended:

    show_result_dialog(
        st.session_state.get("ans1_val", ""),
        st.session_state.get("ans2_val", ""),
        st.session_state.get("ans3_val", ""),
    )


st.divider()
st.write(
    "นางสาวพิมพ์ลภัส สายวงค์เปี้ย เลขที่ 39 ม.4/7"
)

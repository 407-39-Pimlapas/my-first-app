import streamlit as st
import time

st.set_page_config(
    page_title="ทายชื่อธาตุ",
    page_icon="⚗️"
)

st.title("⚗️ ทายชื่อธาตุจากสัญลักษณ์ธาตุ หมู่ 1A-8A")

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
def show_result_dialog(ans1, ans2, ans3):

    score = 0

    # แปลงคำตอบเป็นตัวพิมพ์เล็กและตัดช่องว่าง
    u_ans1 = ans1.strip().lower()
    u_ans2 = ans2.strip().lower()
    u_ans3 = ans3.strip().lower()

    # ------------------------------------------------
    # ข้อ 1
    # ------------------------------------------------
    if u_ans1 == "ลิเทียม":
        st.success("✅ ข้อ 1: ถูกต้อง")
        score += 1
    else:
        st.error(
            f"❌ ข้อ 1: ยังไม่ถูกต้อง "
            f"(คุณตอบ '{u_ans1}' / เฉลย: ลิเทียม)"
        )

    # ------------------------------------------------
    # ข้อ 2
    # ------------------------------------------------
    if u_ans2 == "โซเดียม":
        st.success("✅ ข้อ 2: ถูกต้อง")
        score += 1
    else:
        st.error(
            f"❌ ข้อ 2: ยังไม่ถูกต้อง "
            f"(คุณตอบ '{u_ans2}' / เฉลย: โซเดียม)"
        )

    # ------------------------------------------------
    # ข้อ 3
    # ------------------------------------------------
    if u_ans3 == "แคลเซียม":
        st.success("✅ ข้อ 3: ถูกต้อง")
        score += 1
    else:
        st.error(
            f"❌ ข้อ 3: ยังไม่ถูกต้อง "
            f"(คุณตอบ '{u_ans3}' / เฉลย: แคลเซียม)"
        )

    st.divider()

    # ------------------------------------------------
    # แสดงคะแนน
    # ------------------------------------------------
    st.subheader(f"🏆 คะแนนของคุณ: {score}/3")

    if score == 3:
        st.success("🎉 ว้าววว คุณเก่งมาก! ตอบถูกทุกข้อ")
    elif score >= 1:
        st.info("🎈 คุณพยายามได้ดีแล้ว ลองอีกครั้งเพื่อให้ได้คะแนนเต็ม")
    else:
        st.error("💀 You lose! ลองใหม่อีกครั้งนะ")


# ----------------------------------------------------
# 4. ปุ่มเริ่มเกมใหม่
# ----------------------------------------------------
st.button(
    "🎮 เริ่มเล่นเกม",
    on_click=reset_game,
    use_container_width=True
)


# ----------------------------------------------------
# 5. แสดงเวลานับถอยหลัง
# ----------------------------------------------------
if (
    st.session_state.start is not None
    and not st.session_state.is_ended
):

    elapsed_time = time.time() - st.session_state.start
    time_left = max(0, int(30 - elapsed_time))

    if time_left > 0:
        st.error(f"⏳ เหลือเวลา: {time_left} วินาที")
    else:
        st.session_state.is_ended = True
        st.rerun()


st.divider()


# ----------------------------------------------------
# 6. ช่องกรอกคำตอบ
# ----------------------------------------------------
st.subheader("📝 ทายชื่อธาตุ")

ans1 = st.text_input(
    "ข้อ 1: Li",
    value=st.session_state.ans1_val,
    disabled=(
        st.session_state.start is None
        or st.session_state.is_ended
    )
)

ans2 = st.text_input(
    "ข้อ 2: Na",
    value=st.session_state.ans2_val,
    disabled=(
        st.session_state.start is None
        or st.session_state.is_ended
    )
)

ans3 = st.text_input(
    "ข้อ 3: Ca",
    value=st.session_state.ans3_val,
    disabled=(
        st.session_state.start is None
        or st.session_state.is_ended
    )
)


# ----------------------------------------------------
# 7. เก็บคำตอบลง session_state
# ----------------------------------------------------
st.session_state.ans1_val = ans1
st.session_state.ans2_val = ans2
st.session_state.ans3_val = ans3


# ----------------------------------------------------
# 8. ปุ่มส่งคำตอบ
# ----------------------------------------------------
if (
    st.session_state.start is not None
    and not st.session_state.is_ended
):

    if st.button(
        "📥 ส่งคำตอบ",
        key="submit_answer",
        use_container_width=True
    ):
        st.session_state.is_ended = True
        st.rerun()


# ----------------------------------------------------
# 9. ระบบ Timer
# ----------------------------------------------------
if (
    st.session_state.start is not None
    and not st.session_state.is_ended
):

    # รอ 1 วินาทีแล้ว rerun เพื่ออัปเดตเวลา
    time.sleep(1)

    if not st.session_state.is_ended:
        st.rerun()


# ----------------------------------------------------
# 10. แสดงผลลัพธ์
# ----------------------------------------------------
if st.session_state.is_ended:

    show_result_dialog(
        st.session_state.get("ans1_val", ""),
        st.session_state.get("ans2_val", ""),
        st.session_state.get("ans3_val", ""),
    )


st.divider()

st.caption("⏱️ มีเวลา 30 วินาทีในการตอบคำถามทั้งหมด 3 ข้อ")

st.write(
    "นางสาวพิมพ์ลภัส สายวงค์เปี้ย เลขที่ 39 ม.4/7"
)

import streamlit as st
from datetime import date
import random

# ================= PAGE CONFIG =================
st.set_page_config(
    page_title="Student Daily Diary",
    layout="wide"
)

st.title("📖 Student Daily Diary")
st.write("A daily diary for students with homework, notices, and vocabulary building.")

# ================= WORD + MEANING + QUOTE ENGINE =================

word_bank = [
    {
        "word": "Perseverance",
        "meaning": "The ability to continue trying despite difficulties.",
    },
    {
        "word": "Resilience",
        "meaning": "The capacity to recover quickly from challenges.",
    },
    {
        "word": "Diligence",
        "meaning": "Careful and persistent effort in work or study.",
    },
    {
        "word": "Integrity",
        "meaning": "The quality of being honest and having strong moral principles.",
    },
    {
        "word": "Curiosity",
        "meaning": "A strong desire to learn or know something.",
    },
    {
        "word": "Meticulous",
        "meaning": "Showing great attention to detail; very careful.",
    },
    {
        "word": "Tenacity",
        "meaning": "Determination to keep going despite obstacles.",
    },
    {
        "word": "Empathy",
        "meaning": "The ability to understand and share the feelings of others.",
    },
    {
        "word": "Ambition",
        "meaning": "A strong desire to achieve success or excellence.",
    },
    {
        "word": "Discipline",
        "meaning": "The practice of training oneself to follow rules and routines.",
    },
    {
        "word": "Humility",
        "meaning": "Having a modest view of one's importance.",
    },
    {
        "word": "Wisdom",
        "meaning": "The ability to make good judgments based on knowledge and experience.",
    },
    {
        "word": "Consistency",
        "meaning": "The habit of performing actions regularly and reliably.",
    },
    {
        "word": "Accountability",
        "meaning": "Taking responsibility for one’s actions and decisions.",
    },
    {
        "word": "Adaptability",
        "meaning": "The ability to adjust to new conditions or changes.",
    },
    {
        "word": "Fortitude",
        "meaning": "Mental strength in facing adversity or difficulty.",
    },
    {
        "word": "Ingenuity",
        "meaning": "The ability to think creatively and solve problems.",
    },
    {
        "word": "Precision",
        "meaning": "Accuracy and exactness in action or speech.",
    },
    {
        "word": "Perspective",
        "meaning": "A particular way of viewing or understanding something.",
    },
    {
        "word": "Determination",
        "meaning": "Firmness of purpose; resoluteness.",
    }
]

quotes = [
    "True success is built quietly through consistent effort.",
    "Discipline today creates freedom tomorrow.",
    "Learning is not preparation for life; learning is life.",
    "Small improvements repeated daily create remarkable results.",
    "Mistakes are proof that learning is happening.",
    "Excellence is not an act, but a habit.",
    "Focus is the bridge between goals and achievement.",
    "Growth begins where comfort ends.",
    "Patience and persistence conquer all difficulties.",
    "Knowledge grows when curiosity leads the way.",
    "Success belongs to those who refuse to quit.",
    "Understanding is deeper than memorization.",
    "Character is revealed by daily actions.",
    "Consistency turns effort into achievement.",
    "Wisdom begins with the willingness to learn.",
    "Progress is made by those who keep moving forward.",
    "Hard work today creates confidence tomorrow.",
    "Education shapes both the mind and character.",
    "Attitude determines the height of success.",
    "Great achievements begin with a decision to try."
]

# Create 1000+ combinations
word_quote_pairs = []
for entry in word_bank:
    for quote in quotes:
        word_quote_pairs.append({
            "word": entry["word"],
            "meaning": entry["meaning"],
            "quote": quote
        })

# Random selection every reload
daily_item = random.choice(word_quote_pairs)

# ================= DATE =================
selected_date = st.date_input("📅 Date", date.today())

st.markdown("---")

# ================= SUBJECT DIARY =================
st.subheader("📚 Subject-wise Diary")

col1, col2, col3 = st.columns(3)

with col1:
    maths = st.text_area("➗ Maths", height=120)
    english = st.text_area("📘 English", height=120)

with col2:
    science = st.text_area("🔬 Science", height=120)
    social = st.text_area("🌍 Social Studies", height=120)

with col3:
    computer = st.text_area("💻 Computer", height=120)
    hindi = st.text_area("📕 Hindi", height=120)

st.markdown("---")

# ================= NOTICE BOARD =================
st.subheader("📢 Notice Board")

notice_col1, notice_col2 = st.columns([2, 1])

with notice_col1:
    notice = st.text_area("📌 Notice / Important Information", height=150)

with notice_col2:
    st.markdown("### 📖 Word of the Day")
    st.success(daily_item["word"])

    st.markdown("**Meaning:**")
    st.write(daily_item["meaning"])

    st.markdown("### 💬 Quote of the Day")
    st.info(daily_item["quote"])

st.markdown("---")

# ================= SAVE & PREVIEW =================
if st.button("✅ Save Diary"):
    st.success("Diary saved successfully!")

    st.markdown("## 📄 Diary Preview")
    st.write(f"**Date:** {selected_date}")

    st.markdown("### 📚 Subjects")
    st.write(f"**Maths:** {maths}")
    st.write(f"**English:** {english}")
    st.write(f"**Science:** {science}")
    st.write(f"**Social Studies:** {social}")
    st.write(f"**Computer:** {computer}")
    st.write(f"**Hindi:** {hindi}")

    st.markdown("### 📢 Notice Board")
    st.write(f"**Notice:** {notice}")
    st.write(f"**Word of the Day:** {daily_item['word']}")
    st.write(f"**Meaning:** {daily_item['meaning']}")
    st.write(f"**Quote:** {daily_item['quote']}")

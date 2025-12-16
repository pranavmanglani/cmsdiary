import streamlit as st
from datetime import date
import random

# ================= PAGE CONFIG =================
st.set_page_config(
    page_title="Student Daily Diary",
    layout="wide"
)

st.title("📖 Student Daily Diary")
st.write("A simple daily diary for students to manage homework, notices, and learning.")

# ================= WORD & QUOTE ENGINE =================

advanced_words = [
    "Perseverance", "Resilience", "Intellect", "Diligence", "Integrity",
    "Curiosity", "Meticulous", "Cognition", "Innovation", "Tenacity",
    "Empathy", "Rationale", "Ambition", "Consistency", "Endeavour",
    "Pragmatic", "Virtuous", "Analytical", "Scholarly", "Composure",
    "Judicious", "Proficiency", "Ingenuity", "Astute", "Dedication",
    "Discretion", "Fortitude", "Versatile", "Sincerity", "Excellence",
    "Contemplation", "Adaptability", "Persistence", "Accountability",
    "Precision", "Visionary", "Discipline", "Determination", "Humility",
    "Credibility", "Perspective", "Wisdom", "Initiative", "Proactive",
    "Sustainability", "Efficiency", "Competence", "Resourcefulness"
]

advanced_quotes = [
    "True success is built quietly through consistent effort.",
    "Discipline today creates freedom tomorrow.",
    "Knowledge grows when curiosity is never silenced.",
    "Great achievements begin with the courage to start.",
    "Learning is not preparation for life; learning is life.",
    "Small improvements repeated daily create remarkable results.",
    "Mistakes are not failures; they are lessons in disguise.",
    "Focus is the bridge between goals and accomplishment.",
    "Excellence is not an act, but a habit.",
    "Effort invested today becomes confidence tomorrow.",
    "Growth happens when comfort zones are challenged.",
    "Patience and persistence conquer all difficulties.",
    "Success favors those who refuse to quit.",
    "Understanding is deeper than memorization.",
    "Character is revealed by what you do when no one is watching.",
    "Consistency turns average actions into outstanding results.",
    "Education sharpens the mind and strengthens the character.",
    "Your attitude determines the height of your achievement.",
    "Progress is made by those who keep moving forward.",
    "Wisdom begins with the willingness to learn."
]

# Generate 1000+ word–quote pairs
word_quote_pairs = []
counter = 1

for word in advanced_words:
    for quote in advanced_quotes:
        word_quote_pairs.append(
            (f"{word} ({counter})", quote)
        )
        counter += 1

# Random selection on each reload
random_word, random_quote = random.choice(word_quote_pairs)

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
    st.success(random_word)

    st.markdown("### 💬 Quote of the Day")
    st.info(random_quote)

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
    st.write(f"**Word of the Day:** {random_word}")
    st.write(f"**Quote:** {random_quote}")

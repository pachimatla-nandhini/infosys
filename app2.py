import streamlit as st
import random

# ================= PAGE CONFIG =================
st.set_page_config(
    page_title="Melodia - AI Music Generator",
    page_icon="🎵",
    layout="wide"
)

# ================= CSS =================
st.markdown("""
<style>
.stApp {
    background:
        linear-gradient(rgba(0,0,0,0.65), rgba(0,0,0,0.65)),
        url("https://images.unsplash.com/photo-1511379938547-c1f69419868d");
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}
h1, h2, h3, label, p {
    color: white !important;
}
.stTextArea textarea {
    background-color: rgba(255,255,255,0.95);
}
.stButton>button {
    background-color: #ff4b4b;
    color: white;
    border-radius: 10px;
    padding: 10px 22px;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

# ================= SESSION STATE =================
if "input_history" not in st.session_state:
    st.session_state.input_history = []

if "user_input" not in st.session_state:
    st.session_state.user_input = ""

# ================= HEADER =================
st.title("🎶 Melodia – AI Music Generator")
st.subheader("Frontend Input Interface (Task 2)")
st.info("Tip: Include mood, tempo, and situation for better music results.")

# ================= INPUT AREA =================
st.markdown("### 🎼 Describe the music you want")

user_input = st.text_area(
    "",
    placeholder="E.g., energetic workout music with electronic beats",
    height=100,
    value=st.session_state.user_input
)

# Character counter
st.caption(f"Characters typed: {len(user_input)}")

# ================= MOOD SELECTOR =================
st.markdown("### 😊 Quick Mood")
mood = st.selectbox(
    "Choose Mood",
    ["Happy", "Sad", "Energetic", "Calm", "Romantic", "Dramatic"]
)

# ================= CONTEXT TAGS =================
st.markdown("### 📌 Context / Situation")
context = st.multiselect(
    "Select Context",
    ["Work", "Party", "Sleep", "Exercise", "Study", "Relaxation"]
)

# ================= EXAMPLE PROMPTS =================
st.markdown("### ✨ Example Prompts (Click to Auto-Fill)")

example_prompts = {
    "Happy": [
        "Upbeat pop music with cheerful vibes",
        "Joyful acoustic guitar with claps",
        "Bright summer music with positivity"
    ],
    "Sad": [
        "Slow piano music with emotional depth",
        "Melancholic violin background score",
        "Soft acoustic guitar heartbreak theme"
    ],
    "Energetic": [
        "High tempo EDM for workout",
        "Fast electronic beats for running",
        "Powerful rock music with heavy drums"
    ],
    "Calm": [
        "Soft piano music for meditation",
        "Ambient music with nature sounds",
        "Relaxing instrumental for stress relief"
    ],
    "Romantic": [
        "Gentle piano and violin love theme",
        "Romantic background music for dinner",
        "Warm acoustic guitar romance"
    ],
    "Dramatic": [
        "Epic cinematic orchestral music",
        "Suspenseful movie background score",
        "Dark dramatic soundtrack build-up"
    ]
}

examples = random.sample(example_prompts[mood], 2)
col1, col2 = st.columns(2)

if col1.button(examples[0]):
    st.session_state.user_input = examples[0]

if col2.button(examples[1]):
    st.session_state.user_input = examples[1]

# ================= VALIDATION =================
st.divider()
generate = st.button("🎵 Validate & Proceed")

if generate:
    if user_input.strip() == "":
        st.error("❌ Music description cannot be empty.")
    elif len(user_input) < 10:
        st.warning("⚠ Description too short. Please add more details.")
    else:
        final_prompt = f"{user_input} | Mood: {mood} | Context: {', '.join(context) if context else 'General'}"

        st.session_state.input_history.append(final_prompt)
        st.session_state.input_history = st.session_state.input_history[-5:]

        st.success("✅ Input validated successfully!")
        st.info("Backend AI music generation will be added in the next milestone.")

# ================= HISTORY =================
if st.session_state.input_history:
    st.markdown("### 🕒 Last 5 Inputs")
    for i, text in enumerate(st.session_state.input_history[::-1], 1):
        st.write(f"{i}. {text}")



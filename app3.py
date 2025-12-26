import streamlit as st
import time
import random

# =====================================================
# STEP 1: PAGE CONFIGURATION
# =====================================================
st.set_page_config(
    page_title="Melodia - AI Music Generator",
    page_icon="🎵",
    layout="wide"
)

# =====================================================
# STEP 2: BASIC STYLING
# =====================================================
st.markdown("""
<style>
.stApp {
    background:
        linear-gradient(rgba(0,0,0,0.65), rgba(0,0,0,0.65)),
        url("https://images.unsplash.com/photo-1511379938547-c1f69419868d");
    background-size: cover;
    background-position: center;
}
h1, h2, h3, p, label { color: white !important; }
.stButton>button {
    background-color: #ff4b4b;
    color: white;
    font-weight: bold;
    border-radius: 10px;
    padding: 10px 20px;
}
</style>
""", unsafe_allow_html=True)

# =====================================================
# STEP 3: SESSION STATE INITIALIZATION
# =====================================================
if "current_audio" not in st.session_state:
    st.session_state.current_audio = None

if "generation_params" not in st.session_state:
    st.session_state.generation_params = None

# =====================================================
# STEP 4: BACKEND MUSIC GENERATION PIPELINE (MOCK)
# (Replace later with real AI model)
# =====================================================
def generate_music_pipeline(user_input, mood, context):
    """
    Simulated backend music generation pipeline
    """
    # Simulate processing time
    time.sleep(2)

    # Fake output (no actual audio yet)
    audio_file = "generated_music_placeholder.wav"

    params = {
        "prompt": user_input,
        "mood": mood,
        "context": context,
        "duration": random.choice([20, 30, 40])
    }

    return audio_file, params, user_input

# =====================================================
# STEP 5: FRONTEND UI
# =====================================================
st.title("🎶 Melodia – AI Music Generator")
st.subheader("Task 2.3: Frontend – Backend Integration")

st.markdown("Describe the music you want and generate it using AI.")

# -----------------------------------------------------
# USER INPUT
# -----------------------------------------------------
user_input = st.text_area(
    "🎼 Music Description",
    placeholder="E.g., energetic workout music with electronic beats",
    height=100
)

mood = st.selectbox(
    "😊 Mood",
    ["Happy", "Sad", "Energetic", "Calm", "Romantic", "Dramatic"]
)

context = st.multiselect(
    "📌 Context / Situation",
    ["Work", "Party", "Sleep", "Exercise", "Study", "Relaxation"]
)

# =====================================================
# STEP 6: GENERATION WORKFLOW
# =====================================================
st.divider()

if st.button("🎵 Generate Music", type="primary"):

    # ---------- INPUT VALIDATION ----------
    if user_input.strip() == "":
        st.error("❌ Please enter a music description.")
    else:
        try:
            # ---------- PROGRESS INDICATORS ----------
            progress = st.progress(0)
            status = st.empty()

            status.info("Processing input...")
            progress.progress(30)
            time.sleep(1)

            status.info("Generating music...")
            progress.progress(60)

            # ---------- BACKEND CALL ----------
            audio_file, params, prompt = generate_music_pipeline(
                user_input, mood, context
            )

            progress.progress(90)
            status.info("Finalizing output...")
            time.sleep(1)

            progress.progress(100)
            status.success("✅ Music generation completed!")

            # ---------- STORE IN SESSION STATE ----------
            st.session_state.current_audio = audio_file
            st.session_state.generation_params = params

        except Exception as e:
            # =====================================================
            # STEP 7: ERROR HANDLING
            # =====================================================
            st.error("⚠ Something went wrong during music generation.")
            st.error(str(e))

            st.button("🔄 Retry")

# =====================================================
# STEP 8: DISPLAY OUTPUT
# =====================================================
if st.session_state.current_audio:
    st.markdown("### 🎧 Generated Music Output")
    st.info("Audio playback will be available after AI model integration.")

    st.markdown("### ⚙ Generation Parameters")
    st.json(st.session_state.generation_params)

# =====================================================
# STEP 9: STATUS CALL / DEMO NOTES
# =====================================================
st.divider()
st.markdown("""
### 📌 Status Call Demo Points
- End-to-end working application  
- Frontend → Backend pipeline connection  
- Live generation flow  
- Progress indicators & status messages  
- Error handling implemented  
""")

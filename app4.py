import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import wave
import uuid
import time
from datetime import datetime

# =====================================================
# PAGE CONFIG
# =====================================================
st.set_page_config(
    page_title="Melodia - AI Music Generator",
    page_icon="🎵",
    layout="wide"
)

# =====================================================
# BASIC STYLING
# =====================================================
st.markdown("""
<style>
.stApp {
    background:
        linear-gradient(rgba(0,0,0,0.65), rgba(0,0,0,0.65)),
        url("https://images.unsplash.com/photo-1511379938547-c1f69419868d");
    background-size: cover;
}
h1, h2, h3, p, label { color: white !important; }
.stButton>button {
    background-color: #ff4b4b;
    color: white;
    font-weight: bold;
    border-radius: 10px;
}
</style>
""", unsafe_allow_html=True)

# =====================================================
# SESSION STATE
# =====================================================
if "audio_file" not in st.session_state:
    st.session_state.audio_file = None

if "metadata" not in st.session_state:
    st.session_state.metadata = None

# =====================================================
# STEP 1: MOCK BACKEND AUDIO GENERATION
# =====================================================
def generate_audio():
    sample_rate = 22050
    duration = 3  # seconds
    t = np.linspace(0, duration, int(sample_rate * duration))
    audio = 0.5 * np.sin(2 * np.pi * 440 * t)

    file_name = "melodia_output.wav"

    with wave.open(file_name, "w") as f:
        f.setnchannels(1)
        f.setsampwidth(2)
        f.setframerate(sample_rate)
        f.writeframes((audio * 32767).astype(np.int16).tobytes())

    metadata = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "unique_id": str(uuid.uuid4()),
        "duration": duration,
        "sample_rate": sample_rate,
        "model": "Mock MusicGen v1"
    }

    return file_name, audio, metadata

# =====================================================
# UI HEADER
# =====================================================
st.title("🎶 Melodia – AI Music Generator")
st.subheader("Task 2.4: Output Display & Playback")

st.info("This section displays generated music output with playback and download options.")

# =====================================================
# GENERATE BUTTON
# =====================================================
if st.button("🎵 Generate Music"):
    with st.spinner("Generating music..."):
        time.sleep(2)
        audio_file, audio_data, metadata = generate_audio()

        st.session_state.audio_file = audio_file
        st.session_state.audio_data = audio_data
        st.session_state.metadata = metadata

        st.success("Music generated successfully!")

# =====================================================
# STEP 2: OUTPUT DISPLAY SECTION
# =====================================================
if st.session_state.audio_file:

    st.markdown("## 🎧 Audio Playback")
    st.audio(st.session_state.audio_file, format="audio/wav")

    # -------------------------------------------------
    # STEP 3: DOWNLOAD BUTTON
    # -------------------------------------------------
    with open(st.session_state.audio_file, "rb") as f:
        st.download_button(
            label="⬇ Download Audio",
            data=f,
            file_name=f"melodia_{int(time.time())}.wav",
            mime="audio/wav"
        )

    # -------------------------------------------------
    # STEP 4: GENERATION DETAILS
    # -------------------------------------------------
    with st.expander("📊 Generation Details"):
        st.write("**Original Input:** Demo music generation")
        st.write("**Extracted Parameters:**")
        st.progress(70)
        st.write("Mood: Calm")
        st.write("Energy: Medium")

        st.write("**Model Used:**", st.session_state.metadata["model"])
        st.write("**Generation Time:**", st.session_state.metadata["timestamp"])

    # -------------------------------------------------
    # STEP 5: WAVEFORM VISUALIZATION
    # -------------------------------------------------
    st.markdown("## 📈 Waveform Visualization")

    fig, ax = plt.subplots()
    ax.plot(st.session_state.audio_data)
    ax.set_title("Audio Waveform")
    ax.set_xlabel("Samples")
    ax.set_ylabel("Amplitude")
    st.pyplot(fig)

    # -------------------------------------------------
    # STEP 6: AUDIO PROPERTIES
    # -------------------------------------------------
    st.markdown("## 🎼 Audio Properties")
    st.write(f"Duration: {st.session_state.metadata['duration']} seconds")
    st.write(f"Sample Rate: {st.session_state.metadata['sample_rate']} Hz")

    # -------------------------------------------------
    # STEP 7: METADATA
    # -------------------------------------------------
    st.markdown("## 🧾 Generation Metadata")
    st.json(st.session_state.metadata)

import streamlit as st

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="🎵 AI Music Studio",
    page_icon="🎧",
    layout="centered"
)

# ---------------- SESSION STATE ----------------
if "page" not in st.session_state:
    st.session_state.page = "home"

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "users" not in st.session_state:
    st.session_state.users = {}

# ---------------- MUSIC THEME CSS ----------------
st.markdown("""
<style>
/* Full background */
.stApp {
    background-image: url("https://images.unsplash.com/photo-1511379938547-c1f69419868d");
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}

/* Dark overlay */
.stApp::before {
    content: "";
    position: fixed;
    inset: 0;
    background: rgba(0,0,0,0.55);
    z-index: -1;
}

/* Card */
.music-card {
    background: rgba(15,15,30,0.88);
    border-radius: 18px;
    padding: 30px;
    box-shadow: 0 0 25px rgba(0,255,255,0.4);
    animation: glow 3s infinite alternate;
}

/* Glow animation */
@keyframes glow {
    from { box-shadow: 0 0 15px #00ffff; }
    to { box-shadow: 0 0 35px #ff00ff; }
}

/* Headings */
h1, h2, h3 {
    color: #00ffff;
    text-align: center;
}

/* Buttons */
.stButton>button {
    background: linear-gradient(45deg, #00ffff, #ff00ff);
    color: black;
    font-weight: bold;
    border-radius: 25px;
    padding: 10px 20px;
    width: 100%;
}
</style>
""", unsafe_allow_html=True)

# ---------------- HOME ----------------
def home():
    st.markdown("<div class='music-card'>", unsafe_allow_html=True)
    st.title("🎶 AI Music Studio")

    if st.session_state.logged_in:
        st.success("🎧 Welcome back to your Music Studio!")

        if st.button("🚪 Logout"):
            st.session_state.logged_in = False
            st.session_state.page = "home"
            st.rerun()
    else:
        st.info("Create & explore AI-generated music")

        col1, col2 = st.columns(2)
        with col1:
            if st.button("🔑 Login"):
                st.session_state.page = "login"
                st.rerun()
        with col2:
            if st.button("📝 Signup"):
                st.session_state.page = "signup"
                st.rerun()

    st.markdown("</div>", unsafe_allow_html=True)

# ---------------- LOGIN ----------------
def login():
    st.markdown("<div class='music-card'>", unsafe_allow_html=True)
    st.title("🎧 Music Login")

    user = st.text_input("🎵 Username")
    pwd = st.text_input("🔐 Password", type="password")

    if st.button("Login 🎶"):
        if user in st.session_state.users and st.session_state.users[user] == pwd:
            st.success("🎉 Login successful!")
            st.session_state.logged_in = True
            st.session_state.page = "home"
            st.rerun()
        else:
            st.error("❌ Invalid credentials")

    if st.button("⬅ Back"):
        st.session_state.page = "home"
        st.rerun()

    st.markdown("</div>", unsafe_allow_html=True)

# ---------------- SIGNUP ----------------
def signup():
    st.markdown("<div class='music-card'>", unsafe_allow_html=True)
    st.title("🎼 Music Signup")

    user = st.text_input("🎤 Choose Username")
    pwd = st.text_input("🎹 Choose Password", type="password")

    if st.button("Create Account 🎵"):
        if user in st.session_state.users:
            st.warning("⚠ Username already exists")
        elif user == "" or pwd == "":
            st.warning("⚠ All fields required")
        else:
            st.session_state.users[user] = pwd
            st.success("🎉 Account created!")
            st.session_state.page = "login"
            st.rerun()

    if st.button("⬅ Back"):
        st.session_state.page = "home"
        st.rerun()

    st.markdown("</div>", unsafe_allow_html=True)

# ---------------- ROUTER ----------------
if st.session_state.page == "home":
    home()
elif st.session_state.page == "login":
    login()
elif st.session_state.page == "signup":
    signup()
import streamlit as st

# ================== PAGE CONFIG ==================
st.set_page_config(
    page_title="Melodia - AI Music Generator",
    page_icon="🎵",
    layout="wide"
)

# ================== CUSTOM CSS ==================
st.markdown("""
<style>
.stApp {
    background:
        linear-gradient(rgba(0,0,0,0.6), rgba(0,0,0,0.6)),
        url("https://images.unsplash.com/photo-1511379938547-c1f69419868d");
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}

h1, h2, h3, h4, p, label {
    color: white !important;
}

.stTextArea textarea {
    background-color: rgba(255,255,255,0.9);
}

.stButton>button {
    background-color: #ff4b4b;
    color: white;
    border-radius: 12px;
    padding: 12px 25px;
    font-size: 16px;
    font-weight: bold;
}

.sidebar .sidebar-content {
    background-color: rgba(0,0,0,0.8);
}
</style>
""", unsafe_allow_html=True)

# ================== SESSION STATE ==================
if "history" not in st.session_state:
    st.session_state.history = []

# ================== HEADER SECTION ==================
st.title("🎶 Melodia – AI Music Generator")
st.subheader("Create AI-powered music using simple text prompts")

st.markdown("""
**How it works:**
1. Describe the music you want  
2. Adjust duration & creativity  
3. Click *Generate Music*  
""")

st.divider()

# ================== SIDEBAR ==================
st.sidebar.header("🎛 Music Controls")

duration = st.sidebar.slider(
    "⏱ Duration (seconds)",
    min_value=10,
    max_value=120,
    value=30
)

temperature = st.sidebar.slider(
    "🎨 Creativity Level",
    min_value=0.1,
    max_value=1.0,
    value=0.7
)

genre = st.sidebar.selectbox(
    "🎼 Music Genre",
    ["Classical", "Pop", "Jazz", "Lo-fi", "Rock", "Ambient"]
)

with st.sidebar.expander("⚙ Advanced Settings"):
    tempo = st.selectbox("Tempo", ["Slow", "Medium", "Fast"])
    instruments = st.multiselect(
        "Instruments",
        ["Piano", "Guitar", "Violin", "Drums", "Synth"]
    )

# ================== MAIN INPUT ==================
st.markdown("### 🎼 Music Description")

prompt = st.text_area(
    "",
    placeholder="Example: Soft piano music with calm morning vibes",
    height=120
)

# ================== EXAMPLE PROMPTS ==================
st.markdown("### ✨ Example Prompts")
col1, col2, col3 = st.columns(3)

with col1:
    st.info("🎹 Calm piano with rain ambience")
with col2:
    st.info("🎸 Energetic rock music for workout")
with col3:
    st.info("🎧 Soft lo-fi beats for studying")

# ================== GENERATE BUTTON ==================
st.divider()
generate = st.button("🎶 Generate Music")

# ================== OUTPUT PLACEHOLDER ==================
if generate:
    if prompt.strip() == "":
        st.warning("⚠ Please enter a music description.")
    else:
        with st.spinner("🎵 Generating music..."):
            # Placeholder for backend AI integration
            st.session_state.history.append(prompt)

        st.success("✅ Music generated successfully (Placeholder)")
        st.info("""
        🎧 **Audio Output Placeholder**  
        (AI model integration will be added in next milestone)
        """)

# ================== HISTORY SECTION ==================
if st.session_state.history:
    st.markdown("### 🕒 Generation History")
    for i, item in enumerate(st.session_state.history[::-1], 1):
        st.write(f"{i}. {item}")
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
import streamlit as st
import uuid
import time
import json
from datetime import datetime

# =====================================================
# 1️⃣ PAGE CONFIG
# =====================================================
st.set_page_config(
    page_title="Melodia – History & Favorites",
    page_icon="🎵",
    layout="wide"
)

# =====================================================
# 2️⃣ BACKGROUND + STYLE
# =====================================================
st.markdown("""
<style>
.stApp {
    background:
        linear-gradient(rgba(0,0,0,0.65), rgba(0,0,0,0.65)),
        url("https://images.unsplash.com/photo-1511379938547-c1f69419868d");
    background-size: cover;
}
h1, h2, h3, p, label { color: pink !important; }
.card {
    background: rgba(255,255,255,0.08);
    padding: 15px;
    border-radius: 12px;
    margin-bottom: 12px;
}
</style>
""", unsafe_allow_html=True)

# =====================================================
# 3️⃣ SESSION STATE INITIALIZATION
# =====================================================
if "history" not in st.session_state:
    st.session_state.history = []

# =====================================================
# 4️⃣ APP HEADER
# =====================================================
st.title("🎶 Melodia – History & Favorites")
st.subheader("Task 2.5: Generation History Management")

# =====================================================
# 5️⃣ MOCK GENERATION INPUT
# =====================================================
st.markdown("### 🎼 Generate Music (Demo)")

prompt = st.text_input(
    "Music Description",
    placeholder="Example: Calm piano with emotional feel"
)

if st.button("🎵 Generate"):
    if prompt.strip() == "":
        st.warning("Please enter a prompt")
    else:
        with st.spinner("Generating music..."):
            time.sleep(1.5)

        record = {
            "id": str(uuid.uuid4()),
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "prompt": prompt,
            "audio_file": "melodia_output.wav",
            "params": {
                "mood": "Calm",
                "energy": "Medium"
            },
            "favorite": False
        }

        st.session_state.history.append(record)
        st.success("Music generated and added to history!")

# =====================================================
# 6️⃣ SIDEBAR – FILTERS & ACTIONS
# =====================================================
st.sidebar.title("📂 History Controls")

show_fav_only = st.sidebar.checkbox("❤️ Show Favorites Only")

if st.sidebar.button("🧹 Clear All History"):
    st.session_state.history = []
    st.sidebar.success("History cleared")

# =====================================================
# 7️⃣ HISTORY DISPLAY
# =====================================================
# =====================================================
st.markdown("## 🕒 Generation History")

if not st.session_state.get("history"):
    st.info("No history available yet.")
else:
    for index, item in enumerate(st.session_state.history):

        # Ensure item is a dictionary
        if not isinstance(item, dict):
            continue

        # Skip non-favorites if filter is on
        if show_fav_only and not item.get("favorite", False):
            continue

        # Display the card
        st.markdown('<div class="card" style="padding:10px; border:1px solid #ccc; border-radius:10px; margin-bottom:10px;">', unsafe_allow_html=True)
        
        st.write(f"**Prompt:** {item.get('prompt', 'N/A')}")
        st.write(f"**Timestamp:** {item.get('timestamp', 'N/A')}")
        
        params = item.get('params', {})
        st.write(f"**Mood:** {params.get('mood', 'N/A')}")
        st.write(f"**Energy:** {params.get('energy', 'N/A')}")

        st.markdown('</div>', unsafe_allow_html=True)


        # ▶ Replay (mock)
        with col1:
            st.audio(item["audio_file"])

        # ❤️ Favorite toggle
        with col2:
            if item["favorite"]:
                if st.button("💔 Remove Favorite", key=f"fav_{item['id']}"):
                    st.session_state.history[index]["favorite"] = False
            else:
                if st.button("❤️ Add Favorite", key=f"fav_{item['id']}"):
                    st.session_state.history[index]["favorite"] = True

        # ❌ Delete
        with col3:
            if st.button("🗑 Delete", key=f"del_{item['id']}"):
                st.session_state.history.pop(index)
                st.experimental_rerun()

        st.markdown('</div>', unsafe_allow_html=True)

# =====================================================
# 8️⃣ BATCH OPERATIONS
# =====================================================
st.markdown("## 📦 Batch Operations")

if st.session_state.history:

    # Export history as JSON
    history_json = json.dumps(st.session_state.history, indent=2)

    st.download_button(
        label="⬇ Export History as JSON",
        data=history_json,
        file_name="melodia_history.json",
        mime="application/json"
    )

# =====================================================
# 9️⃣ HISTORY STATISTICS
# =====================================================
st.markdown("## 📊 History Statistics")

total = len(st.session_state.history)
favorites = len([h for h in st.session_state.history if h["favorite"]])

st.metric("Total Generations", total)
st.metric("Favorites Count", favorites)    
import streamlit as st
import time
import uuid
from datetime import datetime

# =========================================================
# STEP 1️⃣ PAGE CONFIGURATION
# =========================================================
st.set_page_config(
    page_title="AI Music Generator – Advanced Features",
    page_icon="🎵",
    layout="wide"
)

# =========================================================
# STEP 2️⃣ FORCE TEXT VISIBILITY
# =========================================================
st.markdown("""
<style>
.stApp {
    background: linear-gradient(rgba(0,0,0,0.6), rgba(0,0,0,0.6)),
                url("https://images.unsplash.com/photo-1511379938547-c1f69419868d");
    background-size: cover;
}
html, body, label, span, div, p {
    color: red !important;
    font-weight: 500;
}
input, textarea {
    color: red !important;
    background-color: white !important;
}
.stButton>button {
    background-color: #ff4b4b;
    color: blue;
    border-radius: 8px;
}
.card {
    background: rgba(255,255,255,0.15);
    padding: 15px;
    border-radius: 12px;
    margin-bottom: 15px;
}
</style>
""", unsafe_allow_html=True)

# =========================================================
# STEP 3️⃣ SESSION STATE
# =========================================================
if "generations" not in st.session_state:
    st.session_state.generations = []

# =========================================================
# STEP 4️⃣ HEADER
# =========================================================
st.title("🎶 AI Music Generator – Advanced Features")
st.caption("Task 2.6: Backend & Frontend – Advanced Functionality")

# =========================================================
# STEP 5️⃣ BASE PROMPT INPUT
# =========================================================
st.subheader("🎼 Base Music Prompt")
base_prompt = st.text_area(
    "Describe the music",
    placeholder="Example: Calm piano music with emotional depth"
)

# =========================================================
# STEP 6️⃣ ADVANCED PARAMETERS
# =========================================================
with st.expander("⚙ Advanced Parameters"):
    col1, col2, col3 = st.columns(3)
    with col1:
        top_k = st.slider("Top-K", 10, 100, 50)
        top_p = st.slider("Top-P", 0.1, 1.0, 0.9)
    with col2:
        cfg = st.slider("CFG Coefficient", 1.0, 10.0, 5.0)
        duration = st.selectbox("Duration (seconds)", [30, 45, 60])
    with col3:
        expert_mode = st.checkbox("Expert Mode")

# =========================================================
# STEP 7️⃣ VARIATION GENERATION FUNCTION
# =========================================================
def generate_variations(prompt, count=3):
    # This is a placeholder for real audio generation
    variations = []
    for i in range(count):
        variations.append({
            "id": str(uuid.uuid4()),
            "prompt": f"{prompt} (Variation {i+1})",
            "audio": "sample_audio.wav",  # Replace with real audio path
            "timestamp": datetime.now().strftime("%H:%M:%S")
        })
    return variations

# =========================================================
# STEP 8️⃣ GENERATE VARIATIONS BUTTON
# =========================================================
if st.button("🎛 Generate 3 Variations"):
    if base_prompt.strip() == "":
        st.warning("Please enter a music description")
    else:
        with st.spinner("Generating variations..."):
            time.sleep(2)
        generated = generate_variations(base_prompt)
        st.session_state.generations.append({
            "base_prompt": base_prompt,
            "params": {"Top-K": top_k, "Top-P": top_p, "CFG": cfg, "Duration": duration},
            "variations": generated
        })
        st.success("Variations generated successfully!")

# =========================================================
# STEP 9️⃣ DISPLAY GENERATED VARIATIONS
# =========================================================
st.subheader("🎧 Generated Variations")
if not st.session_state.generations:
    st.info("No variations generated yet.")
else:
    latest = st.session_state.generations[-1]
    cols = st.columns(3)
    for col, var in zip(cols, latest["variations"]):
        with col:
            st.markdown('<div class="card">', unsafe_allow_html=True)
            st.markdown(f"**{var['prompt']}**")
            try:
                st.audio(var["audio"])
            except:
                st.info("Audio file not found. Please replace 'sample_audio.wav' with a valid file path.")
            st.button("👍 Vote Best", key=var["id"])
            st.markdown('</div>', unsafe_allow_html=True)

# =========================================================
# STEP 🔟 EXTEND MUSIC FEATURE
# =========================================================
st.subheader("⏩ Extend Existing Music")
extend_duration = st.selectbox("Extend by", ["+15 sec", "+30 sec"])
if st.button("🔁 Extend Music"):
    with st.spinner("Extending music..."):
        time.sleep(1.5)
    st.success(f"Music extended {extend_duration} successfully!")

# =========================================================
# STEP 1️⃣1️⃣ BATCH GENERATION
# =========================================================
st.subheader("📦 Batch Prompt Generation")
batch_prompts = st.text_area(
    "Enter multiple prompts (one per line)",
    placeholder="Prompt 1\nPrompt 2\nPrompt 3"
)
if st.button("🚀 Generate Batch"):
    prompts = [p for p in batch_prompts.split("\n") if p.strip()]
    if not prompts:
        st.warning("No valid prompts found")
    else:
        with st.spinner("Generating batch music..."):
            time.sleep(2)
        st.success(f"Generated music for {len(prompts)} prompts!")
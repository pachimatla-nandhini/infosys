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

# =========================================================



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
st.markdown("## 🕒 Generation History")

if not st.session_state.history:
    st.info("No history available yet.")
else:
    for index, item in enumerate(st.session_state.history):

        if show_fav_only and not item["favorite"]:
            continue

        st.markdown('<div class="card">', unsafe_allow_html=True)

        st.write(f"**Prompt:** {item['prompt']}")
        st.write(f"**Timestamp:** {item['timestamp']}")
        st.write(f"**Mood:** {item['params']['mood']}")
        st.write(f"**Energy:** {item['params']['energy']}")

        col1, col2, col3 = st.columns(3)

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

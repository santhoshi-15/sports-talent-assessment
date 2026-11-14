import streamlit as st

st.set_page_config(page_title="Exercise Results", layout="wide")

if "selected_exercise" not in st.session_state:
    st.error("⚠️ No exercise selected. Please go back and predict first.")
    st.stop()

ex_type = st.session_state["selected_exercise"]
result = st.session_state.get(f"result_{ex_type}")

if not result:
    st.error("⚠️ No results available for this exercise.")
    st.stop()

st.title(f"📊 Full Results - {ex_type}")

# Metrics
col1, col2, col3 = st.columns(3)
col1.metric("Exercise", ex_type)
col2.metric("Count/Reps", f"{result['count']:.2f}")
col3.metric("Qualified?", "✅ Yes" if result['qualified'] else "❌ No")

# Accuracy Bar
acc = result['acc']
if acc >= 80: color = "#2ECC71"
elif acc >= 50: color = "#F1C40F"
else: color = "#E74C3C"
st.markdown(f"""
    <div style="background-color: #ddd; border-radius: 10px; padding: 5px; margin-top: 5px;">
        <div style="width: {acc}%; background-color: {color}; padding: 10px; border-radius: 10px; color: white; font-weight: bold; text-align: center;">
            {acc:.2f}%
        </div>
    </div>
""", unsafe_allow_html=True)

# Features
st.subheader("📊 Extracted Features")
st.dataframe(result['features'].T, height=300)

# Video
st.subheader("🎬 Uploaded Video")
with open(result['video_path'], 'rb') as f:
    st.video(f.read())

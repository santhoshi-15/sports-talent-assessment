import streamlit as st

st.set_page_config(page_title="Final Results", layout="wide")

if "results" not in st.session_state or not st.session_state["results"]:
    st.error("⚠️ No results submitted yet. Please complete tests first.")
    st.stop()

results = st.session_state["results"]

st.title("🏅 Final Results Summary")

# Show results table
st.subheader("📊 Performance Summary")
rows = []
for ex, res in results.items():
    rows.append({
        "Exercise": ex,
        "Count/Reps": f"{res['count']:.2f}",
        "Accuracy (%)": f"{res['acc']:.2f}",
        "Qualified": "✅ Yes" if res['qualified'] else "❌ No"
    })

st.dataframe(rows, use_container_width=True)

# Overall Qualification
qualified_exercises = [ex for ex, r in results.items() if r['qualified']]
if len(qualified_exercises) >= 3:
    st.success("🎉 Congratulations! You are qualified for the next round!")
else:
    st.warning("⚠️ Not enough exercises qualified. Keep training and try again!")

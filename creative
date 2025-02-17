import streamlit as st

# App title
st.title("🚀 Creative Benchmarking Tool")
st.subheader("Evaluate Your Creative Idea with Industry Standards")

# Benchmark Criteria
criteria = {
    "Storytelling": "How well does the idea create an emotional and engaging narrative?",
    "Cultural Relevance": "Does the idea resonate with current cultural movements and diverse audiences?",
    "Innovation": "Is the concept fresh, original, and breaking new ground?",
    "Brand Alignment": "How well does it reinforce the brand’s identity and values?",
    "Data-Driven Impact": "Does it leverage insights and metrics for effectiveness?",
}

# Leo Burnett's Humankind Scale Descriptions
humankind_scale = {
    1: "Forgettable work, no impact.",
    2: "Generic execution, no emotional engagement.",
    3: "Basic creative, meets minimal standards.",
    4: "Solid work but lacks depth and cultural relevance.",
    5: "Good work, well-crafted but not remarkable.",
    6: "Effective work, connects with audiences but not groundbreaking.",
    7: "Great work, emotionally engaging and brand-aligned.",
    8: "Outstanding work, culturally relevant and highly engaging.",
    9: "Iconic work, industry-leading, shifts perspectives.",
    10: "Groundbreaking, becomes part of cultural history."
}

# User input for creative idea description
st.text_area("Describe your creative idea:", placeholder="Enter details about your concept...")

# User ratings
st.markdown("### Rate Your Idea on Each Benchmark Criterion")
scores = {}
for key, description in criteria.items():
    scores[key] = st.slider(f"**{key}** - {description}", min_value=1, max_value=10, value=5)

# Calculate results
if st.button("Evaluate Idea"):
    total_score = sum(scores.values())
    avg_score = total_score / len(scores)
    scale_feedback = humankind_scale[int(round(avg_score))]

    # Display results
    st.markdown(f"## 🔥 Your Benchmark Score: **{round(avg_score, 1)}/10**")
    st.info(f"**Feedback:** {scale_feedback}")

    # Additional recommendations
    st.markdown("### 🚀 Suggestions for Improvement:")
    if avg_score < 6:
        st.warning("Consider improving storytelling and emotional engagement.")
    if scores["Cultural Relevance"] < 6:
        st.warning("Ensure the idea resonates with cultural trends and diverse audiences.")
    if scores["Innovation"] < 6:
        st.warning("Push the boundaries of creativity to make the idea more unique.")

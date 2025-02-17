import streamlit as st

# Define Benchmarking Criteria
benchmark_criteria = {
    "Storytelling Power": "Does the idea emotionally connect with people?",
    "Innovation Level": "Is it groundbreaking, like Apple or Tesla?",
    "Cultural Relevance": "Is it aligned with trends, like Nike or Patagonia?",
    "Brand Fit": "Does it reinforce the brand identity?",
    "Engagement Potential": "Does it spark viral conversations, like Red Bull?"
}

# Iconic Brand Inspirations
brand_archetypes = {
    "Nike": "Powerful, motivational storytelling with cultural relevance.",
    "Apple": "Simplicity, design-driven innovation, emotional branding.",
    "Red Bull": "High-energy, adventure-driven content that excites.",
    "Patagonia": "Sustainability, mission-driven storytelling.",
    "Spotify": "Personalized, data-driven engagement.",
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

# App Header
st.title("🚀 Advanced Creative Benchmarking Tool")
st.subheader("Refine your idea with inspiration from iconic brands!")

# Step 1: Define the Idea
st.markdown("## Step 1: Describe Your Idea")
idea = st.text_area("Enter a brief description of your creative idea:", placeholder="What is your concept? What problem does it solve?")

# Step 2: Brand Entry Points
st.markdown("## Step 2: Which Brand Matches Your Vision?")
selected_brand = st.selectbox("Choose the brand closest to your idea:", list(brand_archetypes.keys()))
st.info(f"Your idea aligns with **{selected_brand}**: {brand_archetypes[selected_brand]}")

# Step 3: Benchmarking Criteria
st.markdown("## Step 3: Rate Your Idea")
scores = {}
for key, description in benchmark_criteria.items():
    scores[key] = st.slider(f"**{key}** - {description}", min_value=1, max_value=10, value=5)

# Step 4: Evaluation
if st.button("🔍 Evaluate My Idea"):
    total_score = sum(scores.values())
    avg_score = total_score / len(scores)
    scale_feedback = humankind_scale[int(round(avg_score))]

    # Display Results
    st.markdown(f"## 🔥 Your Benchmark Score: **{round(avg_score, 1)}/10**")
    st.info(f"**Feedback:** {scale_feedback}")

    # Advanced Insights Based on Selected Brand
    if avg_score < 6:
        st.warning(f"🚀 Try enhancing your idea with more **{selected_brand}-style storytelling.**")
    
    if scores["Innovation Level"] < 6:
        st.warning(f"💡 Think bigger! **{selected_brand} thrives on breaking barriers.** How can your idea be more groundbreaking?")
    
    if scores["Cultural Relevance"] < 6:
        st.warning(f"🌍 Make your idea more culturally relevant—look at how **{selected_brand} taps into trends!**")

# Step 5: Idea Refinement Suggestions
st.markdown("## 🎯 Idea Refinement")
st.write("Want to make your idea even stronger? Here are **three ways** you can improve it:")
st.write("1️⃣ Add **storytelling depth** like Nike—how can this idea emotionally connect?")
st.write("2️⃣ Make it **more disruptive** like Apple—how can you simplify while innovating?")
st.write("3️⃣ Enhance its **viral potential** like Red Bull—how can it spread organically?")

st.success("🔄 Keep iterating! A great idea is one that evolves over time.")

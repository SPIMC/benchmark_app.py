import streamlit as st
import openai

# Set up OpenAI API Key (replace with your actual key)
openai.api_key = "your-api-key-here"

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
st.title("🚀 AI-Powered Creative Benchmarking")
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

# Step 4: AI-Powered Evaluation & Suggestions
if st.button("🔍 Evaluate & Improve My Idea"):
    total_score = sum(scores.values())
    avg_score = total_score / len(scores)
    scale_feedback = humankind_scale[int(round(avg_score))]

    # Construct GPT Prompt for Idea Enhancement
    gpt_prompt = f"""
    You are an expert creative strategist. A user has an idea: {idea}
    They rated it using the following scores:
    - Storytelling Power: {scores['Storytelling Power']}
    - Innovation Level: {scores['Innovation Level']}
    - Cultural Relevance: {scores['Cultural Relevance']}
    - Brand Fit: {scores['Brand Fit']}
    - Engagement Potential: {scores['Engagement Potential']}

    The idea aligns most closely with {selected_brand}, a brand known for {brand_archetypes[selected_brand]}.

    Based on this, provide:
    1. An **analysis** of the idea’s strengths and weaknesses.
    2. **Three ways** the user can improve their idea.
    3. A **refined version** of their idea with improvements applied.
    """

    # Get GPT Response
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "system", "content": gpt_prompt}]
    )

    # Extract AI Response
    ai_suggestions = response['choices'][0]['message']['content']

    # Display Results
    st.markdown(f"## 🔥 Your Benchmark Score: **{round(avg_score, 1)}/10**")
    st.info(f"**Feedback:** {scale_feedback}")

    # Display AI-Powered Enhancements
    st.markdown("## 🎯 AI-Powered Idea Refinement")
    st.write(ai_suggestions)

import streamlit as st
import openai
import os
import json

# 🔐 Set OpenAI API Key securely
if "OPENAI_API_KEY" not in os.environ:
    api_key = st.text_input("Enter your OpenAI API Key", type="password")
    if api_key:
        os.environ["OPENAI_API_KEY"] = api_key

openai.api_key = os.environ.get("OPENAI_API_KEY")

# 📦 Load style presets
STYLE_PRESETS = {
    "Persuasive": "Rewrite the text to sound persuasive and convincing, suitable for an advertisement or motivational piece.",
    "Sarcastic": "Rewrite the text with a dry and sarcastic tone, like it’s mocking something subtly.",
    "Mystical": "Rewrite the text with a poetic and mystical vibe, as if narrated by a fantasy oracle.",
    "Professional": "Make the text formal, neutral, and professional, suitable for business writing."
}

# 🧠 Initialize session memory
if "history" not in st.session_state:
    st.session_state.history = []

# 🧠 Core LLM handler
def analyze_with_llm(text, mode="analyze", custom_prompt=None):
    if not text.strip():
        return "⚠️ Please enter some text first."

    # 🧠 Dynamic Prompting
    if mode == "custom" and custom_prompt:
        prompt = f"{custom_prompt}\n\nText:\n{text}"
    elif mode == "analyze":
        prompt = f"""
        Analyze the following text for stylistic elements:
        - Idioms
        - Figures of speech (metaphors, similes, etc.)
        - Tone and writing style (casual, formal, persuasive, etc.)
        Return a bullet-point summary and include examples.

        Text:
        {text}
        """
    elif mode == "rewrite":
        prompt = f"""
        Rewrite the following text to make it:
        - More poetic
        - Slightly more sophisticated
        - Maintain original meaning
        Return only the rewritten version.

        Text:
        {text}
        """
    elif mode == "simplify":
        prompt = f"""
        Simplify the following text to a conversational 8th-grade reading level while keeping the meaning and tone clear.

        Text:
        {text}
        """
    else:
        return "⚠️ Unknown mode."

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
            max_tokens=800
        )
        return response['choices'][0]['message']['content']
    except Exception as e:
        return f"❌ LLM Error: {str(e)}"

# 🌐 Streamlit UI
st.set_page_config(page_title="Semantic Style Analyzer", layout="centered")
st.title("🧠 Semantic Style Analyzer with LLM")
st.markdown("Analyze, detect, and rewrite text using stylistic nuances.")

# ✍️ Input
text = st.text_area("Paste your text below:", height=250)

# 🔍 Style Analysis
if st.button("🔍 Analyze Style"):
    with st.spinner("Analyzing with the LLM..."):
        result = analyze_with_llm(text, mode="analyze")
        st.markdown("### 📊 Style Analysis")
        st.markdown(result)
        st.session_state.history.append({
            "original": text,
            "action": "Style Analysis",
            "output": result
        })

# 🎭 Rewrite Controls
st.subheader("🎭 Rewrite Options")

col1, col2 = st.columns(2)
with col1:
    if st.button("🎨 Rewrite Poetic"):
        with st.spinner("Rewriting poetically..."):
            poetic = analyze_with_llm(text, mode="rewrite")
            st.markdown("### ✨ Rewritten (Poetic)")
            st.markdown(poetic)
            st.session_state.history.append({
                "original": text,
                "action": "Poetic Rewrite",
                "output": poetic
            })

with col2:
    if st.button("📚 Simplify (8th Grade)"):
        with st.spinner("Simplifying..."):
            simplified = analyze_with_llm(text, mode="simplify")
            st.markdown("### 🧒 Simplified Version")
            st.markdown(simplified)
            st.session_state.history.append({
                "original": text,
                "action": "Simplified Version",
                "output": simplified
            })

# 🎯 Target Style Rewriter
st.subheader("🎯 Rewrite to Target Style")

selected_style = st.selectbox("Choose a target style", list(STYLE_PRESETS.keys()))
if st.button("Rewrite in Selected Style"):
    style_prompt = STYLE_PRESETS[selected_style]
    with st.spinner(f"Rewriting as {selected_style}..."):
        styled = analyze_with_llm(text, mode="custom", custom_prompt=style_prompt)
        st.markdown(f"### ✍️ Rewritten ({selected_style})")
        st.markdown(styled)
        st.session_state.history.append({
            "original": text,
            "action": f"{selected_style} Rewrite",
            "output": styled
        })

# 🧠 Memory Panel
st.markdown("---")
st.subheader("🧠 Memory (Past Analyses & Rewrites)")

with st.expander("Show Memory"):
    for i, item in enumerate(reversed(st.session_state.history), 1):
        st.markdown(f"#### {i}. **{item['action']}**")
        st.markdown(f"**Input:**\n```\n{item['original']}\n```")
        st.markdown(f"**Output:**\n{item['output']}")
        st.markdown("---")

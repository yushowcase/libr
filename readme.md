


# 📚 LiBr - Linguistic Breakdown

**LiBr** (short for **Linguistic Breakdown**) is an advanced, LLM-powered semantic analyzer that breaks down your writing into stylistic elements, detects idioms, figures of speech, tone, and helps rewrite your content into various targeted styles — all in real-time.

> Think of it as a creative grammar checker meets a tone artist — your AI style companion.

---

## 🔍 Features

✅ **Semantic Style Analyzer**  
Analyze text for tone, idioms, figures of speech, and advanced grammatical elements using OpenAI GPT models.

✅ **Smart Rewriting**  
Rephrase content into different writing styles like *Poetic*, *Professional*, *Simplified*, or *Sarcastic* with a click.

✅ **Targeted Style Rewrites**  
Choose from a growing library of stylistic presets to adapt your writing's voice.

✅ **Session Memory**  
Keeps track of past analyses and rewrites in your session for comparison, review, or export.

✅ **Streamlit-Powered UI**  
Interactive, responsive UI that runs locally or can be deployed online for user-friendly interaction.

---

## 🧠 Example Use Cases

- **Writers & Editors**: Get instant feedback on tone and literary devices.
- **Students**: Break down and improve essays, speeches, and academic content.
- **Marketers**: Quickly rewrite content for different brand voices or audience segments.
- **Developers**: Use it as a microservice or LLM module in larger content pipelines.

---

## 🚀 Quickstart

### 🔧 Requirements

- Python 3.8+
- OpenAI API Key
- `streamlit`, `openai`

### 📦 Installation

```bash
git clone https://github.com/yourusername/libr.git
cd libr
pip install -r requirements.txt

```

### 🔑 Set Your API Key

You can either:

-   Set the environment variable `OPENAI_API_KEY`, _or_
    
-   Enter it when prompted in the Streamlit interface
    

### ▶️ Run the App

```bash
streamlit run app.py

```

----------

## 📂 Project Structure

```bash
libr/
├── app.py                 # Main Streamlit application
├── style_presets.json     # Config for style rewriting options
├── english_idioms.csv     # Dataset used for idiom detection
├── README.md              # This file
├── requirements.txt       # Python dependencies

```

----------

## 🧪 Tech Stack

-   [Streamlit](https://streamlit.io) — interactive frontend
    
-   [OpenAI GPT-3.5](https://platform.openai.com) — core LLM
    
-   [Pandas](https://pandas.pydata.org/) — dataset processing (e.g., idiom CSV)
    
-   Optional: `spaCy` or `langchain` for future expansion
    

----------

## 🛠️ Roadmap

-   Add document upload (PDF/DOCX) for batch analysis
    
-   Export memory panel as .txt or .md
    
-   Style scoring system (Formality, Creativity, Simplicity, etc.)
    
-   User-auth and persistent cloud storage
    
-   LLM fine-tuning on literary/brand-specific corpora
    

----------

## 🙌 Credits

Built by [Aayush K.](https://github.com/yushowcase)  — a project focused on bridging creativity and clarity in writing with AI.

Feel free to contribute, fork, or reach out for collaboration!

----------

## 📄 License

MIT License


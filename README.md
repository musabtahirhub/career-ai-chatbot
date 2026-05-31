# 🎓 CareerGuide AI

An AI-powered career guidance chatbot built with **Gradio** and **GROQ API**. Get personalized advice on career paths, skills, resume tips, and job interviews.

## ✨ Features

- Interactive chat interface with Gradio
- Professional career guidance for students & graduates
- Resume and interview tips
- Skill recommendations
- Industry trends insights
- Adjustable response creativity
- Fast responses with GROQ LLMs

## 🛠️ Tech Stack

- Python 3.8+
- Gradio (Web UI)
- GROQ API (Fast LLM inference)
- Requests (HTTP client)

## 🚀 Quick Start

### 1. Clone & Install
```bash
git clone https://github.com/musabtahirhub/career-ai-chatbot.git
cd career-ai-chatbot
pip install gradio requests
```

### 2. Set API Key

**Windows:**
```bash
set GROQ_API_KEY=your_api_key_here
```

**Linux/macOS:**
```bash
export GROQ_API_KEY=your_api_key_here
```

Get your free API key from [console.groq.com](https://console.groq.com)

### 3. Run
```bash
python app.py
```

Visit `http://127.0.0.1:7860/` in your browser.

## 💬 Ask About

- Career path selection & guidance
- Skill development recommendations
- Resume writing tips
- Interview preparation
- Higher education options
- Industry trends & job market insights

## ⚙️ Configuration

Edit `app.py` to customize:
```python
MODEL_NAME = "llama3-8b-8192"  # Change model
SYSTEM_PROMPT = """..."""  # Customize behavior
```

## 📝 License

MIT License

## 🔗 Resources

- [GROQ Console](https://console.groq.com)
- [Gradio Docs](https://www.gradio.app/docs)

---

**Made with ❤️ by [musabtahirhub](https://github.com/musabtahirhub)**

Star ⭐ if helpful!

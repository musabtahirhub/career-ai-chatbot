import gradio as gr
import os
import requests

# Load GROQ API key from Hugging Face Secrets
GROQ_API_KEY = os.environ.get("GROQ_API_KEY")

GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"
MODEL_NAME = "llama3-8b-8192"

# 🎯 Career Guidance System Prompt
SYSTEM_PROMPT = """
You are CareerGuide AI, a professional and supportive career guidance assistant.
Your role is to help students and fresh graduates with:
- Career path selection
- Skill recommendations
- Resume and interview tips
- Industry trends
- Higher education guidance

Your answers should be clear, practical, and motivating.
Avoid giving false guarantees and do not provide medical or legal advice.
"""

def query_groq(messages, temperature):
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": MODEL_NAME,
        "messages": messages,
        "temperature": temperature
    }

    response = requests.post(GROQ_API_URL, headers=headers, json=payload)

    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        return f"Error {response.status_code}: {response.text}"

def respond(user_message, chat_history, temperature):
    # Start with system prompt
    messages = [{"role": "system", "content": SYSTEM_PROMPT}]

    # Add previous chat history
    messages.extend(chat_history)

    # Add new user message
    messages.append({"role": "user", "content": user_message})

    # Get AI response
    bot_reply = query_groq(messages, temperature)

    # Update chat history
    chat_history.append({"role": "user", "content": user_message})
    chat_history.append({"role": "assistant", "content": bot_reply})

    return "", chat_history

with gr.Blocks() as demo:
    gr.Markdown("## 🎓 CareerGuide AI – Smart Career Advisor")

    chatbot = gr.Chatbot(
        type="messages",
        height=420
    )

    state = gr.State([])

    msg = gr.Textbox(
        label="Your Question",
        placeholder="Ask about careers, skills, jobs, or education..."
    )

    temperature = gr.Slider(
        minimum=0.2,
        maximum=1.0,
        value=0.6,
        step=0.1,
        label="Response Creativity"
    )

    clear = gr.Button("Clear Chat")

    msg.submit(respond, [msg, state, temperature], [msg, chatbot])
    clear.click(lambda: ([], []), None, [chatbot, state])

demo.launch()

# AI Customer Support Chatbot

A simple, working AI-powered customer support chatbot built with Python, the Anthropic SDK, and Streamlit. Clone it, add your API key, and have it running in under 20 minutes.

**Blog Post:** [Build an AI Customer Support Chatbot in 20 Minutes](https://ashkankardan.com/blog/ai-chatbots-for-business)

---

## What It Does

- Answers customer questions based on your business knowledge base
- Maintains conversation history for multi-turn support conversations
- Knows when to say "I don't know" and routes to human support
- Uses Claude Sonnet 4.6 via the Anthropic API

---

## Quick Start

### Prerequisites

- Python 3.10 or higher
- An Anthropic API key ([get one here](https://console.anthropic.com/))

### Setup

1. **Clone the repo**

   ```bash
   git clone https://github.com/ashkankardan/ai-support-chatbot.git
   cd ai-support-chatbot
   ```

2. **Create a virtual environment** (recommended)

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Add your API key**

   ```bash
   cp .env.example .env
   ```

   Open `.env` and replace `your-api-key-here` with your actual Anthropic API key.

5. **Run the app**

   ```bash
   streamlit run app.py
   ```

The app will open in your browser at `http://localhost:8501`.

---

## Customize It

The chatbot's knowledge comes from `knowledge_base.md`. To make it your own:

1. Open `knowledge_base.md`
2. Replace the sample content with your business info (products, policies, FAQs, etc.)
3. Restart the app

That's it. The chatbot will now answer questions based on your content.

---

## How It Works

The architecture is intentionally simple:

1. Your business knowledge is loaded from a Markdown file
2. It is injected into Claude's system prompt as context
3. Claude answers questions grounded in that context only
4. If the answer is not in the knowledge base, Claude says so and suggests contacting support

No vector database, no embeddings, no RAG pipeline. Just a knowledge file, a system prompt, and an API call. For most small-to-medium businesses with a manageable knowledge base (under roughly 50 pages), this approach works surprisingly well.

---

## Cost

Claude Sonnet 4.6 costs $3 per million input tokens and $15 per million output tokens. A typical support conversation costs about $0.002-0.005. At 1,000 conversations per month, that is roughly $2-5 per month in API costs.

---

## Project Structure

```
ai-support-chatbot/
├── app.py                 # Streamlit chat application
├── knowledge_base.md      # Your business knowledge (edit this!)
├── requirements.txt       # Python dependencies
├── .env.example           # API key template
├── .gitignore
└── README.md
```

---

## Built With

- [Anthropic Python SDK](https://github.com/anthropics/anthropic-sdk-python) - Claude API client
- [Streamlit](https://streamlit.io/) - Chat UI framework
- [Claude Sonnet 4.6](https://docs.anthropic.com/en/docs/about-claude/models) - AI model

---

## License

MIT

---

Built by [Ashkan Kardan](https://ashkankardan.com) - AI Software Engineer

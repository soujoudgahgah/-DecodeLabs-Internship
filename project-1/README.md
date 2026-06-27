# 🤖 Rule-Based AI Chatbot
**Project 1 | DecodeLabs Industrial Training Kit | Batch 2026**
**Author: Soujoud Gahgah**

---

## 📌 About The Project

RuleBot is a rule-based conversational AI chatbot built using pure Python — no machine learning, no external AI APIs. It simulates human interaction through deterministic logic: keyword matching, dictionary-based responses, and control flow.

This project is the foundation of AI engineering — before machines learn on their own, you must master the art of teaching them through explicit rules.

---

## ✨ Features

- 🕐 **Time-aware greeting** — Says "Good morning", "Good afternoon", or "Good evening" based on the actual time
- 🎲 **Random response variation** — Same question, different answer every time (never feels repetitive)
- 🧠 **17 intents** — Covers greetings, identity, AI topics, jokes, weather, and more
- 🔍 **Keyword matching** — Understands natural phrases, not just exact commands
- 🛡️ **Input sanitization** — Handles uppercase, lowercase, and extra spaces automatically
- 💬 **Conversation counter** — Shows how many messages were exchanged when you exit
- ✅ **Clean exit strategy** — Responds to "bye", "quit", "exit", "goodbye", "see you"
- 🔄 **Infinite loop** — Keeps running until you tell it to stop

---

## 🛠️ Built With

- Python 3.x
- `random` (standard library)
- `datetime` (standard library)
- `typing` (standard library)

> No external libraries needed — runs out of the box!

---

## 🚀 How To Run

**1. Make sure Python is installed:**
```bash
python --version
```

**2. Clone this repository:**
```bash
git clone https://github.com/soujoudgahgah/-DecodeLabs-Internship.git
```

**3. Navigate to the project folder:**
```bash
cd -DecodeLabs-Internship
```

**4. Run the chatbot:**
```bash
python rule_based_chatbot.py
```

---

## 💬 Example Conversation

```
Bot: Good evening! 🌙 I'm RuleBot. Type 'help' for topics, or 'bye' to leave.
You: hello
Bot: Hi there! Ready to talk AI today?
You: what is ai
Bot: AI is the simulation of human intelligence by machines — and you're learning to build it!
You: joke
Bot: Why do programmers prefer dark mode? Because light attracts bugs!
You: bye
Bot: Goodbye! We exchanged 3 messages today. See you next time! 👋
```

---

## 📋 Supported Intents

| Keyword | Example Input |
|---|---|
| hello / hi / hey | "hello there" |
| how are you | "how are you doing?" |
| what is your name | "what is your name?" |
| who are you | "who are you?" |
| what can you do | "what can you do?" |
| help | "help" |
| joke | "tell me a joke" |
| what is ai | "what is ai?" |
| machine learning | "what is machine learning?" |
| python | "tell me about python" |
| weather | "what's the weather?" |
| will it rain | "will it rain today?" |
| decodelabs | "tell me about decodelabs" |
| thanks / thank you | "thanks!" |
| bye / exit / quit | "bye" |

---

## 🧠 Key Concepts Demonstrated

- **Control Flow** — if/else logic and while loops
- **Data Structures** — Python dictionaries for the knowledge base
- **Functions** — Clean separation of logic into reusable functions
- **String Manipulation** — Sanitization with `.lower()` and `.strip()`
- **Randomization** — `random.choice()` for response variation
- **Date & Time** — `datetime` for time-aware greetings
- **IPO Model** — Input → Process → Output architecture

---

## 📁 Project Structure

```
DecodeLabs-Internship/
│
├── rule_based_chatbot.py   # Main chatbot script
└── README.md               # Project documentation
```

---

## 🔮 Future Improvements

- [ ] Connect to a weather API for live weather data
- [ ] Add memory to remember the user's name
- [ ] Support multiple languages (Arabic / English)
- [ ] Upgrade to NLP-based intent matching (Project 2+)

---

## 📜 License

This project was built as part of the **DecodeLabs Industrial Training Program**.

---

*"An LLM without rules is a hallucination engine. Today, we build the skeleton that holds the intelligence."* — DecodeLabs

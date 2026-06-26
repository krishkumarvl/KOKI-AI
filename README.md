<div align="center">

# 🤖 PROJECT KOKI

### My personal AI assistant — built from zero.

![Python](https://img.shields.io/badge/Python-3.11-blue?style=flat&logo=python&logoColor=white)
![Gemini](https://img.shields.io/badge/Gemini-2.5_Flash-orange?style=flat&logo=google&logoColor=white)
![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=flat)
![License](https://img.shields.io/badge/License-MIT-yellow?style=flat)
![Week](https://img.shields.io/badge/Week_2-Complete-purple?style=flat)
![Build](https://img.shields.io/badge/Build-In_Public-red?style=flat)

*"I don't want to learn first and build later. I want to build while learning."*

</div>

---

## 🧠 What is KOKI?

KOKI is a personal AI assistant being built from scratch as a public learning journey.

The goal isn't just to use AI APIs — it's to understand how an AI assistant actually works from the inside. Memory systems, conversation flow, context engineering, prompt design — every concept learned by building it, not just reading about it.

Every feature is written by hand. Every bug is a lesson. Every week is a new chapter.

---

## ⚡ How KOKI Works

```
You
 ↓
KOKI  (koki.py)
 ↓
Memory Check  (koki_memory.json + memory.txt)
 ↓
Dictionary Brain  (instant responses)
 ↓
Context Builder  (koki_context.md)
 ↓
Gemini 2.5 Flash  (fallback AI)
 ↓
Response
```

---

## ✨ Current Features

| Feature | Description | Status |
|---------|-------------|--------|
| Dictionary Brain | Instant responses for known topics | ✅ |
| Randomized Responses | Natural, non-robotic replies | ✅ |
| Persistent JSON Memory | Remembers you across sessions | ✅ |
| User Profile | Stores name + interests | ✅ |
| Conversation Pairs | Saves both sides of every chat | ✅ |
| Gemini Integration | Fallback AI for unknown questions | ✅ |
| Multi-turn Context | Last 5 turns sent to Gemini | ✅ |
| Context Engine | KOKI knows its own identity | ✅ |
| Remember Command | Save anything to memory | ✅ |
| Forget Command | Delete wrong memories | ✅ |
| Hinglish Detection | Understands "mujhe X pasand hai" | ✅ |

---

## 📅 Development Progress

| Week | Focus | Status |
|------|-------|--------|
| Week 1 | Dictionary Brain + File Memory + Random Responses | ✅ Done |
| Week 2 | Gemini + JSON Memory + Context Engineering | ✅ Done |
| Week 3 | Modular Architecture + Cleaner Codebase | 🔜 Next |
| Week 4 | Better Conversation Flow + Prompt Engineering | 📋 Planned |
| Week 5+ | Voice + Web Search + File Understanding | 🔮 Future |

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Language | Python 3.11 |
| AI Model | Google Gemini 2.5 Flash |
| Memory | JSON + Plain Text |
| Environment | python-dotenv |
| Version Control | Git + GitHub |
| Editor | VS Code |

---

## 📂 Project Structure

```
PROJECT-KOKI/
│
├── koki.py              ← main assistant
├── koki_context.md      ← KOKI's identity + project context
├── koki_memory.json     ← persistent user memory
├── memory.txt           ← remembered notes
├── requirements.txt     ← dependencies
├── .env                 ← API keys (not pushed)
├── .gitignore
└── README.md
```

---

## ⚙️ Installation

**Clone the repository**
```bash
git clone https://github.com/krishkumarvl/PROJECT-KOKI.git
cd PROJECT-KOKI
```

**Install dependencies**
```bash
pip install -r requirements.txt
```

**Create a `.env` file**
```env
GEMINI_API_KEY=your_api_key_here
```

**Run KOKI**
```bash
python koki.py
```

---

## 🔮 Future Roadmap

```
Phase 1 ✅  →  Memory + Gemini + User Profiles
Phase 2 🔜  →  Modular Code + Better Prompts
Phase 3 📋  →  Voice Assistant + Speech Recognition
Phase 4 📋  →  Vision + PDF Reader + OCR
Phase 5 📋  →  Web Search + Browser Automation
Phase 6 🔮  →  KOKI v1.0 — Public Release
```

---

## 🎯 Why I'm Building This

I believe the best way to learn AI isn't by watching tutorials endlessly. It's by building.

Every bug teaches something. Every feature raises new questions. Every improvement makes the assistant feel a little more alive.

KOKI is my way of learning AI, Python, and software engineering in public — while actually shipping something real.

---
---

## 🤝 Contributing

Suggestions, ideas, and feedback are always welcome.

If you'd like to contribute, feel free to fork the repository and open a pull request.

---

## 🏢 Built Under

**Kryphix.co** — KOKI is the first flagship project.

The long-term vision: build practical AI products that solve real problems and make technology more human.

---

## 👨‍💻 Built By

**Krish Kumar** — CSE Student, AKTU Lucknow

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Krish_Kumar-blue?style=flat&logo=linkedin)](https://linkedin.com/in/krishkumarvl)
[![GitHub](https://img.shields.io/badge/GitHub-krishkumarvl-black?style=flat&logo=github)](https://github.com/krishkumarvl)

*Building in public. Carpe Diem.* 🎸

---

## 📄 License

This project is licensed under the MIT License.
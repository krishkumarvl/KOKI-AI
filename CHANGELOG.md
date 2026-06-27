# 📋 CHANGELOG

All notable changes made during the development of **KOKI** are documented here.

---

# Week 1 — Building the Foundation

## Overview

The goal of the first week was simple:
Instead of directly using an AI API, I wanted to understand how a basic AI assistant works internally.

This week was focused on learning Python fundamentals while gradually turning a simple terminal program into a small assistant.

### Features Added

- Basic terminal-based AI assistant
- Dictionary-based response system
- Multiple predefined conversation topics
- Randomized responses for more natural conversations
- Greeting system
- Current time support
- Exit commands
- Session conversation counter
- File-based memory (`memory.txt`)
- Remember command
- Recall saved memories

### What I Learned

- Python functions
- Dictionaries
- Conditional statements
- Loops
- File handling
- Random module
- Organizing a Python project
- How a rule-based assistant works

---

#  Week 2 — From Rule-Based to AI-Assisted

## Overview

Week 2 was focused on making KOKI more intelligent.

Instead of only replying from a dictionary, KOKI can now use Google's Gemini model whenever it doesn't know an answer.

I also wanted KOKI to remember important information even after closing the program, so I replaced temporary memory with persistent JSON storage.

Finally, I introduced project context so KOKI understands its own identity instead of behaving like a generic chatbot.

### Features Added

- Gemini API integration
- Fallback response system
- Persistent JSON memory
- User profile memory
- Interest tracking
- Chat history
- Project Context (`koki_context.md`)
- Environment variable support using `.env`
- GitHub-ready project structure

### Improvements

- Cleaner conversation flow
- More natural responses
- Better memory organization
- Reduced repetitive replies
- Better prompt design for Gemini
- Improved code readability

### Bugs Fixed

- JSON loading errors
- Duplicate Gemini responses
- Memory initialization issues
- Conversation flow improvements
- Context loading fixes

### What I Learned

- Working with APIs
- Environment variables
- JSON storage
- Prompt Engineering
- Context Engineering
- Debugging real project issues
- Why architecture matters while building AI products

## Week 2 — Final Update

### Bugs Fixed & Improvements

- Chat history now stores conversation pairs {user, koki} instead of only user messages
- Last 5 conversation turns are now passed into Gemini prompt — KOKI can now understand follow-up questions
- Added `forget` command — wrong memories can now be deleted from memory.txt
- Hinglish interest detection improved — "mujhe X pasand hai" and "i love X" now work alongside "i like X"
- User profile now shows memory.txt notes alongside interests
- show history command now displays both sides of the conversation

---

---

# Week 3 — From Script to Software

## Overview

Week 3 was not about adding flashy features.
It was about making KOKI look and feel like a real software project.

The entire codebase was refactored from a single `koki.py` file into a clean modular structure — without changing any existing behavior.

## Refactor

- Split `koki.py` into proper modules
- `config.py` — all constants, API keys, persona, responses dict
- `brain/gemini.py` — Gemini client, prompt builder, ask_gemini()
- `memory/manager.py` — load/save/forget memory, interest detection, chat history
- `main.py` — CLI loop and command routing only

## New Folders

- `brain/` — AI logic
- `memory/` — memory management
- `data/` — all data files (memory.txt, koki_memory.json)
- `prompts/` — KOKI system prompt as a markdown file
- `docs/` — architecture.md + roadmap.md

## New Files

- `prompts/koki_prompt.md` — KOKI personality and rules
- `docs/architecture.md` — full project flow diagram
- `docs/roadmap.md` — phase-by-phase build plan

## Features Added

- YouTube Music integration — "play X" opens song directly in browser (ongoing)
- Zero new behavior changes — all Week 2 features work exactly the same

## What I Learned

- How to split a large Python file into modules
- Why `__init__.py` exists and how imports work across folders
- How folder structure makes a project maintainable
- Why separating concerns (brain vs memory vs config) matters
- How real open-source projects are organized 
 (week 3 final updates will be shown on Friday...this is only day 13th progress)
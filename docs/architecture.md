# KOKI — Architecture

## Folder Structure
KOKI/

├── main.py
├── config.py
├── brain/
│   ├── init.py
│   └── gemini.py
├── memory/
│   ├── init.py
│   └── manager.py
├── prompts/
│   └── koki_prompt.md
├── data/
│   ├── memory.txt
│   └── koki_memory.json
├── docs/
│   ├── architecture.md
│   └── roadmap.md
├── requirements.txt
├── .env
└── .gitignore

## Current Data Flow
User Input → main.py → Interest? / Command? / Dictionary? / Gemini → Reply
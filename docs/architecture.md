# 🏛 KOKI Architecture

> "Good software isn't built by writing more code.
>
> It's built by organizing complexity."

---

# Introduction

KOKI started as a simple Python chatbot.

As the project grew, keeping everything inside a single file quickly became difficult.

Week 3 introduced a complete architectural redesign.

Instead of focusing on adding more features, the goal became building a scalable foundation that future versions of KOKI could grow upon.

Today KOKI follows a modular architecture where every responsibility has its own dedicated layer.

The purpose of this document is to explain those layers and the reasoning behind every architectural decision.

---

# Design Philosophy

KOKI follows five core principles.

## 1. Simplicity

Every module should have one responsibility.

If a file starts doing multiple jobs, it should be split.

---

## 2. Readability

Code is written for humans first.

Future Krish should understand today's code without guessing.

---

## 3. Scalability

Every feature should be easy to expand.

Adding Voice, Tools or AI Agents should not require rewriting the entire project.

---

## 4. Separation of Concerns

Memory should only manage memory.

Brain should only think.

Configuration should only configure.

Every layer has a clear responsibility.

---

## 5. Learn While Building

This project intentionally values learning over speed.

Sometimes architecture changes even when the old code still works.

Because becoming a better engineer is one of KOKI's primary goals.

---

# High Level Architecture

```text
                    USER

                      │

               Terminal Interface

                      │

                  main.py

                      │

      ┌───────────────┼────────────────┐

      │               │                │

   Brain Layer    Memory Layer    Configuration

      │               │

      └────── Gemini API ─────────────┘

                      │

                 AI Response
```

---

# Project Structure

```text
KOKI/

brain/
memory/
docs/
website/
prompts/
data/

main.py
config.py
requirements.txt
README.md
CHANGELOG.md
LICENSE
```

Each folder exists for one specific purpose.

No folder should become responsible for unrelated functionality.

---

# Main Entry Point

File

```text
main.py
```

Responsibilities

- Starts KOKI
- Receives user input
- Routes commands
- Calls Brain
- Calls Memory
- Displays responses
- Controls application flow

main.py should never become overloaded with business logic.

Its job is orchestration, not intelligence.

---

# Brain Layer

Folder

```text
brain/
```

Purpose

The Brain is responsible for thinking.

It does **not** store memory.

It does **not** manage files.

It simply decides how KOKI should respond.

Current responsibilities

- Prompt Engineering
- Gemini Communication
- AI Reasoning
- Response Generation
- Music Handling
- Input Preprocessing

Future responsibilities

- Tool Calling
- Agent Routing
- Voice Understanding
- Vision Models
- Multi-modal Intelligence
---

# Memory Layer

Folder

```text
memory/
```

Purpose

The Memory Layer is responsible for everything KOKI remembers.

Unlike the Brain, Memory never decides *how* to respond.

It simply stores and retrieves information.

---

## Current Responsibilities

- User Profile
- User Name
- Interests
- Long-term Memory
- Conversation History
- JSON Database
- Text Memory
- Remember / Forget Commands

---

## Why Separate Memory?

Imagine if the Brain also handled storage.

Every new feature would make the AI harder to maintain.

Instead:

Brain → Thinks

Memory → Remembers

This separation makes future improvements significantly easier.

---

# Configuration Layer

File

```text
config.py
```

Purpose

Every reusable constant lives here.

Instead of hardcoding values throughout the project, KOKI loads them from one central location.

Examples

- Greetings
- Exit Commands
- Random Responses
- Version Information
- Default Settings
- Model Configuration

Benefits

- Easier maintenance
- Cleaner code
- Faster updates
- Better scalability

---

# Prompt Engineering

Prompt Engineering defines KOKI's personality.

Instead of simply asking Gemini for an answer, KOKI provides context about:

- Who KOKI is
- The project
- The user
- Previous conversations
- Memory
- Personality

This creates much more natural conversations.

---

# Context Engineering

Prompt Engineering tells the AI *who it is.*

Context Engineering tells the AI *what is happening.*

Current Context

- Previous conversations
- User profile
- Stored memories
- Current message
- KOKI identity

Future Context

- Calendar
- Tasks
- Files
- Browser
- Weather
- Location
- Time
- Running tools

---

# Data Flow

Every conversation follows the same pipeline.

```text
User

↓

Preprocessing

↓

Command Detection

↓

Memory Retrieval

↓

Context Building

↓

Prompt Construction

↓

Gemini API

↓

Response

↓

Memory Update

↓

Display Response
```

Every stage has one responsibility.

Keeping this pipeline modular makes debugging significantly easier.

---

# Landing Website Architecture

The Landing Website is completely independent from the Python application.

Purpose

- Showcase KOKI
- Explain Features
- Document Progress
- Present Architecture
- Collect Feedback
- Build Community

Current Technologies

- HTML5
- CSS3
- Responsive Layout
- Google Stitch
- Component Sections

Major Sections

- Hero
- This Week
- Status
- Manifesto
- Feature Showcase
- Architecture
- Design Philosophy
- Community
- Builder Story
- Journey Timeline
- Letter to Every Curious Mind

The website is documentation, not the application itself.

---

# Design System

Theme

Digital Atelier

Core Principles

- Warm
- Human
- Editorial
- Calm
- Minimal
- Story Driven

Color Palette

Background

#F5F0E8

Primary

#1B5E45

Surface

#EFE7DA

Accent

#D8A646

Typography

Inter

Cormorant Garamond

Every design decision follows this system for consistency.

---

# Why HTML & CSS?

The landing page intentionally uses plain HTML and CSS.

Reasons

- Fast loading
- Easy deployment
- No framework dependency
- Easier learning
- Complete control over styling

Frameworks can always be introduced later if needed.
---

# Tool Layer (Week 4)

The Tool Layer represents the next major evolution of KOKI.

Instead of only generating text responses, KOKI will be able to interact with external systems.

Every capability will be implemented as an independent module.

Example

```text
tools/

calculator.py

weather.py

search.py

time.py

files.py

system.py

youtube.py
```

Every tool follows the same interface.

```text
User

↓

Intent Detection

↓

Tool Router

↓

Selected Tool

↓

Result

↓

Natural Language Response
```

This architecture allows new tools to be added without modifying the Brain itself.

---

# Voice Layer

The Voice Layer will allow conversations without using the keyboard.

Pipeline

```text
Voice

↓

Speech Recognition

↓

Preprocessing

↓

Brain

↓

Response

↓

Text To Speech

↓

Voice Output
```

Future goals

- Wake Word

- Streaming Conversation

- Low Latency

- Natural Voice

- Offline Support

---

# Agent Architecture

Long term, KOKI will move beyond a single assistant.

Instead, specialized agents will collaborate.

Example

```text
User

↓

Coordinator

↓

────────────────────────

Research Agent

Coding Agent

Writing Agent

Planning Agent

Student Agent

────────────────────────

↓

Combined Response
```

Each agent will focus on one responsibility instead of trying to solve everything.

---

# Future Modules

Planned architecture

```text
brain/

memory/

tools/

voice/

vision/

agents/

projects/

calendar/

notes/

learning/

analytics/
```

Every folder has one responsibility.

This keeps the system modular and easy to maintain.

---

# Engineering Decisions

## Why Python?

Python provides excellent AI libraries, fast prototyping and a clean syntax that is ideal for experimentation.

---

## Why JSON?

JSON is lightweight, human-readable and perfect for the current stage of KOKI.

As the project grows, JSON can later be replaced with SQLite or PostgreSQL without changing the overall architecture.

---

## Why Gemini?

Gemini 2.5 Flash offers an excellent balance between capability, speed and cost, making it a strong choice for an educational project.

The architecture intentionally avoids vendor lock-in so different LLMs can be integrated later.

---

## Why Modular Architecture?

Because software grows.

What starts as a few hundred lines eventually becomes thousands.

Keeping responsibilities separated makes new features easier to build and reduces technical debt.

---

# Scalability Plan

Current

```text
Single User

↓

Terminal

↓

JSON Memory
```

Next

```text
Multiple Tools

↓

Voice

↓

Desktop App
```

Future

```text
Cloud Sync

↓

Authentication

↓

Multiple Devices

↓

Personal Knowledge Base

↓

AI Operating System
```

The architecture is intentionally designed so each milestone builds upon the previous one without requiring major rewrites.

---

# KOKI Vision

KOKI is not intended to remain a chatbot.

The long-term vision is a Personal AI Operating System that can help people think, learn, create and organize their digital lives.

Future capabilities include

- Long-term Memory
- Tool Calling
- Voice Interaction
- Calendar Management
- Task Planning
- Project Workspace
- Knowledge Base
- Multi-Agent Collaboration
- Cross-device Synchronization
- Personalized Workflows

The objective is to build an assistant that feels less like software and more like a thoughtful companion.

---

# Building Philosophy

KOKI follows one simple principle.

> Build first.
>
> Learn continuously.
>
> Improve forever.

Every feature begins with curiosity.

Every mistake becomes documentation.

Every redesign makes the next version stronger.

This project isn't only about creating an AI.

It's about becoming a better engineer while building one.

---

# Final Architecture

```text
                           USER

                              │

                    Landing Website
                    (Documentation)

                              │

                     Python Interface

                              │

                         main.py

                              │

      ┌──────────────┬──────────────┬──────────────┐

      │              │              │

   Brain         Memory         Config

      │              │

      └─────── Context Engine ───────┘

                     │

               Prompt Builder

                     │

              Gemini 2.5 Flash

                     │

             Natural AI Response

                     │

              Save Conversation

                     │

                Update Memory

                     │

                 Return Output
```

---

# Conclusion

Architecture is not about writing more code.

It is about making future code easier to write.

Every design decision in KOKI aims to keep the project readable, scalable and enjoyable to build.

The architecture will continue evolving as new features are introduced, but the core philosophy will remain unchanged:

> **Don't follow perfection. Follow curiosity.**


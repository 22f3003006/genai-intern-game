# Wasserstoff Gen-AI Internship Task

## Overview

This project is a web-based guessing game powered by AI, where players interact with an AI persona and try to guess words based on a seed word ("rock"). The game leverages FastAPI for the backend and a simple frontend with HTML, CSS, and JavaScript. The backend features cache integration and AI responses. This project is part of the Wasserstoff Gen-AI Internship Task and aims to demonstrate AI-powered game interactions.

---

## Features

- **Game Start/Restart**: Players can start a new game or restart an existing one.
- **Guessing Mechanism**: Players can submit guesses, and the system checks if the guess is correct or if the game is over.
- **AI Integration**: The system uses an AI response based on the player’s guess and a given seed word.
- **Score Tracking**: Player scores are tracked, and history of guesses is maintained.
- **Frontend and Backend Interaction**: Frontend (HTML/JS) interacts with the FastAPI backend to manage game state.

---

## How to Play

1. **Start the Game**: 
   - Click the **"Start"** button to begin a new game. This will initialize a new session with a random seed word (e.g., "Rock").
   
2. **Make a Guess**:
   - Enter your guess in the **"Your guess..."** input field.
   - Select a persona (e.g., **"Serious"**, **"Tricker"**, or **"Cheery"**) from the **persona dropdown**.
   - Click the **"Guess"** button to submit your guess.

3. **Game Feedback**:
   - The game will provide feedback based on your guess:
     - If your guess is correct, you will receive a **"Correct Guess!"** message along with a score.
     - If your guess is wrong or if a duplicate guess is made, the game ends with a **"Game Over!"** message.
   
4. **Score Tracking**:
   - Your score will be displayed on the screen. It will increase as you make correct guesses.
   
5. **View Guess History**:
   - A history of your past guesses will be shown in the **history list**.

6. **Restart the Game**:
   - If you want to restart the game at any time, click the **"Restart"** button. This will reset the game state and allow you to start a new round with a fresh seed word.

## Architecture

### Backend (FastAPI)
- FastAPI is used for creating the API endpoints (`/start`, `/guess`).
- Redis is used for caching AI responses and storing guesses.
- AI responses are retrieved from a simple AI integration that provides a dynamic response to the player’s guess.

### Frontend (HTML, CSS, JS)
- Simple HTML page with input fields for guesses and persona selection.
- JavaScript handles game logic and interactions with the backend (e.g., starting the game, making guesses).
- CSS is used for basic styling, with a focus on making the game visually appealing.

---

## Setup

### Prerequisites

- Python 3.8+
- Docker (if deploying with containers)
- Redis (for caching and storing game state)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/gen-ai-internship-task.git
   cd gen-ai-internship-task

2. Install Dependencies:
   ```bash
   pip install fastapi uvicorn
   pip install aioredis

3. Set up Redis:
   ```bash
   docker run --name redis -p 6379:6379 -d redis

4. Run app:
   ```bash
   uvicorn main:app --reload

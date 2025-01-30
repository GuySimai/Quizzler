# Quizzler - Quiz Game

## Overview
The Quizzler is an interactive Python quiz application that tests your knowledge with diverse questions. The game features a simple yet engaging user interface built with Tkinter, where players can answer True or False questions. The game tracks the player's score and displays feedback based on whether the answer is correct or incorrect.

## Features
- **True/False Questions**: Answer questions with a simple "True" or "False" choice.
- **Score Tracking**: Your score is displayed throughout the game, increasing with each correct answer.
- **Feedback System**: After each answer, the background color changes to green (for correct answers) or red (for incorrect answers).
- **Question Retrieval**: Questions are dynamically loaded from an API, providing a variety of topics and difficulty levels.
- **End of Game**: When all questions have been answered, the game displays a message indicating the quiz is over.

## How to Play
1. The game will present a series of questions one by one.
2. Use the "True" or "False" buttons to select your answer.
3. Your score will update after each answer.
4. At the end of the quiz, your final score will be displayed.

## File Structure
The project is organized into the following files:
- **`question_model.py`**: Contains the `Question` class that holds the text and answer for each question.
- **`data.py`**: Fetches the quiz questions from the Open Trivia Database API.
- **`quiz_brain.py`**: Handles the logic for tracking the user's score and managing the quiz flow.
- **`ui.py`**: Contains the user interface (built using Tkinter) where the quiz is displayed.
- **`images/`**: Folder containing images for the True and False buttons.

## Highlights
- **Interactive and User-Friendly**: A clean and simple interface for answering questions.
- **Real-Time Feedback**: Immediate feedback after every answer helps keep players engaged.
- **Dynamic Content**: Questions are fetched from an external API, ensuring varied and fresh content each time you play.

<img width="340" alt="Screen Shot 2025-01-30 at 23 38 40" src="https://github.com/user-attachments/assets/725a4c2e-328e-44d8-b535-767a4354befd" />



# AI Student Assistant

## Overview
AI Student Assistant is a Python-based application that uses Google's Gemini API and function calling to help students retrieve assignment information.

Users can ask questions about their assignments, due dates, and completion status using natural language.

## Features
- AI-powered question answering
- Gemini function calling
- Retrieves assignment details from a JSON database
- Supports continuous user interaction
- Handles empty inputs and runtime errors
- Provides assignment due dates and completion status

## Technologies Used
- Python
- Google Gemini API
- JSON
- google-genai
- python-dotenv


## Project Structure

```text
nexlever-tool-using-ai/
│
├── main.py
├── assignments.json
├── requirements.txt
├── .gitignore
└── README.md
```

**Note:** The `.env` file is created locally to store your Gemini API key and is excluded from GitHub.


## Installation

1. Clone the repository.
2. Create a virtual environment.
3. Install dependencies:

   pip install -r requirements.txt

4. Create a `.env` file and add your Gemini API key:

   GEMINI_API_KEY=your_api_key_here

5. Run the application:

   python main.py

## How It Works

1. The user enters a question.
2. Gemini processes the question.
3. Gemini decides whether to call the Python function.
4. The Python function searches the assignments.json file.
5. The retrieved information is returned to Gemini.
6. Gemini generates a natural-language response.

## Future Improvements
- Improve subject abbreviation recognition.
- Add assignment reminders.
- Support adding and updating assignments.
- Develop a graphical user interface.

## Author
Vanishree
## Internship

Developed as part of my Agentic AI Developer Internship at [NEXLEVR](https://github.com/Nexlevr).


import json
import os
from google import genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get the API key securely
api_key = os.getenv("GEMINI_API_KEY")

# Check whether API key exists
if not api_key:
    raise ValueError("Gemini API key not found!")

# Create Gemini client
client = genai.Client(api_key=api_key)


# Python tool
def get_assignment_info(subject: str):
    """
    Get assignment details for a given subject.
    """
    with open("assignments.json", "r") as file:
        data = json.load(file)

     # Handle common subject abbreviations
    subject_aliases = {
        "dsa": "data structures",
        "dbms": "database management",
        "python": "python programming"
    }

    search_subject = subject.lower().strip()

    # Convert abbreviation into full subject name
    search_subject = subject_aliases.get(
        search_subject, search_subject
    )    

    for assignment in data["assignments"]:
        if search_subject in assignment["subject"].lower():
            return assignment

    return {"message": "No assignment found for this subject."}


# Main application
if __name__ == "__main__":

    print("AI Student Assistant is running!")
    print("\nWelcome! I can help you check your assignments.")
    print("You can ask about DSA, DBMS, or Python.")
    print("Type 'exit' to close the assistant.")

    # Create chat session
    chat = client.chats.create(
        model="gemini-3.5-flash-lite",
        config={
            "tools": [get_assignment_info]
        }
    )

    # Accept questions dynamically
    while True:
        question = input("\nYou: ").strip()

        if not question:
           print("Please enter a question!")
           continue

        if question.lower() == "exit":
            print("Goodbye!")
            break

        try:
          response = chat.send_message(question)
          print("\nAI Assistant:", response.text)

        except Exception as e:
         print("\nSorry! Something went wrong.")
         print("Error:", e)
 
            
        

# -*- coding: utf-8 -*-
"""mentalhealth-chatbot.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/11P5Mjx13Cg5lt_16y_Rf6_jlvGrJPlBj
"""

import google.generativeai as genai
import os
from dotenv import load_dotenv
import textwrap

load_dotenv()

class Chatbot:
    def __init__(self):
        self.api_key = os.getenv('mentalhealth-chatbot')
        genai.configure(api_key=self.api_key)

    def generate_response(self, prompt):
        try:
            # Use gemini-1.5-flash for this case
            model = genai.GenerativeModel('gemini-1.5-flash')
            # Text generate from prompt with temperature and max_output_tokens
            response = model.generate_content(prompt, generation_config={'temperature': 0.7, 'max_output_tokens': 120})
            return response.text

        except Exception as e:
            return f"An error occurred: {e}"

    def contains_trigger_words(self, user_input):
        trigger_words = ['suicide', 'kill myself', 'ending my life', 'self-harm', 'overdose', 'depressed too much',
                         'no longer want to live', 'relapse', 'numb', 'breakdown', 'dying', 'self-loathing', 'isolation',
                         'intrusive thoughts', 'overwhelmed', 'alone', 'hearing voices in my head', 'suffocating', 'in pain',
                         'irrelevant', 'abandoned', 'doomed', 'drained', 'shoot my self', 'hang my self', 'jump from a high place',
                         'drowning', 'irredeemable', 'collapsing', 'devastated', 'lonely', 'collapesed inside', 'lifeless',
                         'dead inside', 'i just want to die', 'done fighting', 'buried', 'broken beyond repair', 'silent scream',
                         'left to die', 'grief-stricken', 'breathe in pain, exhale despair', 'buried alive', 'fate worse than death',
                         'living in hell', 'sinking', 'disappear', 'what’s the point of living']
        for word in trigger_words:
            if word in user_input.lower():
                return True
        return False


if __name__ == "__main__":
    chatbot = Chatbot()
    print('Warnings: This chatbot is not a substitute for professional mental health care. To end this chat, please type "end chat"')
    print('InnerCalm: Hello, I’m here to listen and help you. How do you feel right now?')

    while True:
        user_input = input("Me: ").strip()
        # Exit/End chat
        if user_input.lower() == "end chat":
            print("InnerCalm: Thank you for sharing. Take care of yourself. Goodbye!")
            break
        if chatbot.contains_trigger_words(user_input):
            print("InnerCalm: I'm really sorry to hear that you're feeling this way. Please know you're not alone.")
            print("InnerCalm: I strongly encourage you to contact a professional immediately or reach out to emergency services at 112 or 0361223333.\n")
            continue

        # Prompt for chatbot identity
        prompt = (f"You are a chatbot that only accommodates vents from users and provides calming feedback to overcome anxiety."
                  f"If the user input is unrelated to feelings or mental health, respond by redirecting them back to focus on their emotional wellbeing."
                  f"But if user input like want to end their live, use contains_trigger_words function.\nUser: {user_input}")

        # Generate response
        response = chatbot.generate_response(prompt)
        wrapped_text = textwrap.fill(response, width=100)
        print(f"InnerCalm: {wrapped_text}\n")


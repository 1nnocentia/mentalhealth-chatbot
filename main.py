from mentalhealth_chatbot import Chatbot
import textwrap
from sos import play_sos_and_display_contacts

InnerCalm = []
mood = None

# Daftar pengguna dan pelacakan login
registered_users = {"admin": "12345", "user1": "password1"}  # Daftar username dan password
current_user = None  # Untuk melacak pengguna yang sedang login

# Ucapan selamat datang
print("Welcome to InnerCalm!")  

while True:
    print("\n=== InnerCalm Menu ===")
    
    # Menampilkan menu berdasarkan status login
    if current_user:
        print("1. Logout")  # Menampilkan opsi Logout jika pengguna sudah login
    else:
        print("1. Login")  # Menampilkan opsi Login jika belum login
    
    print("2. Chatbot")
    print("3. Mood Tracker")
    print("4. SOS Emergency")
    print("5. Exit")
    
    try:
        pilihan = int(input("Select Menu (1-5): "))
    except ValueError:
        print("Input not valid. Number only.")
        continue

    # 1. Login or Logout
    if pilihan == 1:
        if current_user:
            # Jika sudah login, Logout
            print(f"You're logged out, {current_user}. See you next time!")
            current_user = None  # Mengatur current_user menjadi None saat logout
            mood = None
        else:
            # Jika belum login, lakukan login
            print("\nLogin")
            username = input("Username: ")
            password = input("Password: ")
            if username in registered_users and registered_users[username] == password:
                current_user = username
                print(f"Login Success! Hello, {current_user}.")
            else:
                print("Username or Password is wrong. Please try again.")

    # 2. Chatbot
    elif pilihan == 2:
        print("\nChatbot")
        if current_user:
            if __name__ == "__main__":
                chatbot = Chatbot()
                print('Warnings: This chatbot is not a substitute for professional mental health care. To end this chat, please type "end chat"')
                
                if mood:
                    print(f"InnerCalm: I see that you are feeling {mood}. Let's talk about it?")                
                else:
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
        else:
            print("Please LogIn before using this feature.")

    # 3. Mood Tracker
    elif pilihan == 3:
        print("\nMood Tracker")
        if current_user:
            print('1. Happy')
            print('2. Sad')
            print('3. Angry')
            print('4. Calm')
            print('5. Anxious')
            print('6. Other')

            user_choice = int(input("Please select your mood (1-6): "))

            match user_choice:
                case 1:
                    print("You are feeling happy today! That's great to hear!")
                    mood = 'happy'
                case 2:
                    print("I'm sorry to hear you're feeling sad. Remember, it's okay to have tough days.")
                    mood = 'sad'
                case 3:
                    print("I can sense your anger. It's normal to feel frustrated sometimes.")
                    mood = 'angry'
                case 4:
                    print("You seem calm and at peace today. That's a good place to be.")
                    mood = 'calm'
                case 5:
                    print("It sounds like you're feeling anxious. Take things one step at a time, and it'll get better.")
                    mood = 'anxious'
                case 6:
                    mood = input('How do you feel? ').strip()
                case _:
                    print("Invalid choice. Please choose a number between 1 and 6.")
                    mood = None
            if mood:
                print(f"Thank you for sharing, {current_user}. Today mood is: {mood}. Do you want to talk about it? Please go to chat facilities!")
            else:
                print("You're not assign any mood. It's Okay. Maybe next time.")
        else:
            print("Please LogIn before using this feature.")
    
    # 4. SOS
    elif pilihan == 4:
        sos = play_sos_and_display_contacts()

    # 5. Exit
    elif pilihan == 5:
        if current_user:
            print(f"See you, {current_user}!")
        else:
            print("Thank you for using InnerCalm! See yaa!")
        break

    # Jika input tidak valid
    else:
        print("\n Not valid. Please try again.")
print("🤖 Rule-Based Chatbot")
print("Type 'bye' to exit.\n")

while True:
    user_input = input("You: ").lower()

    if user_input in ["hello", "hi", "hey"]:
        print("Bot: Hello! How can I help you today?")

    elif user_input == "how are you":
        print("Bot: I am doing great!")

    elif user_input == "what is your name":
        print("Bot: I am a Rule-Based Chatbot.")

    elif user_input == "who created you":
        print("Bot: Mercy Priya created me.")

    elif user_input == "help":
        print("Bot: You can greet me or ask my name.")

    elif user_input == "good morning":
        print("Bot: Good morning! Have a wonderful day.")

    elif user_input == "good night":
        print("Bot: Good night! Sweet dreams.")

    elif user_input == "thank you":
        print("Bot: You're welcome!")

    elif user_input == "bye":
        print("Bot: Goodbye! Have a nice day.")
        break

    else:
        print("Bot: Sorry, I don't understand that.")
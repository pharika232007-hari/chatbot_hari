print("🤖 Chatbot: Hello! I am your chatbot.")
print("Type 'bye' to exit.")

while True:
    user = input("You:hello").lower()

    if user == "hello":
        print("🤖 Chatbot: Hi! How can I help you?")

    elif user == "how are you":
        print("🤖 Chatbot: I am doing great!")

    elif user == "what is your name":
        print("🤖 Chatbot: My name is SmartBot.")

    elif user == "bye":
        print("🤖 Chatbot: Goodbye! Have a nice day.")
        break

    else:
        print("🤖 Chatbot: Sorry, I don't understand that yet.")
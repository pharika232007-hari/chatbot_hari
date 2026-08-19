print("🤖 Chatbot: Hello! I am SmartBot.")
print("Type 'bye' to exit.")

while True:
    user = input("you: ").lower().strip()

    if user == "hello" or user == "hi":
        print("🤖 SmartBot: Hello! How can I help you?")

    elif user == "how are you":
        print("🤖 SmartBot: I am fine. How are you?")

    elif user == "what is your name":
        print("🤖 SmartBot: My name is SmartBot.")

    elif user == "what is python":
        print("🤖 SmartBot: Python is a popular programming language.")

    elif user == "what is ai":
        print("🤖 SmartBot: AI means Artificial Intelligence.")

    elif user == "bye":
        print("🤖 SmartBot: Goodbye! Have a nice day.")
        break

    else:
        print("🤖 SmartBot: Sorry, I don't understand that question.")
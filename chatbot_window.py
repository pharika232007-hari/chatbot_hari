import random

print("🤖 SmartBot: Hello! I am your smart chatbot.")
print("Type 'bye', 'exit', or 'quit' to stop.\n")

while True:
    user = input("You: ").lower().strip()

    # Greetings
    if user in ["hello", "hi", "hey", "good morning", "good evening"]:
        responses = [
            "Hello! How can I help you?",
            "Hi there! What can I do for you?",
            "Hey! Nice to talk with you!"
        ]
        print("🤖 SmartBot:", random.choice(responses))

    # How are you
    elif user in ["how are you", "how are you doing", "how do you do"]:
        print("🤖 SmartBot: I am doing great! Thanks for asking.")

    # Bot name
    elif user in ["what is your name", "who are you", "your name"]:
        print("🤖 SmartBot: I am SmartBot, your Python chatbot!")

    # Python
    elif "python" in user:
        print("🤖 SmartBot: Python is a powerful and easy-to-learn programming language.")

    # AI
    elif user in ["what is ai", "what is artificial intelligence"] or "artificial intelligence" in user:
        print("🤖 SmartBot: AI stands for Artificial Intelligence. It enables computers to perform tasks that normally require human intelligence.")

    # Help
    elif user in ["help", "what can you do"]:
        print("🤖 SmartBot: I can chat with you and answer questions about Python and AI.")

    # Exit
    elif user in ["bye", "exit", "quit"]:
        print("🤖 SmartBot: Goodbye! Have a great day! 👋")
        break

    # Unknown question
    else:
        answers = [
            "Sorry, I don't understand that yet.",
            "That's interesting! Can you ask in a different way?",
            "I am still learning. Please try another question."
        ]
        print("🤖 SmartBot:", random.choice(answers))
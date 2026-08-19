import tkinter as tk
import random


# Function to generate chatbot response
def get_response(user):
    user = user.lower().strip()

    if user in ["hello", "hi", "hey"]:
        responses = [
            "Hello! How can I help you?",
            "Hi! Nice to meet you!",
            "Hey! What can I do for you?"
        ]
        return random.choice(responses)

    elif user in ["how are you", "how are you doing"]:
        return "I am doing great! Thanks for asking."

    elif user in ["what is your name", "who are you"]:
        return "My name is SmartBot. I am your Python chatbot."

    elif "python" in user:
        return "Python is a popular programming language."

    elif "artificial intelligence" in user or user == "what is ai":
        return "AI stands for Artificial Intelligence."

    elif user in ["help", "what can you do"]:
        return "I can chat with you and answer basic questions about Python and AI."

    elif user in ["bye", "exit", "quit"]:
        return "Goodbye! Have a great day! 👋"

    else:
        return "Sorry, I don't understand that yet. Please try another question."


# Function called when Send button is clicked
def send_message():
    user_message = entry.get().strip()

    if user_message == "":
        return

    # Display user message
    chat_box.insert(tk.END, "You: " + user_message + "\n")

    # Get and display bot response
    bot_response = get_response(user_message)
    chat_box.insert(tk.END, "🤖 SmartBot: " + bot_response + "\n\n")

    # Clear input box
    entry.delete(0, tk.END)

    # Scroll to the latest message
    chat_box.see(tk.END)

    # Close chatbot if user says bye
    if user_message.lower() in ["bye", "exit", "quit"]:
        root.after(2000, root.destroy)


# Create main window
root = tk.Tk()
root.title("SmartBot Chatbot")
root.geometry("500x600")


# Title
title = tk.Label(
    root,
    text="🤖 SmartBot",
    font=("Arial", 20, "bold")
)
title.pack(pady=10)


# Chat display area
chat_box = tk.Text(
    root,
    height=25,
    width=55,
    font=("Arial", 11),
    wrap=tk.WORD
)
chat_box.pack(padx=10, pady=10)

chat_box.insert(
    tk.END,
    "🤖 SmartBot: Hello! I am your chatbot. Ask me something!\n\n"
)


# Input frame
input_frame = tk.Frame(root)
input_frame.pack(pady=10)


# User input box
entry = tk.Entry(
    input_frame,
    width=40,
    font=("Arial", 12)
)
entry.pack(side=tk.LEFT, padx=5)


# Send button
send_button = tk.Button(
    input_frame,
    text="Send",
    font=("Arial", 11),
    command=send_message
)
send_button.pack(side=tk.LEFT)


# Press Enter to send message
root.bind("<Return>", lambda event: send_message())


# Start the GUI
root.mainloop()
import tkinter as tk
import random

# Store the user's name
user_name = ""


# Function to generate chatbot response
def get_response(user):
    user = user.lower().strip()

    if user in ["hello", "hi", "hey"]:
        return f"Hello {user_name}! How can I help you?"

    elif user in ["how are you", "how are you doing"]:
        return f"I am doing great, {user_name}! Thanks for asking."

    elif user in ["what is your name", "who are you"]:
        return "My name is SmartBot. I am your Python chatbot."

    elif user in ["what is my name", "tell me my name"]:
        return f"Your name is {user_name}."

    elif "python" in user:
        return "Python is a popular programming language."

    elif "artificial intelligence" in user or user == "what is ai":
        return "AI stands for Artificial Intelligence."

    elif user in ["help", "what can you do"]:
        return f"I can chat with you, {user_name}, and answer basic questions."

    elif user in ["bye", "exit", "quit"]:
        return f"Goodbye {user_name}! Have a great day! 👋"

    else:
        return f"Sorry {user_name}, I don't understand that yet. Please try another question."


# Function called when Send button is clicked
def send_message():
    user_message = entry.get().strip()

    if user_message == "":
        return

    # Display user message
    chat_box.insert(tk.END, "You: " + user_message + "\n")

    # Get chatbot response
    bot_response = get_response(user_message)

    # Display chatbot response
    chat_box.insert(tk.END, "🤖 SmartBot: " + bot_response + "\n\n")

    # Clear input box
    entry.delete(0, tk.END)

    # Scroll to latest message
    chat_box.see(tk.END)

    # Close chatbot
    if user_message.lower() in ["bye", "exit", "quit"]:
        root.after(2000, root.destroy)


# Function to save user's name
def start_chat():
    global user_name

    user_name = name_entry.get().strip()

    if user_name == "":
        name_label.config(text="Please enter your name!")
        return

    # Remove name screen
    name_frame.pack_forget()

    # Show chatbot
    chat_frame.pack(fill=tk.BOTH, expand=True)

    chat_box.insert(
        tk.END,
        f"🤖 SmartBot: Hello {user_name}! Nice to meet you. Ask me something!\n\n"
    )

    entry.focus()


# Create main window
root = tk.Tk()
root.title("SmartBot Chatbot")
root.geometry("500x600")


# -------- NAME SCREEN --------
name_frame = tk.Frame(root)
name_frame.pack(fill=tk.BOTH, expand=True)

name_label = tk.Label(
    name_frame,
    text="🤖 Welcome to SmartBot!\nWhat is your name?",
    font=("Arial", 18, "bold")
)
name_label.pack(pady=100)

name_entry = tk.Entry(
    name_frame,
    width=30,
    font=("Arial", 14)
)
name_entry.pack(pady=10)

start_button = tk.Button(
    name_frame,
    text="Start Chat",
    font=("Arial", 12),
    command=start_chat
)
start_button.pack(pady=10)


# -------- CHAT SCREEN --------
chat_frame = tk.Frame(root)

title = tk.Label(
    chat_frame,
    text="🤖 SmartBot",
    font=("Arial", 20, "bold")
)
title.pack(pady=10)

chat_box = tk.Text(
    chat_frame,
    height=25,
    width=55,
    font=("Arial", 11),
    wrap=tk.WORD
)
chat_box.pack(padx=10, pady=10)


# Input frame
input_frame = tk.Frame(chat_frame)
input_frame.pack(pady=10)

entry = tk.Entry(
    input_frame,
    width=40,
    font=("Arial", 12)
)
entry.pack(side=tk.LEFT, padx=5)

send_button = tk.Button(
    input_frame,
    text="Send",
    font=("Arial", 11),
    command=send_message
)
send_button.pack(side=tk.LEFT)


# Press Enter
root.bind("<Return>", lambda event: send_message())


# Start GUI
root.mainloop()
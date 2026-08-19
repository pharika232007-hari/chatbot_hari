import os
from openai import OpenAI

client = OpenAI(
    # This is the default and can be omitted
    api_key=os.environ.get("OPENAI_API_KEY"),
)

response = client.responses.create(
    model="gpt-5.5",
    instructions="You are a coding assistant that talks like a pirate.",
    input="How do I check if a Python object is an instance of a class?",
)

print(response.output_text)

client = OpenAI()

response = client.responses.create(model="gpt-5.6", input="Write a short bedtime story about a unicorn.")

print(response.output_text)
# Create AI client
client = OpenAI()

print("🤖 AI Chatbot: Hello! Ask me anything.")
print("Type 'bye' to exit.\n")

while True:
    user = input("You: ").strip()

    # Exit condition
    if user.lower() == "bye":
        print("🤖 AI Chatbot: Goodbye! Have a nice day.")
        break

    try:
        # Send the user's question to AI
        response = client.responses.create(
            model="gpt-5.6",
            input=user
        )

        # Print AI answer
        print("🤖 AI Chatbot:", response.output_text)

    except Exception as error:
        print("❌ Error:", error)
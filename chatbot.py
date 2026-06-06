import datetime
import random

responses = {
    "hello": ["Hi there!", "Hello!", "Hey!"],
    "how are you": ["I'm fine!", "Doing great!", "Awesome!"],
    "name": ["I am DecodeBot.", "My name is DecodeBot."],
    "help": ["Try: hello, time, date, joke, bye"],
    "bye": ["Goodbye!", "See you later!"]
}

jokes = [
    "Why do programmers prefer dark mode? Because light attracts bugs!",
    "Python is my favorite snake.",
    "AI stands for Always Improving!"
]

print("=" * 40)
print("🤖 DecodeBot Started")
print("Type 'exit' to quit")
print("=" * 40)

while True:
    user_input = input("You: ").lower().strip()

    if user_input in ["exit", "quit"]:
        print("Bot: Goodbye! 👋")
        break

    elif user_input == "time":
        print("Bot:", datetime.datetime.now().strftime("%H:%M:%S"))

    elif user_input == "date":
        print("Bot:", datetime.datetime.now().strftime("%d-%m-%Y"))

    elif user_input == "joke":
        print("Bot:", random.choice(jokes))

    elif user_input in responses:
        print("Bot:", random.choice(responses[user_input]))

    else:
        print("Bot: Sorry, I don't understand that.")
import nltk
from nltk.chat.util import Chat, reflections

nltk.download('punkt', quiet=True)

pairs = [
    [r"my name is (.*)", ["Hello %1, nice to meet you!"]],
    [r"hi|hey|hello", ["Hello!", "Hey there!"]],
    [r"what is your name ?", ["I am Chatty, your friendly chatbot."]],
    [r"how are you ?", ["I'm doing well, thank you!", "I'm great! How about you?"]],
    [r"sorry (.*)", ["No worries", "It's okay"]],
    [r"i'm (.*) doing good", ["Nice to hear that!", "Alright, great!"]],
    [r"quit", ["Bye! Have a great day."]],
    [r"(.*)", ["Sorry, I don't understand that.", "Can you please rephrase?"]],
]

def chatbot():
    print("Hi! I’m Chatty — type 'quit' to exit.")
    chat = Chat(pairs, reflections)
    chat.converse()

if __name__ == "__main__":
    chatbot()

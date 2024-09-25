def response(user_input):
    answers = {
    "hi": "Hi there! How can I assist you today?",
    "hello": "Hello! What can I do for you?",
    "good": "Great to hear that! How can I help?",
    "bye": "Goodbye! Have a wonderful day!",
    "thanks": "You're welcome! If you need anything else, just let me know.",
    "help": "Sure, I'm here to help. What do you need assistance with?",
    "how are you": "I'm just a bot, but I'm here to make your day better!",
    "what's up": "Not much, just here to assist you. What’s on your mind?"
    }
    
    user_input = user_input.lower()
    
    if user_input in answers:
        return answers[user_input]
    else:
        return "Invalid input, please try again."


def run_chatbot():
    print("Chatbot: Hello! You can talk to me by typing. Type 'bye' to exit.")
    
    first_message = True
    
    while True:
        user_input = input("You: ")
        
        if first_message:
            print("Chatbot: How can I help you?")
            first_message = False
            continue  
        
        if user_input.lower() == "bye":
            print("Chatbot: " + response(user_input))
            break
        
        print("Chatbot: " + response(user_input))


run_chatbot()

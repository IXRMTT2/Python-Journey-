def chatbot_response(user_input):
    user_input = user_input.lower()

    if any(greet in user_input for greet in ['hi', 'hello', 'hey']):
        return "Hello! How can I help you today?"
    elif 'how are you' in user_input:
        return "I'm just a bot, but I'm doing great! Thanks for asking."
    elif 'your name' in user_input:
        return "The one and only, mrbot, your friendly Python chatbot."
    elif 'weather' in user_input:
        return "I don't have real-time weather info, but I hope it's nice where you are!"
    elif 'bye' in user_input or 'exit' in user_input or 'quit' in user_input:
        return "Goodbye! Have a great day!"
    else:
        return "Sorry, I didn't understand that. Can you try asking something else?"

def main():
    print("MrBot: Hi! Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        response = chatbot_response(user_input)
        print("MrBot:", response)
        if user_input.lower() in ['bye', 'exit', 'quit']:
            break

if __name__ == "__main__":
    main()

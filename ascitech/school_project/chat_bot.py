while True:

    user_input = input("User: ")
    if user_input.lower() == "goodmorning":
        print("chatbot: Goodmorning, how can I help you")

    elif user_input.lower() == "goodbye":
        print("chatbot: Goodbye, see you soon")

    else:
        print("Sorry, I don't understand, can you write it again")
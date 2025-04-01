def get_response(user_input, mood):
    user_input = user_input.lower()

    greetings = ["hello", "hi", "hey", "good morning", "good evening"]
    sad_keywords = ["sad", "depressed", "down", "anxious", "stressed"]
    happy_keywords = ["happy", "great", "excited", "feeling good"]
    help_keywords = ["help", "advice", "support", "talk", "listen"]
    bye_keywords = ["bye", "goodbye", "see you", "later"]

    # Base response
    if any(word in user_input for word in greetings):
        base = "Hey there! How are you feeling today?"
    elif any(word in user_input for word in sad_keywords):
        base = "I'm really sorry to hear that. I'm here for you if you need to talk."
    elif any(word in user_input for word in happy_keywords):
        base = "That's amazing! Always great to hear some positivity 😊"
    elif any(word in user_input for word in help_keywords):
        base = "Of course. I'm always here to listen. Tell me what's on your mind."
    elif any(word in user_input for word in bye_keywords):
        base = "Goodbye! Take care and feel free to come back anytime."
    else:
        base = "Hmm, tell me more about that. I'm listening."

    # Adjust tone based on sentiment
    if mood == "Negative":
        return base + " 💙 Remember, you're not alone."
    elif mood == "Positive":
        return base + " Keep that good energy flowing! 🌟"
    else:
        return base

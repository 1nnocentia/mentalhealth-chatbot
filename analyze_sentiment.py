def analyze_sentiment(text):
    prohibited_keywords = ["politics", "religion", "controvercial"]
    if any(word in input_text.lower() for word in prohibited_keywords):
        return "Sorry, I'm a Mental Health ChatBot."
    return input_text

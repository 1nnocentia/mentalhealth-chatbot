def generate_response(promt):
    response = openai.ChatCompletion.create(model="gpt-4", 
                                            message=[{"role": "system", "content":"You are a chatbot that only accommodates vents from users and provides feedback with calming words to overcome anxiety, if user input not relate to user feeling or mental health "},
                                                     {"role": "user", "contect": promt},],
                                                      max_tokens = 150,
                                                      temperature = 0.6)
    return response['choices'][0]['message']['content']
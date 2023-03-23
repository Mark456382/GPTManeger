import openai

openai.api_key = "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"

# При открытии чата создать messages, в него будут записаваться все последующие сообщения
messages = [
    {"role": "system", "content": ""},
    {"role": "user", "content": ""},
    {"role": "assistant", "content": ""}
]
# Это нужно чтобы нейронка понимала контекст

# Функция для сообщения
def chat_message(content: str):
    messages.append({"role": "user", "content": content})
    response = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      temperature=0.7,
      max_tokens=500,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0,
      messages=messages)
    chat_response = response.choices[0].message.content
    messages.append({"role": "assistant", "content": chat_response})

    return chat_response

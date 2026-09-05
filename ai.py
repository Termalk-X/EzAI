import requests
API_KEY = "API_KEY"
messages = [
    {
        "role": "system",
        "content": "Kamu adalah AI. Ingat informasi yang diberikan pengguna selama percakapan."
    }
]
while True:
    prompt = input("Kamu: ")
    if prompt.lower() == "exit":
        break
    messages.append({
        "role": "user",
        "content": prompt
    })
    response = requests.post(
        "https://api.groq.com/openai/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        },
        json={
            "model": "openai/gpt-oss-20b",
            "messages": messages
        }
    )
    data = response.json()
    jawaban = data["choices"][0]["message"]["content"]
    messages.append({
        "role": "assistant",
        "content": jawaban
    })
    print("AI:", jawaban)

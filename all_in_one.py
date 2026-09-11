import urllib.request
import json

print("🤖 All-in-One AI Assistant & Data Manager Active! (Exit ke liye 'quit' likhein)")
url = "http://localhost:11434/api/generate"

# Yeh AI ka permanent system rule hai
system_instruction = (
    "You are an expert bilingual AI assistant and automated data manager communicating in Roman Hindi and Hinglish. "
    "Rule 1: If the user provides messy data, lists, or text, structure and clean it into a neat Markdown table. "
    "Rule 2: Always reply back in a friendly, conversational tone, explaining the data and chatting normally with the user."
)

while True:
    user_input = input("\nAap: ")
    if user_input.lower() in ['quit', 'exit']:
        print("Alvida! Phir milte hain. 👋")
        break

    # Combine instructions with user input
    full_prompt = f"{system_instruction}\n\nUser Input/Data: {user_input}"

    data = json.dumps({
        "model": "qwen2.5:3b",
        "prompt": full_prompt,
        "stream": False
    }).encode('utf-8')

    req = urllib.request.Request(url, data=data, headers={'Content-Type': 'application/json'})
    
    try:
        with urllib.request.urlopen(req) as response:
            result = json.loads(response.read().decode())
            print("\nAI Assistant:", result['response'])
    except Exception as e:
        print("\nError (Check karein kya 'ollama serve &' chal raha hai?):", e)

import urllib.request
import json

print("🤖 Tumhara Personal AI Assistant Ready Hai! (Bahar aane ke liye 'exit' type karein)")

url = "http://localhost:11434/api/generate"

while True:
    user_prompt = input("\nAap: ")
    if user_prompt.lower() in ['quit', 'exit']:
        print("Goodbye! 👋")
        break

    data = json.dumps({
        "model": "qwen2.5:3b",
        "prompt": "You are a helpful AI assistant. Answer the user: " + user_prompt,
        "stream": False
    }).encode('utf-8')

    req = urllib.request.Request(url, data=data, headers={'Content-Type': 'application/json'})
    
    try:
        with urllib.request.urlopen(req) as response:
            result = json.loads(response.read().decode())
            print("\nAI Assistant:", result['response'])
    except Exception as e:
        print("\nError (Kya server chal raha hai?):", e)

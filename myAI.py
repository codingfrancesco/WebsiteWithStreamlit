import ollama

def tell_response(x):
    return ollama.chat(model="deepseek-r1:1.5b", messages=[{"role": "user", "content": x}])["message"]["content"]
    


if __name__ == "__main__":
    while True:
        x = input("Enter your message: ")
        if x.lower() == "exit":
            break
        response = tell_response(x)
        print(f"Response: {response}")
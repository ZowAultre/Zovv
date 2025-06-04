import ollama


def chat_with_deepseek(messages, model_name="deepseek-r1:7b"):
    response = ollama.chat(
        model=model_name,
        messages=messages
    )
    return response["message"]["content"]

def stream_response(prompt, model_name="deepseek-r1:7b"):
    stream = ollama.chat(
        model=model_name,
        messages=[{"role": "user", "content": prompt}],
        stream=True  # 启用流式响应
    )
    print("[D7]: ", end="", flush=True)
    for chunk in stream:
        print(chunk["message"]["content"], end="", flush=True)
    print()


# while True:
#     user_input = input("[Q]: ").strip()
#     if user_input.lower() in ("stop", "quit"):
#         break
#     stream_response(user_input)


# 初始化对话历史
messages = []
AiCharacterSetting = "请你将自己当成和我聊天的朋友，用简短的口语回应我。"
messages.append({"role": "user", "content": AiCharacterSetting})

while True:
    user_input = input("[Q]: ").strip()
    if user_input.lower() in ("stop", "quit", "exit"):
        print("[D7]: 对话结束。")
        break

    # 添加用户输入到历史
    messages.append({"role": "user", "content": user_input})

    # 获取模型回复并添加到历史
    answer = chat_with_deepseek(messages)
    messages.append({"role": "assistant", "content": answer})

    print("[D7]:", answer)

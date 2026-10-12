from openai import OpenAI

# =========在这里直接粘贴你的Deepseek密钥=========
KEY = "sk-64fb33483a7************6476"
# ==============================================

client = OpenAI(
    api_key=KEY,
    base_url="https://api.deepseek.com"
)

def ask_llm(question, temp=0.7, max_token=300):
    resp = client.chat.completions.create(
        model="deepseek-chat",
        temperature=temp,
        max_tokens=max_token,
        messages=[{"role":"user", "content":question}]
    )
    return resp.choices[0].message.content

# 主程序
if __name__ == "__main__":
    print("学科问答机器人，输入问题提问，输入quit退出")
    log_file = open("chat_log.txt", "a", encoding="utf-8")
    while True:
        user_input = input("请输入你的问题：")
        if user_input.lower() == "quit":
            print("结束对话")
            log_file.close()
            break
        answer = ask_llm(user_input)
        print(f"回答：{answer}")
        log_file.write(f"用户：{user_input}\nAI：{answer}\n---------\n")

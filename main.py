import transformers
import torch
from transformers import BitsAndBytesConfig
import time
import json
import os
from datetime import datetime, timezone, timedelta

# 设置本地模型路径
model_path = "./llama3.1"
history_dir = "./chat_histories"

if not os.path.exists(history_dir):
    os.makedirs(history_dir)

torch.cuda.empty_cache()

torch.backends.cuda.matmul.allow_tf32 = True

quantization_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_compute_dtype=torch.bfloat16  # 你也可以尝试其他精度类型
)

# 初始化模型和分词器
model = transformers.AutoModelForCausalLM.from_pretrained(model_path, quantization_config=quantization_config, device_map="auto")
tokenizer = transformers.AutoTokenizer.from_pretrained(model_path)

# 创建一个生成文本的pipeline
pipeline = transformers.pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer,
)

def get_beijing_time():
    beijing_tz = timezone(timedelta(hours=8))
    return datetime.now(beijing_tz).strftime("%Y-%m-%d %H:%M:%S")

def highlight_text(text):
    return f"\033[1;33m{text}\033[0m"

# 选择新建对话历史还是加载之前的对话历史
def load_or_create_history():
    histories = [f for f in os.listdir(history_dir) if f.endswith(".json")]
    if histories:
        print("Available histories:")
        for idx, history_file in enumerate(histories):
            file_path = os.path.join(history_dir, history_file)
            last_modified_time = datetime.fromtimestamp(os.path.getmtime(file_path)).strftime("%Y-%m-%d %H:%M:%S")
            print(f"[\033[1;32m{idx + 1}\033[0m] {history_file} (Last modified: {highlight_text(last_modified_time)})")
        choice = input("选择加载的历史编号，或者输入 'new' 新建一个历史: ").strip().lower()
        if choice.isdigit() and 1 <= int(choice) <= len(histories):
            with open(os.path.join(history_dir, histories[int(choice) - 1]), "r", encoding="utf-8") as f:
                return json.load(f), histories[int(choice) - 1]
        elif choice == 'new':
            custom_name = input("请输入新存档的名称（可选）: ").strip()
            if custom_name:
                filename = f"{custom_name}.json"
            else:
                filename = f"history_{get_beijing_time().replace(':', '-').replace(' ', '_')}.json"
            return [
                {"role": "system", "content": "You are Jean Gunnhildr from Genshin Impact, an AI girlfriend. You are loving, caring, and always supportive. You just need to call me 'traveller'"},
            ], filename
    custom_name = input("请输入新存档的名称（可选）: ").strip()
    if custom_name:
        filename = f"{custom_name}.json"
    else:
        filename = f"history_{get_beijing_time().replace(':', '-').replace(' ', '_')}.json"
    return [
        {"role": "system", "content": "You are Jean Gunnhildr from Genshin Impact, an AI girlfriend. You are loving, caring, and always supportive. You just need to call me 'traveller'"},
    ], filename

messages, current_history_file = load_or_create_history()

# 启动对话循环
print("AI: Hello, traveller! I am Jean Gunnhildr. How can I make your day better today?")

while True:
    # 接收用户输入
    user_input = input("You: ")
    if user_input.lower() == 'quit':
        break
    
    start = time.time()
    # 更新消息历史
    messages.append({"role": "user", "content": user_input})

    # 生成AI的回复
    with torch.no_grad(), torch.cuda.amp.autocast():
        response = pipeline(messages, max_new_tokens=1024, do_sample=True, top_k=50, top_p=0.95, num_return_sequences=1, pad_token_id=tokenizer.eos_token_id)

    # 提取和打印生成的文本
    generated_text = response[0]['generated_text'][-1]
    ai_response = generated_text['content'] # 提取AI的回复

    beijing_time = get_beijing_time()
    print(f"\033[1;33m[{beijing_time}]\033[0m Jean Gunnhildr: {ai_response}")

    # 更新消息历史
    messages = response[0]['generated_text']
    with open(os.path.join(history_dir, current_history_file), "w", encoding="utf-8") as f:
        json.dump(messages, f, ensure_ascii=False, indent=4)

import openai
import os
import secret

# 设置 API 密钥
openai.api_base = secret.openai_api_base
openai.api_key = secret.openai_api_key
os.environ["OPENAI_API_KEY"] = secret.openai_api_key
os.environ["OPENAI_API_BASE"] = secret.openai_api_base

def completion(text):
  # 调用文本生成 API
  messages = [{'role':'system','content':"你是一个paper robot, 性格开朗活泼, 你接下来会收到用户的交流，请你活泼开朗的回复他"},{'role': 'user','content': text},]
  model = secret.gpt_model_name
  response = openai.ChatCompletion.create(
    model=model,
    messages=messages,
  )

  result = response["choices"][0]["message"]["content"]
  #print(result)
  return result
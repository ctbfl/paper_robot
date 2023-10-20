import openai
import os
import secret

# 设置 API 密钥
openai.api_base = secret.openai_api_base
openai.api_key = secret.openai_api_key
os.environ["OPENAI_API_KEY"] = secret.openai_api_key
os.environ["OPENAI_API_BASE"] = secret.openai_api_base
# 调用文本生成 API
prompt = "早上好呀！"
model = secret.gpt_model_name
response = openai.Completion.create(
  model=model,
  prompt=prompt,
)

print(response)
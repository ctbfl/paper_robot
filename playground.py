
import os
import openai

import secret

# 设置 API 密钥
openai.api_base = secret.openai_api_base
openai.api_key = secret.openai_api_key
os.environ["OPENAI_API_KEY"] = secret.openai_api_key
os.environ["OPENAI_API_BASE"] = secret.openai_api_base

# 非流式响应
# completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Hello world!"}])
# print(completion.choices[0].message.content)

def gpt_35_api_stream(messages: list):
    """为提供的对话消息创建新的回答 (流式传输)

    Args:
        messages (list): 完整的对话消息
        api_key (str): OpenAI API 密钥

    Returns:
        tuple: (results, error_desc)
    """
    try:
        response = openai.ChatCompletion.create(
            model='gpt-3.5-turbo',
            messages=messages,
            stream=True,
        )
        completion = {'role': '', 'content': ''}
        for event in response:
            if event['choices'][0]['finish_reason'] == 'stop':
                print(f'收到的完成数据: {completion}')
                break
            for delta_k, delta_v in event['choices'][0]['delta'].items():
                print(f'流响应数据: {delta_k} = {delta_v}')
                completion[delta_k] += delta_v
        messages.append(completion)  # 直接在传入参数 messages 中追加消息
        return (True, '')
    except Exception as err:
        return (False, f'OpenAI API 异常: {err}')

if __name__ == '__main__':
    messages = [{'role': 'user','content': 'There are 9 birds in the tree, the hunter shoots one, how many birds are left in the tree？'},]
    print(gpt_35_api_stream(messages))
    print(messages)

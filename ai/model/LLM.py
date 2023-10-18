# 供外部调用的函数，通过Get_LLM(获取到模型的信息)
import ai.config as config
import os
from pydantic import BaseModel, Field
from typing import Any

from langchain.agents import ZeroShotAgent
from typing import Dict




def get_LLM(args):
    print(f"当前使用的模型为{args.model},开始加载...")

    llm = FileNotFoundError
    if args.model == "OpenAI":
        # OpenAI
        # from langchain.llms import OpenAI
        import openai
        from langchain.chat_models import ChatOpenAI
        openai.api_base = config.openai_api_base
        openai.api_key = config.openai_api_key
        os.environ["OPENAI_API_KEY"] = config.openai_api_key
        os.environ["SERPAPI_API_KEY"] = config.serpapi_api_key
        llm = ChatOpenAI(model_name=config.gpt_model_name)
        # llm = OpenAI(temperature=0)

    elif args.model == "ChatGLM2":
        # ChatGLM2
        from ai.model.chatglm2 import ChatGLM2
        llm = ChatGLM2()
        llm.load_model(args.model_path)

    else:
        raise Exception("Not LLM loaded!")

    print("LLM loaded")
    return llm
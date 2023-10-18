from random import randint

# 这段是为了能在chat.py内部正确的跑起来程序
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))

from ai.model import LLM
from ai.tools import Tools
import ai.prompt as prompt
import argparse
from langchain import LLMChain
from langchain.agents import ZeroShotAgent, AgentExecutor




class ChatBot:
    def __init__(self, invoker) -> None:
        '''Initialize a chatbot.

        :param invoker: The handler to handle invoking API services.'''
        print("initializing language model...")

        self.parser = argparse.ArgumentParser(description="解析命令参数")

        self.parser.add_argument("--model", help="模型名称", default="ChatGLM2")
        self.parser.add_argument("--model_path", help="模型路径", default="D:\LLMs\chatglm2-6b")
        self.parser.add_argument("--embedding_path", help="嵌入路径", default="D:\LLMs\text2vec-large-chinese")
        self.parser.add_argument("--show_tool_info", help="是否显示工具信息", action="store_true",default=False)


        # 解析参数
        kwargs = self.parser.parse_args()

        self.llm = LLM.get_LLM(kwargs)

        self.tools = Tools.get_all_tools(self.llm, kwargs, chatbot=self)

        self.chinese_prompt = prompt.create_prompt(self.tools)

        self.llm_chain = LLMChain(llm=self.llm, prompt=self.chinese_prompt)

        self.agent = LLM.ZeroShotAgent(chatbot=self, llm_chain=self.llm_chain, allowed_tools=self.tools.name())

        self.agent_executor = AgentExecutor.from_agent_and_tools(
            agent=self.agent, tools=self.tools(), verbose=True
        )

        self.series = randint(1, 100)
        self.handler = invoker

    def chat(self, text: str) -> str:
        '''Chat with the bot.

        :param text: The message to send to the bot.'''
        response = self.agent_executor.run(text)
        return response

    def invoke(self, entity: str, service: str, args: dict={}) -> dict:
        '''Invoke an API service. See main.py function `invoke` and services/api.py function `handle` for detailed information.

        :param entity: The target entity.
        :param service: The service of given entity to invoke.
        :param args: The arguments to pass to the service.'''
        return self.handler(entity, service, args)

    def _chat(self):
        input_text = input("User(exit to quit): ")
        while input_text != "exit":
            response = self.agent_executor.run(input_text)
            print("AI: "+response+"\n")
            input_text = input("User(exit to quit): ")

def debug_invoker(entity, service, args):
    # print("invoker activated!")
    # print(f"entity = {entity}")
    # print(f"service = {service}")
    # print("args")
    return "学号错误！"

# debug
if __name__=='__main__':
    print("run in chat.py")
    new_chat = ChatBot(debug_invoker)
    new_chat.chat("检查我的学号PB21071489是否正确")
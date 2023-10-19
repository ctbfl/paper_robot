from langchain.agents import Tool
from ai.chat import ChatBot
from json import dumps
empty = ""
def empty_func():
    return "没有动作需要执行，你现在可以输出Final Answer: 无需动作！"

def get_tools(chatbot_entity):
    def invoke_clap_hands(*args):
        result = chatbot_entity.invoke("clap_hands",args)
        return result

    def invoke_happy_face(*args):
        result = chatbot_entity.invoke("happy_face",args)
        return result

    val_student_id_tool = Tool(
        name="clap_hands",
        func=invoke_clap_hands,
        description="当判断用户意图为让你拍拍手的时候，你应当调用clap_hands这个工具，该工具Action Input为空"
    )

    get_course_table = Tool(
        name="happy_face",
        func=invoke_happy_face,
        description="判断用户意图为让你笑一笑的时候，你应当调用happy_face这个工具，该工具Action Input为空"
    )

    give_up_tool = Tool(
        name="nothing_to_do",
        func=empty_func,
        description="你不知道该做什么动作的时候，你应当调用nothing_to_do这个工具，该工具Action Input为空"
    )

    return [val_student_id_tool,get_course_table]
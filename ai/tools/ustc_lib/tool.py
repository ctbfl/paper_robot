from langchain.agents import Tool
from ai.chat import ChatBot
from json import dumps
import secret
empty = ""
def empty_func():
    return "没有动作需要执行，你现在可以输出Final Answer: 无需动作！"

def echo(my_string):
    return my_string

def get_tools(chatbot_entity):
    def set_face(face):
        if face == 'happy':
            secret.send_image_id("happy.jpg")
            return "表情happy设置完成，请输出Final Answer: Task Finished"
        elif face == 'sad':
            secret.send_image_id("sad.jpg")
            return "表情sad设置完成，请输出Final Answer: Task Finished"
        elif face == 'angry':
            secret.send_image_id("angry.jpg")
            return "表情angry设置完成，请输出Final Answer: Task Finished"
        elif face == 'nonplussed':
            secret.send_image_id("speechless.jpg")
            return "表情nonplussed设置完成，请输出Final Answer: Task Finished"
        else:
            secret.send_image_id("happy.png")
            return "表情设置完成，请输出Final Answer: Task Finished"

    set_face_tool = Tool(
        name="set_face",
        func=set_face,
        description="在回答用户的输入之前，请你根据你预期回复的语气或者心情选择一个表情。Action Input可选项有 happy, angry, sad, nonplussed，只能在其中选择。该工具返回为执行结果"
    )

    give_up_tool = Tool(
        name="nothing_to_do",
        func=empty_func,
        description="你不知道该做什么动作的时候，你应当调用nothing_to_do这个工具，该工具Action Input为空"
    )

    echo_tool = Tool(
        name = "echo",
        func= echo,
        description="debug专用，请你不要调用这个工具"
    )

    return [set_face_tool,echo_tool]
from ai.tools.Tools import Tool_list
from langchain.prompts import PromptTemplate

def create_prompt(tools: Tool_list):
    tool_descriptions = "\n".join([f"{tool.name}: {tool.description}" for tool in tools()])
    template_content = f"""你是一个智能机器人，需要根据用户的输入判断动作并执行。您可以采取以下Action（工具）帮助你完成用户的需求：

    {tool_descriptions}

    使用以下格式：

    Question: 用户的要求
    Thought: <请思考为了完成这个需求，你需要怎么做>
    Action: <选一个上面提供的工具Action名称>
    Action Input: <你需要执行的Action的具体输入>
    Observation: <Action返回的结果，是否执行成功的信息>
    Thought: ...(这个Thought/Action/Action Input/Observation的过程可以重复N次)
    Observation: <某动作>成功，本轮任务已完成，请返回Final Answer: Task Finished
    Final Answer: Task Finished


    样例：
    Question: 小机器人，笑一笑
    Thought: 为了完成笑一笑这个任务，我应当使用"happy_face"这个工具
    Action: happy_face
    Action Input: 
    Observation: 拍拍手成功，本轮任务已完成，请返回Final Answer: Task Finished
    Final Answer: 提供的学号是正确的

    接下来请你来接受用户需求完成动作，如果觉得不需要执行动作，也请输出Final Answer:无需动作！ 请严格按照上述格式的要求进行输出，最终输出结果前要写Final Answer不要忘记了：
    Question: {{input}}
    {{agent_scratchpad}}"""

    chinese_ReAct_prompt = PromptTemplate(
        input_variables=["input", "agent_scratchpad"], template=template_content
    )

    return chinese_ReAct_prompt
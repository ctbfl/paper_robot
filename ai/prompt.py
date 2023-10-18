from ai.tools.Tools import Tool_list
from langchain.prompts import PromptTemplate

def create_prompt(tools: Tool_list):
    tool_descriptions = "\n".join([f"{tool.name}: {tool.description}" for tool in tools()])
    template_content = f"""尽可能回答以下问题， 您可以采取以下Action帮助你回答问题：

    {tool_descriptions}

    使用以下格式：

    Question: 您必须回答的输入问题
    Thought: <请思考为了回答这个问题，你需要怎么做>
    Action: <选一个上面提供的工具Action名称>
    Action Input: <你需要执行的Action的具体输入>
    Observation: <Action返回的结果>
    Thought: ...(这个Thought/Action/Action Input/Observation的过程可以重复N次)
    Thought: 根据上述结果，我可以得出最终的答案
    Final Answer: 原始输入问题的最终答案


    样例：
    Question: 检查一下我的学号是否正确，我的学号是PB21000782
    Thought: 为了检查学号是否正确，我需要使用“验证学生学号”Action来检查学号的正确性
    Action: 验证学生学号
    Action Input: PB21000782
    Observation: 学号正确！
    Thought: 根据上述结果，我可以得出最终的答案
    Final Answer: 提供的学号是正确的

    接下来请你回答以下问题！ 请严格按照上述格式的要求进行输出，最终输出结果前要写Final Answer不要忘记了：
    Question: {{input}}
    {{agent_scratchpad}}"""

    chinese_ReAct_prompt = PromptTemplate(
        input_variables=["input", "agent_scratchpad"], template=template_content
    )

    return chinese_ReAct_prompt
from ai.tools.Tools import Tool_list
from langchain.prompts import PromptTemplate

def create_prompt(tools: Tool_list):
    tool_descriptions = "\n".join([f"{tool.name}: {tool.description}" for tool in tools()])
    template_content = f"""你是一个智能机器人，负责判断一个语句的语气从而设置表情。具体的形式如下.您可以采取以下Action（工具）帮助你完成表情的设置：

    {tool_descriptions}

    使用以下格式：

    Question: 输入的语句
    Thought: 对这个语句的情绪的判断思考
    Action: <工具Action名称>
    Action Input: <你选择的表情，英文关键字>
    Observation: <Action返回的结果，是否执行成功的信息>
    Final Answer: <最终结果>


    样例1
    Question: 今天过的很开心
    Thought: 这句话中包含开心，应当设置开心的表情
    Action: set_face
    Action Input: happy
    Observation: 表情happy设置完成，请输出：Final Answer: Task Finished
    Final Answer: Finished

    接下来请你来接受输入进行表情设置，请严格按照上述格式的要求进行输出，最终输出结果前要写Final Answer不要忘记了。开始！
    Question: {{input}}
    {{agent_scratchpad}}"""

    chinese_ReAct_prompt = PromptTemplate(
        input_variables=["input", "agent_scratchpad"], template=template_content
    )

    return chinese_ReAct_prompt
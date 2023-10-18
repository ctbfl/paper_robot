from langchain.agents import Tool
from ai.chat import ChatBot
from json import dumps

def get_tools(chatbot_entity):
    def invoke_validate_student_id(student_id):
        result = chatbot_entity.invoke("WestLib","validate_student_id",student_id)['response']
        # print("debug-接口返回值为：", result)
        if  result == True:
            return "经校验，学号正确！"
        else:
            return "经校验，学号错误！"

    def invoke_get_course_table(*args, **kwargs):
        result = chatbot_entity.invoke("JW","get_course_table")['response']
        course_table_string = dumps(result, ensure_ascii=False)   # 在这里写对于课表json转化为易读的文本的处理，目前仅仅转化为字符串，没做可读性提升
        return course_table_string

    val_student_id_tool = Tool(
        name="验证学生学号",
        func=invoke_validate_student_id,
        description="用于验证学生的学号是否正确，输入是一个字符串格式的学号，类似于PB21071489的形式，为两个字母加上八个数字，你需要从用户的输入中找到这个学号，并作为action input进行输入"
    )

    get_course_table = Tool(
        name="获取课表",
        func=invoke_get_course_table,
        description="用于获取用户的课程表，在回答与课程表相关的问题的时候很有用。不需要输入，返回值是用户的课表"
    )

    return [val_student_id_tool,get_course_table]
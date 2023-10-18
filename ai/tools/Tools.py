
class Tool_list:
    def __init__(self, args, llm = None, **kwargs): # 有写tools需要传入特定的参数进行初始化，比如LLM
        self._tools = []
        if llm == None:
            raise Exception("没有为Tool_list对象提供llm")

        chatbot_entity = kwargs.get('chatbot', None)  # Get the value of chatbot from kwargs or default to None

        # 导入USTC的工具

        from ai.tools import ustc_lib
        # self._tools.extend(es_lib.get_tools())
        self._tools.extend(ustc_lib.get_tools(chatbot_entity))


        if len(self._tools) == 0:
            raise NotImplementedError("当前还没有装载工具")

        if args.show_tool_info == True:
            print("所使用的工具：")
            print(self._tools)
            print()

    def name(self):
        return [item.name for item in self._tools]

    def __call__(self):
        return self._tools

    def items(self):
        return self._tools



def get_all_tools(llm, args, **kwargs):
    if llm is None:
        raise ValueError("没有传入LLM或LLM为空")
    if kwargs.get("chatbot") is None:
        raise ValueError("没有传入chatbot或chatbot为空")
    all_tools = Tool_list(args, llm=llm, **kwargs)
    return all_tools
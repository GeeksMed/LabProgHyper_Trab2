from application import tools_list
from application.model.entity.tools import Tools

class ToolsDAO:

    def __init__(self):
        self.tools_list = tools_list

    def retornar_tools(self):
        return self.tools_list
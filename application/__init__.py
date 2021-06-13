from flask import Flask, render_template, request, url_for
import os
from application.model.entity.tools import Tools

app = Flask(__name__, template_folder=os.path.abspath('application/view/templates'), static_folder=os.path.abspath('application/view/static'))

tools_list = [
    Tools(1, "Implementar Formulário Lab Programação Hipermídia", "https://github.com/UniversidadeDeVassouras/labproghiper-2021.1-todoweb",
         "O professor pediu para implementar o formulário no projeto que dei andamento até aqui",
         ["formulário", "programação"]),
    Tools(2, "Transformar o ToDoWeb em MVC", "https://github.com/UniversidadeDeVassouras/labproghiper-2021.1-todoweb",
         "O professor solicitou que eu aplicasse o MVC no projeto ToDoWeb",
         ["ToDoWeb", "MVC"]),
    Tools(3, "teste", "https://www.google.com" , "teste", ["teste", "teste2"]),
]

from application.controller import controller_tools
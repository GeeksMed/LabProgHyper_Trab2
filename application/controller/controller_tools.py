from application import app
from flask import Flask, render_template, request, url_for
from application.model.entity.tools import Tools

tools_list = [
    Tools(1, "Implementar Formulário Lab Programação Hipermídia", "https://github.com/UniversidadeDeVassouras/labproghiper-2021.1-todoweb",
         "O professor pediu para implementar o formulário no projeto que dei andamento até aqui",
         ["formulário", "programação"]),
    Tools(2, "Transformar o ToDoWeb em MVC", "https://github.com/UniversidadeDeVassouras/labproghiper-2021.1-todoweb",
         "O professor solicitou que eu aplicasse o MVC no projeto ToDoWeb",
         ["ToDoWeb", "MVC"]),
    Tools(3, "teste", "https://www.google.com" , "teste", ["teste", "teste2"]),
]

@app.route("/", methods=['GET'])
def home():
    return render_template("index.html", tools_list=tools_list)


@app.route("/inserir", methods=['POST'])
def inserir():
    titulo = request.form.get('titulo', None)
    link = request.form.get('link', None)
    descricao = request.form.get('descricao', None)
    tags = request.form.get('tags', None).split(" ")
    id = len(tools_list) + 1
    tools = Tools(id, titulo, link, descricao, tags)
    tools_list.append(tools)
    return render_template("index.html", tools_list=tools_list)


@app.route("/excluir/<int:id>", methods=['GET'])
def excluir(id: int):
    for tools in tools_list:
        if tools.id == id:
            tools_list.remove(tools)
            return render_template("index.html", tools_list=tools_list)
    return render_template("index.html", tools_list=tools_list), 404


@app.route("/busca")
def busca():
    tools_list_filtrado = []
    palavra_chave = request.args.get('palavra_chave')
    for tools in tools_list:
        if palavra_chave in tools.titulo or palavra_chave in tools.descricao:
            tools_list_filtrado.append(tools)
    return render_template("index.html", tools_list=tools_list_filtrado)

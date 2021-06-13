function fecharPopAdicionar(){
    pop = window.document.getElementById('pop');
    pop.style.display = 'none';
    janela = window.document.getElementById('principal');
    janela.style.opacity = '1.0';
}

function abrirPopAdicionar(){
    pop = window.document.getElementById('pop');
    pop.style.display = 'block';
    janela = window.document.getElementById('principal');
    janela.style.opacity = '0.5';
}

function fecharPopRemover(id){
    popRemover = window.document.getElementById(id);
    popRemover.style.visibility = "hidden";

    janela = window.document.getElementById('nome_principal');
    janela.style.opacity = '1.0';
    janela = window.document.getElementById('formulario-busca-tools');
    janela.style.opacity = '1.0';
    janela = window.document.getElementsByClassName('tools_card');
    for (var i = 0; i < janela.length; i++) {
        janela[i].style.opacity = '1.0';
    }
}

function abrirPopRemover(id){
    popRemover = window.document.getElementById(id);
    popRemover.style.visibility = "visible";

    janela = window.document.getElementById('nome_principal');
    janela.style.opacity = '0.5';
    janela = window.document.getElementById('formulario-busca-tools');
    janela.style.opacity = '0.5';
    janela = window.document.getElementsByClassName('tools_card');
    for (var i = 0; i < janela.length; i++) {
        janela[i].style.opacity = '0.5';
    }
}


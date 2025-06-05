var num1;
var num2;
var num3;

function entrada(){
     //entrada de dados - imputs 
    num1 = document.getElementById("n1").value;
    num2 = document.getElementById("n2").value;
}

function converter(){
    num1 = parseInt(num1);
    num2 = parseInt(num2);
}

function somar(){
    entrada();
    converter();
    //processamento, soma 
    total = num1+num2;
    //saida, escrever na tela
    tela = document.getElementById("resultado");
    tela.innerHTML = total;
}



function subtrair(){
    entrada();
    converter();
    //processamento, soma 
    total = num1 - num2;
    //saida, escrever na tela
    tela = document.getElementById("resultado");
    tela.innerHTML = total;
}

function multiplicar(){
    entrada();
    converter();
    //processamento, soma 
    total = num1 * num2;
    //saida, escrever na tela
    tela = document.getElementById("resultado");
    tela.innerHTML = total;
}
function dividir(){
    entrada();
    converter();
    //processamento, soma 
    total = num1 / num2;
    //saida, escrever na tela
    tela = document.getElementById("resultado");
    tela.innerHTML = total;
}
function limpar(){
    //entrada de dados - imputs
    num1 = document.getElementById("n1").value="";
    num2 = document.getElementById("n2").value="";
    tela = document.getElementById("resultado");
    tela.innerHTML = "";
}    
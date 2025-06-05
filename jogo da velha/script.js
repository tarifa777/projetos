//criando um variável, espaço de memoria a armazena um valor
var jogador = "x";

// uma função executa alguma ação, quando chamada 
//celula é um parâmetro, o valor de celular clicada é passado para a função 
function jogar(celula){

    //se a celula estuver vazia pode marcar
    // == igual
    // != Diferente
    // > Maior
    // < Menor
    if(celula.innerHTML == ""){
        //escrever na celula o "x" ou "0"
        celula.innerHTML = jogador;
        //se jogar for igual a "x"
        if(jogador == "x"){
            jogador = "0";      //altera a variavel para "0"
            celula.style.color = "blue"
        } else {
            jogador ="x"        //se não alterna a váriavel para "x"
            celula.style.color = "red"

        }
    }    

}

function reiniciar(){
    //criar lista com todos os quadros
    var celulas = document.querySelectorAll("td");

    for(var contador=0; contador <= 9; contador ++){
        celulas[contador].innerHTML = "";
        celulas[contador].style.backgroundColor = "";

    }
}
var nomes = ['Isabela', 'Bruno', 'Rafael', 'Angelo', ];
function sortear(){
    //lista / vetor
    //entre aspas é ums String: tipo de dados de texto
    //              0         1         2         3

    
    var nome1 = nomes[ Math.floor( Math.random() * nomes.length) ];
    var nome2 = nomes[ Math.floor( Math.random() * nomes.length) ];
    
    //enquanto nome1 === nome2
    if(nome1 === nome2){
        sortear();
    }else{

        alert("Jogador: " + nome1 + " vs " + nome2);
        //escrever na tela
        document.getElementById('jogador1').textContent = nome1;
    }   document.getElementById('jogador2').textContent = nome2; 
    /*
    alert("Sorteio de número com random" + Math.random());
    alert("Encontrando posição da lista: " + Math.random() * nomes.length);
    alert("Encontrando posição da lista 2: " +Math.floor(Math.random()*nomes.length));
    */
}

function adicionar(){
    //pega o texto do input com id="nome"
    var nome = document.getElementById("nome").value;
    //adiciona nome na lista
    nomes.push(nome);
}
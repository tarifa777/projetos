alert("Parabéns, vc acaba de ganhar uma viagem para pixar, tudo pago por nossa empresa, (só precisa fazer um pequeno deposito de R$ 500 para seu pacote ser liberado");


var visitante= 2000;
var nome = "Gustavo Henrique";

//se o visitante = 2000 ganha o prêmio
if(visitante === 2000){
    alert("parabens "+nome+", você ganhou 50 mil reais!");
}else{
    alert("Perdeu hahaha!!");
}
 


/*comentário*/
//obtém o componente do menu do celular(icone)
var celular = document.querySelector('.celular');
//obtém lista
var listamenu = document.querySelector('.menu ul');

//evento de click no menu
celular.addEventListener('click', function(){
    listamenu.classList.toggle('mostraMenu');
});

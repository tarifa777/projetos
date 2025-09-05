function buscar(){
    //pegar o cep do input
    cep = document.getElementById("cep").value;
    
    var url = "https://viacep.com.br/ws/"+cep+"/json/"

    //faz a busca na api de cep
    fetch(url)
    .then(response => response.json())
    .then(dados => {
        if(dados.erro){
            //se tiver erro
        document.getElementById("resultado").textContent = 'CEP invalido!';
        }else{
            //se nao tiver erro
            document.getElementById("resultado").innerHTML =
            '<strong> Cidade: </strong> '+dados.localidade + '<br>'
            + '<strong> cep: </strong>'+ dados.cep + '<br>'
            + '<strong> logradouro: </strong>'+ dados.logradouro + '<br>'
            + '<strong> complemento: </strong>'+ dados.complemento + '<br>'
            + '<strong> bairro: </strong>'+ dados.bairro + '<br>'
            + '<strong> estado: </strong>'+ dados.estado + '<br>'
            + '<strong> região: </strong>'+ dados.regiao + '<br>'
        }

    } ).catch(error => alert('erro na conexão: '+ error));


}

idade = 17 
#booleano - tipo de dado que pode ser verdadeiro ou falso
estudante = True
temconvite = False

#pode entrar
#Se a pessoa tem mais de 17 anos e tem convite
#ou se a pessoa tem menos de 18 anos e é estudante

if(idade >= 18 and temconvite) or (idade < 18 and estudante):
    print("entra no baile 😎")
else:
    print("nao pode entrar!  😔")


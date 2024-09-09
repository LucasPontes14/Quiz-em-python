"""disciplina: INTRODUÇÃO À PROGRAMAÇÃO
   Turma: INFO 1M
   Componentes: ANA CAROLINA, ANGELA FERNANDES, LETÍCIA GABRIELA E LUCAS PONTES"""

print("Menu para os quizes")

print("digite 1 para ir para o QUIZ SOBRE PAÍSES")
print("digite 2 para ir para o QUIZ SOBRE FILMES")
print("digite 3 para ir para o QUIZ SOBRE A LINGUAGEM DE MARCAÇÃO: HTML")
print("digite 4 para SAIR")

quiz = int(input("Digite dua escolha: "))
 
if (quiz == 1):
    print("Você escolheu o QUIZ SOBRE PAÍSES!!!")
    print("Quiz sobre países!\n")
    print("Bem-vindo(a)!")

    acertos = 0
    total_perguntas = 4

    print("Questão 1:")
    print("Qual é o país mais populoso do mundo?")
    print("1. China")
    print("2. Índia")
    print("3. Estados Unidos")
    print("4. Indonésia")

    resposta_usuario = int(input("Escolha uma opção (1, 2, 3 ou 4): "))

    if resposta_usuario == 1:
        print("Resposta correta!")
        acertos += 1
    elif resposta_usuario == 2:
        print("Resposta incorreta")
    elif resposta_usuario == 3:
        print("Resposta incorreta")
    elif resposta_usuario == 4:
        print("Resposta incorreta")
    else:
        print("Resposta inválida.")
    
    print("Questão 2:")
    print("Qual é a capital dos EUA?")
    print("1. Nova York")
    print("2. Los Angeles")
    print("3. Washington, D.C.")
    print("4. Chicago")

    resposta_usuario = int(input("Escolha uma opção (1, 2, 3 ou 4): "))

    if resposta_usuario == 3:
        print("Resposta correta!")
        acertos += 1
    elif resposta_usuario == 1:
        print("Resposta incorreta")
    elif resposta_usuario == 2:
        print("Resposta incorreta")
    elif resposta_usuario == 4:
        print("Resposta incorreta")
    else:
        print("Resposta inválida")

    print("Questão 3:")
    print("O Brasil fica localizado em qual continente?")
    print("1. Ásia")
    print("2. Europa")
    print("3. Oceania")
    print("4. América")

    resposta_usuario = int(input("Escolha uma opção (1, 2, 3 ou 4): "))

    if resposta_usuario == 4:
        print("Resposta correta!")
        acertos += 1
    elif resposta_usuario == 1:
        print("Resposta incorreta")
    elif resposta_usuario == 2:
        print("Resposta incorreta")
    elif resposta_usuario == 3:
        print("REsposta incorreta")
    else:
        print("Resposta inválida")

    print("Questão 4:")
    print("Qual país tem mais ilhas no mundo?")
    print("1. Noruega")
    print("2. Suécia")
    print("3. Canadá")
    print("4. Grécia")
 
    resposta_usuario_3 = int(input("Escolha uma opção (1, 2, 3 ou 4): "))

    if resposta_usuario_3 == 2:
        print("Resposta correta!")
        acertos += 1
    elif resposta_usuario_3 == 1:
        print("Resposta incorreta")
    elif resposta_usuario_3 == 3:
        print("Resposta incorreta")
    elif resposta_usuario_3 == 4:
        print("Resposta incorreta")
    else:
        print("Resposta inválida")

    percentual_acertos = (acertos / total_perguntas) * 100
    percentual_erros = 100 - percentual_acertos

    print("Situação final:")
    print(f"Você acertou {acertos} de {total_perguntas} perguntas.")
    print(f"Percentual de acertos: {percentual_acertos:.2f}%")
    print(f"Percentual de erros: {percentual_erros:.2f}%")

    print("Fim do quiz sobre países!")
    print("Obrigado por participar!")

elif (quiz == 2):
    print("Você escolheu o QUIZ SOBRE FILMES!!!")
    print("Quiz sobre filmes!")
    print("Bem-vindo(a)!")

    respostascorretas = 0

    print("Questão 1:")
    print("Qual é o clássico de Hollywood que retrata um naufrágio?")
    print("Titanic")
    print("Ghost")
    print("Cantando na chuva")
    print("Uma odisseia no espaço")

    pergunta_1 = input ("Digite aqui a opção correta:")

    if (pergunta_1 == "Titanic"):
        print("Resposta correta!")
        respostascorretas += 1
    elif (pergunta_1 == "Ghost"):
        print("Resposta incorreta")
    elif (pergunta_1 == "Cantando na chuva"):
        print("Resposta incorreta")
    elif (pergunta_1 == "Uma odisseia no espaço"):
        print("Resposta incorreta")
    else:
        print("Resposta inválida! :(")

    print("Questão 2:")
    print("Qual é o filme de maior bilheteria no mundo?")
    print("Avatar (2009)")
    print("Titanic")
    print("Vingadores Ultimato")
    print("Star Wars (2015)")
    
    pergunta_2 = input ("Digite aqui a opção correta:")

    if (pergunta_2 == "Avatar (2009)"):
        print("Resposta correta!")
        respostascorretas += 1
    elif (pergunta_2 == "Titanic"):
        print("Resposta incorreta")
    elif (pergunta_2 == "Vingadores Ultimato"):
        print("Resposta incorreta")
    elif(pergunta_2 == "Star Wars (2015)"):
        print("Resposta incorreta")
    else:
        print("Resposta inválida! :(")

    print("Questão 3:")
    print("Que filme ganhou o primeiro Oscar no mundo?")
    print("Melodia na Broadway")
    print("Grande Hotel")
    print("Asas")
    print("Cimarron")

    pergunta_3 = input ("Digite aqui a opção correta:")

    if (pergunta_3 == "Asas"):
        print("Resposta correta!")
        respostascorretas += 1
    elif (pergunta_3 == "Melodia na Broadway"):
        print("Resposta incorreta")
    elif (pergunta_3 == "Grande Hotel"):
        print("Resposta incorreta")
    elif (pergunta_3 == "Cimarron"):
        print("Resposta incorreta")
    else:
        print("Resposta inválida!!! :(")

    print("Questão 4:")
    print("Qual é a maior saga de filmes do mundo?")
    print("Harry Potter")
    print("Star Wars")
    print("Velozes e Furiosos")
    print("Godzilla")

    pergunta_4 = input ("Digite aqui a opção correta:")

    if (pergunta_4 == "Godzilla"):
        print("Resposta correta!")
        respostascorretas += 1
    elif (pergunta_4 == "Harry Potter"):
        print("Resposta incorreta")
    elif (pergunta_4 == "Star Wars"):
        print("Resposta incorreta")
    elif (pergunta_4 == "Velozes e Furiosos"):
        print("Resposta incorreta")
    else:
        print("Resposta inválida")

    acertosporcento = (respostascorretas/4)*100
    errosporcento = 100-acertosporcento

    print("Total de acertos: ", respostascorretas)
    print("Porcentagem de acertos: ", acertosporcento)
    print("Porcentagem de erros: ", errosporcento)
    print("Fim do quiz sobre filmes!")
    print("Obrigado por participar!")

elif (quiz == 3):
    print("Você escolheu o QUIZ SOBRE A LINGUAGEM DE MARCAÇÃO: HTML!!!")
    print("Quiz sobre HTML!")
    print("Bem-vindo(a)!")

    totalacertos = 0

    print("Questão 1:")
    print("Qual das tags abaixo usamos para informar que estamos na versão do html5?")
    print("<!DOCTYPE html>")
    print("<h1>")
    print("<p>")
    print("<link>")

    quest1 = input("Digite a resposta certa, certifique-se de escrever as tags corretamente: ")

    if (quest1=="<!DOCTYPE html>"):
        print("Resposta certa!")
        totalacertos += 1
    elif (quest1=="<h1>"):
        print("Resposta incorreta")
    elif (quest1=="<p>"):
        print("Resposta incorreta")
    elif (quest1=="<link>"):
        print("Resposta incorreta")
    else:
        print("Resposta inválida")

    print("Questão 2:")
    print("Qual a função da tag <br>?")
    print("a) Criar um parágrafo")
    print("b) Adicionar uma linha horizontal") 
    print("c) Adicionar uma quebra de linha")
    print("d) Adicionar um link")

    quest2 = input("Digite a letra da alternativa correta, certifique-se de escrever em letra minúscula: ")

    if (quest2=="a"):
        print("Resposta incorreta")
    elif (quest2=="b"):
        print("Resposta incorreta")
    elif (quest2=="c"):
        print("Resposta certa!")
        totalacertos += 1
    elif (quest2=="d"):
        print("Resposta incorreta")
    else:
        print("Resposta inválida")

    print("Questão 3")
    print("Qual atributo usamos na tag <img> para alterar sua altura?")
    print("a) Width ")
    print("b) Height")
    print("c) Alt")
    print("d) Href")

    quest3 = input("Digite a letra da alternativa correta, certifique-se de escrever em letra minúscula: ")

    if (quest3=="a"):
        print("Resposta incorreta")
    elif (quest3=="b"):
        print("Resposta certa!")
        totalacertos += 1
    elif (quest3=="c"):
        print("Resposta incorreta")
    elif (quest3=="d"):
        print("Resposta incorreta")
    else:
        print("Resposta inválida")

    print("Questão 4: ")
    print("Qual o atributo que nos permite alterar a fonte utilizada?")
    print("a) id")
    print("b) font-size ")
    print("c) font-style ")
    print("d) font-family")

    quest4 = input("Digite a letra da alternativa correta, certifique-se de escrever em letra minúscula: ")

    if (quest4=="a"):
        print("Resposta incorreta")
    elif (quest4=="b"):
        print("Resposta incorreta")
    elif (quest4=="c"):
        print("Resposta incorreta")
    elif (quest4=="d"):
        print("Resposta certa!")
        totalacertos += 1
    else:
        print("Resposta inválida")

    porcentagemdeacertos = (totalacertos/4)*100
    porcentagemdeerros = 100-porcentagemdeacertos

    print("Suas estatísticas:")
    print("O seu total de acertos foi de: ", totalacertos)
    print("Porcentagem de acertos: ", porcentagemdeacertos)
    print("Porcentagem de erros: ",  porcentagemdeerros)

    print("Fim do quiz sobre HTML")
    print("Obrigado por participar!")
    
elif (quiz == 4):
    print("Saindo...")
else:
    print("Opção inválida. Tente novamente.")   
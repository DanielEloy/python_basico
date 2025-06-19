def verifica_ingresso(idade, cliente_estudante):
	### Seu código aqui.
    if cliente_estudante or idade >= 60:
        return "Você tem direito a meia entrada"
    else:
        return "Você não tem direito a meia entrada"
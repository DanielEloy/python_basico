def calcula_imc(peso, altura):
    imc = peso / (altura ** 2)
    imc = round(imc, 2)
    if imc < 18.5:
        classificacao = "Abaixo do Peso"
    elif 18.5 <= imc < 25:
        classificacao = "Peso Normal"
    elif 25 <= imc < 30:
        classificacao = "Sobrepeso"
    elif 30 <= imc < 35:
        classificacao = "Obesidade Grau I"
    elif 35 <= imc < 40:
        classificacao = "Obesidade Grau II"
    else:
        classificacao = "Obesidade Grau III"
    return classificacao
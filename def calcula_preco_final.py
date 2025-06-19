def calcula_preco_final(preco_unitario, quantidade):
    if 1 <= quantidade <= 5:
        desconto = 0
    elif 6 <= quantidade <= 10:
        desconto = 0.05
    elif 11 <= quantidade <= 20:
        desconto = 0.10
    else:  # acima de 20
        desconto = 0.15
    preco_final = preco_unitario * quantidade * (1 - desconto)
    return round(preco_final, 2)
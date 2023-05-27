preco = float(input("Qual o preço que você vai pagar pelo produto? "))
desconto = preco - (preco * 5) / 100
print(f"Parabéns! você recebeu um desconto de 5%.", end=' ')
print(f"O produto custava R${preco:.2f} e agora vai custar R${desconto:.2f}.")

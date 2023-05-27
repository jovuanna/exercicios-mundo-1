largura = float(input("Largura da parede: "))
altura = float(input("Altura da parede: "))
area = largura * altura
quantidade_de_tinta = area / 2 #a cada litro de tinta da pra pintar 2m² de parede
print(f"Sua parede tem a área igual a {area} e precisará de {quantidade_de_tinta:.2f} litros.")


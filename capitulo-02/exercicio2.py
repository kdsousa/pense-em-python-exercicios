"""
Enunciado 2: Suponha que o preço de capa de um livro seja R$ 24,95, mas as 
livrarias recebem um desconto de 40%. O transporte custa R$ 3,00 para o 
primeiro exemplar e 75 centavos para cada exemplar adicional. 
Qual é o custo total de atacado para 60 cópias?
"""
preco_capa = 24.95
desconto = 0.40
preco_com_desconto = preco_capa * (1 - desconto)
total_copias = 60
custo_livros = preco_com_desconto * total_copias
custo_transporte = 3.00 + (0.75 * (total_copias - 1))
custo_total_atacado = custo_livros + custo_transporte

print(f"O preço de um livro com desconto é: R$ {preco_com_desconto:.2f}")
print(f"O custo total de atacado para 60 cópias é: R$ {custo_total_atacado:.2f}\n")

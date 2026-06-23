"""
3- Se você correr 10 quilômetros em 42 minutos, qual é o seu passo médio (tempo por milha em minutos e segundos)? Qual é a seua velocidade média em milhas por hora?
"""
km = 10
tempo_min = 42

milhas = km / 1.609
passo = tempo_min / milhas

minutos = int(passo)
segundos = round((passo - minutos) * 60)

velocidade = milhas / (tempo_min / 60)

print(f"Passo médio: {minutos}:{segundos:02d} min/milha")
print(f"Velocidade média: {velocidade:.2f} mph")

"""
Enunciado 3: Se eu sair da minha casa às 6:52 e correr 1 quilômetro a um 
certo passo (8min15s por quilômetro), então 3 quilômetros a um passo mais 
rápido (7min12s por quilômetro) e 1 quilômetro no mesmo passo usado em 
primeiro lugar, que horas chego em casa para o café da manhã?
"""
hora_partida_segundos = (6 * 3600) + (52 * 60)
tempo_passo_lento_seg = (8 * 60) + 15 
tempo_passo_rapido_seg = (7 * 60) + 12
tempo_total_corrida_seg = (2 * tempo_passo_lento_seg) + (3 * tempo_passo_rapido_seg)
hora_chegada_segundos = hora_partida_segundos + tempo_total_corrida_seg
hora_chegada = hora_chegada_segundos // 3600
minuto_chegada = (hora_chegada_segundos % 3600) // 60

print(f"Você chegará em casa para o café da manhã às {int(hora_chegada)}:{int(minuto_chegada):02d}")

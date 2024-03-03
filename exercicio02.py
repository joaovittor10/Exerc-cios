Exercicio
2-Código que encontre uma peça repetida dentro de um jogo da memória de 20 peças
Resposta:

pecas = [...]


pecas_analisadas = []
peca_repetida = None

for peca in pecas:
    if peca in pecas_analisadas:
        peca_repetida = peca
        break
    else:
        pecas_analisadas.append(peca)

if peca_repetida:
    print("Peça repetida encontrada:", peca_repetida)
else:
    print("Nenhuma peça repetida encontrada.")

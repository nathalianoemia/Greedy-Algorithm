print('Calorias e macronutrientes: Proteínas, Fibras, Carboidratos\n')
calorias_max = int(input('Digite o número máximo de calorias:\n'))

alimentos = []
calorias_consumidas = 0
proteinas_consumidas = 0
fibras_consumidas = 0
carboidratos_consumidos = 0

Macros = [
    ('Batata doce', 56, 1, 2, 13),
    ('Frango grelhado', 159, 32, 0, 0),
    ('Arroz', 128, 3, 2, 28),
    ('Brócolis Cozido', 25, 2, 4, 5),
    ('Banana', 39, 1, 1, 11),
    ('Iogurte natural', 126, 7, 0, 9),
]

# Ordena a lista de alimentos pelo valor de proteínas (índice 2)
Macros.sort(key=lambda x: x[2], reverse=True)

# Loop para escolher o alimento com maior valor de proteínas
for alimento in Macros:
    nome, calorias, proteinas, fibras, carboidratos = alimento
    if calorias_consumidas + calorias <= calorias_max:
        calorias_consumidas += calorias
        proteinas_consumidas += proteinas
        fibras_consumidas += fibras
        carboidratos_consumidos += carboidratos
        alimentos.append(nome)

#reordena a lista com base nas fibras apenas se o limite de calorias não tiver sido atingido
if calorias_consumidas < calorias_max:
    Macros.sort(key=lambda x: x[3], reverse=True)

    #Escolhe o alimento com maior valor de fibras
    for alimento in Macros:
        nome, calorias, proteinas, fibras, carboidratos = alimento
        if calorias_consumidas + calorias <= calorias_max:
            calorias_consumidas += calorias
            fibras_consumidas += fibras
            carboidratos_consumidos += carboidratos
            alimentos.append(nome)

#reordena a lista com base nos carboidratos apenas se o limite de calorias não tiver sido atingido
if calorias_consumidas < calorias_max:
    Macros.sort(key=lambda x: x[4], reverse=True)

    #escolhe o alimento com maior valor de carboidratos
    for alimento in Macros:
        nome, calorias, proteinas, fibras, carboidratos = alimento
        if calorias_consumidas + calorias <= calorias_max:
            calorias_consumidas += calorias
            carboidratos_consumidos += carboidratos
            alimentos.append(nome)

print('\nAlimentos escolhidos:')
for alimento in alimentos:
    print(alimento)

print(f'\nCalorias consumidas: {calorias_consumidas} kcal')
print(f'Proteínas consumidas: {proteinas_consumidas}g')
print(f'Fibras consumidas: {fibras_consumidas}g')
print(f'Carboidratos consumidos: {carboidratos_consumidos}g')

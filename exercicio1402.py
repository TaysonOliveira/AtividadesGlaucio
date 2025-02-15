print()

alturas = []
generos = []

print("---------- Digite as Informações a Seguir! ----------")
for i in range (15):
    altura = float(input(f"Pessoa {i+1} - Digite a altura em metros: "))
    genero = input("Digite o genero desta peesoa (M/F): ") .upper()

    alturas.append (altura);
    generos.append (genero);

alturas_m = [alturas[i] for i in range(15) if generos[i] == "M"]
alturas_f = [alturas[i] for i in range(15) if generos[i] == "F"]

media_altura_m = sum(alturas_m) / len(alturas_m)
num_f = generos.count("F")

maior_altura_m = max(alturas_m)
menor_altura_m = min(alturas_m)
maior_altura_f = max(alturas_f)
menor_altura_f = min(alturas_f)

print()

print("Média de altura dos homens:", round(media_altura_m, 2), "m")
print("Número de mulheres:", num_f)
print("Maior altura dos homens:", maior_altura_m, "m")
print("Menor altura dos homens:", menor_altura_m, "m")
print("Maior altura das mulheres:", maior_altura_f, "m")
print("Menor altura das mulheres:", menor_altura_f, "m")
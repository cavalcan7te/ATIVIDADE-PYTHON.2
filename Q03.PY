nome = input("Diga seu nome:")
idade = int(input("Diga sua idade:"))
if idade < 16:
    print(f"{nome} não está apto a votar.")
else:
    print(f"{nome} está apto a votar.")
nota = int(input("Digite sua nota:"))
if nota >= 7:
    print("aprovado")
elif nota < 7 and nota >= 5:
    print("recuperação")
else:
    print("reprovado")
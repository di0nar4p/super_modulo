count = 0
print(f"{'*' * 15} Nota media do aluno {'*' * 15}")
for i in range(1, 4+1):
    nota = float(input(f" Digite a {i}ª nota do aluno: "))
    count += nota 
media = count / 4
print(f"A media do aluno é {media}")

if media >= 10:
    print("Aprovado com louvor!!")
elif media >= 7:
    print("Aprovado :)")
elif media == 5: 
    print("Recuperação")
elif media < 5:
    print("Reprovado")
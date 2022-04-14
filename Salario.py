# Aumento Múltiplos -- Salário % dependendo do salário
# R$1250 aumento de 10%
# Inferriores ou igual, o aumento é de 15%
print('###'*20)
salário = float(input("Qual é o salário do funcionario? R$ "))
if salário <= 1300:
    novo = salário + (salário * 15 /100)
else:
    novo = salário + (salário * 10 /100)

print("Quem ganhava  R$ {:.2f} passa ganhar R$ {:.2f} agora.".format(salário, novo))
print('###'*20)
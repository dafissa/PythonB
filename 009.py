print("Qual seu sexo?")
print("1 - Masculino")
print("2 - Feminino")
input()
peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura (sem pontuação): '))

imc = peso / (altura * 2)

print('Seu IMC é: {0}'.format(imc))

if imc <= 18.5:
    print("Você está abaixo do peso!")
elif imc > 18.5 and imc <= 24.9:
    print("Você está no peso ideal.")
elif imc > 24.9 and imc <= 29.9:
    print("Você está acima do peso!")
else:
    print("Você está com obesidade")

torax = float(input("Digite as medidas do seu tórax (em centímetros): "))
cintura = float(input("Digite as medidas da sua cintura (em centímetros): "))
quadril = float(input("Digite asmedidas do seu quadril (em centímetros): "))

abdomen = input()

if abdomen <= 94.0:
    print("Você tem o abdomen ideal!")
elif abdomen > 94:
    print("Seu abdomen está acima da média. Preste atenção!")

input()
print("Olá, seja bem-vindo ao atendimento expresso da clínica de Guarulhos! Por favor, digite um dos números abaixo para que póssamos agendar sua consulta.")
print("1 - Pediatria")
print("2 - Clínico geral")
print("3 - Ginecologia")
print("4 - Obstetrícia")
print("5 - Dermatologia")
print("6 - Cardiologia")
print("7 - Ortopedia")
numero = input()
if numero == ("1"):
    print("Ok, verificaremos as datas dispóniveis para a pediatra.")
if numero == ("2"):
    print("Ok, verificaremos as datas dispóniveis para o clínico geral.")
if numero == ("3"):
    print("Ok, verificaremos as datas dispóniveis para a ginecologista.")
if numero == ("4"):
    print("Ok, verificaremos as datas dispóniveis para a obstétrico.")
if numero == ("5"):
    print("Ok, verificaremos as datas dispóniveis para a dermatologista.")
if numero == ("6"):
    print("Ok, verificaremos as datas dispóniveis para a cardiologista.")
if numero == ("7"):
    print("Ok, verificaremos as datas dispóniveis para a ortopedista.")
else:
    print("Desculpe, não identificamos o número que foi digitado. Por favor, escolha e digite uma das opções acima.")

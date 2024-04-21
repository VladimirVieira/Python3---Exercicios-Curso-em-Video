'''
Faça um programa que leia algo pelo teclado e motre na tela o sequ tipo primitivo
e todas as informações possíveis sobre ele.
'''
algo = input("Digite alguma informação que deseja analisar:")
print("O tipode primitivo desse valor é:",type(algo))
print("Só tem espaços:", algo.isspace())
print("É um número:",algo.isnumeric())
print("É alfabético:",algo.isalpha())
print("É alfanumérico:",algo.isalnum())
print("Está em maiusculas:",algo.isupper())
print("Está em minusculas:",algo.islower())
print("Está capitalizado:",algo.istitle())

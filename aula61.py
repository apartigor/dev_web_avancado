""" Calculadora com While """



while True:

    num1 = input("Digite o primeiro número: ")
    num2 = input("Digite o segundo número: ")
    op = input("Selecione o operador (+-*/): ")

    nums_validos = None

    try:
        num1_float = float(num1)
        num2_float = float(num2)
        nums_validos = True
    except:
        nums_validos = None
    
    if nums_validos is None:
        print("Um ou ambos os números digitados são inválidos.")
        continue

    op_permitidos = '+-*/'

    if op not in op_permitidos:
        print("Operador inválido")
        continue

    if len(op) > 1:
        print("Digite apenas um operador")
        continue

    print("Realizando a conta...")

    if op == "+":
        resultado = num1_float + num2_float
        print(f"Resultado da soma entre {num1} e {num2} é igual a: {resultado:.2f}")
    elif op == "-":
        resultado = num1_float - num2_float
        print(f"Resultado da subtração entre {num1} e {num2} é igual a: {resultado:.2f}")
    elif op == "*":
        resultado = num1_float * num2_float
        print(f"Resultado da multiplicação entre {num1} e {num2} é igual a: {resultado:.2f}")
    elif op == "/":
        if num2_float != 0:
            resultado = num1_float / num2_float
            print(f"Resultado da divisão entre {num1} e {num2} é igual a: {resultado:.2f}")
        else:
            print('Impossível realizar divisão com 0!')
    else:
        print("Como chegou aqui?")
    
    sair = input("Deseja finalizar o sistema? [S]im: ").lower().startswith("s")
    if sair is True:
        break

    

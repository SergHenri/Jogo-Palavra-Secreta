""" Faça um jogo para o usuário adivinhar qual a palavra secreta.

Você vai propor uma palavra secreta qualquer e vai dar a possibilidade para o usuário digitar apenas uma letra.
Quando o usuário digitar uma letra, você vai conferir se a letra digitada está na palavra secreta.
Se a letra digitada estiver na palavra secreta; exiba a letra;
Se a letra digitada não estiver na palavra secreta; exiba *. Faça a contagem de tentativas do seu usuário. """



# Início de um loop infinito para continuar realizando operações até o usuário escolher sair
while True:
    # Solicita ao usuário dois números e um operador para a operação
    numero_1 = input('Digite um numero')  # Solicita o primeiro número
    numero_2 = input('Digite um numero')  # Solicita o segundo número
    operador = input('Digite um operador (+-/*)')  # Solicita o operador (soma, subtração, multiplicação ou divisão)

    # Variável para verificar se os números fornecidos são válidos
    numeros_validos = None

    # Inicializa as variáveis para os números convertidos para float
    numero_1_float = 0
    numero_2_float = 0

    # Tenta converter os números fornecidos para tipo float
    try:
        numero_1_float = float(numero_1)  # Converte o primeiro número para float
        numero_2_float = float(numero_2)  # Converte o segundo número para float
        numeros_validos = True  # Se a conversão for bem-sucedida, marca os números como válidos
    except:
        # Se ocorrer erro na conversão, marca os números como inválidos
        numeros_validos = None

    # Verifica se algum dos números não foi válido
    if numeros_validos is None:
        print('Um dos numero não é valido')  # Exibe uma mensagem de erro
        continue  # Reinicia o loop, pedindo os números novamente

    # Define os operadores permitidos
    operadores_permitidos = '+-/*'

    # Verifica se o operador fornecido é válido
    if operador not in operadores_permitidos:
        print('Operador Invalido')  # Exibe uma mensagem de erro caso o operador seja inválido
        continue  # Reinicia o loop, pedindo os dados novamente

    # Verifica se o usuário forneceu mais de um caractere para o operador
    if len(operador) > 1:
        print('Digite apenas um operador')  # Exibe uma mensagem de erro
        continue  # Reinicia o loop, pedindo os dados novamente

    # Informa ao usuário que a operação será realizada
    print('Realizando sua conta. Confira o resultado abaixo')

    # Realiza a operação conforme o operador fornecido
    if operador == '+':
        print(numero_1_float + numero_2_float)  # Realiza a soma
    elif operador == '-':
        print(numero_1_float - numero_2_float)  # Realiza a subtração
    elif operador == '*':
        print(numero_1_float * numero_2_float)  # Realiza a multiplicação
    elif operador == '/':
        print(numero_1_float / numero_2_float)  # Realiza a divisão
    else:
        print('Operador Invalido')  # Caso o operador não seja reconhecido, exibe uma mensagem de erro

    # Pergunta ao usuário se ele deseja sair do programa
    sair = input('Quer sair? [s]im: ').lower().startswith('s')

    # Se o usuário digitar "sim", o loop é interrompido
    if sair is True:
        break  # Encerra o loop e o programa

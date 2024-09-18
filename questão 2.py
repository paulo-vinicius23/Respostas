def pertence_fibonacci(numero):
    # Inicia a sequência de Fibonacci com os dois primeiros valores
    fibonacci = [0, 1]
    
    # Gera a sequência até que o último valor seja maior ou igual ao número informado
    while fibonacci[-1] < numero:
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    
    # Verifica se o número informado pertence à sequência de Fibonacci
    if numero in fibonacci:
        return f"O número {numero} pertence à sequência de Fibonacci."
    else:
        return f"O número {numero} não pertence à sequência de Fibonacci."

numero_verificar = int(input("Digite um número: "))
print(pertence_fibonacci(numero_verificar))

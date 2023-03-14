def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

num = int(input("Digite um número para verificar se ele pertence à sequência de Fibonacci: "))

pertence = False
i = 0
while fibonacci(i) <= num:
    if fibonacci(i) == num:
        pertence = True
        break
    i += 1

if pertence:
    print(f"{num} pertence à sequência de Fibonacci.")
else:
    print(f"{num} não pertence à sequência de Fibonacci.")
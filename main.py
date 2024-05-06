import math

# Os computadores usualmente calculam diferentes senos, usando a série de taylor. 
# Exemplo a baixo: 

# Poderia-se usar a função math.factorial, 
# mas também podemos escrever a nossa própria:
def fatorial(n):
    fatorial = 1
    if n == 0:
        return fatorial
    else:
        for i in range(n):
            i += 1
            fatorial *= i
    return fatorial

def seno(x):
    somatorio = 0.0
    n = 0
    while(n <= 80):

        # Calcula-se os três elementos do somatório 
        # Separando a fórmula em três elementos
        # e salvando o valor de cada um, numa variável.
        # Cada elemento está separado por cor na imagem anexa.
        numerador = math.pow(-1.0, n) # Está em amarelo na imagem.
        denominador = fatorial(2 * n + 1) # Está em rosa. 
        fator = x ** (2*n + 1) # Está em laranja. 
        # Calcula-se o termo do somatório com o valor de n atual: 
        termo = numerador / denominador * fator
        # Soma-se aos calculos já feitos: 
        somatorio += termo
        n += 1
    # A função retorna o valor calculado: 
    return somatorio

# Usando as funções:
print(seno(3.14/4))


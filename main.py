import math

# Os computadores usualmente calculam diferentes senos, usando a série de taylor. 
# A série de taylor encontra-se anexada nos arquivos. 

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


def graus_em_radi(x):
    return x * math.pi / 180 # Acessando o valor de pi pela biblioteca math

def seno(x):
    if x > 360 or x < 0:
        return None # Terminamos a execução da função caso o valor de x, seja inválido. Graus são de 0 a 360.
    somatorio = 0.0
    n = 0
    # converte o valor em graus salvo na variável x em radiano, e salva na própria x 
    x = graus_em_radi(x)
    while(n < 80):
        # Serão realizadas 80 somas, é o suficiente, visto que quando maior n, a fórmula mais tende a 0. 
        # Realiza-se o cálculo separando a função em três partes distinstas
        # e salvando o valor de cada oarte, numa variável.
        # Cada parte está separada por uma cor na imagem anexa.
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
print("Seno de 30 graus:",seno(30)) # O ângulo é passado em graus. 
print("Seno de 40 graus:",seno(40)) # O ângulo é passado em graus. 
print("Seno de 50 graus:",seno(50)) # O ângulo é passado em graus. 
print("Seno de 255 graus:",seno(50)) # O ângulo é passado em graus. 
print("Seno de -5 graus:",seno(-5)) #Inválido. 

import matplotlib.pyplot as plt
import numpy as np


def adicao(x,y):
    adicao1 = x + y
    print(f"{x} + {y} = {adicao1}")
    
def subtracao(x,y):
    subtracao1 = x - y
    print(f"{x} - {y} = {subtracao1}")
    
def multiplicacao(x,y):
    multiplicacao1 =  x * y
    print(f"{x} x {y} = {multiplicacao1}")
    
def divisao(x,y):
    divisao1 =  x / y
    print(f"{x} ÷ {y} = {divisao1}")

def exponenciacao(x,y):
    exponenciacao1 = x ** y
    print(f"{x}^{y} = {exponenciacao1}")

def fatorial(z):
    if z == 0:
        return 1
    elif z != 0:
        fatorial1 = 1
        for numero in range(1, z + 1):
            fatorial1 *= numero
        return fatorial1

def funcaolinear(x, a, b):
    return a * x + b # type: ignore
    
    
def graflinear(a, b):
    x = np.linspace(-10, 10, 100)
    y = funcaolinear(x, a, b)
    plt.plot(x, y, color="pink")
    plt.title(f'Gráfico da função linear {a}x + {b}')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)
    plt.show()
    
def funcaoquadratica(x, a, b, c):
    return a * x ** 2 + b * x + c

def calcularraizes(a, b, c):
    delta = b ** 2 - 4 * a * c
    if delta > 0:
        raizdelta = delta ** 0.5
        raiz1 = (-b + raizdelta) / (2*a)
        raiz2 = (-b - raizdelta) / (2*a)
        return raiz1, raiz2
    elif delta == 0:
        raiz = -b / (2*a)
        return raiz
    else:
        return "Dá não mano :\ "

def grafquadratica(a, b, c):
    x = np.linspace(-10, 10, 50)
    y = funcaoquadratica(x, a, b, c)
    plt.plot(x, y, label=f'{a}x² + {b}x + {c}', color= "pink")
    plt.title('Gráfico de uma Função Quadrática')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.legend()
    plt.grid(True)
    plt.show()
    
def graffatorial(z):
    x = list(range(z + 1))
    y = [fatorial(i) for i in x]
    plt.plot(x, y, marker='o', linestyle='-', color="pink")
    plt.title('Gráfico do Fatorial')
    plt.xlabel('Número')
    plt.ylabel('Fatorial')
    plt.grid(True)
    plt.show()

def pergunta():
    while True:
        pergunta1 = input("Deseja começar?(S/N): ")
        if pergunta1 == "N" or pergunta1 == "n":
            print('---- Poxa! volte sempre que puder :( ----')
            break
        else:
            menu = '''
             _________________
            |  _____________  |
            | |_____________| |
            | |             | |
            | | x² √  CE  C | |
            | | 7  8  9   / | |
            | | 4  5  6   * | |
            | | 1  2  3   - | |
            | | 0  .  =   + | |
            | |_____________| |
            |_________________|
            '''
            print(menu)
            pergunta2 = int(input("Insira aqui um valor para básicas(1) ou funções(2): "))
            if pergunta2 == 1:
                menu2 = '''
                -------- CALCULADORA --------
                ------  1 - adição (+) ------
                ----- 2 - subtração (-) -----
                --- 3 - multiplicação (X) ---
                ------ 4 - divisão (÷) ------
                --- 5 - exponenciação(^x) ---
                ----- 6 - fatorial (!) ------
                '''
                print(menu2)
                pergunta3 = int(input("Insira aqui um dos números de cima: "))
                if pergunta3 == 6:
                    z = int(input("Insira um valor aqui: "))
                    resposta = fatorial(z)
                    print(f"{z}! = {resposta}")
                else:
                    x = int(input("Insira um valor aqui: "))
                    y = int(input("Insira, agora, um outro valor aqui: "))
                    if pergunta3 == 1:
                        adicao(x,y)
                    elif pergunta3 == 2:
                        subtracao(x,y)
                    elif pergunta3 == 3:
                        multiplicacao(x,y)
                    elif pergunta3 == 4:
                        divisao(x,y)
                    elif pergunta3 == 5:
                        exponenciacao(x,y)
            if pergunta2 == 2:
                menu3 = '''
                --------   FUNÇÕES   --------
                ------  1 - linear     ------
                ----- 2 - gráfico linear ----
                --- 3 - calculo de raízes ---
                ------ 4 - quadrática  ------
                - 5 - gráfico de quadrática -
                -- 6 - gráfico de fatorial --
                '''
                print(menu3)
                pergunta4 = int(input("Insira aqui um dos números de cima: "))
                if pergunta4 == 1:
                    x = int(input("Insira um valor aqui: "))
                    a = int(input("Insira um valor aqui: "))
                    b = int(input("Insira um valor aqui: "))
                    funcaolinear(x,b, a)
                if pergunta4 == 2:
                    a = int(input("Insira um valor aqui: "))
                    b = int(input("Insira um valor aqui: "))
                    graflinear(a,b)
                if pergunta4 == 3:
                    a = int(input("Insira um valor aqui: "))
                    b = int(input("Insira um valor aqui: "))
                    c = int(input("Insira, agora, um outro valor aqui: "))
                    calcularraizes(a, b, c)
                if pergunta4 == 4:
                    x = int(input("Insira um valor aqui: "))
                    a = int(input("Insira um valor aqui: "))
                    b = int(input("Insira um valor aqui: "))
                    c = int(input("Insira, agora, um outro valor aqui: "))
                    funcaoquadratica(x, a, b, c)
                if pergunta4 == 5:
                    a = int(input("Insira um valor aqui: "))
                    b = int(input("Insira um valor aqui: "))
                    c = int(input("Insira, agora, um outro valor aqui: "))
                    grafquadratica(a, b, c)
                if pergunta4 == 6:
                    z = int(input("Insira um valor aqui: "))
                    graffatorial(z)

                
print("----Bem vinde a calculadora 2.0! :D----") # type: ignore
pergunta()



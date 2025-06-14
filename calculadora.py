import sympy as sp
import matplotlib.pyplot as plt

def calcular_funcao():
    x = sp.symbols('x')
    str_expr = input("Digite a função (por exemplo, x**2 + 2*x): ")
    try:
        expr = sp.sympify(str_expr)
        x_val = float(input("Digite o valor de x: "))
        resultado = expr.subs(sp.symbols('x'), x_val)
        print(f"O resultado de {str_expr} quando x = {x_val} é: {resultado:.2f}")

        plotar = input("Deseja ver o gráfico dessa função? (s/n): ")
        if plotar.lower() == 's':
            x_vals = [i for i in range(int(x_val)-10, int(x_val)+11)]
            y_vals = [float(expr.subs(x, val)) for val in x_vals]
            plt.plot(x_vals, y_vals, label=str_expr)
            plt.scatter([x_val], [resultado], color='red', label=f"x={x_val}")
            plt.xlabel('x')
            plt.ylabel('f(x)')
            plt.title(f"Gráfico de {str_expr}")
            plt.legend()
            plt.grid(True)
            plt.show()
    except (sp.SympifyError, TypeError) as e:
        print(f"Erro ao calcular a função: {e}")
    except ZeroDivisionError:
        print("Erro: Divisão por zero ao calcular a função.")

def calcular_limite():
    x = sp.symbols('x')
    str_expr = input("Digite a função(por exemplo, sin(x)/x): ")
    ponto = float(input("Digite o ponto para qual x tende: "))
    try:
        expr = sp.sympify(str_expr)
        limite = sp.limit(expr, x, ponto)
        print(f"O limite de {str_expr} quando x tende a {ponto} é: {limite:.2f}")
    except (sp.SympifyError, TypeError) as e:
        print(f"Erro ao calcular o limite: {e}")
    except ZeroDivisionError:
        print("Erro: Divisão por zero ao calcular o limite.")
        
def calcular_derivada():
    x = sp.symbols('x')
    str_expr = input("Digite a função (por exemplo, x**2 + 2*x): ")
    try:
        expr = sp.sympify(str_expr)
        derivada = sp.diff(expr, x)
        print(f"A derivada de {str_expr} em relação a x é: {derivada:.2f}")
    except (sp.SympifyError, TypeError) as e:
        print(f"Erro ao calcular a derivada: {e}")
    except ZeroDivisionError:
        print("Erro: Divisão por zero ao calcular a derivada.")

def calcular_integral():
    x = sp.symbols('x')
    str_expr = input("Digite a função (por exemplo, x**2): ")
    try:
        expr = sp.sympify(str_expr)
        tipo = input("Você quer calcular a integral definida ou indefinida? (d/i): ").strip().lower()
        if tipo == 'd':
            a = float(input("Digite o limite inferior: "))
            b = float(input("Digite o limite superior: "))
            integral = sp.integrate(expr, (x, a, b))
            print(f"A integral definida de {str_expr} de {a} a {b} é: {integral:.2f}")
        elif tipo == 'i':
            integral = sp.integrate(expr, x)
            print(f"A integral indefinida de {str_expr} é: {integral:.2f}")
        else:
            print("Tipo de integral inválido. Use 'd' para definida ou 'i' para indefinida.")
    except (sp.SympifyError, TypeError) as e:
        print(f"Erro ao calcular a integral: {e}")
    except ZeroDivisionError:
        print("Erro: Divisão por zero ao calcular a integral.")
        
def main():
    while True:
        print("\nCalculadora de Função, Limites, Derivadas e Integrais")
        print("1. Calcular função")
        print("2. Calcular Limite")
        print("3. Calcular Derivada")
        print("4. Calcular Integral")
        print("0. Sair")
        
        escolha = input("Escolha uma opção: ")
        
        match escolha:
            case '1':
                calcular_funcao()
            case '2':
                calcular_limite()
            case '3':
                calcular_derivada()
            case '4':
                calcular_integral()
            case '0':
                print("Saindo da calculadora.")
                break
            case _:
                print("Opção inválida. Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    main()
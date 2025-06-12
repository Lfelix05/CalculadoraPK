# CalculadoraPK

Este é um pequeno projeto de calculadora matemática feito em Python para um trabalho de faculdade. O programa permite calcular valores de funções, limites, derivadas e integrais de funções matemáticas utilizando as bibliotecas SymPy e Matplotlib.

## Funcionalidades

- **Cálculo de Função:** Informe uma função e um valor de x para calcular o resultado numérico.
- **Gráfico da Função:** Após calcular o valor da função, é possível visualizar o gráfico da função no intervalo próximo ao valor de x informado.
- **Cálculo de Limites:** Informe uma função e um ponto para calcular o limite.
- **Cálculo de Derivadas:** Informe uma função para obter sua derivada em relação a x.
- **Cálculo de Integrais:** Escolha entre integral definida (com limites) ou indefinida.

## Como usar

1. Certifique-se de ter o Python 3.12 instalado.
2. Instale as bibliotecas necessárias:
   ```bash
   pip install sympy matplotlib
   ```
3. Execute o programa:
   ```bash
   python calculadora.py
   ```
4. Siga as instruções na tela para realizar cálculos.

## Exemplo de Uso

- Para calcular o valor de uma função e visualizar o gráfico:
  - Selecione a opção "Calcular função".
  - Informe a função, por exemplo: `x**2 + 2*x`
  - Informe o valor de x, por exemplo: `3`
  - O programa mostrará o resultado e perguntará se deseja ver o gráfico. Digite `s` para visualizar.
- Para calcular o limite de `sin(x)/x` quando `x` tende a 0:
  - Selecione a opção de cálculo de limites.
  - Informe a função `sin(x)/x`.
  - Informe o ponto `0`.
  - O programa retornará `1`, que é o limite da função nesse ponto.

## Observações

- Este projeto é uma demonstração acadêmica e pode não conter todos os recursos de uma calculadora matemática completa.
- As funções devem ser digitadas no formato Python, por exemplo: `x**2 + 2*x`, `sin(x)/x`.
- Para integrais definidas, informe os limites inferior e superior quando solicitado.
- Para sair do programa, basta fechar a janela do terminal ou usar `Ctrl+C`.

---

Projeto desenvolvido apenas para fins acadêmicos.
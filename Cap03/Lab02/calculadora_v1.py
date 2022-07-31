# Calculadora em Python

# Desenvolva uma calculadora em Python com tudo que você aprendeu nos capítulos 2 e 3. 
# A solução será apresentada no próximo capítulo!
# Assista o vídeo com a execução do programa!

def soma(valor1, valor2):
    # Função que deve retornar a soma de dois valores numéricos
    resultado = valor1 + valor2
    return f'Resultado: {str(valor1)} + {str(valor2)} = {resultado}'


def subtracao(valor1, valor2):
    # Função que deve retornar a subtração de dois valores numéricos
    resultado = valor1 - valor2
    return f'Resultado: {str(valor1)} - {str(valor2)} = {resultado}'


def multiplicacao(valor1, valor2):
    # Função que deve retornar a multiplicação de dois valores numéricos
    resultado = valor1 * valor2
    return f'Resultado: {str(valor1)} * {str(valor2)} = {resultado}'


def divisao(valor1, valor2):
    # Função que deve retornar a divisao de dois valores numéricos
    resultado = valor1 / valor2
    return f'Resultado: {str(valor1)} / {str(valor2)} = {resultado}'


def menu_principal():
    # Função principal que exibe o menu de interações tratando as possíveis exceções    
    while True:
        print("\n******************* Python Calculator *******************")

        try:
            option = input('Selecione o número da opção desejada:'
                           '\n\t[ 1 ] Soma'
                           '\n\t[ 2 ] Subtração'
                           '\n\t[ 3 ] Multiplicação'
                           '\n\t[ 4 ] Divisão'
                           '\nDigite sua opção: ')
        except Exception as err:
            print(f'( ! ) Houve um erro: {err=}, {type(err)=}.')
            menu_principal()

        if option not in map(lambda x: str(x), range(1, 5)):
            print('( ! ) Houve um erro: valor inserido não é uma opção válida.')
            continue

        else:
            while True:
                try:
                    valor1 = int(input('Digite o primeiro número: '))
                    valor2 = int(input('Digite o segundo número: '))
                except ValueError:
                    print('( ! ) Houve um erro: valores não numéricos.')
                    menu_principal()
                except Exception as err:
                    print(f'( ! ) Houve um erro: {err=}, {type(err)=}.')
                    menu_principal()

                if option == '1':
                    print(soma(valor1, valor2))

                elif option == '2':
                    print(subtracao(valor1, valor2))

                elif option == '3':
                    print(multiplicacao(valor1, valor2))

                elif option == '4':
                    if valor2 == 0:
                        # Verifica se um dos parâmetros é zero
                        print('( ! ) Houve um erro: divisão por zero.')
                        continue  # Retorna ao diálogo para o usuário digitar novamente os valores

                    print(divisao(valor1, valor2))

                while True:
                    try:
                        option = input('Deseja realizar outra operação?'
                                       '\n[ 1 ] Sim'
                                       '\n[ 2 ] Não\n')

                        if option not in map(lambda x: str(x), range(1, 3)):
                            print('( ! ) Houve um erro: valor inserido não é uma opção válida.')
                            continue
                        break

                    except Exception as err:
                        print(f'( ! ) Houve um erro: {err=}, {type(err)=}.')

                if option == '1':
                    # Retorna ao menu principal
                    break

                elif option == '2':
                    # Encerra o programa
                    return


menu_principal()  # Invoca o menu principal da calculadora

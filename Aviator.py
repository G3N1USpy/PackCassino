import random
import os

# Função para limpar a tela
def limpar_tela():
    if os.name == 'posix':
        os.system('clear')  # Limpar a tela em sistemas Unix/Linux
    else:
        os.system('cls')    # Limpar a tela em sistemas Windows

# Função para prever o próximo número secreto com base no histórico
def prever_proximo_numero_secreto(historico):
    if len(historico) < 2:
        return random.uniform(1.0, 10.0)  # Se não houver histórico suficiente, faça uma previsão aleatória entre 1.00 e 10.00

    # Use a média de todos os números secretos anteriores como previsão
    soma_numeros_secretos = sum(historico)
    proximo_numero_secreto = soma_numeros_secretos / len(historico)

    return proximo_numero_secreto

# Histórico de números secretos
historico_numeros_secretos = []

# Cores ANSI (pode não funcionar em todos os ambientes)
COR_VERDE = "\033[32m"
COR_RESET = "\033[0m"

# Loop para interagir com o usuário e atualizar o histórico
while True:
    limpar_tela()  # Limpar a tela antes de cada print
    print(" █▀▀█ █░░▒█ ▀█▀ █▀▀█ ▀▀█▀▀ █▀▀▀█ █▀▀█")
    print(" █▄▄█ ▒█▒█░ ░█░ █▄▄█ ░▒█░░ █░░▒█ █▄▄▀")
    print(" █░▒█ ░▀▄▀░ ▄█▄ █░▒█ ░▒█░░ █▄▄▄█ █░▒█")
    print(COR_VERDE + "Feito por GENIUS" + COR_RESET)
    print("")
    print(COR_VERDE + "Histórico de resultados:", historico_numeros_secretos)
    proxima_previsao = prever_proximo_numero_secreto(historico_numeros_secretos)
    print("Próxima previsão: {:.2f}".format(proxima_previsao) + COR_RESET)
    
    try:
        resultado_real = float(input(COR_VERDE + "Insira o resultado que caiu (formato 0.00): " + COR_RESET))
        historico_numeros_secretos.append(resultado_real)
            
    except ValueError:
        print(COR_VERMELHA + "Entrada inválida. Insira um número no formato 0.00 (ex: 3.55)." + COR_RESET)

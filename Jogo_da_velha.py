def criar_tabuleiro():
    return [" " for _ in range(9)]


def imprimir_tabuleiro(tabuleiro):
    for i in range(3):
        print("|" + "|".join(tabuleiro[i*3:(i+1)*3]) + "|")
        if i < 2:
            print("-----")


def receber_jogada(jogador, tabuleiro):
    while True:
        posicao = input(f"Jogador {jogador}, escolha uma posição de 1 a 9: ")
        if posicao.isdigit() and 1 <= int(posicao) <= 9:
            posicao = int(posicao) - 1
            if tabuleiro[posicao] == " ":
                return posicao
            else:
                print("Esta posição já está ocupada!")
        else:
            print("Entrada inválida. Por favor, escolha uma posição de 1 a 9.")


def checar_vitoria(tabuleiro, jogador):
    linhas = [(0, 1, 2), (3, 4, 5), (6, 7, 8)]
    colunas = [(0, 3, 6), (1, 4, 7), (2, 5, 8)]
    diagonais = [(0, 4, 8), (2, 4, 6)]
    for seq in linhas + colunas + diagonais:
        if all(tabuleiro[i] == jogador for i in seq):
            return True
    return False


def checar_empate(tabuleiro):
    return " " not in tabuleiro


def jogo_da_velha():
    tabuleiro = criar_tabuleiro()
    jogador_atual = "X"

    while True:
        imprimir_tabuleiro(tabuleiro)
        posicao = receber_jogada(jogador_atual, tabuleiro)
        tabuleiro[posicao] = jogador_atual

        if checar_vitoria(tabuleiro, jogador_atual):
            imprimir_tabuleiro(tabuleiro)
            print(f"Jogador {jogador_atual} venceu!")
            break
        elif checar_empate(tabuleiro):
            imprimir_tabuleiro(tabuleiro)
            print("Empate!")
            break

        jogador_atual = "O" if jogador_atual == "X" else "X"


if __name__ == "__main__":
    jogo_da_velha()

# Algoritmo de Sudoku - Técnica: Backtracking (Busca com Retrocesso)
# Integrantes:
# Ana Beatriz Carvalho Oliveira
# Cristiane Almeida Santos Nascimento
# Yuri Rezende Santos

from colorama import Fore, Style, init
init(autoreset=True)

def mostrar(tabuleiro, original=None):
    """Exibe o Sudoku de forma visual, clara e alinhada."""
    print("╔" + "════╦" * 8 + "════╗")
    for i in range(9):
        linha = "║"
        for j in range(9):
            valor = tabuleiro[i][j]
            if valor == 0:
                char = "  "
            else:
                if original and original[i][j] != 0:
                    char = f"🔵{valor}"  # número original
                else:
                    char = f"🟢{valor}"  # número resolvido
            linha += f" {char} "
            if (j + 1) % 3 == 0 and j != 8:
                linha += "║"
        linha += "║"
        print(linha)
        if (i + 1) % 3 == 0 and i != 8:
            print("╠" + "════╬" * 8 + "════╣")
    print("╚" + "════╩" * 8 + "════╝")


def encontrar_vazio(tabuleiro):
    """Encontra a próxima posição vazia (representada por 0)."""
    for i in range(9):
        for j in range(9):
            if tabuleiro[i][j] == 0:
                return i, j  # linha, coluna
    return None

def valido(tabuleiro, num, pos):
    """Verifica se é válido colocar 'num' em 'pos' (linha, coluna)."""
    linha, coluna = pos

    # Verificar linha
    for j in range(9):
        if tabuleiro[linha][j] == num and coluna != j:
            return False

    # Verificar coluna
    for i in range(9):
        if tabuleiro[i][coluna] == num and linha != i:
            return False

    # Verificar subgrade 3x3
    inicio_linha = (linha // 3) * 3
    inicio_coluna = (coluna // 3) * 3
    for i in range(inicio_linha, inicio_linha + 3):
        for j in range(inicio_coluna, inicio_coluna + 3):
            if tabuleiro[i][j] == num and (i, j) != pos:
                return False

    return True

def resolver(tabuleiro):
    """Resolve o Sudoku usando Backtracking."""
    vazio = encontrar_vazio(tabuleiro)
    if not vazio:
        return True  # resolvido!
    else:
        linha, coluna = vazio

    for num in range(1, 10):
        if valido(tabuleiro, num, (linha, coluna)):
            tabuleiro[linha][coluna] = num

            if resolver(tabuleiro):
                return True

            tabuleiro[linha][coluna] = 0  # volta atrás

    return False  # sem solução possível

# Exemplo de entrada (0 representa espaço vazio)
tabuleiro_exemplo = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

# Faz uma cópia do tabuleiro original (para saber quais números já existiam)
original = [linha[:] for linha in tabuleiro_exemplo]

print("Tabuleiro inicial:")
mostrar(tabuleiro_exemplo, original)

if resolver(tabuleiro_exemplo):
    print("\nSudoku resolvido:")
    mostrar(tabuleiro_exemplo, original)
else:
    print("Não existe solução para este Sudoku.")

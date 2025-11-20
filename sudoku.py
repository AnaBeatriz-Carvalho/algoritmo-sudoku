import os
from colorama import Fore, Style, init
init(autoreset=True)

# --- Funções do seu código original (estão corretas) ---

def mostrar(tabuleiro, original=None):
    """Exibe o Sudoku com cores: ciano para originais, verde para resolvidos."""
    print("+" + "---+" * 9)
    for i in range(9):
        for j in range(9):
            valor = tabuleiro[i][j]
            if valor == 0:
                char = " "
            else:
                if original and original[i][j] != 0:
                    char = f"{Fore.CYAN}{valor}{Style.RESET_ALL}"  # número original
                else:
                    char = f"{Fore.GREEN}{valor}{Style.RESET_ALL}"  # número resolvido
            print(f"| {char}", end=" ")
        print("|")
        if (i + 1) % 3 == 0:
            print("+" + "---+" * 9)

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

            tabuleiro[linha][coluna] = 0  # volta atrás (Backtrack)

    return False  # sem solução possível

# --- Função ADICIONADA para cumprir os requisitos ---

def carregar_instancia_de_arquivo(caminho_arquivo):
    """
    Lê uma instância do Sudoku de um arquivo .txt.
    Formato esperado: 9 linhas, cada linha com 9 números separados por vírgula.
    Ex: 5,3,0,0,7,0,0,0,0
    """
    if not os.path.exists(caminho_arquivo):
        print(f"{Fore.RED}ERRO: Arquivo de instância não encontrado em '{caminho_arquivo}'")
        return None
    
    tabuleiro = []
    try:
        with open(caminho_arquivo, 'r') as f:
            for linha_str in f:
                linha_limpa = linha_str.strip()
                if not linha_limpa:
                    continue
                
                numeros = [int(n) for n in linha_limpa.split(',')]
                
                if len(numeros) != 9:
                    raise ValueError(f"Linha inválida, não 9 números: '{linha_limpa}'")
                
                tabuleiro.append(numeros)
        
        if len(tabuleiro) != 9:
             raise ValueError(f"Arquivo não 9 linhas: encontrado {len(tabuleiro)}")
        
        return tabuleiro
    
    except Exception as e:
        print(f"{Fore.RED}ERRO ao ler o arquivo: {e}")
        return None

# --- Bloco Principal de Execução (main) ---
def main():
    """
    Função principal que organiza a execução do programa.
    """
    # 1. DEFINIR A ENTRADA
    # O código vai procurar por uma pasta "dados" e um arquivo "sudoku_facil.txt"
    # Isso cumpre os requisitos [cite: 8, 13]
    NOME_ARQUIVO = "sudoku_facil.txt"
    CAMINHO_PASTA = "dados"
    caminho_instancia = os.path.join(CAMINHO_PASTA, NOME_ARQUIVO)
    
    # 2. CARREGAR A INSTÂNCIA
    tabuleiro_exemplo = carregar_instancia_de_arquivo(caminho_instancia)

    # Se não conseguir carregar, encerra o programa
    if tabuleiro_exemplo is None:
        print(f"Por favor, crie a pasta '{CAMINHO_PASTA}' e o arquivo '{NOME_ARQUIVO}' nela.")
        return

    # 3. EXECUTAR E MOSTRAR
    # Faz uma cópia do tabuleiro original (para saber quais números já existiam)
    original = [linha[:] for linha in tabuleiro_exemplo]

    print(f"Instância carregada de: '{caminho_instancia}'")
    print("Tabuleiro inicial:")
    mostrar(tabuleiro_exemplo, original)

    if resolver(tabuleiro_exemplo):
        print(f"\n{Fore.GREEN}Sudoku resolvido! (Técnica: Backtracking)")
        mostrar(tabuleiro_exemplo, original)
    else:
        print(f"{Fore.RED}\nNão existe solução para este Sudoku.")


# Garante que a função main() seja executada quando o script for rodado
if __name__ == "__main__":
    main()
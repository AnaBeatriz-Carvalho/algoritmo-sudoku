# Algoritmo de Resolução de Sudoku

Este projeto implementa um algoritmo em Python para resolver quebra-cabeças de Sudoku automaticamente utilizando a técnica de **Backtracking**. O programa lê uma instância de Sudoku de um arquivo, exibe o tabuleiro inicial e, em seguida, apresenta a solução encontrada.

## 📋 Funcionalidades

- **Resolução Automática:** Utiliza o algoritmo de backtracking para encontrar a solução do Sudoku.
- **Leitura de Arquivo:** Carrega tabuleiros a partir de arquivos de texto (ex: `dados/sudoku_facil.txt`).
- **Visualização Colorida:** Utiliza a biblioteca `colorama` para diferenciar os números originais (Ciano) dos números preenchidos pelo algoritmo (Verde) no terminal.
- **Validação:** Verifica as regras do Sudoku (linha, coluna e subgrade 3x3) para garantir a validade dos movimentos.

## 📺 Demonstração no YouTube

Confira o vídeo de demonstração e explicação do projeto no link abaixo:

[![Assista ao Vídeo](https://img.youtube.com/vi/VIDEO_ID_AQUI/maxresdefault.jpg)](https://www.youtube.com/watch?v=VIDEO_ID_AQUI)



## 🚀 Como Executar

### Pré-requisitos

Certifique-se de ter o **Python** instalado em sua máquina.

### Instalação

1. Clone este repositório:
   ```bash
   git clone https://github.com/AnaBeatriz-Carvalho/algoritmo-sudoku.git
   cd algoritmo-sudoku
   ```

2. Instale as dependências necessárias (Colorama):
   ```bash
   pip install -r requirements.txt
   ```

### Uso

Para rodar o programa e resolver o Sudoku padrão:

```bash
python sudoku.py
```

O programa irá ler o arquivo configurado (por padrão em `dados/sudoku_facil.txt`) e exibir o resultado no terminal.

## 📂 Estrutura do Projeto

- `sudoku.py`: Código fonte principal contendo a lógica do solver e visualização.
- `requirements.txt`: Lista de dependências do projeto.
- `dados/`: Pasta contendo arquivos de entrada com os tabuleiros de Sudoku.

## 🛠️ Tecnologias Utilizadas

- Python 3
- Colorama (para cores no terminal)

## ✒️ Autores

- **Ana Beatriz Carvalho Oliveira** 
- **Cristiane Almeida Santos Nascimento** 
- **Yuri Rezende Santos** 
---


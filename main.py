import math

# Representação inicial do tabuleiro
def print_board(board):
    for row in board:
        print(" | ".join(row))
    print()

# Verifica se há um vencedor
def check_winner(board):
    # Linhas, colunas e diagonais
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != " ":
            return row[0]
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return board[0][col]
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return board[0][2]
    return None

# Verifica se o tabuleiro está cheio
def is_full(board):
    return all(cell != " " for row in board for cell in row)

# Algoritmo Minimax
def minimax(board, depth, is_maximizing):
    winner = check_winner(board)
    if winner == "X":  # Computador vence
        return 1
    if winner == "O":  # Humano vence
        return -1
    if is_full(board):  # Empate
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "X"
                    score = minimax(board, depth + 1, False)
                    board[i][j] = " "
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "O"
                    score = minimax(board, depth + 1, True)
                    board[i][j] = " "
                    best_score = min(score, best_score)
        return best_score

# Determina a melhor jogada para o computador
def best_move(board):
    best_score = -math.inf
    move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "X"
                score = minimax(board, 0, False)
                board[i][j] = " "
                if score > best_score:
                    best_score = score
                    move = (i, j)
    return move

# Jogo principal
def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    print("Bem-vindo ao Jogo da Velha!")
    print("Você é 'O' e o computador é 'X'.")
    print_board(board)

    while True:
        # Jogada do humano
        row, col = map(int, input("Digite sua jogada (linha e coluna, 0-2 separados por espaço): ").split())
        if board[row][col] == " ":
            board[row][col] = "O"
        else:
            print("Espaço já ocupado. Tente novamente.")
            continue

        print_board(board)

        # Verifica se o humano venceu
        if check_winner(board) == "O":
            print("Você venceu!")
            break
        if is_full(board):
            print("Empate!")
            break

        # Jogada do computador
        move = best_move(board)
        if move:
            board[move[0]][move[1]] = "X"
            print("Computador jogou:")
            print_board(board)

        # Verifica se o computador venceu
        if check_winner(board) == "X":
            print("Você perdeu!")
            break
        if is_full(board):
            print("Empate!")
            break

# Executa o jogo
tic_tac_toe()

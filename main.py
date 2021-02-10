

def check_end(board):
    # 0
    if board[0] != '0' and board[0] == board[1] == board[2] == board[3]:
        return True, board[0]
    elif board[0] != '0' and board[0] == board[4] == board[8] == board[12]:
        return True, board[0]
    elif board[0] != '0' and board[0] == board[5] == board[10] == board[15]:
        return True, board[0]
    elif board[0] != '0' and board[0] == board[1] == board[4] == board[5]:
        return True, board[0]
    # 1
    elif board[1] != '0' and board[1] == board[2] == board[5] == board[6]:
        return True, board[1]
    elif board[1] != '0' and board[1] == board[5] == board[9] == board[13]:
        return True, board[1]
    # 2
    elif board[2] != '0' and board[2] == board[3] == board[6] == board[7]:
        return True, board[2]
    elif board[2] != '0' and board[2] == board[6] == board[10] == board[14]:
        return True, board[2]
    # 3
    elif board[3] != '0' and board[3] == board[7] == board[11] == board[15]:
        return True, board[3]
    # 4
    elif board[4] != '0' and board[4] == board[5] == board[8] == board[9]:
        return True, board[4]
    elif board[4] != '0' and board[4] == board[5] == board[6] == board[7]:
        return True, board[4]
    # 5
    elif board[5] != '0' and board[5] == board[6] == board[9] == board[10]:
        return True, board[5]
    # 6
    elif board[6] != '0' and board[6] == board[7] == board[10] == board[11]:
        return True, board[6]
    # 7
    # None
    # 8
    elif board[8] != '0' and board[8] == board[9] == board[12] == board[13]:
        return True, board[8]
    elif board[8] != '0' and board[8] == board[9] == board[10] == board[11]:
        return True, board[8]
    # 9
    elif board[9] != '0' and board[9] == board[10] == board[13] == board[14]:
        return True, board[9]
    # 10
    elif board[10] != '0' and board[10] == board[11] == board[14] == board[15]:
        return True, board[10]
    # 11
    # None
    # 12
    elif board[12] != '0' and board[12] == board[13] == board[14] == board[15]:
        return True, board[12]
    elif board[12] != '0' and board[12] == board[9] == board[6] == board[3]:
        return True, board[12]
    # Tie Case
    elif board.count('0') == 0:
        return True, 'tie'
    else:
        return False, ''


def next_move(board, team, other, depth):
    best_score = -5
    best_pos = None
    count = 0
    for pos in range(0, 16):
        if board[pos] == '0':
            board[pos] = team
            (score, count) = minimax(board, False, team, other, count + 1, depth - 1)
            board[pos] = '0'
            if score > best_score:
                best_pos = pos
                best_score = score
    return best_pos, count


def minimax(board, max_player, team, other, count, depth) -> tuple:
    res = check_end(board)
    if res[0] or depth <= 0:
        if res[1] == other:
            return -1, count
        elif res[1] == team:
            return 1, count
        elif res[1] == 'tie':
            return 0, count
        else:
            return 0, count
    if max_player:
        best_score = -100
        for pos in range(0, 16):
            if board[pos] == '0':
                board[pos] = team
                (current, count) = minimax(board, False, team, other, count + 1, depth - 1)
                best_score = max(current, best_score)
                board[pos] = '0'
        return best_score, count
    if not max_player:
        best_score = 100
        for pos in range(0, 16):
            if board[pos] == '0':
                board[pos] = other
                (current, count) = minimax(board, True, team, other, count + 1, depth - 1)
                best_score = min(current, best_score)
                board[pos] = '0'
        return best_score, count


def alphabetanext_move(board, team, other, depth):
    best_score = -5
    best_pos = None
    count = 0
    for pos in range(0, 16):
        if board[pos] == '0':
            board[pos] = team
            (score, count) = alphabetaminimax(board, False, team, other, depth - 1,  -100, 100, count + 1)
            board[pos] = '0'
            if score > best_score:
                best_pos = pos
                best_score = score
    return best_pos, count


def alphabetaminimax(board, max_player, team, other, depth, alpha, beta, count) -> tuple:
    res = check_end(board)
    if res[0] or depth <= 0:
        if res[1] == other:
            return -1, count
        elif res[1] == team:
            return 1, count
        elif res[1] == 'tie':
            return 0, count
        else:
            return 0, count
    if max_player:
        best_score = -100
        for pos in range(0, 16):
            if board[pos] == '0':
                board[pos] = team
                (current, count) = alphabetaminimax(board, False, team, other, depth - 1, alpha, beta, count + 1)
                best_score = max(current, best_score)
                board[pos] = '0'
                alpha = max(alpha, current)
                if beta <= alpha:
                    break
        return best_score, count
    if not max_player:
        best_score = 100
        for pos in range(0, 16):
            if board[pos] == '0':
                board[pos] = other
                (current, count) = alphabetaminimax(board, True, team, other, depth - 1, alpha, beta, count + 1)
                best_score = min(current, best_score)
                board[pos] = '0'
                beta = min(beta, current)
                if beta <= alpha:
                    break
        return best_score, count


def printboard(board):
    print(board[0:4])
    print(board[4:8])
    print(board[8:12])
    print(board[12:16])
    print('\n')


def main():
    depth = 5
    board = ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0']
    alphaboard = ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0']
    player1 = 'x'
    player2 = 'o'
    turn = 1
    total_x, total_y = 0,0
    print(f"This is turn {turn}")
    while True:
        if turn % 2 != 0:
            (best_pos, count) = next_move(board, player1, player2, 5)
            total_x += count
            board[best_pos] = player1
        if turn % 2 == 0:
            (best_pos, count) = next_move(board, player2, player1, 5)
            total_y += count
            board[best_pos] = player2
        res = check_end(board)
        if res[0]:
            winner = res[1]
            break
        # printboard(board)
        turn += 1

    print(f"the winner is: {winner} and was completed in x:{total_x}, o:{total_y} boards")
    printboard(board)

    turn = 1
    print(f"This is alphabeta pruning turn {turn}")
    alphabeta_total_x = 0
    alphabeta_total_y = 0
    while True:
        if turn % 2 != 0:
            (best_pos, count) = alphabetanext_move(alphaboard, player1, player2, 5)
            alphabeta_total_x += count
            alphaboard[best_pos] = player1
        if turn % 2 == 0:
            (best_pos, count) = alphabetanext_move(alphaboard, player2, player1, 5)
            alphabeta_total_y += count
            alphaboard[best_pos] = player2
        res = check_end(alphaboard)
        if res[0]:
            winner = res[1]
            break
        # printboard(alphaboard)
        turn += 1

    print(f"the winner is: {winner} and was completed in x:{alphabeta_total_x}, o:{alphabeta_total_y} boards")
    printboard(alphaboard)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

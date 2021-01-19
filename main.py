
one = [0, 3, 12, 15]
two = [1, 2, 4, 7, 8, 11, 13, 14]
three = [5, 6, 9, 10]


def check_valid(board, leaf):
    if leaf == 1:
        for pos in one:
            if board[pos] == '0':
                return pos
    elif leaf == 2:
        for pos in two:
            if board[pos] == '0':
                return pos
    elif leaf == 3:
        for pos in three:
            if board[pos] == '0':
                return pos
    else:
        return None


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
        return False, None


def next_move(board, team):
    if team == 'x':
        best_score = -5
        best_pos = None
        for x in range(1, 4):
            pos = check_valid(board, x)
            if pos is not None:
                board[pos] = 'x'
                score = minimax(board, 'o', 0)
                board[pos] = '0'
                if score > best_score:
                    best_pos = pos
        return best_pos
    if team == 'o':
        best_score = 5
        best_pos = None
        for x in range(1, 4):
            pos = check_valid(board, x)
            if pos is not None:
                board[pos] = 'x'
                score = minimax(board, 'o', 0)
                board[pos] = '0'
                if score < best_score:
                    best_pos = pos
        return best_pos


def minimax(board, team, depth) -> int:
    depth += 1
    res = check_end(board)
    if res[0]:
        if res[1] == 'o':
            return -1
        elif res[1] == 'x':
            return 1
        elif res[1] == 'tie':
            return 0
    if team == 'x':
        best_score = -5
        for x in range(1, 4):
            pos = check_valid(board, x)
            if pos is not None:
                board[pos] = team
                score = minimax(board, 'o', depth)
                best_score = max(score, best_score)
                board[pos] = '0'
        return best_score
    if team == 'o':
        best_score = 5
        for x in range(1, 4):
            pos = check_valid(board, x)
            if pos is not None:
                board[pos] = team
                score = minimax(board, 'x', depth)
                best_score = min(score, best_score)
                board[pos] = '0'
        return best_score


def main():
    winner = ''
    board = ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0']
    player1 = 'x'
    player2 = 'o'
    turn = 1
    print(f"Next round this is turn {turn}")
    print(board[0:4])
    print(board[4:8])
    print(board[8:12])
    print(board[12:16])
    print('\n')
    while True:
        if turn % 2 != 0:
            board[next_move(board, player1)] = player1
        if turn % 2 == 0:
            board[next_move(board, player2)] = player2
        res = check_end(board)
        if res[0]:
            winner = res[1]
            break
        print(f"Next round this is turn {turn}")
        print(board[0:4])
        print(board[4:8])
        print(board[8:12])
        print(board[12:16])
        print('\n')
        turn += 1

    print(f"the results are: {winner}")
    print(f"Next round this is turn {turn}")
    print(board[0:4])
    print(board[4:8])
    print(board[8:12])
    print(board[12:16])
    print('\n')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

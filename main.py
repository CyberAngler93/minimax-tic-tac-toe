import random
import math

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
    best_score = -math.inf
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


def alphabeta_next_move(board, team, other, depth):
    best_score = -math.inf
    best_pos = None
    count = 0
    for pos in range(0, 16):
        if board[pos] == '0':
            board[pos] = team
            (score, count) = alphabeta_minimax(board, False, team, other, depth - 1, -100, 100, count + 1)
            board[pos] = '0'
            if score > best_score:
                best_pos = pos
                best_score = score
    return best_pos, count


def alphabeta_minimax(board, max_player, team, other, depth, alpha, beta, count) -> tuple:
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
        best_score = -math.inf
        for pos in range(0, 16):
            if board[pos] == '0':
                board[pos] = team
                (current, count) = alphabeta_minimax(board, False, team, other, depth - 1, alpha, beta, count + 1)
                best_score = max(current, best_score)
                board[pos] = '0'
                alpha = max(alpha, current)
                if beta <= alpha:
                    break
        return best_score, count
    if not max_player:
        best_score = math.inf
        for pos in range(0, 16):
            if board[pos] == '0':
                board[pos] = other
                (current, count) = alphabeta_minimax(board, True, team, other, depth - 1, alpha, beta, count + 1)
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


def random_move(board):
    while True:
        move = random.randint(0, 15)
        if board[move] == '0':
            return move


def game(player1, player2, gamemode, pflag, gamecount, depth):
    winners = []
    x_boards = 0
    y_boards = 0
    while gamecount > 0:
        board = ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0']
        turn = 1
        total_x, total_y = 0, 0
        while True:
            if pflag:
                print(f"This is turn {turn}")
            best_pos, count = None, None
            if turn % 2 != 0:
                if gamemode == 1:
                    (best_pos, count) = next_move(board, player1, player2, depth)
                if gamemode == 2:
                    (best_pos, count) = alphabeta_next_move(board, player1, player2, depth)
                if gamemode == 3:
                    best_pos = random_move(board)
                    count = 1
                if gamemode == 4:
                    (best_pos, count) = alphabeta_next_move(board, player1, player2, depth)
                if gamemode == 5:
                    best_pos = random_move(board)
                    count = 1
                total_x += count
                board[best_pos] = player1
            if turn % 2 == 0:
                if gamemode == 1:
                    (best_pos, count) = alphabeta_next_move(board, player2, player1, depth)
                if gamemode == 2:
                    (best_pos, count) = next_move(board, player2, player1, depth)
                if gamemode == 3:
                    (best_pos, count) = alphabeta_next_move(board, player2, player1, depth)
                if gamemode == 4:
                    best_pos = random_move(board)
                    count = 1
                if gamemode == 5:
                    (best_pos, count) = alphabeta_next_move(board, player2, player1, depth)
                total_y += count
                board[best_pos] = player2
            res = check_end(board)
            if res[0]:
                winner = res[1]
                break
            if pflag:
                printboard(board)
            turn += 1
        if pflag:
            print(f"the winner is: {winner} and was completed in x:{total_x}, o:{total_y} boards")
            printboard(board)
        winners.append(winner)
        x_boards += total_x
        y_boards += total_y
        gamecount -= 1
    return winners, x_boards, y_boards


def main():
    player1 = 'x'
    player2 = 'o'
    games = 1000
    depth = 1
    (ret, x, o) = game(player1, player2, 4, False, games, depth)
    print(f"{games} games were played with x as alphabeta at depth {depth}, o as random player and the results were x:{ret.count('x')} and evaluated an average of {x/1000} boards, o:{ret.count('o')} and evaluated an average of {o/1000} boards, tie:{ret.count('tie')}")
    (ret, x, o) = game(player1, player2, 5, False, games, depth)
    print(f"{games} games were played with x as random at depth {depth}, o as alphabeta player and the results were x:{ret.count('x')} and evaluated an average of {x/1000} boards, o:{ret.count('o')} and evaluated an average of {o/1000} boards, tie:{ret.count('tie')}")

    depth = 2
    (ret, x, o) = game(player1, player2, 4, False, games, depth)
    print(f"{games} games were played with x as alphabeta at depth {depth}, o as random player and the results were x:{ret.count('x')} and evaluated an average of {x/1000} boards, o:{ret.count('o')} and evaluated an average of {o/1000} boards, tie:{ret.count('tie')}")
    (ret, x, o) = game(player1, player2, 5, False, games, depth)
    print(f"{games} games were played with x as random at depth {depth}, o as alphabeta player and the results were x:{ret.count('x')} and evaluated an average of {x/1000} boards, o:{ret.count('o')} and evaluated an average of {o/1000} boards, tie:{ret.count('tie')}")

    depth = 3
    (ret, x, o) = game(player1, player2, 4, False, games, depth)
    print(f"{games} games were played with x as alphabeta at depth {depth}, o as random player and the results were x:{ret.count('x')} and evaluated an average of {x/1000} boards, o:{ret.count('o')} and evaluated an average of {o/1000} boards, tie:{ret.count('tie')}")
    (ret, x, o) = game(player1, player2, 5, False, games, depth)
    print(f"{games} games were played with x as random at depth {depth}, o as alphabeta player and the results were x:{ret.count('x')} and evaluated an average of {x/1000} boards, o:{ret.count('o')} and evaluated an average of {o/1000} boards, tie:{ret.count('tie')}")

    depth = 4
    (ret, x, o) = game(player1, player2, 4, False, games, depth)
    print(f"{games} games were played with x as alphabeta at depth {depth}, o as random player and the results were x:{ret.count('x')} and evaluated an average of {x/1000} boards, o:{ret.count('o')} and evaluated an average of {o/1000} boards, tie:{ret.count('tie')}")
    (ret, x, o) = game(player1, player2, 5, False, games, depth)
    print(f"{games} games were played with x as random at depth {depth}, o as alphabeta player and the results were x:{ret.count('x')} and evaluated an average of {x/1000} boards, o:{ret.count('o')} and evaluated an average of {o/1000} boards, tie:{ret.count('tie')}")

    depth = 5
    (ret, x, o) = game(player1, player2, 4, False, games, depth)
    print(f"{games} games were played with x as alphabeta at depth {depth}, o as random player and the results were x:{ret.count('x')} and evaluated an average of {x/1000} boards, o:{ret.count('o')} and evaluated an average of {o/1000} boards, tie:{ret.count('tie')}")
    (ret, x, o) = game(player1, player2, 5, False, games, depth)
    print(f"{games} games were played with x as random at depth {depth}, o as alphabeta player and the results were x:{ret.count('x')} and evaluated an average of {x/1000} boards, o:{ret.count('o')} and evaluated an average of {o/1000} boards, tie:{ret.count('tie')}")

    depth = 6
    (ret, x, o) = game(player1, player2, 4, False, games, depth)
    print(f"{games} games were played with x as alphabeta at depth {depth}, o as random player and the results were x:{ret.count('x')} and evaluated an average of {x/1000} boards, o:{ret.count('o')} and evaluated an average of {o/1000} boards, tie:{ret.count('tie')}")
    (ret, x, o) = game(player1, player2, 5, False, games, depth)
    print(f"{games} games were played with x as random at depth {depth}, o as alphabeta player and the results were x:{ret.count('x')} and evaluated an average of {x/1000} boards, o:{ret.count('o')} and evaluated an average of {o/1000} boards, tie:{ret.count('tie')}")

    depth = 8
    (ret, x, o) = game(player1, player2, 4, False, games, depth)
    print(f"{games} games were played with x as alphabeta at depth {depth}, o as random player and the results were x:{ret.count('x')} and evaluated an average of {x/1000} boards, o:{ret.count('o')} and evaluated an average of {o/1000} boards, tie:{ret.count('tie')}")
    (ret, x, o) = game(player1, player2, 5, False, games, depth)
    print(f"{games} games were played with x as random at depth {depth}, o as alphabeta player and the results were x:{ret.count('x')} and evaluated an average of {x/1000} boards, o:{ret.count('o')} and evaluated an average of {o/1000} boards, tie:{ret.count('tie')}")



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

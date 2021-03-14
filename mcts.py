import math
import random
import copy
import time


class Node:
    def __init__(self, board, parent, player):
        self.board = board
        self.player = player
        self.is_terminal = False
        self.winner = None
        self.check_end()
        self.is_expanded = self.is_terminal
        self.parent = parent
        self.score = 0
        self.count = 0
        self.child = {}
        self.valid = [i for i in range(0, 16) if self.board[i] == '0']


    def check_end(self):
        # 0
        if self.board[0] != '0' and self.board[0] == self.board[1] == self.board[2] == self.board[3]:
            self.is_terminal = True
            self.winner = self.board[0]
        elif self.board[0] != '0' and self.board[0] == self.board[4] == self.board[8] == self.board[12]:
            self.is_terminal = True
            self.winner = self.board[0]
        elif self.board[0] != '0' and self.board[0] == self.board[5] == self.board[10] == self.board[15]:
            self.is_terminal = True
            self.winner = self.board[0]
        elif self.board[0] != '0' and self.board[0] == self.board[1] == self.board[4] == self.board[5]:
            self.is_terminal = True
            self.winner = self.board[0]
        # 1
        elif self.board[1] != '0' and self.board[1] == self.board[2] == self.board[5] == self.board[6]:
            self.is_terminal = True
            self.winner = self.board[1]
        elif self.board[1] != '0' and self.board[1] == self.board[5] == self.board[9] == self.board[13]:
            self.is_terminal = True
            self.winner = self.board[1]
        # 2
        elif self.board[2] != '0' and self.board[2] == self.board[3] == self.board[6] == self.board[7]:
            self.is_terminal = True
            self.winner = self.board[2]
        elif self.board[2] != '0' and self.board[2] == self.board[6] == self.board[10] == self.board[14]:
            self.is_terminal = True
            self.winner = self.board[2]
        # 3
        elif self.board[3] != '0' and self.board[3] == self.board[7] == self.board[11] == self.board[15]:
            self.is_terminal = True
            self.winner = self.board[3]
        # 4
        elif self.board[4] != '0' and self.board[4] == self.board[5] == self.board[8] == self.board[9]:
            self.is_terminal = True
            self.winner = self.board[4]
        elif self.board[4] != '0' and self.board[4] == self.board[5] == self.board[6] == self.board[7]:
            self.is_terminal = True
            self.winner = self.board[4]
        # 5
        elif self.board[5] != '0' and self.board[5] == self.board[6] == self.board[9] == self.board[10]:
            self.is_terminal = True
            self.winner = self.board[5]
        # 6
        elif self.board[6] != '0' and self.board[6] == self.board[7] == self.board[10] == self.board[11]:
            self.is_terminal = True
            self.winner = self.board[6]
        # 7
        # None
        # 8
        elif self.board[8] != '0' and self.board[8] == self.board[9] == self.board[12] == self.board[13]:
            self.is_terminal = True
            self.winner = self.board[8]
        elif self.board[8] != '0' and self.board[8] == self.board[9] == self.board[10] == self.board[11]:
            self.is_terminal = True
            self.winner = self.board[8]
        # 9
        elif self.board[9] != '0' and self.board[9] == self.board[10] == self.board[13] == self.board[14]:
            self.is_terminal = True
            self.winner = self.board[9]
        # 10
        elif self.board[10] != '0' and self.board[10] == self.board[11] == self.board[14] == self.board[15]:
            self.is_terminal = True
            self.winner = self.board[10]
        # 11
        # None
        # 12
        elif self.board[12] != '0' and self.board[12] == self.board[13] == self.board[14] == self.board[15]:
            self.is_terminal = True
            self.winner = self.board[12]
        elif self.board[12] != '0' and self.board[12] == self.board[9] == self.board[6] == self.board[3]:
            self.is_terminal = True
            self.winner = self.board[12]
        # Tie Case
        elif self.board.count('0') == 0:
            self.is_terminal = True
            self.winner = 'tie'
        else:
            self.is_terminal = False

    def make_move(self):
        self.valid = [i for i in range(0, 16) if self.board[i] == '0']
        self.board[random.choice(self.valid)] = self.player
        if self.player == 'x':
            self.player = 'o'
        else:
            self.player = 'x'
        self.check_end()


class MCTS:
    def __init__(self, initial_state, player, sec):
        self.root = Node(initial_state, None, player)
        self.best_move = None
        self.time = sec
        self.exploration_constant = 5

    def search(self):
        start = time.time()
        while time.time() - start <= self.time:
            node = self.traverse(self.root)
            score = self.rollout(node)
            self.backpropagate(node, score)
        return self.get_best_move(self.root)

    def traverse(self, node):
        while node.is_terminal is not True:
            if node.is_expanded:
                node = self.get_best_move(self.root)
            else:
                return self.expand(node)
        return node


    def expand(self, node):
        for moves in node.valid:
            if str(moves) not in node.child:
                new_board = copy.deepcopy(node.board)
                new_player = copy.deepcopy(node.player)
                new_board[moves] = new_player
                if new_player == 'x':
                    new_player = 'o'
                else:
                    new_player = 'x'
                new_node = Node(new_board, node, new_player)
                node.child[str(moves)] = new_node
                if len(node.valid) == len(node.child):
                    node.is_expanded = True
                return new_node

    def rollout(self, node):
        while node.is_terminal is not True:
            node.make_move()
        if node.winner == 'x':
            return 1 * node.count
        elif node.winner == 'o':
            return -1 * node.count
        elif node.winner == 'tie':
            return 0

    def backpropagate(self, node, score):
        while node is not None:
            node.count += 1
            node.score += score
            node = node.parent

    def get_best_move(self, node):
        best_score = -math.inf
        best_moves = []

        for child_node in node.child:
            if node.child[child_node].winner == 'x':
                current_player = 1
            elif node.child[child_node].winner == 'o':
                current_player = -1
            else:
                current_player = 0

            move_score = current_player * node.child[child_node].score / node.child[child_node].count + self.exploration_constant * math.sqrt(
                math.log(node.count / node.child[child_node].count))

            if move_score > best_score:
                best_score = move_score
                best_moves = [child_node]

            elif move_score == best_score:
                best_moves.append(child_node)
            self.best_move = random.choice(best_moves)
        return node.child[self.best_move]
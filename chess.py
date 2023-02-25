LETTERS = {7: "a", 6: "b", 5: "c", 4: "d", 3: "e", 2: "f", 1: "g", 0: "h"}
letters = {'a': 7, 'b': 6, 'c': 5, 'd': 4, 'e': 3, 'f': 2, 'g': 1, 'h': 0}


class Chess:
    def __init__(self):
        self.board = [['R.h', 'N.g', 'B.f', 'Q', 'K', 'B.c', 'N.b', 'R.a'],
                      ['P.h', 'P.g', 'P.f', 'P.e', 'P.d', 'P.c', 'P.b', 'P.a'],
                      [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                      [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                      [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                      [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                      ['p.h', 'p.g', 'p.f', 'p.e', 'p.d', 'p.c', 'p.b', 'p.a'],
                      ['r.h', 'n.g', 'b.f', 'q', 'k', 'b.c', 'n.b', 'r.a']]

    def render_board(self):
        new_board = []
        for y, line in enumerate(self.board):
            new_board.append([])
            for x, piece in enumerate(line):
                if "p" in piece.lower() or "b" in piece.lower() or "r" in piece.lower():
                    piece, file = piece.split(".")
                    new_board[y].append(piece)
                else:
                    new_board[y].append(piece)

        for line in new_board:
            print(line)
        print("\n")

    def get_piece_coords(self, piece):
        for y, line in enumerate(self.board):
            for x, _piece in enumerate(line):
                if _piece == piece:
                    return x, y

    def move_piece(self, piece, move):
        x, y = move
        x = letters[x]
        y = int(y) - 1
        old_x, old_y = self.get_piece_coords(piece)
        self.board[y][x] = piece
        self.board[old_y][old_x] = " "

    def check_legal_moves(self, piece):
        x, y = self.get_piece_coords(piece)
        legal_moves = []
        # checks for legal moves with a pawn
        if "p" in piece.lower():
            if "P" in piece:
                if self.board[y + 1][x] == " ":
                    if y == 1 and self.board[y + 2][x] == " ":
                        legal_move = [piece, f"{LETTERS[x]}{y + 3}"]
                        legal_moves.append(legal_move)
                    legal_move = [piece, f"{LETTERS[x]}{y + 2}"]
                    legal_moves.append(legal_move)
                for i in range(-1, 2, 2):
                    try:
                        if self.board[y + 1][x + i] != " ":
                            legal_move = [piece, f"{LETTERS[x + i]}{y + 2}"]
                            legal_moves.append(legal_move)
                    except IndexError:
                        pass

            elif "p" in piece:
                if self.board[y - 1][x] == " ":
                    if y == 6 and self.board[y - 2][x] == " ":
                        legal_move = [piece, f"{LETTERS[x]}{y - 3}"]
                        legal_moves.append(legal_move)
                    legal_move = [piece, f"{LETTERS[x]}{y - 2}"]
                    legal_moves.append(legal_move)
                for i in range(-1, 2, 2):
                    try:
                        if self.board[y - 1][x + i] != " ":
                            legal_move = [piece, f"{LETTERS[x + i]}{y - 2}"]
                            legal_moves.append(legal_move)
                    except IndexError:
                        pass
        # checks for legal moves with a rook
        if "r" in piece.lower():
            # checks for legal moves with a rook downwards
            for i in range(1, 7 - y + 1):
                new_y = y + i
                if self.board[new_y][x] == " ":
                    legal_move = [piece, f"{LETTERS[x]}{new_y + 1}"]
                    legal_moves.append(legal_move)
                else:
                    if "R" in piece and contains_capital(self.board[new_y][x]):
                        break
                    elif "r" in piece and not contains_capital(self.board[new_y][x]):
                        break
                    else:
                        legal_move = [piece, f"{LETTERS[x]}{new_y + 1}"]
                        legal_moves.append(legal_move)
                    break
            # checks for legal moves with a rook upwards
            for i in range(1, y + 1):
                new_y = y - i
                if self.board[new_y][x] == " ":
                    legal_move = [piece, f"{LETTERS[x]}{new_y + 1}"]
                    legal_moves.append(legal_move)
                else:
                    if "R" in piece and contains_capital(self.board[new_y][x]):
                        break
                    elif "r" in piece and not contains_capital(self.board[new_y][x]):
                        break
                    else:
                        legal_move = [piece, f"{LETTERS[x]}{new_y + 1}"]
                        legal_moves.append(legal_move)
                    break
            # checks for legal moves with a rook to the left
            for i in range(1, x + 1):
                new_x = x - i
                if self.board[y][new_x] == " ":
                    legal_move = [piece, f"{LETTERS[new_x]}{y + 1}"]
                    legal_moves.append(legal_move)
                else:
                    if "R" in piece and contains_capital(self.board[y][new_x]):
                        break
                    elif "r" in piece and not contains_capital(self.board[y][new_x]):
                        break
                    else:
                        legal_move = [piece, f"{LETTERS[new_x]}{y + 1}"]
                        legal_moves.append(legal_move)
                    break
            # checks for legal moves with a rook to the right
            for i in range(1, 7 - x + 1):
                new_x = x + i
                if self.board[y][new_x] == " ":
                    legal_move = [piece, f"{LETTERS[new_x]}{y + 1}"]
                    legal_moves.append(legal_move)
                else:
                    if "R" in piece and contains_capital(self.board[y][new_x]):
                        break
                    elif "r" in piece and not contains_capital(self.board[y][new_x]):
                        break
                    else:
                        legal_move = [piece, f"{LETTERS[new_x]}{y + 1}"]
                        legal_moves.append(legal_move)
                    break
        # checks for legal moves with a bishop
        if "b." in piece.lower():
            # checks for legal moves with a bishop to the top-right
            for i in range(1, max(7 - x, 7 - y) + 1):
                new_x, new_y = x + i, y - i
                try:
                    if self.board[new_y][new_x] == " ":
                        legal_move = [piece, f"{LETTERS[new_x]}{new_y + 1}"]
                        legal_moves.append(legal_move)
                    else:
                        if "B" in piece and contains_capital(self.board[new_y][new_x]):
                            break
                        elif "b" in piece and not contains_capital(self.board[new_y][new_x]):
                            break
                        else:
                            legal_move = [piece, f"{LETTERS[new_x]}{new_y + 1}"]
                            legal_moves.append(legal_move)
                        break
                except IndexError:
                    pass
            # checks for legal moves with a bishop to the top left
            for i in range(1, min(x, y) + 1):

                new_x, new_y = x - i, y - i
                if self.board[new_y][new_x] == " ":
                    legal_move = [piece, f"{LETTERS[new_x]}{new_y + 1}"]
                    legal_moves.append(legal_move)
                else:
                    if "B" in piece and contains_capital(self.board[new_y][new_x]):
                        break
                    elif "b" in piece and not contains_capital(self.board[new_y][new_x]):
                        break
                    else:
                        legal_move = [piece, f"{LETTERS[new_x]}{new_y + 1}"]
                        legal_moves.append(legal_move)
                    break
            # checks for legal moves with a bishop to the bottom right
            for i in range(1, min(7 - y, 7 - x) + 1):
                new_x, new_y = x + i, y + i
                if self.board[new_y][new_x] == " ":
                    legal_move = [piece, f"{LETTERS[new_x]}{new_y + 1}"]
                    legal_moves.append(legal_move)
                else:
                    if "B" in piece and contains_capital(self.board[new_y][new_x]):
                        break
                    elif "b" in piece and not contains_capital(self.board[new_y][new_x]):
                        break
                    else:
                        legal_move = [piece, f"{LETTERS[new_x]}{new_y + 1}"]
                        legal_moves.append(legal_move)
                    break
            # checks for legal moves with a bishop to the bottom left
            for i in range(1, min(x, 7 - y) + 1):
                new_x, new_y = x - i, y + i
                if self.board[new_y][new_x] == " ":
                    legal_move = [piece, f"{LETTERS[new_x]}{new_y + 1}"]
                    legal_moves.append(legal_move)
                else:
                    if "B" in piece and contains_capital(self.board[new_y][new_x]):
                        break
                    elif "b" in piece and not contains_capital(self.board[new_y][new_x]):
                        break
                    else:
                        legal_move = [piece, f"{LETTERS[new_x]}{new_y + 1}"]
                        legal_moves.append(legal_move)
                    break
        # checks for legal moves with a knight
        if "n" in piece.lower():
            # checks for legal moves with a knight to the right
            for i in range(-1, 2, 2):
                new_x, new_y = x + 2, y + i
                print(new_x, new_y)
                if self.board[new_y][new_x] == " ":
                    legal_move = [piece, f"{LETTERS[new_x]}{new_y + 1}"]
                    legal_moves.append(legal_move)
                else:
                    if "N" in piece and contains_capital(self.board[new_y][new_x]):
                        pass
                    elif "n" in piece and not contains_capital(self.board[new_y][new_x]):
                        pass
                    else:
                        legal_move = [piece, f"{LETTERS[new_x]}{new_y + 1}"]
                        legal_moves.append(legal_move)

            # checks for legal moves with a knight to the left
            for i in range(-1, 2, 2):
                new_x, new_y = x - 2, y + i
                if self.board[new_y][new_x] == " ":
                    legal_move = [piece, f"{LETTERS[new_x]}{new_y + 1}"]
                    legal_moves.append(legal_move)
                else:
                    if "N" in piece and contains_capital(self.board[new_y][new_x]):
                        pass
                    elif "n" in piece and not contains_capital(self.board[new_y][new_x]):
                        pass
                    else:
                        legal_move = [piece, f"{LETTERS[new_x]}{new_y + 1}"]
                        legal_moves.append(legal_move)

            # checks for legal moves with a knight to the bottom
            for i in range(-1, 2, 2):
                new_x, new_y = x + i, y + 2
                if self.board[new_y][new_x] == " ":
                    legal_move = [piece, f"{LETTERS[new_x]}{new_y + 1}"]
                    legal_moves.append(legal_move)
                else:
                    if "N" in piece and contains_capital(self.board[new_y][new_x]):
                        break
                    elif "n" in piece and not contains_capital(self.board[new_y][new_x]):
                        break
                    else:
                        legal_move = [piece, f"{LETTERS[new_x]}{new_y + 1}"]
                        legal_moves.append(legal_move)
            # checks for legal moves with a knight to the top
            for i in range(-1, 2, 2):
                new_x, new_y = x + i, y - 2
                if self.board[new_y][new_x] == " ":
                    legal_move = [piece, f"{LETTERS[new_x]}{new_y + 1}"]
                    legal_moves.append(legal_move)
                else:
                    if "N" in piece and contains_capital(self.board[new_y][new_x]):
                        break
                    elif "n" in piece and not contains_capital(self.board[new_y][new_x]):
                        break
                    else:
                        legal_move = [piece, f"{LETTERS[new_x]}{new_y + 1}"]
                        legal_moves.append(legal_move)
        # checks for legal moves with a queen
        if "q" in piece.lower():
            # checks for legal moves with a queen to the top-right
            for i in range(1, max(7 - x, 7 - y) + 1):
                new_x, new_y = x + i, y - i
                try:
                    if self.board[new_y][new_x] == " ":
                        legal_move = [piece, f"{LETTERS[new_x]}{new_y + 1}"]
                        legal_moves.append(legal_move)
                    else:
                        if "Q" in piece and contains_capital(self.board[new_y][new_x]):
                            break
                        elif "q" in piece and not contains_capital(self.board[new_y][new_x]):
                            break
                        else:
                            legal_move = [piece, f"{LETTERS[new_x]}{new_y + 1}"]
                            legal_moves.append(legal_move)
                        break
                except IndexError:
                    pass
            # checks for legal moves with a queen to the top left
            for i in range(1, min(x, y) + 1):

                new_x, new_y = x - i, y - i
                if self.board[new_y][new_x] == " ":
                    legal_move = [piece, f"{LETTERS[new_x]}{new_y + 1}"]
                    legal_moves.append(legal_move)
                else:
                    if "Q" in piece and contains_capital(self.board[new_y][new_x]):
                        break
                    elif "q" in piece and not contains_capital(self.board[new_y][new_x]):
                        break
                    else:
                        legal_move = [piece, f"{LETTERS[new_x]}{new_y + 1}"]
                        legal_moves.append(legal_move)
                    break
            # checks for legal moves with a queen to the bottom right
            for i in range(1, min(7 - y, 7 - x) + 1):
                new_x, new_y = x + i, y + i
                if self.board[new_y][new_x] == " ":
                    legal_move = [piece, f"{LETTERS[new_x]}{new_y + 1}"]
                    legal_moves.append(legal_move)
                else:
                    if "Q" in piece and contains_capital(self.board[new_y][new_x]):
                        break
                    elif "q" in piece and not contains_capital(self.board[new_y][new_x]):
                        break
                    else:
                        legal_move = [piece, f"{LETTERS[new_x]}{new_y + 1}"]
                        legal_moves.append(legal_move)
                    break
            # checks for legal moves with a queen to the bottom left
            for i in range(1, min(x, 7 - y) + 1):
                new_x, new_y = x - i, y + i
                if self.board[new_y][new_x] == " ":
                    legal_move = [piece, f"{LETTERS[new_x]}{new_y + 1}"]
                    legal_moves.append(legal_move)
                else:
                    if "Q" in piece and contains_capital(self.board[new_y][new_x]):
                        break
                    elif "q" in piece and not contains_capital(self.board[new_y][new_x]):
                        break
                    else:
                        legal_move = [piece, f"{LETTERS[new_x]}{new_y + 1}"]
                        legal_moves.append(legal_move)
                    break

            # checks for legal moves with a queen downwards
            for i in range(1, 7 - y + 1):
                new_y = y + i
                if self.board[new_y][x] == " ":
                    legal_move = [piece, f"{LETTERS[x]}{new_y + 1}"]
                    legal_moves.append(legal_move)
                else:
                    if "Q" in piece and contains_capital(self.board[new_y][x]):
                        break
                    elif "q" in piece and not contains_capital(self.board[new_y][x]):
                        break
                    else:
                        legal_move = [piece, f"{LETTERS[x]}{new_y + 1}"]
                        legal_moves.append(legal_move)
                    break
            # checks for legal moves with a queen upwards
            for i in range(1, y + 1):
                new_y = y - i
                if self.board[new_y][x] == " ":
                    legal_move = [piece, f"{LETTERS[x]}{new_y + 1}"]
                    legal_moves.append(legal_move)
                else:
                    if "Q" in piece and contains_capital(self.board[new_y][x]):
                        break
                    elif "q" in piece and not contains_capital(self.board[new_y][x]):
                        break
                    else:
                        legal_move = [piece, f"{LETTERS[x]}{new_y + 1}"]
                        legal_moves.append(legal_move)
                    break
            # checks for legal moves with a queen to the left
            for i in range(1, x + 1):
                new_x = x - i
                if self.board[y][new_x] == " ":
                    legal_move = [piece, f"{LETTERS[new_x]}{y + 1}"]
                    legal_moves.append(legal_move)
                else:
                    if "Q" in piece and contains_capital(self.board[y][new_x]):
                        break
                    elif "q" in piece and not contains_capital(self.board[y][new_x]):
                        break
                    else:
                        legal_move = [piece, f"{LETTERS[new_x]}{y + 1}"]
                        legal_moves.append(legal_move)
                    break
            # checks for legal moves with a queen to the right
            for i in range(1, 7 - x + 1):
                new_x = x + i
                if self.board[y][new_x] == " ":
                    legal_move = [piece, f"{LETTERS[new_x]}{y + 1}"]
                    legal_moves.append(legal_move)
                else:
                    if "Q" in piece and contains_capital(self.board[y][new_x]):
                        break
                    elif "q" in piece and not contains_capital(self.board[y][new_x]):
                        break
                    else:
                        legal_move = [piece, f"{LETTERS[new_x]}{y + 1}"]
                        legal_moves.append(legal_move)
                    break
        # checks for legal moves with a king
        if "k" in piece.lower():
            for i in range(-1, 2):
                for j in range(-1, 2):
                    new_x, new_y = x + i, y + j
                    if new_x == x and new_y == y:
                        continue
                    if self.board[new_y][new_x] == " ":
                        legal_move = [f"{LETTERS[new_x]}{new_y+1}"]
                        legal_moves.append(legal_move)
                    else:
                        if "K" in piece and contains_capital(self.board[new_y][new_x]):
                            continue
                        elif "k" in piece and not contains_capital(self.board[new_y][new_x]):
                            continue
                        else:
                            legal_move = [f"{LETTERS[new_x]}{new_y + 1}"]
                            legal_moves.append(legal_move)

        return legal_moves


def contains_capital(string):
    for char in string:
        if char.isupper():
            return True
    return False


chess = Chess()
# chess.move_piece("R.h", "e4")
# chess.render_board()
# print(chess.check_legal_moves("R.h"))
chess.move_piece("p.d", "d6")
chess.move_piece("P.d", "d4")
chess.move_piece("k", "e5")

chess.render_board()
print(chess.check_legal_moves("k"))

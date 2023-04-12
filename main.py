#Kółko i Krzyżyk
print("""---------------------------

KÓŁKO i KRZYŻYK

----------------------------""")


#stałe globalne
X = "X"
O = "O"
EMPTY = " "
TIE = "TIE"
NUM_SQUARES = 9


def display_instruct():
    """WYŚWIETL INSTRUKCJĘ GRY."""
    print(
        """
        Witaj w najwiekszym intelektualnym wyzwaniu wszech czasów, jakim jest gra 'Kółko i krzyżyk'.
        Jest to jedna z najważniejszych gier decydującym o wszystkich sporachz zaraz po 'Kamień, papier, nożyce'.
        
        Ruchy w grze możesz dokonywać poprzez wprowadzenie liczby z zakresu od 0 do 8,
        każda liczba odpowiada pozycji na planszy, zgodnej z poniższym schematem:
        
                0 | 1 | 2
                ---------
                3 | 4 | 5
                ---------
                6 | 7 | 8
                
        Kto wygra w tym pojedynku, ludzki mózg czy krzemowy procesor?
        Sprawdźmy się.
        
        """
    )

def ask_yes_no(question):
    "Zadaj pytanie, na które można odpowiedzieć tylko tak lub nie. (t / n)"
    response = None
    while response not in ("t", "n"):
        response = input(question).lower()
    return response

def ask_number(question, low, high):
    """Poproś o podanie liczby od 0 do 8"""
    response = None
    while response not in range(low, high):
        response = int(input(question))
    return response

def pieces():
    """Ustal, czy pierwszy rych należy do gracza, czy do komputera."""
    go_first = ask_yes_no("Czy chcesz mieć prawo do pierwszego ruchu? ( t / n ): ")
    if go_first == "t":
        print("\nWięc pierwszy ruch należy do Ciebie. Będzie Ci potrzebny :). ")
        human = X
        computer = O
    else:
        print("\nTwoją odwaga Cię zgubi ... Ja wykonuję pierwszy ruch.")
        computer = X
        human = O
    return computer, human

def new_board():
    """Utwórz nową planszę gry."""
    board = []
    for square in range (NUM_SQUARES):
        board.append(EMPTY)
    return board

def display_board(board):
    """Wyświetl planszę gry na ekranie."""

    print("\n\t", board[0], "|", board[1], "|", board[2])
    print("\t", "--------")
    print("\t", board[3], "|", board[4], "|", board[5])
    print("\t", "--------")
    print("\t", board[6], "|", board[7], "|", board[8], "\n")

def legal_moves(board):
    """Utwórz listę prawidłowych ruchów."""
    moves = []
    for square in range(NUM_SQUARES):
        if board[square] == EMPTY:
            moves.append(square)
    return moves

def winner(board):
    """Ustal zwycięzcę gry."""
    WAYS_TO_WIN = ((0, 1, 2),
                   (3, 4, 5),
                   (6, 7, 8),
                   (0, 3, 6),
                   (1, 4, 7),
                   (2, 5, 8),
                   (0, 4, 8),
                   (2, 4, 6))


    for row in WAYS_TO_WIN:
        if board[row[0]] == board[row[1]] == board[row[2]] != EMPTY:
            winner = board[row[0]]
            return winner

    if EMPTY not in board:
        return TIE

    return None

def human_move(board, human):
    """Odczytaj ruch człowieka."""
    legal = legal_moves(board)
    move = None
    while move not in legal:
        move = ask_number("Jaki będzie Twój ruch? 0 - 8: ", 0, NUM_SQUARES)
        if move not in legal:
            print("\nTo pole jest już zajęte, wybierz inne. \n")
    print("Znakomicie... ")
    return move

def computer_move(board, computer, human):
    """Spowoduj wykonanie ruchu przez komputer."""
    # utwórz kopię roboczą, ponieważ funkcja będzie zmieniać listę.
    board = board[:]

    #najlepsze możliwe miejsca do zajęcia na planszy
    BEST_MOVES = (4, 0, 2, 6, 8, 1, 3, 5, 7)

    print("Wybieram pole numer", end = " ")

    #jesli pc moze wygrac to wykonaj:

    for move in legal_moves(board):
        board[move] = computer
        if winner(board) == computer:
            print(move)
            return move
    #ten ruch został sprawdzony, wycofaj go
    board[move] = EMPTY

    #brak mozliwosci wygranej w nastepnej rundzie, wiec najlepszy ruch.

    for move in BEST_MOVES:
        if move in legal_moves(board):
            print(move)
            return move

def next_turn(turn):
    """Zmień wykonawcę ruchu."""

    if turn == X:
        return O
    else:
        return X

def congrat_winner(the_winner, computer, human):
    """Pogratuluj zwyciezcy."""
    if the_winner != TIE:
        print(the_winner, " jest zwycięzcą!\n")
    else:
        print("REMIS!\n")

    if the_winner == computer:
        print("EZ CZŁOWIEKU")
    elif the_winner == human:
        print("Komputer: Jestem leszczem.")
    elif the_winner == TIE:
        print("Miałeś farta.")

def main():
    display_instruct()
    computer, human = pieces()
    turn = X
    board = new_board()
    display_board(board)

    while not winner(board):
        if turn == human:
            move = human_move(board, human)
            board[move] = human
        else:
            move = computer_move(board, computer, human)
            board[move] = computer
        display_board(board)
        turn = next_turn(turn)

    the_winner = winner(board)
    congrat_winner(the_winner, computer, human)

#start programu
main()

input("\nAby zakończyć grę, naciśnij klawisz Enter.")
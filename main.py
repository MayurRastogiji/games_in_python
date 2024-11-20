import random
import pyttsx3
import bot_keys
import bot_mail
import bot_whatsapp
import bot_game
import os
import bot_db as db
import time
engine = pyttsx3.init()

def speakandprint(str):
    print(str)
    engine.say(str)
    engine.runAndWait()

def speak(str):
    engine.say(str)
    engine.runAndWait()

# QUIZ GAME
def quiz(name, attempt):
    questions = ["What is the primary function of a CPU?", "Which protocol is used for sending emails?", "What is the file extension for a Microsoft Word document?", "What does \"HTML\" stand for in web development?", "What programming language is often used for web development?", "What is the term for a program that replicates itself and spreads to other computers?", " Which programming language is known for its use in data analysis and scientific computing?", "What does \"URL\" stand for?",
                 "In computing, what does \"RAM\" stand for?", "Which company developed the Windows operating system?", " What is the standard protocol used for secure web communication?", "What is the code name of the open-source web browser developed by Mozilla?", "What is the term for a small piece of code that performs a specific task within a larger program?", "What type of software allows users to view web pages on the internet?", "What is the file extension for a compressed archive format commonly used on Windows?"]
    answers = ["processing data", "smtp", "docx", "hypertext markup language", "javascript", "virus", "python",
               "uniform resource locator", "random access memory", "microsoft", "https", "firefox", "function", "web browser", "zip"]
    speakandprint(f"welcome {name} to the quiz game")
    prize = 0
    i = 0
    while i < attempt:
        if i != 0:
            speakandprint("your next question is\n")
        random_index = random.randint(0, len(questions) - 1)
        speakandprint(questions[random_index])
        speakandprint("your options are:")
        lst_options = set()
        for j in range(1, 4):
            options = random.randint(0, len(answers) - 1)
            lst_options.add(answers[options])
            if answers[random_index] in lst_options:
                lst_options.add(answers[random.randint(0, len(answers) - 1)])
            else:
                lst_options.add(answers[random_index])
                print(answers[random_index])
        # random.shuffle(lst_options)
        print(lst_options)
        for j in lst_options:
            speakandprint(f"{j}")

        speakandprint("enter your answer : \n")
        a = input()
        if a == answers[random_index]:
            print("your answer is \033[32mcorrect \nyou won 1000 rupees\033[0m \n ")
            speak("your answer is correct you won 1000 rupees ")
            prize = prize + 1000
        else:
            print("your answer is \033[91mwrong \nyou lost 500 rupees\033[0m \n ")
            speak("your answer is wrong you lost 500 rupees ")
            prize = prize - 500
        i = i+1
    if prize > 0:
        db.winner_price(name)
        print(name, " won: \033[32mCongratulations\033[0m")
        speak(f"Congratulations {name} you won {prize} rupees")
    else:
        print(name, " lost: \033[91mTry Again\033[0m")
        speak(f"Try Again {name}")

def check_computer_output(n):
    if n == 0:
        return "rock"
    elif n == 1:
        return "paper"
    else:
        return "scissors"
# ROCK PAPER SCISSORS GAME
def rockpaperscissors(name, n):
    speakandprint(f"Welcome {name} to our \n Rock, Paper and Scissors game.")
    output = [
        [0, 1, 2],
        [2, 0, 1],
        [1, 2, 0]
    ]
    a = 1
    player_score = 0
    computer_score = 0
    while a <= n:
        speakandprint("enter 0 for Rock\nenter 1 for Paper\nenter 2 for Scissors\n")
        user_input = int(input())
        if user_input > 2:
            speakandprint("Enter the correct input")
            continue
        computer_input = random.randint(0, 2)
        print(f"your input is {user_input}")
        print(f"computer input is {check_computer_output(computer_input)}")
        if output[user_input][computer_input] == 0:
            print("\033[38;5;214mMatch Draw\033[0m")
            speak("Match Draw")
        elif output[user_input][computer_input] == 1:
            player_score += 1
            print(f"\033[32m{name} wins\033[0m")
            speak(f"{name} wins")
        else:
            computer_score += 1
            print("\033[91mcomputer wins\033[0m")
            speak("computer wins")
        a += 1
    speakandprint(f"score of player {name} : {player_score}")
    speakandprint(f"score of computer : {computer_score}")
    if (player_score < computer_score):
        print(f"\033[91mcomputer wins by\033[0m {computer_score - player_score}")
        speak(f"computer wins by {computer_score - player_score}")
    elif (player_score == computer_score):
        print("\033[38;5;214mIt's a Draw.\033[0m")
        speak("It's a Draw")
    else:
        db.winner_price(name)
        print(f"\033[32m{name} wins by\033[0m {player_score - computer_score}")
        speak(f"{name} wins by {player_score - computer_score}")

# SNAKE WATER GUN GAME
def SnakeWaterGun(name, n):
    speakandprint(f"Hello {name} to our \n SNAKE, WATER and GUN game.")
    output = [
        [0, 1, 2],
        [2, 0, 1],
        [1, 2, 0]
    ]
    # n = int(input("how many chances"))
    a = 1
    player_score = 0
    computer_score = 0
    while a <= n:
        user_input = int(
            input("enter 0 for SNAKE\nenter 1 for WATER\nenter 2 for GUN\n"))
        computer_input = random.randint(0, 2)
        if output[user_input][computer_input] == 0:
            print("\033[38;5;214mMatch Draw\033[0m")
            speak("Match Draw")
        elif output[user_input][computer_input] == 1:
            player_score += 1
            print(f"\033[92m{name} wins\033[0m")
            speak(f"{name} wins")
        else:
            computer_score += 1
            print("\033[91mcomputer wins\033[0m")
            speak("computer wins")
        a += 1
    speakandprint(f"score of player {name} : {player_score}")
    speakandprint(f"score of computer : {computer_score}")
    if (player_score < computer_score):
        print(f"\033[91mcomputer wins by\033[0m {computer_score - player_score}")
        speak(f"computer wins by {computer_score - player_score}")
    elif (player_score == computer_score):
        print("\033[38;5;214mIt's a draw\033[0m")
        speak("It's a draw")
    else:
        db.winner_price(name)
        print(f"\033[32m{name} wins by\033[0m {player_score - computer_score}")
        speak(f"{name} wins by {player_score - computer_score}")


# TIC TAC TOE GAME
"""
There are two ways to playa game of Tic Tac Toe.
one is to play with computer and other is to play with another player.
if you want to play with computer then you have to call the function tic_tac_toe(name)
if you want to play with another player then you have to call the function tic_tac_toe(player1, player2)
if you choose to play with computer then you have to selecr your level of difficulty.
there are three levels of difficulty.
1. Easy
    where computer will play randomly.
2. Medium
    where computer will play randomly but it always stops the player from winning.
3. Hard
    where computer will play randomly but it always stops the player from winning and tries to win the game., it had some of its own techiniques ot win the game as well."""


# tic_tac_toe for 1 player
def tic_tac_toe_computer(name):
    speakandprint(f"Welcome {name} to the Tic Tac Toe game.")
    speakandprint("Its the simple 3X3 grid game .")
    speakandprint(
        "You have to enter the row and column number to place your mark.")
    speakandprint(
        "The player who gets 3 marks in a row, column or diagonal wins the game.")
    speakandprint("Lets start the game.")
    speakandprint("Enter your choice of symbol (X or O) : ")
    choice_symbol = input()
    if choice_symbol == 'X':
        computer = 'O'
        speakandprint("Computer will play with O")
    else:
        computer = 'X'
        speakandprint("Computer will play with X")

    speakandprint("Enter the level of difficulty (easy, medium, hard) : ")
    mode = input()
    board = [
        [' ', '1', '2', '3'],
        ['1', '.', '.', '.'],
        ['2', '.', '.', '.'],
        ['3', '.', '.', '.']
    ]

    def print_board(board):
        for i in range(4):
            for j in range(4):
                print(board[i][j], end=" ")
            print()

    def check_winner(board):
        for i in range(1, 4):
            if board[i][1] == board[i][2] == board[i][3] and board[i][1] != '.':
                return board[i][1]
            if board[1][i] == board[2][i] == board[3][i] and board[1][i] != '.':
                return board[1][i]
        if board[3][3] == board[1][1] == board[2][2] and board[1][1] != '.':
            return board[1][1]
        if board[1][3] == board[2][2] == board[3][1] and board[1][3] != '.':
            return board[1][3]
        else:
            return None

    def check_draw(board):
        if check_winner(board) == None:
            for i in range(4):
                for j in range(4):
                    if board[i][j] == '.':
                        return False
            return True

    def easy_mode(board):
        speakandprint("Computer's turn")
        turn = 'c'
        computer_row = random.randint(1, 3)
        computer_col = random.randint(1, 3)
        speakandprint("Computer is thinking...")
        speakandprint(computer_row, computer_col)
        while turn == 'c':
            if board[computer_row][computer_col] == '.':

                board[computer_row][computer_col] = computer
                print_board(board)
                turn = 'p'
            else:
                computer_row = random.randint(1, 3)
                computer_col = random.randint(1, 3)
                continue

    def is_occupied(board, row, col):
        if board[row][col] == '.':
            return False
        else:
            return True

    def index_loo(board, computer_row, computer_col):
        turn = 'c'
        change = 0
        chance = 1
        while turn == 'c':
            if not is_occupied(board, computer_row, computer_col):
                if not is_occupied(board, 2, 2) and chance == 1:
                    computer_row = 2
                    computer_col = 2
                    change = 1
                    chance = 0
                for i in range(1, 4):
                    if board[i][1] == board[i][2] and board[i][1] == choice_symbol and change != 1 and board[i][3] != computer:
                        computer_row = i
                        computer_col = 3
                        change = 1
                        break
                    elif board[i][1] == board[i][3] and board[i][1] == choice_symbol and change != 1 and board[i][2] != computer:
                        computer_row = i
                        computer_col = 2
                        change = 1
                        break
                    elif board[i][2] == board[i][3] and board[i][2] == choice_symbol and change != 1 and board[i][1] != computer:
                        computer_row = i
                        computer_col = 1
                        change = 1
                        break
                    if board[1][i] == board[2][i] and board[1][i] == choice_symbol and change != 1 and board[3][i] != computer:
                        computer_row = 3
                        computer_col = i
                        change = 1
                        break
                    elif board[1][i] == board[3][i] and board[1][i] == choice_symbol and change != 1 and board[2][i] != computer:
                        computer_row = 2
                        computer_col = i
                        change = 1
                        break
                    elif board[2][i] == board[3][i] and board[2][i] == choice_symbol and change != 1 and board[1][i] != computer:
                        computer_row = 1
                        computer_col = i
                        change = 1
                        break
                if board[3][3] == board[1][1] and board[1][1] == choice_symbol and change != 1 and board[2][2] != computer:
                    computer_row = 2
                    computer_col = 2
                    change = 1
                elif board[1][1] == board[2][2] and board[1][1] == choice_symbol and change != 1 and board[3][3] != computer:
                    computer_row = 3
                    computer_col = 3
                    change = 1
                elif board[3][3] == board[2][2] and board[3][3] == choice_symbol and change != 1 and board[2][2] != computer:
                    computer_row = 2
                    computer_col = 2
                    change = 1
                if board[1][3] == board[3][1] and board[1][3] == choice_symbol and change != 1 and board[2][2] != computer:
                    computer_row = 2
                    computer_col = 2
                    change = 1
                elif board[3][1] == board[2][2] and board[3][1] == choice_symbol and change != 1 and board[1][3] != computer:
                    computer_row = 1
                    computer_col = 3
                    change = 1
                elif board[2][2] == board[1][3] and board[3][1] == choice_symbol and change != 1 and board[3][1] != computer:
                    computer_row = 3
                    computer_col = 1
                    change = 1
                if is_occupied(board, 2, 2) and change != 1:
                    if not is_occupied(board, 1, 1):
                        computer_row = 1
                        computer_col = 1
                        change = 1
                    elif not is_occupied(board, 1, 3):
                        computer_row = 1
                        computer_col = 3
                        change = 1
                    elif not is_occupied(board, 3, 1):
                        computer_row = 3
                        computer_col = 1
                        change = 1
                    elif not is_occupied(board, 3, 3):
                        computer_row = 3
                        computer_col = 3
                        change = 1
                if not is_occupied(board, computer_row, computer_col):
                    print(computer_row, computer_col)
                    return computer_row, computer_col
                    turn = 'p'
                else:
                    computer_row = random.randint(1, 3)
                    computer_col = random.randint(1, 3)
                    continue
            else:
                computer_row = random.randint(1, 3)
                computer_col = random.randint(1, 3)

    def hard_mode(board):
        speakandprint("Computer's turn")
        speakandprint("Computer is thinking...")
        row, column = index_loo(board, 2, 2)
        board[row][column] = computer
        print_board(board)

    def medium_mode(board):
        speakandprint("Computer's turn")
        turn = 'c'
        change = 0
        computer_row = random.randint(1, 3)
        computer_col = random.randint(1, 3)
        speakandprint("Computer is thinking...")
        while turn == 'c':
            if not is_occupied(board, computer_row, computer_col):
                if board[1][1] or board[1][3] or board[3][1] or board[3][3] == choice_symbol and board[2][2] != choice_symbol or computer and change == 1:
                    computer_row = 2
                    computer_col = 2
                if board[1][2] == choice_symbol:
                    if not is_occupied(board, 1, 1):
                        computer_row = 1
                        computer_col = 1
                    elif not is_occupied(board, 1, 3):
                        computer_row = 1
                        computer_col = 3
                    else:
                        computer_row, computer_col = index_loo(board)
                elif board[2][1] == choice_symbol:
                    if not is_occupied(board, 1, 1):
                        computer_row = 1
                        computer_col = 1
                    elif not is_occupied(board, 3, 1):
                        computer_row = 1
                        computer_col = 3
                    else:
                        computer_row, computer_col = index_loo(board)
                elif board[3][2] == choice_symbol:
                    if not is_occupied(board, 3, 1):
                        computer_row = 1
                        computer_col = 1
                    elif not is_occupied(board, 3, 3):
                        computer_row = 1
                        computer_col = 3
                    else:
                        computer_row, computer_col = index_loo(board)
                elif board[2][3] == choice_symbol:
                    if not is_occupied(board, 1, 3):
                        computer_row = 1
                        computer_col = 1
                    elif not is_occupied(board, 3, 3):
                        computer_row = 1
                        computer_col = 3
                    else:
                        computer_row, computer_col = index_loo(board)
                else:
                    computer_row, computer_col = index_loo(board)

                board[computer_row][computer_col] = computer
            print_board(board)
            turn = 'p'

    print_board(board)
    for i in range(1, 4):
        for j in range(1, 4):
            while board[i][j] == '.':
                speakandprint("Enter row: ")
                row = int(input())
                speakandprint("Enter col: ")
                col = int(input())
                if row > 3 or col > 3:
                    speakandprint(
                        "Enter the row and column number again.\n You have entered the wrong row and column number.")
                    continue
                if board[row][col] == '.':
                    board[row][col] = choice_symbol
                    print_board(board)
                else:
                    speakandprint("Cell is already occupied")
                    speakandprint("Enter the row and column number again.")
                    continue
                if check_draw(board):
                    print_board(board)
                    print("\033[38;5;214mDraw!\033[0m")
                    speak("Draw!")
                    exit()
                elif check_winner(board) == choice_symbol:
                    print_board(board)
                    print(f"\033[32m{name} wins!\033[0m")
                    speak(f"{name} wins!")
                    db.winner_price(name)
                    exit()
                elif check_winner(board) == computer:
                    print_board(board)
                    print("\033[91mComputer wins!\033[0m")
                    speak("Computer wins!")
                    exit()
                else:
                    if mode == 'easy':
                        easy_mode(board)
                    elif mode == 'medium':
                        medium_mode(board)
                    elif mode == 'hard':
                        hard_mode(board)
                if check_draw(board):
                    print_board(board)
                    print("\033[38;5;214mDraw!\033[0m")
                    speak("Draw!")
                    exit()
                elif check_winner(board) == choice_symbol:
                    print_board(board)
                    print(f"\033[32m{name} wins!\033[0m")
                    speak(f"{name} wins!")
                    db.winner_price(name)
                    exit()
                elif check_winner(board) == computer:
                    print_board(board)
                    print("\033[91mComputer wins!\033[0m")
                    speak("Computer wins!")
                    exit()

# tic_tac_toe for 2 players
def tic_tac_toe_person(player1, player2):
    speakandprint(
        f"Welcome {player1} and {player2} to the game of Tic Tac Toe game.")
    speakandprint("Its the simple 3X3 grid game .")
    speakandprint(
        "You have to enter the row and column number to place your mark.")
    speakandprint(
        "The player who gets 3 marks in a row, column or diagonal wins the game.")
    speakandprint("Lets start the game.")
    speakandprint(f"{player1} Enter your choice of symbol (X or O) : ")
    choice_symbol_1 = input()
    if choice_symbol_1 == 'X':
        choice_symbol_2 = 'O'
        speakandprint(f"{player2} will play with O")
    else:
        choice_symbol_2 = 'X'
        speakandprint(f"{player2} will play with X")
    board = [
        [' ', '1', '2', '3'],
        ['1', '.', '.', '.'],
        ['2', '.', '.', '.'],
        ['3', '.', '.', '.']
    ]

    def print_board(board):
        for i in range(4):
            for j in range(4):
                print(board[i][j], end=" ")
            print()

    def check_winner(board):
        for i in range(1, 4):
            if board[i][1] == board[i][2] == board[i][3] and board[i][1] != '.':
                return board[i][1]
            if board[1][i] == board[2][i] == board[3][i] and board[1][i] != '.':
                return board[0][i]
        if board[3][3] == board[1][1] == board[2][2] and board[1][1] != '.':
            return board[1][1]
        if board[1][3] == board[3][3] == board[3][1] and board[1][3] != '.':
            return board[1][3]
        else:
            return None

    def check_draw(board):
        if check_winner(board) == None:
            for i in range(4):
                for j in range(4):
                    if board[i][j] == '.':
                        return False
            return True

    def check(board):
        if check_draw(board):
            print_board(board)
            speakandprint("Draw!")
            return True
        elif check_winner(board) == choice_symbol_1:
            print_board(board)
            speakandprint(f"{player1} wins!")
            db.winner_price(player1)
            return True
        elif check_winner(board) == choice_symbol_2:
            print_board(board)
            speakandprint(f"{player2} wins!")
            db.winner_price(player2)
            return True

    print_board(board)
    for i in range(1, 4):
        for j in range(1, 4):
            while board[i][j] == '.':
                turn = 'p1'
                while turn == 'p1':
                    speakandprint("Enter row: ")
                    row = int(input())
                    speakandprint("Enter col: ")
                    col = int(input())
                    if row > 3 or col > 3:
                        speakandprint(
                            "Enter the row and column number again.\n You have entered the wrong row and column number.")
                        continue
                    if board[row][col] == '.':
                        board[row][col] = choice_symbol_1
                        print_board(board)
                        turn = 'p2'
                    else:
                        speakandprint("Cell is already occupied")
                        speakandprint("Enter the row and column number again.")
                        continue

                if check(board):
                    exit()

                else:
                    speakandprint(f"{player2} turn")
                    while turn == 'p2':
                        speakandprint("Enter row: ")
                        row = int(input())
                        speakandprint("Enter col: ")
                        col = int(input())
                        if row > 3 or col > 3:
                            speakandprint("Enter the row and column number again.\n You have entered the wrong row and column number.")
                            continue
                        if board[row][col] == '.':
                            board[row][col] = choice_symbol_2
                            print_board(board)
                            turn = 'p1'
                        else:
                            speakandprint("Cell is already occupied")
                            speakandprint("Enter the row and column number again.")
                            continue
                if check(board):
                    exit()

#  sudoku solver
def sudoku():
    sudoku = [[0, 7, 0, 5, 8, 3, 0, 2, 0],
              [0, 5, 9, 2, 0, 0, 3, 0, 0],
              [3, 4, 0, 0, 0, 6, 5, 0, 7],
              [7, 9, 5, 0, 0, 0, 6, 3, 2],
              [0, 0, 3, 6, 9, 7, 1, 0, 0],
              [6, 8, 0, 0, 0, 2, 7, 0, 0],
              [9, 1, 4, 8, 3, 5, 0, 7, 6],
              [0, 3, 0, 7, 0, 1, 4, 9, 5],
              [5, 6, 7, 4, 2, 9, 0, 1, 3]]

    def custom_input():
        for i in range(9):
            for j in range(9):
                sudoku[i][j] = int(input(f"enter value of {i+1} row and {j+1} column : "))

    def print_board(sudoku):
        for i in range(9):
            if i % 3 == 0 and i != 0:
                print("- - - - - - - - - - - -")
            for j in range(9):
                if j % 3 == 0 and j != 0:
                    print("|", end=" ")
                if j == 8:
                    print(sudoku[i][j])
                else:
                    print(str(sudoku[i][j]) + " ", end="")

    def find_empty(sudoku):
        empty = []
        for i in range(9):
            for j in range(9):
                if sudoku[i][j] == 0:
                    return (i, j)
        return None

    def is_valid(sudoku, row, col, num):
        for i in range(9):
            if sudoku[row][i] == num:
                return False
        for i in range(9):
            if sudoku[i][col] == num:
                return False
        start_row = row - row % 3
        start_col = col - col % 3
        for i in range(3):
            for j in range(3):
                if sudoku[i + start_row][j + start_col] == num:
                    return False
        return True

    def solve(sudoku):
        find = find_empty(sudoku)
        if not find:
            return True
        else:
            row, col = find

        for i in range(1, 10):
            if is_valid(sudoku, row, col, i):
                sudoku[row][col] = i

                if solve(sudoku):
                    return True

                sudoku[row][col] = 0
        return False
    
    n = int(input("if you want to enter elements of sudoku press 1 , is you want to solve prior mentioned sudoku press any key \n"))
    if n == 1:
        custom_input()
    else:
        pass
    speakandprint("Sudoku before solving:")
    print_board(sudoku)
    # empty = find_empty(sudoku)
    # print(empty)
    solve(sudoku)
    print("\n")
    speakandprint("Sudoku after solving:")
    print_board(sudoku)

def main():
    speakandprint("enter your name : \n")
    name = input()
    bot_mail.making_message(name)
    # time.sleep(5)
    # os.system(f"python bot_mail.py {name}")
    # os.environ["USER_NAME"] = name
    if db.check_name(name):
        check = 0
        while check == 0:
            speakandprint("Enter your password \nEnter 1 if you forgot your password and want to reset it\nEnter 2 if you want to get your password on whatsapp")
            password_input = input()
            if password_input == '1':
                speakandprint("Enter your number to reset your password")
                number = input()
                number = "+91" + number
                if db.check_ph_no(number, name):
                    bot_whatsapp.send_message(number, name)
                    if bot_keys.otp_verification(bot_whatsapp.otp, int(input("enter the otp : \n"))):
                        speakandprint("Your number is verified")
                    else:
                        speakandprint("Your number is not verified")
                        exit()
                    bot_game.change_password(name)
                else:
                    speakandprint("Your number is not registered")
                    exit()
            elif password_input == '2':
                bot_game.send_password_via_whatsapp(name)
            else:
                if db.check_password(name, password_input):
                    check = 1 
                    speakandprint("You are logged in")
                else:
                    speakandprint("Incorrect password")
                    exit()

    else:
        speakandprint("enter your email : \n")
        email = input()
        bot_game.verify_email(email)
        speakandprint("enter your phone number for verification : \n")
        ph_no = input()
        ph_no = "+91" + ph_no
        bot_game.verify_number(ph_no, name)
        db.insert_data(email, name, ph_no)
        bot_game.change_password(name)
    speakandprint(f"welcome {name} to the world of games.")
    # print("Your name is : ", name)
    # print("Your email is : ", db.check_email(name)[0][0])
    email = db.check_email(name)[0][0]
    bot_mail.send_email(bot_mail.subject_logged_in, email, bot_mail.html_loged_in)
    print("------------------------------------")
    db.print_data(name)
    print("------------------------------------")
    ph_no = db.get_ph_no(name)[0][0]
    bot_whatsapp.send_message_loged_in(ph_no, name)
    speakandprint("We have many games for you to play")
    speakandprint("choose the game you want to play")
    choice = 0
    while True:
        speakandprint("1. Quiz Game \n2. Rock Paper Scissors \n3. Tic Tac Toe \n4. Snake Water Gun \n5. sudoku solver \n6. VIEW PROFILE \n7. setting \n8. EXIT ")
        choice = input()
        speakandprint(f"You choice is : {choice}")
        if choice in ['1', '2', '3', '4', '5']:
            print("Entry fees of any game will be \033[38;5;214m100RS\033[0m,\nIf you win your account will be credited with \033[32m500RS\033[0m")
            speak("Entry fees of any game will be 100RS, If you win your account will be credited with 500RS")
        if choice == '1':
            db.entry_fees(name)
            speakandprint("enter number of attempts : \n")
            attempt = int(input())
            quiz(name, attempt)
        elif choice == '2':
            db.entry_fees(name)
            speakandprint("enter number of attempts : \n")
            attempt = int(input())
            rockpaperscissors(name, attempt)
        elif choice == '3':
            db.entry_fees(name)
            speakandprint("Do you want to play with computer or with another player")
            choice_in = input()
            if choice_in == 'computer':
                tic_tac_toe_computer(name)
            else:
                speakandprint("enter the name of player 2 : ")
                player2 = input()
                if db.check_name(player2):
                    pass
                else:
                    speakandprint("enter your email : \n")
                    email = input()
                    speakandprint("enter your phone number with your country code\n")
                    ph_no_2 = input()
                    ph_no_2 = "+91" + ph_no_2
                    bot_game.verify_email(email)
                    bot_game.verify_number(ph_no_2, player2)
                    db.insert_data(email, player2, ph_no_2)
                db.entry_fees(player2)
                tic_tac_toe_person(name, player2)
        elif choice == '4':
            db.entry_fees(name)
            speakandprint("enter number of attempts : \n")
            attempt = int(input())
            SnakeWaterGun(name, attempt)
        elif choice == '5':
            db.entry_fees(name)
            speakandprint("Welcome to sudoku solver")
            sudoku()
        elif choice == '6':
            speakandprint("If you want to send your profile details at your whatsapp number press 1, if no press any key.")
            n = input()
            db.print_data(name, n)
        elif choice == '7':
            speakandprint("1. Change Password \n2. Change Email \n3. Change Phone Number \n4. exit")
            choice_setting = input()
            if choice_setting == '1':
                speakandprint("Enter your old password : \n")
                old_password = input()
                if db.check_password(name, old_password):
                    bot_game.change_password(name)
                else:
                    speakandprint("Incorrect password")
            elif choice_setting == '2':
                speakandprint("Enter your new email : \n")
                new_email = input()
                bot_game.verify_email(new_email)
                db.change_email(new_email, name)
                speakandprint("Email changed successfully")
            elif choice_setting == '3':
                speakandprint("Enter your new phone number : \n")
                new_ph_no = input()
                new_ph_no = "+91" + new_ph_no
                bot_game.verify_number(new_ph_no, name)
                db.change_ph_no(new_ph_no, name)
                speakandprint("Phone number changed successfully")
            elif choice_setting == '4':
                bot_game.send_password_via_whatsapp(name)
            elif choice_setting == '5':
                speakandprint("Thank you for playing. Have a great day")
                exit()
            else:
                speakandprint("Enter the correct choice")
        elif choice == '8':
            speakandprint("Thank you for playing. Have a great day")
            exit()
        else:
            speakandprint("Enter the correct choice")
            continue

if __name__ == "__main__":
    main()


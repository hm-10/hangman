import random
<<<<<<< HEAD
aaaalfdlajaaaa
=======
aaa
>>>>>>> 90abce39e0505329cb995b8cf71c4f6c4fd9899f
def hangman():
    wordlist = ["getwild","lemon","honey"]
    word = random.choice(wordlist)
    wrong = 0
    stages =["",
             "__________       ",
             "|        |       ",
             "|        |       ",
             "|        O       ",
             "|      / | \     ",
             "|       / \      ",
             "|                ",
             ]
    rletters = list(word)
    board = ["_"] * len(word)
    win = False
    print("ハングマンへようこそ！")

    while wrong < len(stages) - 1:
        #print("lenst:",len(stages)-1,"wrong:",wrong)
        print("\n")
        msg = "1文字を予想してね："
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = '$'
        else:
            wrong += 1
        print(" ".join(board))
        e = wrong + 1
        print("\n".join(stages[0:e]))
        if "_" not in board:
            print("あなたの勝ち！")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n".join(stages[0:wrong+1]))
        print("あなたの負け！正解は{}.".format(word))
hangman()

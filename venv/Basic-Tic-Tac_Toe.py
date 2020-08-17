def wincondition():
    straights = [elements[:3], elements[3:6], elements[6:], elements[0:9:3], elements[1:9:3], elements[2:9:3],
                 elements[0:9:4],
                 elements[2:7:2]]
    return straights

def showboard(elements):
    print('---------')
    print('|', ' '.join(elements[:3]), '|')
    print('|', ' '.join(elements[3:6]), '|')
    print('|', ' '.join(elements[6:]), '|')
    print('---------')


def checklogic(elements, straights):
    global winner
    if abs(elements.count('X') - elements.count('O')) > 1 or ('XXX' in straights and 'OOO' in straights):
        print('Impossible')
    elif 'XXX' in straights:
        print('X wins')
        winner = "X"
        return winner
    elif 'OOO' in straights:
        print('O wins')
        winner = "O"
        return winner
    # elif elements.count('_') > 0:
    # print('Game not finished')
    elif elements.count('_') == 0:
        print('Draw')
        winner = "Draw"
        return winner
    winner = ""
    return winner


def chk(elements):
    while True:
        move = input("Enter the coordinates: ")
        move_chk = move.replace(" ", "").isdigit()
        if move_chk != True:
            print("You should enter numbers!")
            continue
        x, y = move.split()
        if int(x) not in range(1, 4) or int(y) not in range(1, 4):
            print("Coordinates should be from 1 to 3!")
            continue
        index = (int(x) - 1) + (9 - (3 * int(y)))
        if elements[index] != "_":
            print("This cell is occupied! Choose another one!")
            continue
        break
    return index

def move(element, index, plays):
    global elements, play
    list_temp = list(elements)
    list_temp.pop(index)
    list_temp.insert(int(index), play[0])
    play.pop(0)
    elements = "".join(list_temp)
    showboard(elements)

elements = "_________"
play = ["X", "O", "X", "O", "X", "O", "X", "O", "X"]
winner = ""

while any(winner) == False:
    showboard(elements)
    index = chk(elements)
    move(elements, index, play)
    straights = wincondition()
    winner = checklogic(elements, straights)
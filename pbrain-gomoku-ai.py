#!/usr/bin/env python3
import sys
import ai

boardSize = 0
boardGame = None

def display(str):
    print(str)
    sys.stdout.flush()

def doStart(size, u1):
    global boardSize
    global boardGame

    boardSize = int(size)
    if (boardSize <= 0):
        display("invalid board size")
        return
    boardGame = [[0 for x in range(boardSize)] for y in range(boardSize)]
    display("OK")

def doTurn(pos, u1):
    global boardGame

    p2_X, p2_Y, *_ = pos.split(",")
    boardGame[int(p2_Y)][int(p2_X)] = 1000

    p1_X, p1_Y = ai.move(boardGame)
    boardGame[p1_Y][p1_X] = 1
    display(f"{p1_X},{p1_Y}")

def doBegin(u1, u2):
    global boardGame

    p1_X, p1_Y = ai.move(boardGame)
    boardGame[p1_Y][p1_X] = 1
    display(f"{p1_X},{p1_Y}")

def doBoard(u1, u2):
    global boardGame

    line = sys.stdin.readline().strip()
    while line != "DONE":
        p_X, p_Y, P, *_ = line.split(",")
        boardGame[int(p_Y)][int(p_X)] = 1000 if int(P) == 2 else int(P)
        line = sys.stdin.readline().strip()

    p1_X, p1_Y = ai.move(boardGame)
    boardGame[p1_Y][p1_X] = 1
    display(f"{p1_X},{p1_Y}")

def doInfo(a, b):
    pass

def doEnd(u1, u2):
    sys.exit(0)

def doAbout(u1, u2):
    display('name="Gomoku", version="1.0", author="auguste THOMANN patrick EIERMANN Clement MUTH", country="France"')

COMMANDS = {
    'START': doStart,
    'TURN': doTurn,
    'BEGIN': doBegin,
    'BOARD': doBoard,
    'INFO': doInfo,
    'END': doEnd,
    'ABOUT': doAbout
}

def main():
    while True:
        tab = sys.stdin.readline().strip().split(" ")
        cmd = tab[0] if len(tab) > 0 else 0
        arg1 = tab[1] if len(tab) > 1 else 0
        arg2 = tab[2] if len(tab) > 2 else 0
        if cmd in COMMANDS.keys():
            COMMANDS[cmd](arg1, arg2)
        else:
            display(f"UNKNOWN : unknown command \"{cmd}\"")

if __name__ == "__main__":
    main()
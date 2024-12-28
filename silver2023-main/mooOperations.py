#Moo Operations (Python-3.6.9)
#Akshat Garg (aksgarg)
#Submitted: Sun, Jan 29, 2023 15:53:06 EST
#Contest: USACO 2023 January Contest, Bronze


from math import *

def main():
    n = int(input())
    words = [input().strip("\n") for j in range(n)]
    moves = [0 for j in range(n)]
    for j in range(n):
        if len(words[j])<3:
            moves[j] = -1 
        elif 'O' not in words[j][1:-1]:
            moves[j] = -1   
        else:
            move = []
            for k in range(len(words[j][1:-1])):
                if words[j][k+1] == 'O':
                    if words[j][k] == 'M' and words[j][k+2] == 'O':
                        move.append(len(words[j])-3)
                    elif words[j][k] == 'O' and words[j][k+2] == 'O':
                        move.append(len(words[j])-2)
                    elif words[j][k] == 'M' and words[j][k+2] == 'M':
                        move.append(len(words[j])-2)
                    elif words[j][k] == 'O' and words[j][k+2] == 'M':
                        move.append(len(words[j])-1)
            moves[j] = min(move)
    for k in moves:
        print(k)

main()

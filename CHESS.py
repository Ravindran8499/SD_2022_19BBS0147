# -*- coding: utf-8 -*-
"""
Created on Sat Sep 10 18:16:39 2022

@author: Ravi P
"""


chessBoard  = [ ]
piecesDict = {}

aPieces = 5
bPieces = 5

for i in range(5):
    chessBoard.append( [0]*5 )




p1input = input("Player1 Input: ").split(",")
for i in range(5):
    chessBoard[4][i] = "A:" + p1input[i]
    piecesDict["A:" + p1input[i]] = [4,i]


p2input = input("Player2 Input: ").split(",")
for i in range(5):
    chessBoard[0][i] = "B:" + p2input[i]
    piecesDict["B:" + p2input[i]] = [0,i]




turn = 0


while aPieces>0 and bPieces>0:
    if turn == 0:
        p1Move = input("Player A's Move").split(":")
        aPosition = piecesDict[ "A:" +  p1Move[0]]
        if p1Move[1] == "F" and aPosition[0] - 1 >= 0 and aPosition[0] - 1 <= 4:
            if chessBoard[aPosition[0]-1][aPosition[1]]!=0 and chessBoard[aPosition[0]-1][aPosition[1]].split(":")[0] == "A":
                pass
            else:
                if chessBoard[aPosition[0]-1][aPosition[1]]!=0 and chessBoard[aPosition[0]-1][aPosition[1]].split(":")[0] == "B":
                    del piecesDict[chessBoard[aPosition[0]-1][aPosition[1]]]
                    bPieces-=1
                chessBoard[aPosition[0] -1 ][aPosition[1]] = chessBoard[aPosition[0]][aPosition[1]] 
                chessBoard[aPosition[0]][aPosition[1]] = 0
                piecesDict[ "A:" +  p1Move[0]] = [aPosition[0] -1 , aPosition[1]]


        elif p1Move[1] == "B" and aPosition[0] + 1 >= 0 and aPosition[0] + 1 <= 4:
            if chessBoard[aPosition[0] + 1][aPosition[1]]!=0 and chessBoard[aPosition[0]+1][aPosition[1]].split(":")[0] == "A":
                pass
            else:
                if chessBoard[aPosition[0] + 1][aPosition[1]]!=0 and chessBoard[aPosition[0]-1][aPosition[1]].split(":")[0] == "B":
                    del piecesDict[chessBoard[aPosition[0] + 1][aPosition[1]]]
                    bPieces-=1
                chessBoard[aPosition[0] + 1 ][aPosition[1]] = chessBoard[aPosition[0]][aPosition[1]] 
                chessBoard[aPosition[0]][aPosition[1]] = 0
                piecesDict[ "A:" +  p1Move[0]] = [aPosition[0] + 1 , aPosition[1]]


        elif p1Move[1] == "L" and aPosition[1]-1>=0 and aPosition[1]-1<=4:
            if chessBoard[aPosition[0]][aPosition[1]-1]!=0 and chessBoard[aPosition[0]][aPosition[1]-1].split(":")[0] == "A":
                pass
            else:
                if chessBoard[aPosition[0]][aPosition[1]-1]!=0 and chessBoard[aPosition[0]][aPosition[1]-1].split(":")[0] == "B":
                    del piecesDict[chessBoard[aPosition[0]][aPosition[1]-1]]
                    bPieces-=1
                chessBoard[aPosition[0] ][aPosition[1]-1] = chessBoard[aPosition[0]][aPosition[1]] 
                chessBoard[aPosition[0]][aPosition[1]] = 0
                piecesDict[ "A:" +  p1Move[0]] = [aPosition[0], aPosition[1]-1]
        
        elif p1Move[1] == "R" and aPosition[1] + 1>=0 and aPosition[1]+1<=4:
            if chessBoard[aPosition[0]][aPosition[1]+1]!=0 and chessBoard[aPosition[0]][aPosition[1]+1 ].split(":")[0] == "A":
                pass
            else:
                if chessBoard[aPosition[0]][aPosition[1] + 1]!=0 and chessBoard[aPosition[0]][aPosition[1]+1].split(":")[0] == "B":
                    del piecesDict[chessBoard[aPosition[0]][aPosition[1]+1]]
                    bPieces-=1
                chessBoard[aPosition[0] ][aPosition[1]+1] = chessBoard[aPosition[0]][aPosition[1]] 
                chessBoard[aPosition[0]][aPosition[1]] = 0
                piecesDict[ "A:" +  p1Move[0]] = [aPosition[0], aPosition[1]+1]
        

        print(chessBoard)
        turn  = 1
    else:
        p2Move = input("Player B's Move").split(":")
        bPosition = piecesDict[ "B:" +  p2Move[0]]
        if p2Move[1] == "F" and bPosition[0] + 1 >= 0 and bPosition[0] + 1 <= 4:
            if chessBoard[bPosition[0]+1][bPosition[1]]!=0 and chessBoard[bPosition[0]+1][bPosition[1]].split(":")[0] == "B":
                pass
            else:
                if chessBoard[bPosition[0]+1][bPosition[1]]!=0 and chessBoard[bPosition[0]+1][bPosition[1]].split(":")[0] == "A":
                    del piecesDict[chessBoard[bPosition[0]+1][bPosition[1]]]
                    aPieces=-1
                chessBoard[bPosition[0] + 1 ][bPosition[1]] = chessBoard[bPosition[0]][bPosition[1]] 
                chessBoard[bPosition[0]][bPosition[1]] = 0
                piecesDict[ "B:" +  p2Move[0]] = [bPosition[0] + 1 , bPosition[1]]

        elif p2Move[1] == "B" and bPosition[0] - 1 >= 0 and bPosition[0] - 1 <= 4:
            if chessBoard[bPosition[0]+1][bPosition[1]]!=0 and chessBoard[bPosition[0]+1][bPosition[1]].split(":")[0] == "B":
                pass
            else:
                if chessBoard[bPosition[0] - 1][bPosition[1]]!=0 and chessBoard[bPosition[0] - 1][bPosition[1]].split(":")[0] == "A":
                    del piecesDict[chessBoard[bPosition[0] - 1][bPosition[1]]]
                    aPieces=-1
                chessBoard[bPosition[0] - 1 ][bPosition[1]] = chessBoard[bPosition[0]][bPosition[1]] 
                chessBoard[bPosition[0]][bPosition[1]] = 0
                piecesDict[ "B:" +  p2Move[0]] = [bPosition[0] - 1 , bPosition[1]]

        elif p2Move[1] == "L" and bPosition[1] + 1 >= 0 and bPosition[0] + 1 <= 4:
            if chessBoard[bPosition[0]][bPosition[1]+1]!=0 and chessBoard[bPosition[0]][bPosition[1]+1].split(":")[0] == "B":
                pass
            else:
                if chessBoard[bPosition[0]][bPosition[1] +1 ]!=0 and chessBoard[bPosition[0] ][bPosition[1] + 1].split(":")[0] == "A":
                    del piecesDict[chessBoard[bPosition[0]][bPosition[1] + 1]]
                    aPieces=-1
                chessBoard[bPosition[0] ][bPosition[1] +1 ] = chessBoard[bPosition[0]][bPosition[1]] 
                chessBoard[bPosition[0]][bPosition[1]] = 0
                piecesDict[ "B:" +  p2Move[0]] = [bPosition[0], bPosition[1]+1]

        elif p2Move[1] == "R" and bPosition[1] - 1 >= 0 and bPosition[0] - 1 <= 4:
            if chessBoard[bPosition[0]][bPosition[1]-1]!=0 and chessBoard[bPosition[0]][bPosition[1]-1].split(":")[0] == "B":
                pass
            else:
                if chessBoard[bPosition[0]][bPosition[1] -1 ]!=0 and chessBoard[bPosition[0] ][bPosition[1] - 1].split(":")[0] == "A":
                    del piecesDict[chessBoard[bPosition[0]][bPosition[1] + 1]]
                    aPieces=-1
                chessBoard[bPosition[0] ][bPosition[1] -1 ] = chessBoard[bPosition[0]][bPosition[1]] 
                chessBoard[bPosition[0]][bPosition[1]] = 0
                piecesDict[ "B:" +  p2Move[0]] = [bPosition[0], bPosition[1]-1]
        print(chessBoard)


        turn = 0


if aPieces==0:
    print("B is the Winner")
else:
    print("A is the Winner")

            
            
            
    
        
        
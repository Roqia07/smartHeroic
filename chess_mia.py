#importing libraries
import pygame as p

class GameState:
    # Making the board
    def __init__(self):
        self.board = [
            ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
            ["bP", "bP", "bP", "bP", "bP", "bP", "bP", "bP"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["wP", "wP", "wP", "wP", "wP", "wP", "wP", "wP"],
            ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"]
        ]
        self.whitemoves = True
        self.movelog = []
    def makeMove(self,move):
        self.board[move.startRow][move.startCol]="--"
        self.board[move.endRow][move.endCol]=move.pieceMoved
        self.movelog.append(move)
        self.whitemoves= not self.whitemoves #swap players
    
    def getValidMoves(self):
        return self.getAllPossibleMoves()
    
    def getAllPossibleMoves(self):
        moves=[]
        for r in range(len(self.board)):
            for c in range(len(self.board[r])):  # nu,ber of rows in row
                turn=self.board[r][c][0]
                if (turn=="w" and self.whitemoves) or (turn=="b"and not self.whitemoves):
                    piece=self.board[r][c][1]
                    if piece=='p':
                        self.getPawnMoves(r,c,moves)
                        
                    elif piece=='R':
                        self.getRookMoves(r,c,moves)
                    

    def getPawnMoves(self,r,c,moves):
        if self.whitemoves:
            if self.board[r-1][c]=="--":
                moves.append(Move((r,c),(r-1,c),self.board))
                if r==6 and self.board[r-2][c]=="--":
                    moves.append(Move((r,c,),(r-1,c),self.board))
        


    

class Move():
    #map keys to values
    ranksToRows={"1":7,"2":6 , "3":5,"4":4,
                 "5":3,"6":2,"7":1,"8":0}
    rowsToRanks={v:k for k, v in ranksToRows.items()}
    filestoCols={"a":0,"b":1,"c":2,"d":3,
                 "e":4,"f":5,"g":6,"h":7}
    colsToFiles={v:k for k, v in filestoCols.items()}
    
    def __init__(self,startSq,endSq,board):
        self.startRow=startSq[0]
        self.startCol=startSq[1]
        self.endRow=endSq[0]
        self.endCol=endSq[1]
        self.pieceMoved=board[self.startRow][self.startCol]
        self.pieceCaptured=board[self.endRow][self.endCol]
    
    def getchessNotation(self):
        return self.getRankFile(self.startRow,self.startCol)+self.getRankFile(self.endRow,self.endCol)

    def getRankFile(self,r,c):
        return self.colsToFiles[c]+self.rowsToRanks[r]

    


# Main
p.init()
width = height = 400
Dimension = 8
Square_size = height // Dimension
Fps = 15
Images = {}

# Images dict
def LoadImages():
    pieces = ["wB", "wK", "wN", "wP", "wQ", "wR", "bK", "bB", "bN", "bQ", "bR", "bP"]
    for piece in pieces:
        Images[piece] = p.transform.scale(p.image.load( piece + ".png"), (Square_size,Square_size))

def drawGameState(screen, gs):
    drawBoard(screen)  # Draw squares
    drawPieces(screen, gs.board)  # Draw pieces on squares

def drawBoard(screen):
    colors = [p.Color("white"), p.Color("grey")]
    for i in range(Dimension):  # Representing the row
        for j in range(Dimension):  # Representing the column
            color = colors[(i + j) % 2]
            p.draw.rect(screen, color, p.Rect(j * Square_size, i * Square_size, Square_size, Square_size))

def drawPieces(screen, board):
    for i in range(Dimension):  # Representing the row
        for j in range(Dimension):  # Representing the column
            piece = board[i][j]
            if piece != "--":
                screen.blit(Images[piece], p.Rect(j * Square_size, i * Square_size, Square_size, Square_size))



# User input 
def main():
    screen = p.display.set_mode((width, height))
    clock = p.time.Clock()
    gs = GameState()
    LoadImages()
    running = True
    sqSelected=() #no square selected tuple(row,col)
    playerClicks=[]  #keepin track od player clicks, 2 tuples: selected square and the square where the part goes
    while running:
        for n in p.event.get():
            if n.type == p.QUIT:
                running = False
            elif n.type==p.MOUSEBUTTONDOWN:
                location=p.mouse.get_pos()  #x,y mouse position
                col=location[0]//Square_size
                row=location[1]//Square_size
                if sqSelected==(row,col):   # if the same square is clicked on twics , deselect it
                    sqSelected=()   #deslelcting 
                    playerClicks=[]
                else:
                    sqSelected=(row,col)
                    playerClicks.append(sqSelected)
                if len(playerClicks)==2:    #after 2 clicks(selecting the piece and movinf it)
                    move=Move(playerClicks[0],playerClicks[1],gs.board)
                    print(move.getchessNotation())
                    gs.makeMove(move)
                    sqSelected=()
                    playerClicks=[]


                sqSelected=(row,col)
        drawGameState(screen, gs)
        clock.tick(Fps)
        p.display.flip()
    p.quit()

main()








    


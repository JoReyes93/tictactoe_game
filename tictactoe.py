##TIC TAC TOC GAME V.21.10.8 JOSEPH REYES
def main():
    lista = [
        ["7","8","9"],
        ["4","5","6"],
        ["1","2","3"]
        ]

    i = 0
    p1_count = 0
    p2_count = 0

    def score():
        print("\nSCORE\n" +
              f"Player 1 = {p1_count}\n" +
              f"Player 2 = {p2_count}\n")

    def grafica():
        print(f"_{lista[0][0]}_|_{lista[0][1]}_|_{lista[0][2]}_\n" +
              f"_{lista[1][0]}_|_{lista[1][1]}_|_{lista[1][2]}_\n" +
              f" {lista[2][0]} | {lista[2][1]} | {lista[2][2]} ")

    def winner():
        global i
        
        if lista[0][0] == lista[0][1] and lista[0][1] == lista[0][2]:
            win = True
        elif lista[1][0] == lista[1][1] and lista[1][1] == lista[1][2]:
            win = True
        elif lista[2][0] == lista[2][1] and lista[2][1] == lista[2][2]:
            win = True
        elif lista[0][0] == lista[1][0] and lista[1][0] == lista[2][0]:
            win = True
        elif lista[0][1] == lista[1][1] and lista[1][1] == lista[2][1]:
            win = True
        elif lista[0][2] == lista[1][2] and lista[1][2] == lista[2][2]:
            win = True
        elif lista[0][0] == lista[1][1] and lista[1][1] == lista[2][2]:
            win = True
        elif lista[0][2] == lista[1][1] and lista[1][1] == lista[2][0]:
            win = True
        else:
            win = False

        return win

    score()
    grafica()

    #loop counter to complete the chart
    while (i < 9):

        if (i+1)%2 == 0:
            player = 2
            letter = "O"
        else:
            player = 1
            letter = "X"
            
        value = input(f"Player {player} turn ({letter}): ")

        for f in range(0,3):
            for c in range(0,3):

                #PLAYER 1 VALIDATION 
                if value == lista[f][c] and player == 1 and lista[f][c] != "X":
                    lista[f][c] = "X"
                    i += 1

                #PLAYER 2 VALIDATION    
                if value == lista[f][c] and player == 2 and lista[f][c] != "O":
                    lista[f][c] = "O"
                    i += 1

        grafica()
        print("\n"*10)
        
        if winner() == True:
            i = 9
            if player == 1:
                p1_count += 1
            else:
                p2_count += 1
            print(f"Player {player} Wins!!!")
        elif winner() == False and i == 9:
            print("Drawn:0!")

    score()

if __name__=="__main__":
    main()

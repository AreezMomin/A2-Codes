
#Question1_J2022



# part 1(a)
class HighScore:
    def __init__ (self):
        self.PlayerName = ""
        self.PlayerScore = 0

HighScoreArray = [ HighScore() for i in range (11) ]
NewArray = [ HighScore() for i in range (10)]


# part 1(b)
def ReadHighScores ():
    global HighScoreArray
    ScoreFile = open("HighScore.txt" , "rt")

    Name = ScoreFile.readline()

    for i in range (10):
        Score = ScoreFile.readline()
        Name = Name.strip()
        Score = Score.strip()

        HighScoreArray[i].PlayerName = Name
        HighScoreArray[i].PlayerScore = str(Score)

        Name = ScoreFile.readline()
    ScoreFile.close()


# part 1(c)
def OutputHighScores ():
    for i in range (10):
        Name = HighScoreArray[i].PlayerName
        Score = HighScoreArray[i].PlayerScore
        print (Name , Score)
    print ('\n')

# part 1(eii)
def ishighScore(InputName , InputScore):
    HighScoreArray[10].PlayerName = InputName
    HighScoreArray[10].PlayerScore = InputScore

    temp = ""
    temp2 = ""
    for i in range (11):
        for j in range (10):
            if int(HighScoreArray[j].PlayerScore) < int(HighScoreArray [i].PlayerScore):
                temp = HighScoreArray[j].PlayerScore
                temp2 = HighScoreArray [j].PlayerName
                HighScoreArray[j].PlayerName = HighScoreArray [i].PlayerName
                HighScoreArray [i].PlayerName = temp2
                HighScoreArray[j].PlayerScore = HighScoreArray [i].PlayerScore
                HighScoreArray [i].PlayerScore = temp


    HighScoreArray[10].PlayerName = ""
    HighScoreArray[10].PlayerScore = ""



# part f
def WriteTopTen():
    NewFile = open ("NewHighScore.txt" , "wt")
    for i in range (10):
        Name = HighScoreArray[i].PlayerName
        Score = HighScoreArray[i].PlayerScore

        NewFile.write(Name + '\n')
        NewFile.write(str(Score) + '\n')

    NewFile.close()


#main_program
# part 1(di) in main program
# part 1(ei) in main program

ReadHighScores()
OutputHighScores()
InputName = input("Enter a 3 letter player name: ")
while len(InputName) != 3:
    InputName = input("Enter a 3 letter player name: ")
InputScore = int(input("Enter a player score from 0 to 100,000 inclusive: "))
while InputScore < 0 and InputScore > 100000:
    InputScore = int(input("Enter a player score from 0 to 100,000 inclusive: "))
ishighScore (InputName, InputScore )
OutputHighScores()
WriteTopTen()









































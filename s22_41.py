
"""
#Question1_J2022
class HighScore:
    def __init__ (self):
        self.PlayerName = ""
        self.PlayerScore = 0

HighScoreArray = [ HighScore() for i in range (11) ]
NewArray = [ HighScore() for i in range (10)]


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



def OutputHighScores ():
    for i in range (10):
        Name = HighScoreArray[i].PlayerName
        Score = HighScoreArray[i].PlayerScore
        print (Name , Score)
    print ('\n')


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


def WriteTopTen():
    NewFile = open ("NewHighScore.txt" , "wt")
    for i in range (10):
        Name = HighScoreArray[i].PlayerName
        Score = HighScoreArray[i].PlayerScore

        NewFile.write(Name + '\n')
        NewFile.write(str(Score) + '\n')

    NewFile.close()


#main_program


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

#Question2_J2022

class Balloon:
    def __init__(self, PColour, PDefenceItem):
        self.__Health = 100
        self.__Colour = PColour
        self.__DefenceItem = PDefenceItem

    def GetDefenceItem(self):
        return self.__DefenceItem

    def ChangeHealth(self,  PHealth):
        self.__Health = self.__Health + PHealth

    def CheckHealth(self):
        if self.__Health <= 0:
            return True
        else:
            return False

def Defend(MyBalloon):
    OppStrength = int(input("Enter the opponents strength: "))
    MyBalloon.ChangeHealth(-OppStrength)
    print ("You defended with a", str(MyBalloon.GetDefenceItem()))
    result = MyBalloon.CheckHealth()
    if result == False:
        print("Defence was succcessfull")
    else:
        print("Denfence failed")

    return MyBalloon


#main Program
PDefenceItem = input("Enter the defence item: ")
PColour = input("Enter a colour: ")
Balloon1 = Balloon(PColour, PDefenceItem)
Defend(Balloon1)



#Question1_J2022

#HeadPointer AS INTERGER
#TailPointer AS INTERGER
#NumberItems AS INTERGER
#QueueArray AS ARRAY[0:9]

HeadPointer = 0
TailPointer = 0
NumberItems = 0
QueueArray  = [ "" for i in range(10)]

def Enqueue (DataToAdd):
    global QueueArray, HeadPointer, TailPointer, NumberItems

    if NumberItems == 10:
        return False
    QueueArray[TailPointer] = DataToAdd
    if TailPointer >= 9:
        TailPointer = 0
    else:
        TailPointer += 1
    NumberItems += 1
    return True


def Dequeue ():
    global QueueArray, HeadPointer, TailPointer, NumberItems

    if NumberItems == 0:
        return False

    Value = QueueArray[HeadPointer]
    NumberItems -= 1

    if HeadPointer >= 9:
        HeadPointer = 0
    else:
        HeadPointer +=1

    return (Value)

#main program
added = True
while added:
    Value = input("Enter a value to add: ")
    added = Enqueue(Value)
    if added :
        print("Value added successfully")
    else:
        print("Queue full")
Value = Dequeue()
print(Value, "removed")
Value = Dequeue()
print(Value, "removed")

"""











































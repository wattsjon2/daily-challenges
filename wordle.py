from operator import le
from typing import Counter


class wordle():
    def __init__ (self, givenWord = "worde", counter = 0):
        self.givenWord = givenWord
        self.counter = counter


    def givenWordSet(self):
        return set(x for x in self.givenWord)

    def givenWordEnum(self):
        return dict((j,i) for j,i in enumerate(self.givenWord))

    def givenWordCount(self):
        givenCount = {}
        for letter in self.givenWord:
            if letter in givenCount:
                givenCount[letter] += 1
            else:
                givenCount[letter] = 1
        return givenCount

    def guessWordInput(self):
        guessWord = input("Please enter a 5 letter word ").lower()
        if len(guessWord) != 5:
            return "That is not a 5 letter word"
        elif guessWord.isalpha() != True:
            return "Please enter only letters"
        else:
            return self.wordCompare(guessWord)
            

    def wordCompare(self, guessWord):
        givenDict = self.givenWordEnum()
        givenCount = self.givenWordCount()
        responesArr = []

        guessWordCount = []
        guessWordCountDict = {}
        responseYGCount = {}

        
        for letter in guessWord:
            if letter in guessWordCountDict:
                guessWordCountDict[letter] += 1
                guessWordCount.append([letter, guessWordCountDict[letter]])
            else:
                guessWordCount.append([letter, 1])
                guessWordCountDict[letter] = 1


        for i in range(len(guessWord)):
            if guessWord[i] in givenCount:
                if givenDict.get(i) == guessWord[i]:
                    responesArr.append([guessWord[i], "Green"])
                    if guessWord[i] in responseYGCount:
                        responseYGCount[guessWord[i]] += 1
                    else:
                        responseYGCount[guessWord[i]] = 1
                else:
                    responesArr.append([guessWord[i], "Yellow"])
                    if guessWord[i] in responseYGCount:
                        responseYGCount[guessWord[i]] += 1
                    else:
                        responseYGCount[guessWord[i]] = 1
            else:
                responesArr.append([guessWord[i], "Red"]) 


        for i in range(len(guessWord)):
            if guessWord[i] not in givenCount:
                pass
            elif guessWordCountDict.get(guessWord[i]) > givenCount.get(guessWord[i]):
                
                greenLetters = 0
                yellowLetters = 0
                letterFind = guessWord[i]
                modifyArr = []
                while responseYGCount.get(letterFind) > givenCount.get(letterFind):
                    counter = 0
                    
                    if greenLetters == 0 and yellowLetters == 0:
                        
                        for j in range(len(guessWord)):
                            
                            if guessWord[j] == letterFind:
                                
                                if responesArr[j][1] == "Yellow":
                                    yellowLetters += 1
                                    modifyArr.append(j)
                                    
                                elif responesArr[j][1] == "Green":
                                    greenLetters += 1
                                    
                    else:
                        
                        for k in range(len(modifyArr)):
                            
                            if counter + greenLetters < givenCount.get(letterFind):
                                counter += 1
                            elif counter + greenLetters >= givenCount.get(letterFind):
                                
                                responesArr[modifyArr[k]][1] = "Red" 
                                responseYGCount[letterFind] -= 1
                                counter += 1
                             
                    
            
        
        
        self.counter += 1

        if guessWord == self.givenWord:
            print("You Win!")
            return False

        elif self.counter < 6:
            print(f'You have {6 - self.counter} tries remaining')
            return (responesArr)
        else:
            print("You are out of tries")
            print(f"The answer is: {self.givenWord}")
            return False




def run():

    test = wordle()
    response = True
    
    while response != False:
        response = test.guessWordInput()
        if response != False:
            print(response)

run()
            
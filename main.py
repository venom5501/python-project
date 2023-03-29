import json
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
  

def delete():
    print("Enter the word you wanna delete: \n")
    wordToDelete = input()
    myDictionary = open("./dictionary.txt", "r")
    allWords = myDictionary.readlines()
    flag = True
    for x in allWords:
        if f"{wordToDelete}:" in x:
            allWords.remove(x)
            dataFile = open('./dictionary.txt',"w")
            dataFile.writelines(allWords)
            dataFile.close()
            print(f"{bcolors.WARNING}Your given word deleted successfully.")
            flag = False
            myDictionary.close()
    if flag:
        myDictionary.close()
        print("The word you wanna delete is not found in the dictionary.")
 



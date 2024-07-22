
def read_book(pathToBook):
    with open(pathToBook) as f: 
        content = f.read()
        return content

def count_words(stringToCount):
    words = stringToCount.split()
    c = 0
    for i in words: 
        c += 1
    return c 

def count_letters(words):
    letters_counted = {}
    for l in words:
        le = l.lower()
        if le in letters_counted:
            letters_counted[le] += 1
        elif le.isalpha(): 
            letters_counted[le] = 1
    
    return letters_counted

def makeList(dict):
    dictList = []
    tempDict = {}
    for letter in dict:
        tempDict[letter] = dict[letter]
        dictList.append(tempDict) 
    print(dictList)



def main():
    pathToBook = "books/frankenstein.txt"
    frankenstein = read_book(pathToBook)
    count = count_words(frankenstein)
    letters = count_letters(frankenstein)
    makeList(letters)

main()

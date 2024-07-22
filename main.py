
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
    letterList = []
    tempDict = {}
    for letter in dict:
        tempDict["letter"] = letter
        tempDict["num"] = dict[letter]
        letterList.append(tempDict)
        tempDict = {}
    return letterList

def sort_on(dict):
    return dict["num"]

def rev_list(list):
    sort_list = makeList(list)
    sort_list.sort(reverse=True, key=sort_on)
    return sort_list
    

def main():
    pathToBook = "books/frankenstein.txt"
    frankenstein = read_book(pathToBook)
    count = count_words(frankenstein)
    letters = count_letters(frankenstein)
    listOfLetters = rev_list(letters)
    print(f"--- Begin report of book {pathToBook} ---")
    print(f"{count} words in doc")
    for l in listOfLetters:
        print(f"The {l['letter']} was found {l['num']} times!")
    print("--- EOF ---")


    

main()

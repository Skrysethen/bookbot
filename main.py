
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

def main():
    pathToBook = "books/frankenstein.txt"
    frankenstein = read_book(pathToBook)
    count = count_words(frankenstein)
    print(count)
    

main()

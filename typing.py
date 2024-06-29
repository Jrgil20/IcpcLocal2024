neighbors = [
    ["a","b","c","d","e","f","g","h","i"],
    ["j","k","l","m","n","o","p","q","r"],
    ["s","t","u","v","W","x","y","z"]
]

def isNeighbor(c1,c2):
    for letters1 in neighbors:
        if c1 in letters1:
            i=neighbors.index(letters1)
            j=letters1.index(c1)
            for letters2 in neighbors:
                m=neighbors.index(letters2)
                if m > 0 and m < len(neighbors):
                    for n in range(len(letters2)):
                        if n in range(0, j+1) and n<len(letters2):
                            if letters2[m][n]==c2:
                                return True
    return False

def isIdentical(word1,word2):
    if word1 in word2:
        return True
    return False

def isSimilar(word1,word2):
    if len(word1)==len(word2):
        for c1,c2 in zip(word1,word2):
            if isNeighbor(c1,c2):
                return True
    return False

def checkCases(word1,word2):
    if isIdentical(word1,word2):
        return 1
    elif isSimilar(word1,word2):
        return 2
    else:
        return 3

words = input().split(" ")
word1=words[0]
word2=words[1]
print(checkCases(word1,word2))
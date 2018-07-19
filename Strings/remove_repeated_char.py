"""
Strings Chpter Porblem 12
"""


def removeChar(word):
    i = 1
    while i < len(word):
        while i >=0 and i < len(word) and word[i] == word[i-1]  :
            word = word[:i-1] + word[i+1:]
            i -=1
             
        i +=1
    
    
    return word
            


if __name__ == "__main__":
#     word = "ABCCBCBA"
#     word = removeChar(word)
#     print(word)

    word = "ABCBCBAA"
    word = removeChar(word)
    print("word : %s"%word)
    word = "ABCBCBAABCBCBA"
    word = removeChar(word)
    print("word : %s"%word)
    

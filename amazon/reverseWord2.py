"""
For example,
Given s = "the sky is blue",
return "blue is sky the".

Could you do it in-place without allocating extra space?

"""


def reverseUtil(word, i, j):
    while i < j:
        word[i], word[j] = word[j], word[i]
        i +=1
        j -=1
    
    
    

def reverseWord(word):
    i = 0
    word = list(word)
    for j in xrange(1,len(word)):
        if word[j] == " ":
            reverseUtil(word, i, j-1)
            i = j + 1
    
    reverseUtil(word, i, len(word)-1)
    reverseUtil(word, 0, len(word)-1)
    word = "".join(word)
    return word


if __name__ == "__main__":
    word = "the sky is blue"
    print(reverseWord(word))
def strtok(string, sep = "."):
    curr = ""
    for i in xrange(len(string)):
        
        if string[i] != sep:
            #print(string[i])
            curr +=  string[i]
        else:
            yield curr
            curr = ""

    yield curr


name = "vishal singh jasrotia"
token  = strtok(name, " ")

for tok in token:
    print(tok)
    
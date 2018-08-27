

def justify(text = [], maxwidth = 0):
    res = []
    group = []
    
    curlen = 0
    spaces = []
    for word in text:
        if len(group) >= 1:
            total_length = curlen + len(word) + len(group)
        else:
            total_length = curlen
            
        if total_length <=  maxwidth:
            group.append(word)
            curlen +=  len(word)
        else :
            if len(group) > 1:
                spaces = [" "]*(len(group) - 1)
                 # remove last space
                rightspaces = maxwidth -  ( curlen + len(spaces))
                evenspaces = rightspaces/(len(spaces))
                remspaces = rightspaces%(len(spaces))
                
                idx = 0
                while idx  < len(spaces) and evenspaces > 0:
                    spaces[idx] += " "*evenspaces
                    idx +=1
                
                idx = 0
                while remspaces > 0:
                    spaces[idx] += " "
                    remspaces -=1
                    idx +=1
                    
                cur_line = group[0]
                group = group[1:]
                
                for space , wd in zip(spaces, group):
                     cur_line += space + wd 
            else:
                
                cur_line = group[0] + " "*(maxwidth -  len(group[0]))
                
            
            
            res.append(cur_line)
            curlen = 0
            spaces = []
            group = []
            
            group.append(word)
            curlen +=  len(word)
    
    
    
    spaces = [" "]*(len(group) - 1)
    cur_line = group[0]
    group = group[1:]
    for space , wd in zip(spaces, group):
        cur_line += space + wd 
    cur_line = cur_line + " "*(maxwidth - len(cur_line))
    res.append(cur_line)
    return res



if __name__ == "__main__":
    words = ["Science","is","what","we","understand","well","enough","to","explain",
         "to","a","computer.","Art","is","everything","else","we","do"]
    maxWidth = 20
    res = [
        "Science  is  what we",
        "understand      well",
        "enough to explain to",
        "a  computer.  Art is",
        "everything  else  we",
        "do                  "
        ]
    
    print(justify(words, maxWidth ) == res)
    
    words = ["What","must","be","acknowledgment","shall","be"]
    maxWidth = 16
    res = [
        "What   must   be",
        "acknowledgment  ",
        "shall be        "
        ]
    print(justify(words, maxWidth ) ==  res)
    
    words = ["This", "is", "an", "example", "of", "text", "justification."]
    maxWidth = 16
    res = [
        "This    is    an",
        "example  of text",
        "justification.  "
        ] 
    print(justify(words, maxWidth ))
    print(justify(words, maxWidth ) ==  res)



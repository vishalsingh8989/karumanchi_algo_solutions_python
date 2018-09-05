

def match(text, patt):
    if not patt:
        return not text
    
    
    first_match = bool(text) and patt[0] in {text[0], "."}
    
    if len(patt) >= 2 and patt[1] == "*":
        return self.match(text , patt[2:] ) or ( first_match and self.match(text[1:], patt ))
    else:
        return first_match and self.match(text[1:], patt[1:])
    
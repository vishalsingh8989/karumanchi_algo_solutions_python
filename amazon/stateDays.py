def cellCompete(states, days):
    # WRITE YOUR CODE HERE
    row = [0] + states + [0]
    
    print(row)
    for day in xrange(days):
        prev = row[0]
        for i in xrange(1, len(row)-1):
            next_prev = row[i]
            if prev == row[i+1]:
                row[i] = 0
            else:
                row[i] = 1
            prev = next_prev
    
        print(row)
    return list(row[1:-1])


if __name__ == "__main__":
    
    states = [1,1,1,0,1,1,1,1]
    print(cellCompete(states, 2))
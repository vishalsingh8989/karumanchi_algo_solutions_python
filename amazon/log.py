

from collections import defaultdict

def logparser(filename):




    fd = open(filename)
    
    lines = fd.readlines()
    
    data = defaultdict(int)
    
    for line in lines:
        line = line.split("- -")
        domain = line[0].strip()
        data[domain] += 1

    
    
    fin = open("output.txt", 'w')
    
    for key, val in data.iteritems():
        fin.write(key  + " " + str(val) + "\n")
    
    
    fin.close()
    
    
    
logparser("logfile.txt")
        
    
    
    
    
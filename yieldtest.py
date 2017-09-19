print("Hello")
def enum(lt, start=0):
    n = start
    for element in lt:
            yield n, element
            n = n  + 1



for idx, name in enum(["vishal" , "hello" , "ho"]):
    print(idx ,name)

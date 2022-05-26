def solution(s):
    right = 0 # all right going commanders
    salutes = 0 # total salutes
    
    # Traversing the path
    for char in s:
        if char == '>':
            right+=1
        if char == '<':
            salutes+= right*2
    
    return salutes
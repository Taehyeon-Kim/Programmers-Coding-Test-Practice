def solution(strings, n):    
    strings.sort()
    print(strings)
    return sorted(strings, key=lambda x:(x[n],x))
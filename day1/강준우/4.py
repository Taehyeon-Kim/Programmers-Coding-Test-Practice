'''
half=len(s)//2
홀수 -> return s[half]
짝수 -> return s[half-1:half+1]
'''

def solution(s):
    half = len(s)//2
    is_odd = len(s)%2
    
    if is_odd:
        return s[half]
    else:
        return s[half-1:half+1]
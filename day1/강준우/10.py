'''
    공백이면 그대로 +=
    유니코드 바꾸고 밀어서, 범위 벗어나면 -=26
    
'''
def process(code, n,start_code, end_code):
    if start_code<=code+n and code+n<=end_code:
        return chr(code+n)
    else:
        return chr(code+n-26)


def solution(s, n):
    code_A=ord('A'); code_Z=ord('Z'); code_a=ord('a'); code_z=ord('z')
    answer = ''
    
    for alph in s:
        if alph==' ':
            answer+=alph; continue
        
        code = ord(alph)
        if code_A<=code and code<=code_Z:
            answer+=process(code, n, code_A, code_Z)
        else:
            answer+=process(code, n, code_a, code_z)
    
    return answer
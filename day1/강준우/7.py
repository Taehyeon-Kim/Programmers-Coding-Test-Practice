def solution(s):
    answer = ''
    return ''.join(sorted(s, reverse=True))
    '''
    for alph in sorted(s, reverse=True):
        
        answer+=alph
    return answer
    '''
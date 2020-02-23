def solution(n):
    answer = ''
    for i in range(n//2):
        answer+='수박'
    if n%2:
        answer+='수'
    return answer
def solution(arr, divisor):
    answer = []
    for element in arr:
        if not element%divisor:
            answer.append(element)
    
    if not answer:
        answer.append(-1)
    return sorted(answer)
'''
    supoja1=[12345 12345 ...] 5씩 ㄱ
    supoja2=[21 23 24 25 21 23 24 25] 8씩 ㄱ
    supoja3=[33 11 22 44 55 33 11 22 44 55 ...] 10씩 ㄱ
    
    dap 길이에 따른 수포자 리스트 만들고 bf
'''
def get_score(supoja, answers):
    score=0
    for i in range(len(answers)):
        if supoja[i]==answers[i]:
            score+=1
    return score


def solution(answers):
    ans_n=len(answers)
    supoja1=[1,2,3,4,5]*(ans_n//5+1)
    supoja2=[2,1,2,3,2,4,2,5]*(ans_n//8+1)
    supoja3=[3,3,1,1,2,2,4,4,5,5]*(ans_n//10+1)
    
    score1=get_score(supoja1, answers)
    score2=get_score(supoja2, answers)
    score3=get_score(supoja3, answers)
    
    max_score=max(score1, score2, score3)
    answer = []
    if max_score==score1:
        answer.append(1)
    if max_score==score2:
        answer.append(2)
    if max_score==score3:
        answer.append(3)
    
    return answer
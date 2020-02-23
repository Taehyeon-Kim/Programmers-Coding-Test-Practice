def solution(participant, completion):
    hi={c:p for c in completion for p in participant}
    print(hi)
    return 0
def slow_solution(participant, completion):
    for wanjuja in completion:
        participant[participant.index(wanjuja)]=' '
    #return participant[0]

def strange_solution(participant, completion):
    p=set(participant)
    c=set(completion)
    print(p.difference(c))
    return 0
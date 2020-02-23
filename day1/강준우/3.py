'''
    양옆사람한테만 빌리기 가능
    전체 학생 n
    체육복없는학생 lost[]
    체육복두개학생 reserve[]
    
    for reserve_student in reserve:
        if reserve_student-1 in lost:
            lost.remove(reserve_student-1)
        elif reserve_student+1 in lost:
            lost.remove(reserve_student+1)
'''

def solution(n, lost, reserve):    
    for reserve_student in reserve:
        if reserve_student in lost:
            lost.remove(reserve_student)
            continue
            
        if reserve_student+1 in lost:
            #print('a')
            lost.remove(reserve_student+1)
        elif reserve_student-1 in lost:
            #print('c')
            lost.remove(reserve_student-1)
    answer = n-len(lost)
    return answer
#map

def solution(n, arr1, arr2):
    answer = []
    for a1,a2 in zip(arr1,arr2):
        a12=str(bin(a1|a2))[2:]
        a12="0"*(n-len(a12))+a12
        a12=a12.replace('1','#')
        a12=a12.replace('0',' ')
        answer.append(a12)
    return answer

#### zip : 같은 타입의 배열 문자 등을 묶는다
 zip(arr1,arr2):

#### bin(2) 2진법의 수로 바꾸어 준다
 0b01

#### a12.replace('a','b') a12에 있는 모든 a를 b로 바꾸어 준다

#### a12=str(bin(a1|a2))[2:]
    [2:] str 데이터의 2번째 인덱스부터 슬라이싱한다








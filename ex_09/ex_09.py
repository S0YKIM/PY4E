fname = input('Enter File: ')
if len(fname) < 1 : fname = 'clown.txt'
hand = open(fname)

di = dict()
for lin in hand :
    lin = lin.rstrip()
    wds = lin.split()
    # 현재 단어 딕셔너리에 저장
    for w in wds :
        di[w] = di.get(w,0) + 1

# 가장 자주 등장한 단어 찾기
# largest: 가장 자주 등장한 단어 횟수
# theword: 가장 자주 등장한 단어
largest = -1
theword = None
for k, v in di.items() :
    if v > largest : 
        largest = v
        theword = k
        
print(theword, largest)

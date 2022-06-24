# done 이라고 입력하기 전까지 입력한 숫자들의 평균 구하기
num = 0
total = 0.0
while True :
    input_val = input('Enter a number:')
    if input_val == 'done' :
        break
    try :
        float_val = float(input_val)
    except :
        print('Invalid input')
        continue

    num = num + 1
    total = total + float_val

# 총합, 개수, 평균
print(total, num, total/num)

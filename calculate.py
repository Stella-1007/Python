choose , answer, num, x, y = 0, 0, "", 0, 0

choose = int(input("1. 입력한 수식 계산 2. 두 수 사이의 합계 :"))

if choose == 1:
    num = input(" *** 수식을 입력하세요 :")
    answer = eval(num)
    print(" %s 결과는 %5.1f 입니다. " %(num, answer))
elif choose == 2:
    x = int(input(" *** 첫 번째 숫자를 입력하세요 :"))
    y = int(input(" *** 두 번째 숫자를 입력하세요 :"))
    for i in range(x, y+1) :
        answer = answer + i
    print(x, "+...+", y, "는", answer, "입니다.")
else :
    print("1 또는 2만 입력하십시오")

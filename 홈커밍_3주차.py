'''
백준 코드 3주차 과제
'''

# 1330
# 두 정수 A와 B가 주어졌을 때, A와 B를 비교하는 프로그램을 작성하시오.
a, b = input("정수 a와 b를 입력해주세요:").split()
a = float(a)
b = float(b)
if a > b:
    print(a, '가 ', b, '보다 큽니다.')
if a < b:
    print(b, '가 ', a, '보다 큽니다.')
if a == b:
        print(a, '와 ', b, '의 크기가 같습니다.')

# 9498
# 시험 점수를 입력받아 
# 90 ~ 100점은 A, 80 ~ 89점은 B, 70 ~ 79점은 C, 60 ~ 69점은 D,
# 나머지 점수는 F를 출력하는 프로그램을 작성하시오.
a = input("시험점수를 입력해주세요.:")
a = int(a)
if 89 < a <= 100:
    print('A')
elif 79 < a <= 89:
    print('B')
elif 69 < a <= 79:
    print('C')
elif 59 < a <= 69:
    print('D')
else:
    print('F')

# 2753
# 연도가 주어졌을 때, 윤년이면 1, 아니면 0을 출력하는 프로그램을 작성하시오.
# 윤년은 연도가 4의 배수이면서, 100의 배수가 아닐 때 또는 400의 배수일 때이다.
# 예를 들어, 2012년은 4의 배수이면서 100의 배수가 아니라서 윤년이다. 
# 1900년은 100의 배수이고 400의 배수는 아니기 때문에 윤년이 아니다. 
# 하지만, 2000년은 400의 배수이기 때문에 윤년이다.
a = input("연도를 입력하시오.:")
a = int(a)
if (a % 4 == 0) and (a % 100 != 0):
    print('1')
elif a % 400 == 0:
    print('1')
else:
    print('0')

#14681
# 흔한 수학 문제 중 하나는 주어진 점이 어느 사분면에 속하는지 알아내는 것이다.
# 사분면은 아래 그림처럼 1부터 4까지 번호를 갖는다. 
# "Quadrant n"은 "제n사분면"이라는 뜻이다.
# 예를 들어, 좌표가 (12, 5)인 점 A는 x좌표와 y좌표가 모두 양수이므로 제1사분면에 속한다. 
# 점 B는 x좌표가 음수이고 y좌표가 양수이므로 제2사분면에 속한다.
# 점의 좌표를 입력받아 그 점이 어느 사분면에 속하는지 알아내는 프로그램을 작성하시오.
# 단, x좌표와 y좌표는 모두 양수나 음수라고 가정한다.
(a, b) = input("점의 좌표를 입력해주세요:").split()
a = float(a)
b = float(b)
if (a > 0) and (b > 0):
    print('제1사분면에 속합니다.')
elif (a > 0) and (b < 0):
    print('제2사분면에 속합니다.')
elif (a < 0) and (b < 0):
    print('제3사분면에 속합니다.')
elif (a < 0) and (b > 0):
    print('제4사분면에 속합니다.')
else:
    print('점이 x축이나 y축 위에 있습니다.')
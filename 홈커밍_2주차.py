'''
2주차 학습
강의: CHAPTER 2(변수, 표현식 및 코드)
실습: 백준 1000, 1001, 10998, 1008, 10869, 10430, 2588
'''

#1000
#두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
a, b = input("정수 a와 b를 입력해주세요:").split()
a = int(a)
b = int(b)
print(a+b)

#1001
#두 정수 A와 B를 입력받은 다음, A-B를 출력하는 프로그램을 작성하시오.
a, b = input("정수 a와 b를 입력해주세요:").split()
a = int(a)
b = int(b)
print(a-b)

#10998
#두 정수 A와 B를 입력받은 다음, A×B를 출력하는 프로그램을 작성하시오.
a, b = input("정수 a와 b를 입력해주세요:").split()
a = int(a)
b = int(b)
print(a*b)

#1008
#두 정수 A와 B를 입력받은 다음, A/B를 출력하는 프로그램을 작성하시오.
a, b = input("정수 a와 b를 입력해주세요:").split()
a = int(a)
b = int(b)
if b != 0:
    print(a/b)

#10869
#두 자연수 A와 B가 주어진다. 이때, A+B, A-B, A*B, A/B(몫), A%B(나머지)를 출력하는 프로그램을 작성하시오.
a, b = input("정수 a와 b를 입력해주세요:").split()
a = int(a)
b = int(b)
print("%d, %d, %d, %d" % (a+b, a-b, a*b, a/b)) 

#10430
#(A+B)%C는 ((A%C) + (B%C))%C 와 같을까? 
#(A×B)%C는 ((A%C) × (B%C))%C 와 같을까? 
#세 수 A, B, C가 주어졌을 때, 위의 네 가지 값을 구하는 프로그램을 작성하시오.
a, b, c = input("정수 a와 b와 c를 입력해주세요:").split()
a = int(a)
b = int(b)
c = int(c)
print('(a+b)%c = ', (a+b)%c)
print('((a%c) + (b%c))%c = ', ((a%c) + (b%c))%c)
print('(a*b)%c = ', (a*b)%c)
print('((a%c) × (b%c))%c = ', ((a%c)*(b%c))%c)

#2588
#(세 자리 수) × (세 자리 수)는 다음과 같은 과정을 통하여 이루어진다.
#(1)과 (2)위치에 들어갈 세 자리 자연수가 주어질 때 
#(3), (4), (5), (6)위치에 들어갈 값을 구하는 프로그램을 작성하시오.
a, b = input("세자리 수 a와 b를 입력해주세요:").split()
a = int(a)
b = int(b)
#c=(3), d=(4), e=(5), f=(6)
c = a*(((b%100))%10)
d = a*(b%100)
e = a*((b-(b%100))/100)
f = a*b
print('(3)값:', c)
print('(4)값:', d)
print('(5)값:', e)
print('(6)값:', f)
# 문제4 반복문을 이용하여 369게임에서 박수를 쳐야 하는 경우의 수를 순서대로 화면에
# 출력해보세요. 1부터 99까지만 실행하세요.

number = int(input(''))
temp = number
clap = ''
while number >= 1:
    if (number % 10) % 3 == 0:
        clap +='짝'
    number /= 10
    number = int(number)
print(temp, clap)
#1.5) https://github.com/inhadeepblue2024_KEB_datastrucutre_algorithm의
# v0.7 guess number 예제를 자동화 하고 로그 파일(guess.txt)을 남기도록 코드를 수정하시오 fp.write 사용
#단 , 해당 프로그램이 로그 시간을 갖도록 한다.

# with open('guess.txt', 'w') as fp:
#     fp.write("inha university")


import random

answer = random.randint(1, 100)
chance = 7

while chance != 0:
    guess = int(input("Input guess number : "))
    if guess == answer:
        print(f'You win. Answer is {answer}')
        break
    elif guess > answer:
        chance = chance - 1
        print(f'{guess} is bigger. Chance left : {chance}')
    else:
        chance = chance - 1
        print(f'{guess} is lower. Chance left : {chance}')
else:
     print(f'You lost. Answer is {answer}')

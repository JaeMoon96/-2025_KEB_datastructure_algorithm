import random

try:
    with open("students.csv", 'r') as fp:
        students_list = fp.readlines()
        students_list.remove("이상혁\n")
        students_list.remove("조윤하\n")
        students_list.remove("김철중\n")
        students_list.remove("김현민\n")
        students_list.remove("김찬빈\n")

        for _ in range(3):
            random_pick = random.choice(students_list)
            print(random_pick, end='')
            students_list.remove(random_pick)

        #print(random.choice(students_list), end='')
        # if "도종명\n" in students_list:
        #     print("!")
except FileNotFoundError as err:
    print(err)
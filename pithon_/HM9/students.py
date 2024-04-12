
studentList = ["Вася", "Петя", "Влад", "Рома", "Даня"]
score = [5, 5, 4, 4, 3, 3, 2]
score0 = [5, 5, 4, 3]
score1 = [2, 3, 4, 2]
score2 = [5, 3, 4, 5]
score3 = [2, 3, 3, 2]
score4 = [2, 3, 4, 3]

while True:
    answer = int(input("выберите действие\n"
                        "1-добавить студента\n"
                        "2-удалить студента по номеру\n"
                        "3-удалить студента по имени\n"
                        "4-посмотреть список студентов\n"
                        "5-посмотреть список оценок\n"
                        "6-посмотреть успеваемость всех студентов\n"
                        "7-посмотреть успеваемость студента\n"
                        "8-добавить оценку студенту\n"
                        "0-выход\n"))

    if answer not in [1, 2, 3, 4, 5, 6, 7, 8, 0]:
        print("такой команды нет")
        continue

    if answer == 1:
        newStudent = input("введите имя студента: ")
        studentList.append(newStudent)

    elif answer == 2:
        delNumber = int(input("введите номер студента для удаления: "))
        if delNumber < len(studentList):
            studentList.pop[delNumber]
        else:
            print("Неправильный номер студента")

    elif answer == 3:
        delName = input("введите имя студента для удаления: ")
        if delName in studentList:
            studentList.remove(delName)
        else:
            print("Такого студента нет в списке")

    elif answer == 4:
        print(studentList)

    elif answer == 5:
        print(score)

    elif answer == 6:
            print(studentList[0])
            print(score0)
            print(studentList[1])
            print(score1)
            print(studentList[2])
            print(score2)
            print(studentList[3])
            print(score3)
            print(studentList[4])
            print(score4)

    elif answer == 7:
        n = int(input("введите номер студента: "))
        if n < len(studentList):
            print(studentList[n])
            if n == 0:
                print(score0)
            elif n == 1:
                print(score1)
            elif n == 2:
                print(score2)
            elif n == 3:
                print(score3)
            elif n == 4:
                print(score4)
            else:
                print("У студента нет оценок")
        else:
            print("Неправильный номер студента")

    elif answer == 8:
        n = int(input("введите номер студента: "))
        if n < len(studentList):
            if n == 0:
                score0 = int(input("введите оценку"))
            elif n == 1:
                score1 = int(input("введите оценку"))
            elif n == 2:
                score2 = int(input("введите оценку"))
            elif n == 3:
                score3 = int(input("введите оценку"))
            elif n == 4:
                score4 = int(input("введите оценку"))
        else:
            print("Неправильный номер студента")

    elif answer == 0:
        break
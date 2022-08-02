import random

level = int(input("Выберите уровень: "))
print("Для остановки напишите \"стоп\".")
print("Вводите ответ в формате {число}/{число}. Например, \"1/2\".")
answer = []
rating = 0

while True:
    numbers = [random.randint(1, 10 ** level) for i in range(4)]
    if numbers[0] == numbers[1] or numbers[2] == numbers[3]:
        continue
    print('{}/{} + {}/{}'.format(numbers[0], numbers[1], numbers[2], numbers[3]))
    result = round(numbers[0] / numbers[1] + numbers[2] / numbers[3], 5)

    answer = input("Введите ответ: ")

    if answer == "стоп":
        break

    try:
        answer = answer.split("/")

        if len(answer) == 1:
            answer.append(1)

        if result == round(float(answer[0]) / int(answer[1]), 5):
            print("\t\033[32m{}\033[0m".format("Правильно!"))
            rating += 3 * level
        else:
            print("\t\033[31m{}\033[0m".format("Неправильно!"))
            rating -= 1
    except:
        print("\tSomething went wrong!")
    print("\t\033[34m{}{} \n\tВаш рейтинг: {}\033[0m".format("Ответ: ", round(result, 5), rating))

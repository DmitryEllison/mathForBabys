import random

level = int(input("Выберите уровень: "))
print("Для остановки напишите \"стоп\".")

typeOfProgram = input("Сделайте выбор \"+\" или \"*\"!")
                
while typeOfProgram != "+" or typeOfProgram != "*":
    typeOfProgram = input("Сделайте выбор \"+\" или \"*\"!")
print("Вводите ответ в формате {число}/{число}. Например, \"1/2\".")

answer = []
rating = 0

while True:
    numbers = [random.randint(1, 10 ** level) for i in range(2*(1 + level))]
    print('{}/{} {} {}/{}'.format(numbers[0], numbers[1], typeOfProgram, numbers[2], numbers[3]))
    result = round(numbers[0] / numbers[1] + numbers[2] / numbers[3], 5) if typeOfProgram == "+" \
        else round(numbers[0] / numbers[1] * numbers[2] / numbers[3], 5) 

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
            print("\t\033[31mНеправильно, ответ {}!\033[0m".format(result))
            rating -= 1
        print("\t\033[34m\tВаш рейтинг: {}\033[0m".format(rating))
    except:
        print("\tSomething went wrong!")

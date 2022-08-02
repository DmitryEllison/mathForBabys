import random

level = int(input("Выберите уровень: "))
print("Для остановки напишите \"стоп\".")
print("Вводите ответ в формате {число}/{число}. Например, \"1/2\".")
answer = []
rating = 0

while True:
    numbers = [random.randint(1, 10**level) for i in range(4)]
    if numbers[0] == numbers[1] or numbers[2] == numbers[3]:
        continue
    print('{}/{} + {}/{}'.format(numbers[0], numbers[1], numbers[2], numbers[3]))
    result = numbers[0]/numbers[1] + numbers[2]/numbers[3]

    answer = input("Введите ответ: ")

    if answer == "стоп":
        break

    try:
        answer = answer.split("/")

        if len(answer) == 1:
            answer.append(1)
            
        if result == int(answer[0])/int(answer[1]):
            print("\t\033[32m{}\033[0m".format("Правильно!")) 
            rating += 3*level
        else:
          print("\t\033[31m{}\033[0m".format("Неправильно!"))
          rating -= 1
          
        print("\t\033[34m{}{}\033[0m".format("Ответ: ", round(result, 3)))
    except:
        print("\tSomething went wrong!")

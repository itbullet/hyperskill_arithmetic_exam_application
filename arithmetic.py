import random


def answer(score, solution):
    while True:
        try:
            user_answer = int(input())
            if solution == user_answer:
                print('Right!')
                score += 1
                return score
            else:
                print('Wrong!')
                return score
        except ValueError:
            print('Incorrect format.')


def save_score(score, difficulty_level, level_description, i_):
    file_store = input(f'Your mark is {score}/{i_}. Would you like to save the result? Enter yes or no.\n')
    if file_store in ['yes', 'YES', 'y', 'Yes']:
        user_name = input('What is your name?\n')
        with open('results.txt', 'a') as file:
            file.write(f'{user_name}: {score}/{i_} in level {difficulty_level} ({level_description})\n')
            print('The results are saved in "results.txt".')


def exam():
    level_description1 = 'simple operations with numbers 2-9'
    level_description2 = 'integral squares of 11-29'
    while True:
        difficulty_level_ = input(f'Which level do you want? Enter a number:\n'
                                  f'1 - {level_description1}\n'
                                  f'2 - {level_description2}\n')
        if difficulty_level_ == '1':
            level_description_ = level_description1
            break
        elif difficulty_level_ == '2':
            level_description_ = level_description2
            break
        else:
            print('Incorrect format.')
    score_ = 0
    if difficulty_level_ == '1':
        for i in range(1, 6):
            operations = ['+', '-', '*']
            number1 = random.randint(2, 9)
            number2 = random.randint(2, 9)
            operation = random.choice(operations)
            task_str = f'{number1} {operation} {number2}'
            print(task_str)
            solution_ = eval(task_str)
            score_ = answer(score_, solution_)
        save_score(score_, difficulty_level_, level_description_, i)
    elif difficulty_level_ == '2':
        for i in range(1, 6):
            number3 = random.randint(11, 29)
            print(number3)
            solution_ = number3 ** 2
            score_ = answer(score_, solution_)
        save_score(score_, difficulty_level_, level_description_, i)


if __name__ == '__main__':
    exam()

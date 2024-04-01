from fastapi import FastAPI
import random

practice_api = FastAPI()


def generate_task_beginner():
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    operation = random.randint(0, 1)
    if operation == 0:
        return f'{a} + {b} = ', a + b
    elif operation == 1:
        return f'{a} - {b} = ', a - b
    else:
        return f'No such operation: {operation}', 0


def generate_task_easy():
    task_str = ''
    operation_list = ['+', '-', '*', '/']
    operation = random.choice(operation_list)

    if operation == '*':
        a = random.randint(2, 9)
        b = random.randint(2, 9)
        task_str += str(a) + f' {operation} ' + str(b)
        correct_answer = eval(task_str)
    elif operation == '+' or operation == '-':
        a = random.randint(5, 20)
        b = random.randint(5, 20)
        task_str += str(a) + f' {operation} ' + str(b)
        correct_answer = eval(task_str)
    elif operation == '/':
        a = random.randint(5, 20)
        b = random.randint(5, 20)
        minimal = min(a, b)
        multiplication = a * b
        task_str += str(multiplication) + f' {operation} ' + str(minimal)
        correct_answer = int(multiplication / minimal)
    else:
        return f'Unknown operation: {operation}', None

    return task_str + '=', correct_answer


def generate_task_medium(operand_number):
    task_str = ''
    operation_list = ['+', '-', '*']
    for i in range(operand_number):
        operand = random.randint(1, 10)
        task_str += str(operand) + ' '
        if i == operand_number - 1:
            break
        else:
            operation = operation_list[random.randint(0, 2)]
            task_str += operation + ' '
    correct_answer = eval(task_str)
    return task_str + '=', correct_answer


@practice_api.get("/beginner/{amount}")
def beginner_level(amount):
    response_obj = dict()
    for i in range(int(amount)):
        task, answer = generate_task_beginner()
        response_obj[f'{i + 1}'] = [task, answer]
    return response_obj


@practice_api.get("/easy/{amount}")
def easy_level(amount):
    response_obj = dict()
    for i in range(int(amount)):
        task, answer = generate_task_easy()
        response_obj[f'{i+1}'] = [task, answer]
    return response_obj


@practice_api.get("/medium/{amount}")
def medium_level(amount):
    response_obj = dict()
    for i in range(int(amount)):
        operand_num = random.randint(3, 4)
        task, answer = generate_task_medium(operand_num)
        response_obj[f'{i + 1}'] = [task, answer]
    return response_obj

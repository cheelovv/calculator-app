#!/usr/bin/env python3

import logging

logging.basicConfig(
    filename='calculator.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError("Ошибка: деление на ноль невозможно")
    return x / y

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            logging.warning("Пользователь ввел некорректное значение при запросе числа")
            print("Ошибка: введите корректное число")

def get_operation():
    while True:
        print("\nВыберите операцию:")
        print("1. Сложение (+)")
        print("2. Вычитание (-)")
        print("3. Умножение (*)")
        print("4. Деление (/)")
        print("5. Выход")
        
        choice = input("Введите номер операции (1-5): ").strip()
        
        if choice in ['1', '2', '3', '4', '5']:
            return choice
        else:
            logging.warning(f"Пользователь выбрал некорректную операцию: {choice}")
            print("Ошибка: выберите операцию от 1 до 5")

def main():
    logging.info("=" * 50)
    logging.info("Калькулятор запущен")
    logging.info("=" * 50)
    
    print("=" * 40)
    print("Калькулятор командной строки")
    print("=" * 40)
    
    while True:
        operation = get_operation()
        
        if operation == '5':
            logging.info("Пользователь завершил работу с калькулятором")
            logging.info("=" * 50)
            print("\nСпасибо за использование калькулятора!")
            break
        
        num1 = get_number("Введите первое число: ")
        num2 = get_number("Введите второе число: ")
        
        result = 0
        symbol = ''
        operation_name = ''
        
        try:
            if operation == '1':
                result = add(num1, num2)
                symbol = '+'
                operation_name = 'Сложение'
            elif operation == '2':
                result = subtract(num1, num2)
                symbol = '-'
                operation_name = 'Вычитание'
            elif operation == '3':
                result = multiply(num1, num2)
                symbol = '*'
                operation_name = 'Умножение'
            elif operation == '4':
                result = divide(num1, num2)
                symbol = '/'
                operation_name = 'Деление'
            
            logging.info(f"{operation_name}: {num1} {symbol} {num2} = {result}")
            print(f"\nРезультат: {num1} {symbol} {num2} = {result}")
            
        except ValueError as e:
            logging.error(f"Ошибка при выполнении операции: {e}")
            print(f"\n{e}")
        
        print("-" * 40)

if __name__ == "__main__":
    main()

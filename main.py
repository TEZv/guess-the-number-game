import random

def guess_the_number():
    """
    Консольна гра "Вгадай число", де комп'ютер загадує випадкове число.
    """
    print("Вітаємо у грі 'Вгадай число'!")
    print("Я загадаю ціле число у діапазоні від 1 до 100.")
    print("У тебе буде 7 спроб, щоб його вгадати.")

    # Генерація випадкового числа від 1 до 100
    secret_number = random.randint(1, 100)
    max_attempts = 7
    attempts_taken = 0

    while attempts_taken < max_attempts:
        try:
            guess = int(input(f"Спроба {attempts_taken + 1}/{max_attempts}. Введи своє число: "))

            if not (1 <= guess <= 100):
                print("Будь ласка, введи число у діапазоні від 1 до 100.")
                continue # Продовжуємо до наступної спроби без збільшення лічильника
            
            attempts_taken += 1 # Збільшуємо лічильник тільки якщо введено коректне число

            if guess < secret_number:
                print("Занадто маленьке!")
            elif guess > secret_number:
                print("Занадто велике!")
            else:
                print(f"Вітаємо! Ти вгадав число {secret_number} за {attempts_taken} спроб!")
                return # Завершуємо гру після перемоги
        except ValueError:
            print("Невірний ввід. Будь ласка, введи ціле число.")
            # Не збільшуємо attempts_taken, оскільки це не була валідна спроба

    # Якщо гравець вичерпав усі спроби
    print(f"\nНа жаль, у тебе закінчились спроби. Загадане число було: {secret_number}.")
    print("Спробуй ще раз!")

# Запуск гри
if __name__ == "__main__":
    guess_the_number()
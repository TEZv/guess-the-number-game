# -*- coding: utf-8 -*-
import random

def guess_the_number():
    """
    Консольна гра "Вгадай число", де комп'ютер загадує випадкове число.
    Включає динамічний діапазон чисел, змінну кількість спроб та "коефіцієнт удачі".
    """
    print("Привітики у грі 'Вгадай число'!")
    
    # --- Додаткова цікавинка: Динамічний діапазон чисел та кількість спроб ---
    min_range = random.randint(1, 10)  # Мінімальне значення діапазону
    max_range = random.randint(50, 200) # Максимальне значення діапазону
    
    # Забезпечуємо, щоб максимальне значення було більшим за мінімальне
    if min_range >= max_range:
        max_range = min_range + random.randint(50, 100)

    # Динамічна кількість спроб залежно від розміру діапазону
    # Наприклад, (max_range - min_range) / 10 + 3, округлене до цілого
    max_attempts = max(5, round((max_range - min_range) / random.uniform(8, 15))) # Змінюємо дільник випадково
    
    print(f"Я загадаю ціле число у діапазоні від {min_range} до {max_range}.")
    print(f"У тебе буде {max_attempts} спроб, щоб його вгадати.")

    secret_number = random.randint(min_range, max_range)
    attempts_taken = 0

    # --- Додаткова цікавинка: Випадковий "коефіцієнт удачі" для підказок ---
    # Це додає невелику випадковість до формулювання підказок
    luck_factor = random.choice(["трохи", "трішки", "зовсім небагато", "доволі", "дуже"])
    
    while attempts_taken < max_attempts:
        try:
            guess_input = input(f"Спроба {attempts_taken + 1}/{max_attempts}. Введи своє число: ")
            
            # Обробка введення для виходу з гри
            if guess_input.lower() == 'вихід':
                print("Шкода, що ти так швидко здаєшся. До зустрічі!")
                return
            
            guess = int(guess_input)

            if not (min_range <= guess <= max_range):
                print(f"Будь ласка, введи число у діапазоні від {min_range} до {max_range}.")
                continue # Продовжуємо до наступної спроби без збільшення лічильника
            
            attempts_taken += 1 # Збільшуємо лічильник тільки якщо введено коректне число

            difference = abs(secret_number - guess)
            
            if guess < secret_number:
                # --- Додаткова цікавинка: "Розумніші" підказки ---
                if difference <= 5:
                    print(f"Занадто маленьке! Але {luck_factor} близько!")
                elif difference <= 20:
                    print(f"Занадто маленьке. Але ти {luck_factor} на правильному шляху!")
                else:
                    print("Занадто маленьке!")
            elif guess > secret_number:
                if difference <= 5:
                    print(f"Занадто велике! Але {luck_factor} близько!")
                elif difference <= 20:
                    print(f"Занадто велике. Але ти {luck_factor} на правильному шляху!")
                else:
                    print("Занадто велике!")
            else:
                print(f"\n Вітаннячка! Вгадано число {secret_number} за {attempts_taken} спроб! Майстер/майстриня вгадування - це точно про тебе!")
                return # Завершуємо гру після перемоги
        except ValueError:
            print("Невірний ввід. Будь ласка, введи ціле число або 'вихід'.")
            # Не збільшуємо attempts_taken, оскільки це не була валідна спроба

    # Якщо гравець вичерпав усі спроби
    print(f"\n😔 На жаль, у тебе закінчились спроби. Загадане число було: {secret_number}.")
    print("Спробуй ще раз! Можливо, цього разу тобі пощастить більше. 😉")

# Запуск гри
if __name__ == "__main__":
    guess_the_number()
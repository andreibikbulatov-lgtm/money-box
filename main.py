import json
from goal import Goal
from reminder import set_reminder, check_reminders


def load_goals(filename):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def save_goals(goals, filename):
    with open(filename, 'w') as file:
        json.dump(goals, file)


def main():
    goals = load_goals('data.json')

    while True:
        print(
            "\n1. Добавить цель\n2. Изменить баланс\n3. Просмотр прогресса\n4. Установить напоминание\n5. Удалить цель\n6. Выход")
        choice = input("Выберите действие: ")

        if choice == "1":
            title = input("Введите название цели: ")
            target_amount = float(input("Введите итоговую сумму: "))
            category = input("Введите категорию: ")
            goal = Goal(title, target_amount, category)
            goals.append(goal.__dict__)
            save_goals(goals, 'data.json')

        elif choice == "2":
            if not goals:
                print("Список целей пуст. Сначала добавьте цель.")
                continue

            for index, goal in enumerate(goals):
                print(
                    f"{index + 1}. {goal['title']} - {goal['current_balance']}/{goal['target_amount']} [{goal['status']}]")
            goal_index_input = input("Выберите номер цели для изменения баланса: ")

            try:
                goal_index = int(goal_index_input) - 1
                if 0 <= goal_index < len(goals):
                    amount = float(input(
                        "Введите сумму для изменения баланса (положительное - увеличение, отрицательное - уменьшение): "))
                    if amount > 0:
                        goals[goal_index]['current_balance'] += amount
                    else:
                        goals[goal_index]['current_balance'] += amount
                    goals[goal_index]['current_balance'] = max(0, goals[goal_index][
                        'current_balance'])  # Не даем значение ниже 0
                    goals[goal_index]['status'] = 'Выполнена' if goals[goal_index]['current_balance'] >= \
                                                                 goals[goal_index]['target_amount'] else 'Новая'
                    save_goals(goals, 'data.json')
                else:
                    print("Некорректный выбор.")
            except ValueError:
                print("Ошибка: введите номер цели.")

        elif choice == "3":
            if not goals:
                print("Список целей пуст. Сначала добавьте цель.")
            else:
                for goal in goals:
                    progress = goal['current_balance'] / goal['target_amount'] * 100
                    print(f"Цель: {goal['title']}, Прогресс: {progress:.2f}% [{goal['status']}]")

        elif choice == "4":
            if not goals:
                print("Список целей пуст. Сначала добавьте цель.")
                continue

            for index, goal in enumerate(goals):
                print(
                    f"{index + 1}. {goal['title']} - {goal['current_balance']}/{goal['target_amount']} [{goal['status']}]")
            goal_index_input = input("Выберите номер цели для установки напоминания: ")

            try:
                goal_index = int(goal_index_input) - 1
                if 0 <= goal_index < len(goals):
                    due_date = set_reminder(goals[goal_index])
                    if due_date:
                        goals[goal_index]['due_date'] = due_date
                        save_goals(goals, 'data.json')
                        print(f"Напоминание установлено для '{goals[goal_index]['title']}' до {due_date}.")
                else:
                    print("Некорректный выбор.")
            except ValueError:
                print("Ошибка: введите номер цели.")

        elif choice == "5":
            if not goals:
                print("Список целей пуст. Сначала добавьте цель.")
                continue

            for index, goal in enumerate(goals):
                print(f"{index + 1}. {goal['title']}")
            goal_index_input = input("Выберите номер цели для удаления: ")

            try:
                goal_index = int(goal_index_input) - 1
                if 0 <= goal_index < len(goals):
                    del goals[goal_index]
                    save_goals(goals, 'data.json')
                    print("Цель удалена.")
                else:
                    print("Некорректный выбор.")
            except ValueError:
                print("Ошибка: введите номер цели.")

        elif choice == "6":
            break


        check_reminders(goals)


if __name__ == "__main__":
    main()

from datetime import datetime, timedelta


def set_reminder(goal):
   
    amount_per_contribution = float(input("Введите сумму пополнения: "))
    frequency = int(input("Введите частоту пополнений (в днях): "))

  
    remaining_amount = goal['target_amount'] - goal['current_balance']

    if remaining_amount <= 0:
        print("Цель уже выполнена!")
        return


    contributions_needed = remaining_amount / amount_per_contribution

    
    days_needed = contributions_needed * frequency

    
    due_date = datetime.now() + timedelta(days=days_needed)

    return due_date.strftime("%Y-%m-%d")


def check_reminders(goals):
    current_date = datetime.now().date()

    for goal in goals:
        due_date_str = goal.get('due_date')
        if due_date_str:
            due_date = datetime.strptime(due_date_str, "%Y-%m-%d").date()
            if due_date <= current_date:
                print(
                    f"Напоминание: цель '{goal['title']}' должна быть завершена к {due_date_str}! Проверьте ваш прогресс.")
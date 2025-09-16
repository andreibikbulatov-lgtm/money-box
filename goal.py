class Goal:
    def __init__(self, title, target_amount, category):
        self.title = title
        self.target_amount = target_amount
        self.current_balance = 0.0
        self.category = category
        self.status = "Новая"
        self.due_date = None  

    def add_balance(self, amount):
        if self.current_balance + amount > self.target_amount:
            print("Ошибка: Сумма превышает итоговую сумму.")
        else:
            self.current_balance += amount

    def subtract_balance(self, amount):
        if self.current_balance - amount < 0:
            print("Ошибка: Нельзя уменьшать баланс ниже нуля.")
        else:
            self.current_balance -= amount

    def progress(self):
        return (self.current_balance / self.target_amount) * 100

    def update_status(self):
        if self.current_balance >= self.target_amount:
            self.status = "Выполнена"
            self.due_date = None  # Убираем дату завершения, если цель выполнена

    def remove_goal(self):
      
        pass

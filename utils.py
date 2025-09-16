def validate_positive_amount(amount):
    if amount <= 0:
        raise ValueError("Сумма должна быть положительной.")
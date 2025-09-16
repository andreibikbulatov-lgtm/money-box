from utils import load_goals, save_goals, total_progress
from goal import Goal

def add_goal(goals, name, target_amount, category):
    new_goal = Goal(name, target_amount, category)
    goals.append(new_goal)

def remove_goal(goals, index):
    if 0 <= index < len(goals):
        del goals[index]
    else:
        print("Неверный индекс цели!")

def display_goals(goals):
    for index, goal in enumerate(goals):
        print(f"{index}. {goal}")
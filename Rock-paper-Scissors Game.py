import random

user_actions=input('enter your actions(rock,paper,scissors):')
possible_actions=['rock','paper','scissors']
computer_actions=random.choice(possible_actions)
print(f"\nYou chose {user_actions}, computer chose {computer_actions}.\n")
if user_actions==computer_actions:
    print(f"both the players selected {user_actions},its a tie")
elif user_actions=='rock' and computer_actions=='scissors':
    print(f"You won {user_actions} won")
elif user_actions=='paper' and computer_actions=='rock':
    print(f"computer won{computer_actions}")
elif user_actions=="scissors" and computer_actions=='paper':
    print(f"You won {user_actions}")



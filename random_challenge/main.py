import random
import challenges_list



def get_random_challenge() -> None:
    random_number1 = 1
    random_number2 = 1
    random_number2 = 1
    difficulty: str = input("Enter difficulty level (beginner (B), intermediate (I), advanced (A)): ").upper()
    if difficulty not in ['B', 'I', 'A']:
        print("Invalid difficulty level. Please enter B, I, or A.")
        difficulty = input("Enter difficulty level (beginner (B), intermediate (I), advanced (A)): ").upper()
        return None
    elif difficulty == 'B':
        random_number1 = random.randint(1, 30)
        random_number2 = random.randint(1, 30)
        random_number3 = random.randint(1, 30)
    else:
        random_number1: int = random.randint(1, 40)
        random_number2: int = random.randint(1, 40)
        random_number3: int = random.randint(1, 40)
    weekly_challenge1:str = difficulty + "0" + str(random_number1)
    weekly_challenge2:str = difficulty + "0" + str(random_number2)
    weekly_challenge3:str = difficulty + "0" + str(random_number3)
    return print(f"Your weekly challenge is: {challenges_list.challenges_list.get(weekly_challenge1)}  ({weekly_challenge1}) \nor {challenges_list.challenges_list.get(weekly_challenge2)} ({weekly_challenge2}) \nor {challenges_list.challenges_list.get(weekly_challenge3)} ({weekly_challenge3})")

week_challenge: None = get_random_challenge()
if __name__ == "__main__":
    print(week_challenge)

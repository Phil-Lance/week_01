import random
import challenge_dict



def get_random_challenge() -> None:
    difficulty: str = input("Enter difficulty level (beginner (B), intermediate (I), advanced (A)): ").upper()
    if difficulty not in ['B', 'I', 'A']:
        print("Invalid difficulty level. Please enter B, I, or A.")
        difficulty = input("Enter difficulty level (beginner (B), intermediate (I), advanced (A)): ").upper()
        return None
    elif difficulty == 'B':
        random_number = random.randint(1, 15)
    else:
        random_number: int = random.randint(1, 20)
    weekly_challenge:str = difficulty + str(random_number)
    return print(f"Your weekly challenge is: {challenge_dict.challenge_dict.get(weekly_challenge)}  ({weekly_challenge})")

week_challenge: None = get_random_challenge()
if __name__ == "__main__":
    print(week_challenge)

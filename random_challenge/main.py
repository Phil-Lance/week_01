import random
import challenges_list
import selected_challenges
choice1: str = ""
choice2: str = ""
choice3: str = ""



def get_random_challenge() -> None:
    counter = 0
    global choice1, choice2, choice3
    weekly_challenge1:str = ""
    weekly_challenge2:str = ""
    weekly_challenge3:str = ""
    difficulty: str = input("Enter difficulty level (beginner (B), intermediate (I), advanced (A)): ").upper()
    while counter < 3:
        if difficulty not in ['B', 'I', 'A']:
            print("Invalid difficulty level. Please enter B, I, or A.")
            difficulty = input("Enter difficulty level (beginner (B), intermediate (I), advanced (A)): ").upper()
            return None
        elif difficulty == 'B':
            temp_number = random.randint(1, 30)
        else:
            temp_number: int = random.randint(1, 40)
        if temp_number == range(1, 9) and counter == 0:
            weekly_challenge1: str = difficulty + "0" + str(temp_number)
            if weekly_challenge1 in selected_challenges.selected_challenges:
                continue
            else:
                choice1 = weekly_challenge1
                counter += 1
        elif temp_number in range(10, 40) and counter == 0:
            weekly_challenge1: str = difficulty + str(temp_number)
            if weekly_challenge1 in selected_challenges.selected_challenges:
                continue
            else:
                choice1 = weekly_challenge1
                counter += 1
        elif temp_number in range(1, 9) and counter == 1:
            weekly_challenge2: str = difficulty + "0" + str(temp_number)
            if weekly_challenge1 == weekly_challenge2:
                continue
            else:
                if weekly_challenge1 in selected_challenges.selected_challenges:
                    continue
                else:
                    choice2 = weekly_challenge2
                    counter += 1
        elif temp_number in range(10, 40) and counter == 1:
            weekly_challenge2: str = difficulty + str(temp_number)
            if weekly_challenge1 == weekly_challenge2:
                continue
            else:
                if weekly_challenge1 in selected_challenges.selected_challenges:
                    continue
                else:
                    choice2 = weekly_challenge2
                    counter += 1
        elif temp_number in range(1, 9) and counter == 2:
            weekly_challenge3: str = difficulty + "0" + str(temp_number)
            if weekly_challenge1 == weekly_challenge2:
                continue
            else:
                if weekly_challenge1 in selected_challenges.selected_challenges:
                    continue
                else:
                    choice3 = weekly_challenge3
                    counter += 1
        elif temp_number in range(10, 40) and counter == 2:
            weekly_challenge3: str = difficulty + str(temp_number)
            if weekly_challenge1 == weekly_challenge2:
                continue
            else:
                if weekly_challenge1 in selected_challenges.selected_challenges:
                    continue
                else:
                    choice3 = weekly_challenge3
                    counter += 1
        

    return print(f"Your weekly challenge is: \n-{challenges_list.challenges_list.get(weekly_challenge1)}  ({weekly_challenge1}) \n-or {challenges_list.challenges_list.get(weekly_challenge2)} ({weekly_challenge2}) \n-or {challenges_list.challenges_list.get(weekly_challenge3)} ({weekly_challenge3})")

week_challenge: None = get_random_challenge()
if __name__ == "__main__":
    print(week_challenge)
challenge_choice:str = input("Which challenge would you like to choose? (1, 2, or 3): ")
if challenge_choice not in ['1', '2', '3']:
    print("Invalid choice. Please select 1, 2, or 3.")
    
if challenge_choice == '1':
    # selected_challenges.selected_challenges.append(choice1)
    print(f"You chose: {choice1} - {challenges_list.challenges_list.get(choice1)}")
elif challenge_choice == '2':
    # selected_challenges.selected_challenges.append(choice2)
    print(f"You chose: {choice2} - {challenges_list.challenges_list.get(choice2)}")
elif challenge_choice == '3':
    # selected_challenges.selected_challenges.append(choice3)
    print(f"You chose: {choice3} - {challenges_list.challenges_list.get(choice3)}")
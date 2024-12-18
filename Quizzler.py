
quiz = {
    1: {"question": "What is the capital of France?", 
        "options": ["1. Paris", "2. Berlin", "3. Madrid", "4. Rome"], 
        "answer": 1},
    2: {"question": "Which programming language is this?", 
        "options": ["1. Java", "2. Python", "3. C++", "4. JavaScript"], 
        "answer": 2},
    3: {"question": "What is 5 + 3?", 
        "options": ["1. Six", "2. Seven", "3. Eight", "4. Nine"], 
        "answer": 3},
}

def add_custom_questions():
    print("\n=== Add Your Own Questions ===")
    while True:
        question = input("Enter the question: ").strip()
        options = []
        for i in range(1, 5):  
            option = input(f"Enter option {i}: ").strip()
            options.append(f"{i}. {option}")
        try:
            correct_option = int(input("Enter the number of the correct option (1-4): "))
            if 1 <= correct_option <= 4:
                print("hello")
            else:
                print("Please enter a number between 1 and 4.")
        except ValueError:
                print("Invalid input. Please enter a number.")
        question_number = len(quiz) + 1
        quiz[question_number] = {"question": question, "options": options, "answer": correct_option}
        print("Question added successfully!")
        more = input("Do you want to add another question? (yes/no): ").strip().lower()
        if more != "yes":
            break


def run_quiz():
    score = 0
    for q_no, q_data in quiz.items():
        print(f"\nQuestion {q_no}: {q_data['question']}")
        for option in q_data["options"]:
            print(option)
        while True:
            try:
                answer = int(input("Enter the option number: "))
                if 1 <= answer <= len(q_data["options"]):
                    break
                else:
                    print("Invalid choice. Choose a number within the options.")
            except ValueError:
                print("Please enter a valid number.")
        
        if answer == q_data["answer"]:
            print("Correct!")
            score += 1
        else:
            print("Wrong!")
    return score


def main():
    while True:
        print("\n=== Welcome to the Quiz Game! ===")
        print("1. Play Quiz")
        print("2. Add Custom Questions")
        print("3. Exit")
        
        choice = input("Enter your choice: ").strip()
        if choice == "1":
            score = run_quiz()
            print(f"\nYou scored {score}/{len(quiz)}.")
            if score == len(quiz):
                print("Excellent!")
            elif score >= len(quiz) // 2:
                print("Good job!")
            else:
                print("Better luck next time!")
        elif choice == "2":
            add_custom_questions()
        elif choice == "3":
            print("Thanks for playing! Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

main()
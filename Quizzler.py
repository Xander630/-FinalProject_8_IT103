# Quiz Data: Questions, Options, and Correct Answers
# This dictionary holds all the questions in the quiz, each with its options and the correct answer.
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

# Function to allow users to add custom questions
def add_custom_questions():
    """
    Allows users to add new questions to the quiz.
    Prompts for the question, four options, and the correct answer.
    """
    print("\n=== Add Your Own Questions ===")
    while True:
        # Input the question
        question = input("Enter the question: ").strip()
        
        # Input 4 options for the question
        options = []
        for i in range(1, 5):  # Assuming 4 options for each question
            option = input(f"Enter option {i}: ").strip()
            options.append(f"{i}. {option}")  # Format the option with a number
        
        # Input and validate the correct option
        while True:
            try:
                correct_option = int(input("Enter the number of the correct option (1-4): "))
                if 1 <= correct_option <= 4:
                    break
                else:
                    print("Please enter a number between 1 and 4.")
            except ValueError:
                print("Invalid input. Please enter a number.")
        
        # Add the custom question to the quiz dictionary
        question_number = len(quiz) + 1  # Assign the new question a number
        quiz[question_number] = {"question": question, "options": options, "answer": correct_option}
        print("Question added successfully!")

        # Ask the user if they want to add another question
        more = input("Do you want to add another question? (yes/no): ").strip().lower()
        if more != "yes":
            break

# Function to display the quiz and get answers
def run_quiz():
    """
    Displays each question to the user, collects their answers,
    and calculates the score based on correct responses.
    """
    score = 0  # Initialize the user's score

    # Iterate through each question in the quiz
    for q_no, q_data in quiz.items():
        print(f"\nQuestion {q_no}: {q_data['question']}")
        for option in q_data["options"]:  # Display all options for the current question
            print(option)
        
        # Validate and accept the user's answer
        while True:
            try:
                answer = int(input("Enter the option number: "))
                if 1 <= answer <= len(q_data["options"]):  # Ensure the answer is within the range
                    break
                else:
                    print("Invalid choice. Choose a number within the options.")
            except ValueError:
                print("Please enter a valid number.")
        
        # Check if the answer is correct
        if answer == q_data["answer"]:
            print("Correct!")
            score += 1  # Increment score for correct answers
        else:
            print("Wrong!")
    
    return score  # Return the final score

# Main Function
def main():
    """
    Controls the overall program flow.
    Allows users to play the quiz, add custom questions, or exit.
    """
    while True:
        print("\n=== Welcome to the Quiz Game! ===")
        print("1. Play Quiz")
        print("2. Add Custom Questions")
        print("3. Exit")
        
        # Get the user's choice
        choice = input("Enter your choice: ").strip()
        if choice == "1":
            # Run the quiz and display the user's score
            score = run_quiz()
            print(f"\nYou scored {score}/{len(quiz)}.")
            if score == len(quiz):  # Perfect score
                print("Excellent!")
            elif score >= len(quiz) // 2:  # Half or more correct
                print("Good job!")
            else:  # Less than half correct
                print("Better luck next time!")
        elif choice == "2":
            # Allow the user to add custom questions
            add_custom_questions()
        elif choice == "3":
            # Exit the program
            print("Thanks for playing! Goodbye!")
            break
        else:
            # Handle invalid menu choices
            print("Invalid choice. Please try again.")
main()  # Start the program

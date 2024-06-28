import itertools

# Define the questions and possible answer types
questions = {
    "Q1: Do you like ice cream? (yes/no)": ["yes", "no"],
    "Q2: Is today a sunny day? (true/false)": ["true", "false"],
    "Q3: Choose a random letter (a, b, c)": ["a", "b", "c"],
    "Q4: Pick a random number (1, 2, 3)": ["1", "2", "3"]
}

# Function to interactively answer questions
def answer_questions(questions):
    answers = {}
    for question, options in questions.items():
        while True:
            answer = input(f"{question} ").strip().lower()
            if answer in options:
                answers[question] = answer
                break
            else:
                print("Invalid input. Please choose from:", options)
    return answers

# Generate all possible combinations of answers
def generate_universes(questions):
    keys = sorted(questions.keys())
    options = [questions[key] for key in keys]
    universes = []

    for combo in itertools.product(*options):
        universe = {keys[i]: combo[i] for i in range(len(keys))}
        universes.append(universe)

    return universes

# Function to navigate through universes and select one
def navigate_universes(universes):
    for idx, universe in enumerate(universes):
        print(f"Universe {idx + 1}:")
        for key, value in universe.items():
            print(f"{key}: {value}")
        print()

    return universes

# Interactive shell function with split-screen comparison
def interactive_shell(universes, user_answers):
    while True:
        command = input("\nEnter command ('all' to show all universes, 'vX' to visit universe X, 'exit' to quit): ").strip().lower()

        if command == 'all':
            navigate_universes(universes)
        elif command.startswith('v'):
            try:
                idx = int(command[1:]) - 1
                if 0 <= idx < len(universes):
                    selected_universe = universes[idx]
                    print("\n+-------------------------+-------------------------+")
                    print("|      Your Universe      |       Universe", idx + 1, "      |")
                    print("+-------------------------+-------------------------+")
                    for key in questions.keys():
                        your_answer = user_answers[key]
                        universe_answer = selected_universe[key]
                        print(f"| {your_answer:<23} | {universe_answer:<23} |")
                    print("+-------------------------+-------------------------+")
                else:
                    print(f"Universe {idx + 1} does not exist.")
            except ValueError:
                print("Invalid command format. Please enter 'vX' where X is a valid universe number.")
        elif command == 'exit':
            print("Exiting...")
            break
        else:
            print("Invalid command. Please enter a valid command.")

# Example usage:
if __name__ == "__main__":
    print("Please answer the following questions:")
    user_answers = answer_questions(questions)
    print("\nYour answers:")
    for question, answer in user_answers.items():
        print(f"{question}: {answer}")

    print("\nGenerating possible universes...")
    all_universes = generate_universes(questions)

    print("\nInteractive shell:")
    interactive_shell(all_universes, user_answers)

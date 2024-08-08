class Quiz:
    def __init__(self):
        self.questions = {
            "What is the capital of France?": {
                "options": ["Berlin", "Paris", "London", "Rome"],
                "correct": 1
            },
            "What is the largest planet in our solar system?": {
                "options": ["Earth", "Saturn", "Jupiter", "Uranus"],
                "correct": 2
            },
            "Who painted the Mona Lisa?": {
                "options": ["Leonardo da Vinci", "Michelangelo", "Raphael", "Caravaggio"],
                "correct": 0
            }
        }
        self.score = 0

    def run_quiz(self):
        for question, data in self.questions.items():
            print(question)
            for i, option in enumerate(data["options"]):
                print(f"{i+1}. {option}")
            try:
                answer = int(input("Enter the number of your answer: "))
                if answer == data["correct"] + 1:
                    print("Correct!")
                    self.score += 1
                else:
                    print(f"Incorrect. The correct answer is {data['options'][data['correct']]}")
            except ValueError:
                print("Invalid input. Please enter a number.")
        print(f"Your final score is {self.score} out of {len(self.questions)}")

quiz = Quiz()
quiz.run_quiz()
import datetime
import random

def games():
    print("Chatbot : Lets Play games")
    print(" 1. Number Guessing Game ")
    print(" 2. Quiz Game ")
    print(" 3. Rock paper scissors Game ")
    
    print("Chatbot : Enter the number of game u want to play ")
    game_no = input("You : ").strip()
    
    if game_no == '1':
        number_guessing()
        return ""
    elif game_no == '2':
        quiz_game()
        return ""  
    elif game_no == '3':
        rock_paper_scissors()
        return ""
    else:
        return ("Invalid choice")   
    
def rock_paper_scissors():
    print("\n🎮 Welcome to Rock Paper Scissors!")
    print("Enter:")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")

    choices = ["Rock", "Paper", "Scissors"]

    while True:
        user = input("\nYour choice (1/2/3): ").strip()

        if user not in ("1", "2", "3"):
            print("❌ Invalid choice! Please enter 1, 2, or 3.")
            continue

        user_choice = choices[int(user) - 1]
        computer_choice = random.choice(choices)

        print(f"\n🧑 You chose: {user_choice}")
        print(f"🤖 Computer chose: {computer_choice}")

        if user_choice == computer_choice:
            print("🤝 It's a Draw!")

        elif (
            (user_choice == "Rock" and computer_choice == "Scissors") or
            (user_choice == "Paper" and computer_choice == "Rock") or
            (user_choice == "Scissors" and computer_choice == "Paper")
        ):
            print("🎉 You Win!")

        else:
            print("😢 Computer Wins!")

        play_again = input("\nDo you want to play again? (yes/no): ").lower()

        if play_again != "yes":
            print("👋 Thanks for playing!")
            break 
    
def quiz_game():
    print("\n🧠 Welcome to the Python Quiz Game!")
    print("Each correct answer gives you 1 point.\n")

    score = 0

    # Question 1
    print("Q1. Who developed Python?")
    print("A. James Gosling")
    print("B. Guido van Rossum")
    print("C. Dennis Ritchie")
    print("D. Bjarne Stroustrup")

    ans = input("Your Answer (A/B/C/D): ").upper()

    if ans == "B":
        print("✅ Correct!\n")
        score += 1
    else:
        print("❌ Wrong! Correct Answer: B. Guido van Rossum\n")

    # Question 2
    print("Q2. Which symbol is used for comments in Python?")
    print("A. //")
    print("B. <!-- -->")
    print("C. #")
    print("D. **")

    ans = input("Your Answer (A/B/C/D): ").upper()

    if ans == "C":
        print("✅ Correct!\n")
        score += 1
    else:
        print("❌ Wrong! Correct Answer: C. #\n")

    # Question 3
    print("Q3. Which data type stores True or False?")
    print("A. int")
    print("B. float")
    print("C. bool")
    print("D. string")

    ans = input("Your Answer (A/B/C/D): ").upper()

    if ans == "C":
        print("✅ Correct!\n")
        score += 1
    else:
        print("❌ Wrong! Correct Answer: C. bool\n")

    # Question 4
    print("Q4. Which keyword is used to define a function?")
    print("A. function")
    print("B. define")
    print("C. def")
    print("D. func")

    ans = input("Your Answer (A/B/C/D): ").upper()

    if ans == "C":
        print("✅ Correct!\n")
        score += 1
    else:
        print("❌ Wrong! Correct Answer: C. def\n")

    # Question 5
    print("Q5. Which loop is used to iterate over a sequence?")
    print("A. for")
    print("B. repeat")
    print("C. whiledo")
    print("D. foreach")

    ans = input("Your Answer (A/B/C/D): ").upper()

    if ans == "A":
        print("✅ Correct!\n")
        score += 1
    else:
        print("❌ Wrong! Correct Answer: A. for\n")

    print("=" * 40)
    print(f"🎯 Your Final Score: {score}/5")

    if score == 5:
        print("🏆 Excellent! Perfect Score!")
    elif score >= 3:
        print("👏 Good Job!")
    else:
        print("📚 Keep Practicing!")

def number_guessing():
    print("\n🎮 Welcome to Number Guessing Game!")
    print("I'm thinking of a number between 1 and 10.")

    secret_number = random.randint(1, 10)
    attempts = 3

    while attempts > 0:
        try:
            guess = int(input("Enter your guess: "))

            if guess == secret_number:
                print("🎉 Congratulations! You guessed it correctly.")
                return

            elif guess < secret_number:
                print("📉 Too low!")

            else:
                print("📈 Too high!")

            attempts -= 1
            print(f"Attempts left: {attempts}\n")

        except ValueError:
            print("❌ Please enter a valid number.")

    print(f"😢 Game Over! The correct number was {secret_number}.")  
      
def get_reply(txt):
    text = txt.lower().strip()
    
    if text in ("hi","hello","hey"):
        return "Hi !"
    elif text in ("how are you", "how are you?"):
        return "I'm fine, thanks!"
    elif text in ("bye", "goodbye", "exit", "quit"):
        return "Goodbye!"
    elif "name" in text:
        return "I'm a simple rule-based chatbot."
    elif text == "time":
        return f"The current time is {datetime.datetime.now().strftime('%I:%M %p')}"

    elif text == "date":
        return f"Today's date is {datetime.datetime.now().strftime('%d-%m-%Y')}"

    elif text == "day":
        return f"Today is {datetime.datetime.now().strftime('%A')}"
    elif text == "i am sad":
        return "I'm sorry you're feeling that way. I hope tomorrow is a better day."

    elif text == "i am happy":
        return "That's wonderful! Keep smiling. 😄"

    elif text == "good night":
        return "Good Night! Sweet dreams. 🌙"
    elif text in ("game", "playgame","games"):
        games()
        return ""


    else:
        return "Sorry, I don't understand that yet."
    
def greet():
    hour = int(datetime.datetime.now().hour)
    if hour < 12:
        print("Chatbot : Good morning, sir")
    elif hour < 18:
        print("Chatbot : Good afternoon, sir")
    else:
        print("Chatbot : Good evening, sir")
        
def runchatbot():
    print("*"*50)
    print("Welcome to Chatbot ".center(50).upper())
    print("*"*50)
    greet()


    
    while True:
        user_input = input("You :")
        reply =get_reply(user_input)
        if reply is not None and reply != "":
            print(f"Chatbot : {reply}")
        if user_input.lower().strip() in ("bye", "goodbye", "exit", "quit"):
            break

if __name__ == "__main__":
    try:
        runchatbot()
    except KeyboardInterrupt:
        print("\n\nProgram interrupted by user.bye! 👋")
    except Exception as e:
        print(f"\n❌ An unexpected error occurred: {e}")
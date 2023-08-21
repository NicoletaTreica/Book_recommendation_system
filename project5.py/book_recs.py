# Importing profile and random module
import profile
import random


# Defining a class which stores the users profile with various attributes (name, age, etc)
class Profile:
    def __init__(
        self,
        name: str,
        age: int,
        gender: str,
        nationality: str,
        username: str,
        password: str,
    ) -> None:
        self.name = name
        self.age = age
        self.gender = gender
        self.nationality = nationality
        self.username = username
        self.password = password

    # displaying profile when user_info is called
    # The attributes of the profile will be displayed
    def user_info(self) -> None:
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Gender: {self.gender}")
        print(f"nationality: {self.nationality}")
        print(f"username: {self.username}")
        print(f"password: {self.password}")


# Defining a class to store the questions in the questionaire and the possible choices associated with each question
class Questions:
    def __init__(self, question: str, choice: list[str]) -> None:
        self.question = question
        self.choice = choice


# Definening a class which stores the information of the books
class Book:
    def __init__(self, title: str, author: str, genre: str, rating: int) -> None:
        self.title = title
        self.author = author
        self.genre = genre
        self.rating = rating


# Def register is a function that is asking the user to register their profile
def register() -> Profile:
    # Get user information
    print("Register your new account by: ")
    name = input("Entering your name: ")
    age = input("Entering your age: ")
    gender = input("Entering your gender: ")
    nationality = input("Entering your nationality: ")
    print("It was nice getting to know you!")
    print("")
    print("Now think of an unique username and password, then enter it below: ")
    username = input("Enter your new username: ")
    password = input("Enter your new password: ")
    # creating a new profile instance with the user information
    return Profile(name, age, gender, nationality, username, password)


# Function for user login
def login(registered_profiles: list[Profile]) -> Profile:
    # this list will store the registered profiles
    while True:
        print("To log into your bookrecs account please enter your details below: ")
        user_username = input("Enter your username: ")
        user_password = input("Enter your password: ")
        # Loop through registered profiles to check for a match
        for profile in registered_profiles:
            if profile.username == user_username and profile.password == user_password:
                print("Thank You for logging in today! ")
                return profile
        else:
            print("Your details are not yet registered.")
            choice = input("Would you like to register? type yes or no: ")
            if choice.lower() == "yes":
                # registers a new profile
                registered_profiles.append(register())
            elif choice.lower() == "no":
                break

    return None


# Function to ask questions and get user choice as well as return what the user has choosen
def ask_questions(question: Questions) -> str:
    print(question.question)
    for choice in question.choice:
        print(choice)
    user_choice = input("Enter your choice (A, B, C, etc.): ")
    return user_choice.upper()


# Function to display a user menu and handle user choices
# The questions are passed through the menu because they are defined after the menu, without this, the ->
# -> program wouldn't known what we are referring to
# Questions defined after menu so we pass the questions in def menu so that it can work with it
def menu(
    logged_in_profile: Profile,
    question_1: Questions,
    question_2: Questions,
    question_3: Questions,
    question_4: Questions,
    question_5: Questions,
    books: list[Book],
) -> None:
    while True:
        print(
            "Welcome to bookrecs, choose a service I can do for you from the below options"
        )
        print("-------------------------------")
        print("choose one of the options below")
        print("-------------------------------")
        print("1. Go to my profile")
        print("2. Go to the books that I have read")
        print("3. Help me discover a new book")
        print("4. Recommend a book to me")
        print("5. Sign out")

        choice = input("Enter your number choice here: ")

        if choice == "1":
            # showing the information of the user
            logged_in_profile.user_info()
        elif choice == "2":
            # regestering which books the user has read
            previously_read = input("which books have you read before: ")
            print(previously_read)
        elif choice == "3":
            # Determine user mood and recommend a book genre based on the questions asked
            determining_mood = input(
                "Select the mood that you are in: bored, sad, happy, angry, or productive "
            )

            if determining_mood.lower() == "bored":
                user_choice_question = ask_questions(question_1)
            elif determining_mood.lower() == "sad":
                user_choice_question = ask_questions(question_2)
            elif determining_mood.lower() == "happy":
                user_choice_question = ask_questions(question_3)
            elif determining_mood.lower() == "angry":
                user_choice_question = ask_questions(question_4)
            elif determining_mood.lower() == "productive":
                user_choice_question = ask_questions(question_5)
            else:
                print("Sorry I didn't catch that")

            if user_choice_question.upper() == "A":
                recommended_genre = "Fiction"
            elif user_choice_question.upper() == "B":
                recommended_genre = "Mystery"
            elif user_choice_question.upper() == "C":
                recommended_genre = "Thriller"
            elif user_choice_question.upper() == "D":
                recommended_genre = "Romance"
            elif user_choice_question.upper() == "E":
                recommended_genre = "Young Adult"
            elif user_choice_question.upper() == "F":
                recommended_genre = "Non Fiction"
            recommended_books = [
                book for book in books if book.genre == recommended_genre
            ]
            if recommended_books:
                recommended_book = random.choice(recommended_books)
                print(
                    f"I recommend you read '{recommended_book.title}' by {recommended_book.author} because you seem to be in the mood for {recommended_genre}."
                )

        elif choice == "4":
            # Giving the user a random book recomendation
            random_book = random.choice(books)
            print(f"{random_book.title} by {random_book.author}")

        elif choice == "5":
            # Exiting the program
            print("Looking forward to seeing you again, Bye!")
        break


# Creating an instance of the question class for all of the questions
question_1 = Questions(
    "what is your favorite genre to read when bored?",
    [
        "A. Fiction ",
        "B. Mystery ",
        "C. Thriller",
        "D. Romance",
        "E. Young Adult",
        "F. Non Fiction",
    ],
)

question_2 = Questions(
    "What is your favourite genre to read when you're feeling sad?",
    [
        "A. Fiction ",
        "B. Mystery ",
        "C. Thriller",
        "D. Romance",
        "E. Young Adult",
        "F. Non Fiction",
    ],
)

question_3 = Questions(
    "What is your favourite genre to read when you're feeling happy?",
    [
        "A. Fiction ",
        "B. Mystery ",
        "C. Thriller",
        "D. Romance",
        "E. Young Adult",
        "F. Non Fiction",
    ],
)

question_4 = Questions(
    "What is your favourite genre to read when you're feeling angry?",
    [
        "A. Fiction ",
        "B. Mystery ",
        "C. Thriller",
        "D. Romance",
        "E. Young Adult",
        "F. Non Fiction",
    ],
)

question_5 = Questions(
    "What is your favourite genre to read when you're feeling productive?",
    [
        "A. Fiction ",
        "B. Mystery ",
        "C. Thriller",
        "D. Romance",
        "E. Young Adult",
        "F. Non Fiction",
    ],
)

question_6 = Questions(
    "what is your favourite author between the one's presented?",
    [
        "A. Stephen King",
        "B. Agatha Christie",
        "C. Lee Child ",
        "D. Colleen Hoover ",
        "E. John Green",
        "F. James Baldwin",
    ],
)

question_7 = Questions(
    "What is your favourite theme in a book?",
    [
        "A. Good vs Evil",
        "B. Coming-of-age",
        "C. Death",
        "D. Love",
        "E. Morality",
        "F. Courage",
    ],
)

question_8 = Questions(
    "What human behaviour would you like to learn more about?",
    [
        "A. superpowers",
        "B. violence",
        "C. psychology",
        "D. love",
        "E. Maturing",
        "F. the history of humans",
    ],
)

question_9 = Questions(
    "What rating do you prefer a prospective book to have",
    [
        "A. zero-one",
        "B. one-tow",
        "C. two-three",
        "D. three-four",
        "E. four-five",
        "F.five",
    ],
)

question_list = [
    question_1,
    question_2,
    question_3,
    question_4,
    question_5,
    question_6,
    question_7,
    question_8,
    question_9,
]


# A list of book their instances
books = [
    Book("A game of Gods", "Scarlett St.Claire", "Fiction", 4.16),
    Book("Dark water Daughter", "HM Long", "Fiction", 4.06),
    Book("Call the Canaries Home", "Laura Barrow", "Fiction", 4.11),
    Book("The Da Vinci Code", "Dan Brown", "Fiction", 3.91),
    Book("None of this is true", "Lisa Jewell", "Mystery", 4.41),
    Book("One of us is back", "Karen McManus", "Mystery", 4.15),
    Book("Goodbye Earl", "Lessa Cross-Smith", "Mystery", 3.58),
    Book("A good House of Children", "Kate Collins", "Thriller", 3.80),
    Book("Silver Nitrate", "Silva Moreno-Garcia", "Thriller", 3.83),
    Book("Deep sky", "Yume Kittasei", "Thriller", 3.87),
    Book("House of roots and ruin", "Erin Craig", "Thriller", 4.35),
    Book("Never Lie", "Fredia McFadden", "Thriller", 4.18),
    Book("Hello Stranger", "Katherine Center", "Romance", 4.11),
    Book("In the likely event", "Rebecca Yarros", "Romance", 4.37),
    Book("People we meet on vacation", "Emily Henry", "Romance", 3.91),
    Book("The fault in our stars", "John Green", "Romance", 4.15),
    Book("Give me a sign", "Anna Sortino", "Young Adult", 4.23),
    Book("Their Vicious Games", "Joelle Wellington", "Young Adult", 4.22),
    Book("Divergent", "Veronica Roth", "Young Adult", 4.15),
    Book("The grace year", "Kim Liggett", "Young Adult", 4.15),
    Book("Strip Tees", "Kate Flannery", "Non-Fiction", 3.96),
    Book("Atomic Habits", "James Clear", "Non-Fiction", 4.49),
    Book("The diary of a young girl", "Anne Frank", "Non-Fiction", 4.19),
    Book("Educated", "Tara Westover", "Non-Fiction", 4.47),
]

# Create an empty list representing the registered profiles.
# The `login` function is going to append to the list when an user is creating a new profile.
registered_profiles = []

new_to_recs = input("Do you already have an account with bookrecs? enter yes or no ")
if new_to_recs.lower() == "yes":
    logged_in_profile = login(registered_profiles)
else:
    logged_in_profile = register()

# Call the menu function
menu(
    logged_in_profile, question_1, question_2, question_3, question_4, question_5, books
)

# Looping the menu so that user can select other options
while True:
    repeating = input("Can I help you with anything else? Type yes or no: ")
    if repeating.lower() == "yes":
        menu(
            logged_in_profile,
            question_1,
            question_2,
            question_3,
            question_4,
            question_5,
            books,
        )
    else:
        break

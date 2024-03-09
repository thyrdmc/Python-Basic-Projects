## Crypto News Alert (crypto-news-alert)
It's the project you can use for follow cryptocurrencies price actions and news.
The stock price datas in this project was provided by API requests from the [alphavantage](https://www.alphavantage.co/) webservice.
Also analyzes the daily price changes of the selected cryptocurrency and lists the news about it via [newsapi](https://newsapi.org/) webservice.
After these steps, the news is sent to your phone as sms via [twilio](https://www.twilio.com/en-us) webservice.

You need to take apikey for webservices. After you complete this step, You need to fill constant parameters with your apikeys like;

STOCK_NAME = "BTC"

NEWS_API_KEY = "your_api_key"

STOCK_API_KEY = "your_api_key"

TWILIO_SID = "your_twilio_sid"

TWILIO_AUTH_TOKEN = "your_twilio_auth_token"


## Py-Millionaire Knowledge Competition (knowledge-competition with WEB API)
It's the python version of Who Wants to be a Millionaire. The dataset in this project was provided by API requests from the https://opentdb.com/api.php webservice.
 
###  - Documentation:
<ins> Question Class </ins>

 *Attributes:
  - text
   (str) The text of the question. e.g. “The HTML5 standard was published in 2014.”
  - answer
   (booelan) The answer of the question. e.g True

<ins> QuestionMachine Class </ins>
 
 *Attributes:
  - question_list
   (list) The list of the question dataset.
  - question_number
   (int) The number of the question. e.g Question 1
  - score
   (int) Number of questions that the user answered correctly. e.g 1
  - current_question
   (int) Number of current question. e.g 1
 
 *Methods:
 - any_unused_question()
   Navigate through the dataset to check that all questions have been answered. Returns True or False

 - next_question()
   Receives the response from the user, and is sent to the function where the response is checked.
 
 - check_answer(user_answer, correct_answer)
   Parameter user_answer: (str) User's answer to the question
   Parameter correct_answer: (str) Correct answer of Question
 
 congrats to user if the user gives the correct answer, shows the user's score

 <img width="250" alt="ScreenShot" src="https://github.com/thyrdmc/Python-Basic-Projects/assets/62545306/0ecb359a-df1f-4f65-a3b9-204aafd617b8">

## Password Generator (password-generator)
This project has been developed to Mobile Phone Users.  
The project enables users to generate and store secure passwords for the mobile applications(Banking Industry App, Social Media Apps...)

###  - Documentation:
*Methods:
 - generate_password()
   Generates Randomly Complex Password for High Level Security
   
 - save_text()
   Stores Categorized User Password and Application Information(Facebook, Instagram, GarantiBBVA)
   
   
<img width="611" alt="Ekran Resmi 2023-08-26 19 35 58" src="https://github.com/thyrdmc/Python-Basic-Projects/assets/62545306/6f2d130a-c1f9-4320-a57a-b727796f782e">


## Time Manager for Students (timeManager)
This project has been developed to [increase students' efficiency](https://en.wikipedia.org/wiki/Pomodoro_Technique) in studying. 
The [tkinter](https://docs.python.org/3/library/tkinter.html) library was used during the development of the project.

###  - Documentation:
*Methods:
 - reset_timer()
   Sets timer to reset for a student who wants to start a new study plan
   
 - start_timer()
   Starts the timer depending on what stage of the plan we are in

 - countdown()
   Determines where we are in the plan. (WORK- LONG BREAK - SHORT BREAK)

*Constants:
 SB_COLOR, LB_COLOR, RED, YELLOW, DARK_GREEN, FONT_NAME, WORK_MIN, SHORT_BREAK_MIN, LONG_BREAK_MIN, REPS, TIMER


## Cost Calculator (costCalculator)
This project was developed to save users from the complexity of calculating the cost of purchases made on Exchanges and Cryptocurrencies.
The [tkinter](https://docs.python.org/3/library/tkinter.html) library was used during the development of the project.

###  - Documentation:
*Methods:
 - calculate()
   It calculates the cost over the data in the csv file.
   
 - button_clicked()
   Adds the new data entered in the textboxes by the user to the dataset.


## Crossy Road Arcade Game (crossy-road-game)
It's the python version of [Crossy Road Game](https://apps.apple.com/us/app/crossy-road/id924373886).
This project was developed using [Turtle library](https://docs.python.org/3/library/turtle.html#).

###  - Documentation:
<ins> Player Class </ins>
 
 *Attributes:
  - The Turtle library is inherited.

 *Methods:
 - walk()
   Provides the object controlled by the user to move.
   
 - is_finish()
   Checks if the user has reached the endpoint. Returns True or False

<ins> Scoreboard Class </ins>
 
 *Attributes:
   - The Turtle library is inherited.
   - level
   (int) Returns level of the game. e.g. “Level 5”

 *Methods:
 - next_level()
   Provides to switch to the new section of game.
   
 - game_over()
   Controls the ending condition of the game. If game is over, prints to screen "Game Over"

- clear_board()
   Clears the screen when switching to a new section of game.

<ins> CarManager Class </ins>
 
 *Attributes:
   - all_cars
   (array) To store car objects. e.g. “[]”
   - speed
   (int) Represents the speed of the car. e.g. “5”

 *Methods:
 - create_cars()
   Produces cars at random positions on the initial axis.
   
 - move()
   Provides the cars to move.

- increase_speed()
   Provides to increase the speed of the cars to a certain extent.


## Best Eleven Guessing Game (best-eleven-guessing-game)
This python project is a game that tries to make the fans guess 11 players from Fenerbahce football history.
It includes the python version of the project whose mobile application will be made.

<img width="700" alt="Best 11 Guessing Game" src="https://github.com/thyrdmc/Python-Basic-Projects/assets/62545306/8cc8e407-2bee-45fa-9eeb-bbad108a2a2f">


## T-Hirst's NFT Creator Project (T-Hirst's-painting)
This project was developed to produce [NFT](https://www.theverge.com/22310188/nft-explainer-what-is-blockchain-crypto-art-faq) images.
[The works of Damien Hirst](https://en.wikipedia.org/wiki/Damien_Hirst) were inspired while producing the paintings.


## Py-Millionaire Knowledge Competition (knowledge-competition)

It's the python version of Who Wants to be a Millionaire.

###  - Documentation:
<ins> Question Class </ins>
 
 *Attributes:
  - text
   (str) The text of the question. e.g. “The HTML5 standard was published in 2014.”
  - answer
   (booelan) The answer of the question. e.g True

<ins> QuestionMachine Class </ins>
 
 *Attributes:
  - question_list
   (list) The list of the question dataset.
  - question_number
   (int) The number of the question. e.g Question 1
  - score
   (int) Number of questions that the user answered correctly. e.g 1
 
 *Methods:
 - any_unused_question()
   Navigate through the dataset to check that all questions have been answered. Returns True or False

 - next_question()
   Receives the response from the user, and is sent to the function where the response is checked.
 
 - check_answer(user_answer, correct_answer)
   Parameter user_answer: (str) User's answer to the question
   Parameter correct_answer: (str) Correct answer of Question
 congrats to user if the user gives the correct answer, shows the user's score


## Python-Basic-Project-1 (coffee_machine.py)
This project includes the software prepared for the coffee machine. This coffee machine has 5 different commands for users.

About Software Development Stages;
 - This project was developed in 4 phases.
 - Function <b>check_resources</b> checks the amount of resources for the coffee the user wants.
 - Function <b>check_money</b> compares the price of coffee with the money entered by the user.


## Python-Basic-Project-3 (find_your_speciality.py)
 This project is for Computer Engineering students. The game guides how they should progress in the sector in line with their interests.

<img width="869" alt="Find Your Speciality" src="https://user-images.githubusercontent.com/62545306/223971403-e1c89acd-984e-421d-ad21-1375f91fc45d.png">


## Python-Basic-Project-4 (python_auction.py)
 This program has been developed to manage secret  auctions.
 
 <img width="794" alt="Python Auction" src="https://user-images.githubusercontent.com/62545306/235444892-2531f05b-4ec3-41ad-b426-3ad02880b7b0.png">


## Python-Basic-Project-5 (caesar_chiper.py)
 This project is for encryption and decryption program to users wanna send private message.
 
 <img width="518" alt="Caesar Chiper" src="https://user-images.githubusercontent.com/62545306/235106874-10165409-5493-4614-87c0-36c05dc96e03.png">


## Python-Basic-Project-6 (rock-paper-scissors.py)
 This project is for playing game with Computer that people who are bored. 
 
 <img width="869" alt="Rock Paper Scissors" src="https://user-images.githubusercontent.com/62545306/228789030-c84bc671-2762-49f4-8b70-6c10470f4531.png">


## Python-Basic-Project-7 (hangman.py)
 This project is for playing game with Computer that people who are bored. 
 
 <img width="650" alt="Hangman" src="https://user-images.githubusercontent.com/62545306/234534275-f65efd2d-ac58-4808-bf21-4afcc15d446f.png">


## Python-Basic-Project-8 (higher_lower_game.py)
 This project includes Game of Guessing Instagram Followers of Famous Persons.

<img width="534" alt="Higher_Lower_Game" src="https://github.com/thyrdmc/Python-Basic-Projects/assets/62545306/da92d40f-3fe0-47c5-bd9e-005f2aded979">


## Python-Basic-Project-9 (password-generator.py)
 This project includes Password Generator App for Users.

#### Example for Password Generator : 

 Welcome to the Password Generator!
 
 How many letters would you like in your password?
 
 3
 
 How many symbols would you like?
 
 1
 
 How many numbers would you like?
 
 1
 
 Your password is h6zZ$

 
## Python-Basic-Project-10 (password-generator.py)
 This project includes a basic Calculator Program with simple UI for users.
 
 <img width="878" alt="Py-Calc Program" src="https://user-images.githubusercontent.com/62545306/235683162-2f315a72-9006-4792-b6bf-705e945c7ac6.png">

 
 ## Python-Basic-Project-11 (blackjack-game.py)
 This project includes a Blackjack Game with simple UI for users.

<img width="524" alt="BlackJack Game" src="https://github.com/thyrdmc/Python-Basic-Projects/assets/62545306/c1d18eb5-9a16-4f98-96b5-a16a95d9a8a2">


 ## Python-Basic-Project-12 (guess-number.py)
 This project includes a Guess Number Game with simple UI for users.

<img width="838" alt="Guess Number Game" src="https://github.com/thyrdmc/Python-Basic-Projects/assets/62545306/46d5e308-a21b-4448-9c2d-f5691eb9aa4e">


## Python-Basic-Project-13 (flatten_and_reverse_function.py)
 This project includes Flattening and Reversing functions for Multi-Layer Lists.

#### Example for Flattening Function : 

 input: [[1, 'a', ['cat'], 2], [[[3]], 'dog'], 4, 5]
 
 output: [1, 'a', 'cat', 2, 3, 'dog', 4, 5]
 
#### Example for Reversing Function :

 input: [[1, 2], [3, 4], [5, 6, 7]]
 
 output: [[[7, 6, 5], [4, 3], [2, 1]]


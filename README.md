# [WEATHER WISE](https://weather-wise-project-e6ccd7a6b753.herokuapp.com)

[![GitHub commit activity](https://img.shields.io/github/commit-activity/t/AshLaw96/weather-wise)](https://github.com/AshLaw96/weather-wise/commits/main)
[![GitHub last commit](https://img.shields.io/github/last-commit/AshLaw96/weather-wise)](https://github.com/AshLaw96/weather-wise/commits/main)
[![GitHub repo size](https://img.shields.io/github/repo-size/AshLaw96/weather-wise)](https://github.com/AshLaw96/weather-wise)

---

Weather Wise is a multiple choice weather quiz that users can play to help improve there knowledge about weather and is a fun game for all ages, so everyone can play.

When a user first opens the quiz it will show a menu with a title and a brief overview of what it actually is. Below this it will then show a list of options with what the user would like to do next. Depending on there choice it will either start the game, show the instructions on how to play the game or quit the game. If the user inputs an incorrect value they will then be informed that whatever they have just inputted was incorrect and they need to write either 1, 2 or 3 depending on there choice. With the second option been chosen, it will then ask the user what level of difficulty the user would like for example easy, medium or hard. Again if the user inputs an incorrect value it will tell them that they have done so and need to write either 1, 2 or 3. Following there choice it will then ask how many questions they would like to answer for example 10, 20 or 30. Once more if the user didn't type a correct value it will tell them so and that they need to type either 1, 2 or 3. After this the app will then access data from the questions library and start asking randomly chosen multiple choice questions up until the user has answered there desired amount, for example what is rain? a. god peeing b. condensation from clouds c. water squirting from plains d. water that falls from clouds in the sky, that happens when tiny water droplets in the clouds join together and become too heavy to stay in the air. Once again if the user doesn't input a, b, c or d for any question they will be told to write a correct value from the options given. When the quiz has been finished there score will be toted up and then shown to the user, then the user will be asked if they would like to play again or quit the game. If the user doesn't input a correct value again they will be informed of this and asked to input a correct value. Providing they have chosen a correct value it will either take them to the menu or show message saying thank you for playing, goodbye. However at the menu screen if the user inputted the second option the app will then show the user how to play the quiz and once they have read this it will return them back to the menu. Finally if the user chose the last option it will then double check they want to quit and if they do show the thank you for playing, goodbye. 

Deployed site:
https://ui.dev/amiresponsive?url=https://weather-wise-project-e6ccd7a6b753.herokuapp.com

![screenshot](documentation/mockup.png)

source: [amiresponsive](https://ui.dev/amiresponsive?url=https://weather-wise-project-e6ccd7a6b753.herokuapp.com)

---

## User Stories

### New Site Users

- As a new site user, I would like to be able to know what the program does, so that I can quickly decide if I want to continue.
- As a new site user, I would like to know how to play the quiz, so that I can easily understand what I need to do and start playing.
- As a new site user, I would like to choose how hard the quiz is, so that I can challenge myself with harder questions.
- As a new site user, I would like to choose the amount of questions I get asked, so that I don't get bored.
- As a new site user, I would like to keep playing the game as many times as I want, so that I can keep learning interesting facts about the weather.

### Returning Site Users

- As a returning site user, I would like to be able to try answering any question again if I didn't input one of the given options, so that my score isn't effected because of this.
- As a returning site user, I would like to be able to see my high score, so that I can try and beat it and improve my knowledge.
- As a returning site user, I would like to have different questions asked, so that I'm not repeating the same questions every time I play.
- As a returning site user, I would like to see different icons or images, so that I can be visually pleased whilst learning cool facts at the same time.
- As a returning site user, I would like to see other peoples high score, so that I can try and get on the top of the leaderboard.

## Features

### Existing Features

- **Header section**

  - This will show the user what the app is called and a brief explanation of what it actually does.  

![screenshot](documentation/features/head.png)

- **Menu section**

  - The app will then show three options 1. Play quiz 2. How to play 3. Quit. The user will then be asked to either input 1, 2 or 3 depending on what they would like to do.

![screenshot](documentation/features/menu.png)

- **Incorrect input for menu**

  - If the user inputted an incorrect value the app will show that there value was not correct and the need to input either 1, 2 or 3.

![screenshot](documentation/features/menu-error.png)

- **Level option**

  - When the user chooses the 2nd option on the menu the program will then ask the user what difficulty level they would like. 1. Easy 2. Medium 3. Hard. The user will then be asked to input either 1, 2 or 3. 

![screenshot](documentation/features/level.png)


- **Incorrect Level option**

  - If the user choose an option that wasn't there they will be informed that there value was incorrect and that they would need to type either 1, 2 or 3.

![screenshot](documentation/features/level-error.png)

- **Amount option**

  - Once the user has chosen there difficulty they will then be asked how many questions they will like to be asked and they will again need to type 1,2 or 3.

![screenshot](documentation/features/amount.png)

- **Incorrect amount option**

  - If the user choose an option that wasn't there they will be informed that there value was incorrect and that they would need to type either 1, 2 or 3.

![screenshot](documentation/features/amount-error.png)

- **Rules option**

  - If the user chooses the rules choice in the menu screen, the program will show the user instructions on how to play the game and once they have read the rules the program will take them back to the menu.

![screenshot](documentation/features/rules.png)

- **Quit option**

  - When the user chooses the quit option, the program will ask the user if they are sure they want to quit and if so to press Y/y but if not to press N/n which will return them to the main menu. If they do type Y/y it will show a message saying thankyou for playing, goodbye.

<details>
<summary> Click here to view the quit options </summary>

Y/y or N/n

![screenshot](documentation/features/quit.png)

Y/y input

![screenshot](documentation/features/quit-yes.png)

</details>

- **Incorrect quit option**

  - If the user typed an incorrect value they will be informed that there value was incorrect and that they would need to type either Y/y or N/n.

![screenshot](documentation/features/quit-error.png)

- **The quiz**

  - When the player has chosen there difficulty level and how many questions they would like to answer, the app will then access the questions library and choose data from the chosen level and pick random question from it and start asking the user until there chosen amount has been completed.

![screenshot](documentation/features/quiz.png)

- **Incorrect value for quiz**

  - If the user inputs an incorrect value they will be shown that there input is incorrect and they must type either A/a, B/b, C/c or D/d.

![screenshot](documentation/features/quiz-error.png)

- **Correct and incorrect values**

  - When the user answers a question the program will inform the user if they got the answer right or wrong.

<details>
<summary> Click here to see both right and wrong answers </summary>

Correct

![screenshot](documentation/features/right.png)

Incorrect

![screenshot](documentation/features/wrong.png)

</details>

- **Score**

  - When the user has finished the quiz there score will be toted up and then printed to the screen showing them what they have achieved and will ask them to enter there name.

![screenshot](documentation/features/score.png)

- **Finished**

  - Once the user has received there score they will be informed that their score has been added to a leaderboard. They will then be asked if they would like to play again or quit, if they chose option 1 it will take the back to the menu if they chose option 2 it will then ask again if they are sure they would like to quit and if not it will take them to the menu but if they do it will show them the message thankyou for playing, goodbye.

<details>
<summary> Click here to view the finished game options </summary>

leaderboard

![screenshot](documentation/features/leaderboard.png)

options

![screenshot](documentation/features/play-again.png)

</details>

- **Incorrect value at finish**

  - If the user inputs an incorrect value they will be shown that there input is incorrect and they must type either Y/y or N/n.

![screenshot](documentation/features/play-again-error.png)

### Future Features

1. Allow users to play split-screen or multiplayer.
2. Add the leaderboard to the program so users can see the high score.
3. Add links to other quizzes or cool facts about weather.
4. Make leaderboard put the highest scores at the top of the leaderboard and only add top 10 scores for each difficulty and for each amount of questions answered.
5. Add sound effects to the program.
6. Add error validation for name (name must be > 2 but < 15 and only include letters).

## Tools & Technologies Used

- [![Markdown Builder](https://img.shields.io/badge/Markdown_Builder-grey?logo=markdown&logoColor=000000)](https://tim.2bn.dev/markdown-builder) used to generate README and TESTING templates.
- [![Git](https://img.shields.io/badge/Git-grey?logo=git&logoColor=F05032)](https://git-scm.com) used for version control. (`git add`, `git commit`, `git push`)
- [![GitHub](https://img.shields.io/badge/GitHub-grey?logo=github&logoColor=181717)](https://github.com) used for secure online code storage.
- [![Gitpod](https://img.shields.io/badge/Gitpod-grey?logo=gitpod&logoColor=FFAE33)](https://gitpod.io) used as a cloud-based IDE for development.
- [![Python](https://img.shields.io/badge/Python-grey?logo=python&logoColor=3776AB)](https://www.python.org) used as the back-end programming language.
- [![Heroku](https://img.shields.io/badge/Heroku-grey?logo=heroku&logoColor=430098)](https://www.heroku.com) used for hosting the deployed back-end site.
- [![Google Sheets](https://img.shields.io/badge/Google_Sheets-grey?logo=googlesheets&logoColor=34A853)](https://docs.google.com/spreadsheets) used for storing data from my Python program for the leaderboard.
- [![ChatGPT](https://img.shields.io/badge/ChatGPT-grey?logo=chromatic&logoColor=75A99C)](https://chat.openai.com) used to help generate weather questions.
- [![Draw.io](https://img.shields.io/badge/Draw.io-grey?logo=diagramsdotnet&logoColor=#F08705)](https://www.draw.io) used for creating the flowchart of the Python program.

## Data Model

### Flowchart

To follow best practice, a flowchart was created for the app's logic,
and mapped out before coding began using a free version of
[Draw.io](https://www.draw.io).

Below is the flowchart of the main process of this Python program. It shows the entire cycle of the program.

![screenshot](documentation/flowchart.png)

I used Mermaid to create an interactive flowchart as well.

``` mermaid
flowchart TD
    Start([Start]) --> A1[Show menu of what the user needs to do and what the app does e.g. info of what program actually is 1. press 1 to show instructions 2. press 2 to play game 3. press 3 to quit.]
    A1 --> B1[Asks user what difficulty level they want for example 1. easy 2. medium 3. hard]
    B1 --> C1{1, 2 or 3}
    C1 --> D1[Check what difficulty the user has inputted and then ask how many questions they want to answer e.g. 1. press 1 for 10 questions 2. press 2 for 20 questions 3. press 3 for 30 questions.]
    D1 --> E1{1, 2 or 3}
    E1 --> F1[Checks what amount the user would like then access data from the questions library and pulls random questions from this.]
    F1 --> G1[Starts the quiz asking the user multiple choice questions e.g. what is a cloud? a. pillow b. the sky c. a group of tiny water droplets or ice crystals that float in the sky d. rain]
    G1 --> H1{a, b, c or d}
    H1 --> I1[When the user has answered their chosen amount of questions, they will then show their score and be asked to input their name.]
    I1 --> J1[Their score will then be added to a leaderboard and they will then be asked if they'd like to play again or quit e.g. 1. press 1 to play again 2. press 2 to quit]
    J1 --> K1{1 or 2}
    K1 --> |1| A1
    K1 --> |2| End([End])

    A1 --> L1[Shows the user instructions on how to play the game.]
    A1 --> M1[Shows a message making sure the user wants to quit the game e.g. 1. press 1 to keep playing 2. press 2 to quit.]
    A1 --> N1[Incorrect input by user shows they inputted incorrect value and what they need to type.]
    N1 --> A1
```

Source: [Mermaid](https://mermaid.live/edit#pako:eNptVcFy2zgM_RWMLtvOOBpTquPEh91Jk7RNu9tLOrMza-dAi5TNsURqSaqu6uTfFyAlW27WB1smgAe8RwA6JIURMlkkZWX2xZZbD9_uVhrw8-jx35tl-Hl6CxcXv8MNWz5uzR5qqVswJey33IPfSmidtKClFA68AWGAa3Gy8qbBM-lAppsUlC7NMbixZmN5DbzwLa-qDpQDluKxdPhAYI4SKu28bQuvjHaQDfaM7E3FO9jwWkI-nOd0_m-rfPoUqdywUP57trxxOxerDemFKktVtJXvoJLfZUXldrDn2kNpLMgfvG4qSRVJ7jrKXEuh2ppyoViix38f8W_ZgU2wKozMX6LlNlru2PJ2K4vdq6xH8bbcIcum9V6KoB5aNHC3gyA41x0yki4qcKrSk9RujwBB25F0VD-bjoJGspEtG9tG0pEtH9kGDe8ik_vXHO-j5UPP0UWSvDatHnXH3rSVgErtZE-tKCih4J5DaU0dPE8VVWptue2CFE1bVQ4sPqLbyaWPUscSP8RCPrLYtK6HVD9JR6U3p2JqFF_RzRZbo4px3iBjIICdyKGoTCv-AI76qApHBNZpQHG7DooUHTbWtA21s1ea7sQjurAGsTE_ikTohe2c5xXVg7g4aYSujzgiRW5K9yQ-RhKf2IFPYD2BglBEL_WnaHxgy79Jw7PuiX0gQ-coS8wcyRyvAQs8cpz0_YOE4lWEEYtRrjBWBtHXklQjOBMbs_fQOGqD4A-xnM9s-W0UfQImDCEiBscJ40LatcG5GTq8-8U5JFRlMP02dEs_43yDIpEYNNmv2v3c63xFUEBf8edY8RfsYoLKel2_xONn9oy74vwoe4Z7Ld4s8evp7UqfLZQ_4z50p4s4W1RGh-EdSiOnzUi9HuSvAYTjcnGObySOe2hX11o5GiCcdzfQOYL9nxA7KZuQkkBeS_FL_q9s-aDx4qwsfH_T6y6mdAO57rSb1NH3O69aebbpu_AOoDy-a448v7L-5bHSySSppa25EvjKOZB5lWBcLVfJAh8Ft7tVstIv6Mdbbx47XSQLFFROEpyzzTZZlDhH-K9tcHHIO8Xp7TG4NFwni0PyI1mwS5bOsun8cjqb5lPG8nySdMnigrGr9OqSzbPrbHb97jqf5y-T5KcxCMFSdjWfz9m7_Ho2y_LpnAXAf4KR8F_-Ay4fVeQ)

### Classes & Functions

The program uses classes as a blueprint for the project's objects (OOP). This allows for the object to be reusable.

```python
class SelectionChecker:
    """  Check user input and display errors if input is invalid. """
    def __init__(self, selections):
        self.selections = selections
```

```python
class CheckerFactory:
    """   Provides different types of selection checkers based on input. """
    @staticmethod
```

```python
class UIManager:
    """  Handles the starting functions so the program can run. """
    def __init__(self):
        pass
```

```python
class QuizGame:
    """  Handles all the game functions. """
    def __init__(self):
        self.difficulty = None
        self.num_questions = None
        self.total_score = 0
```

```python
class LeaderboardManager:
    """  Authenticates to the Google Sheets API and returns the sheet object. """
    def __init__(self):
        self.sheet = None
```

```python
class StyleHelper:
    """  Handles all the styling operations and definitions. """
```

```python
class ProgramHelper:
    """  Handles all the helper functions. """
```

The primary functions used on this application are:

- `menu()`
  - Shows the first screen the user sees allowing them to choose what they want to do first.
- `header()`
  - Shows the title and all of its styles and content.
- `checker()`
  - Adds code validation for the menu section if a user inputs incorrect values.
- `remove()`
  - Clears the content allowing user to see what's running next.
- `rules()`
  - Shows how to play the game and adds all of it's styling for this section.
- `exit()`
  - Allows the user to end the game and all the styling for this section.
- `exit_checker()`
  - Adds code validation for the exit section if a user inputs incorrect values.
- `level_selector()`
  - Let's the user choose what level of difficulty they would like the questions to be and adds styling for this section.
- `level_checker()`
  - Adds code validation for the level section if a user inputs incorrect values.
- `questions_amount()`
  - Let's the user choose how many questions they would like to answer and adds styling for this section.
- `amount_checker()`
  - Adds code validation for the amount section if a user inputs incorrect values.
- `random_questions()`
  - Selects the chosen amount and difficulty of questions the user asked for and randomly picks from the specified category and adds the styling.
-  `qst_checker()`
  - Adds code validation for the question section if a user inputs incorrect values.
- `next_qst()`
  - Brings up the next question and checks if the user is correct or not.
- `user_answered_select()`
  - Shows the questions and choices and makes sure the user inputted correctly and if not informs them.
- `auth_g_sheets()`
  - Sets up Google Sheets API and returns the correct worksheet based on difficulty.
- `update_leaderboard()`
  - Updates the Google Sheets leaderboard with the user's name, score, amount of questions answered and the time/date.
- `loading_message()`
  - Used to create a message that makes the dots after it appear one by one after so many seconds.
- `main()`
    - Run all program functions.

### Imports

I've used the following Python packages and/or external imported packages.

- `gspread`: used with the Google Sheets API
- `google.oauth2.service_account`: used for the Google Sheets API credentials
- `time`: used for adding time delays
- `os`: used for adding a `remove()` function
- `colorama`: used for including color in the terminal
- `random`: used to get a random choice from a list
- `questions`: used to pull all the questions from my own made file
- `helpers`: used to pull helper variables and functions
- `game`: used for all the game functions the program uses
- `checks`: used for error handling
- `string`: used for adding `ascii_lowercase`
- `datetime`: used for adding the current time and date
- `sys`: used to exit the program

## Testing

> [!NOTE]  
> For all testing, please refer to the [TESTING.md](TESTING.md) file.

## Deployment

Code Institute has provided a [template](https://github.com/Code-Institute-Org/python-essentials-template) to display the terminal view of this backend application in a modern web browser.
This is to improve the accessibility of the project to others.

The live deployed application can be found deployed on [Heroku](https://weather-wise-project-e6ccd7a6b753.herokuapp.com).

### Heroku Deployment

This project uses [Heroku](https://www.heroku.com), a platform as a service (PaaS) that enables developers to build, run, and operate applications entirely in the cloud.

Deployment steps are as follows, after account setup:

- Select **New** in the top-right corner of your Heroku Dashboard, and select **Create new app** from the dropdown menu.
- Your app name must be unique, and then choose a region closest to you (EU or USA), and finally, select **Create App**.
- From the new app **Settings**, click **Reveal Config Vars**, and set the value of KEY to `PORT`, and the value to `8000` then select *add*.
- If using any confidential credentials, such as CREDS.JSON, then these should be pasted in the Config Variables as well.
- Further down, to support dependencies, select **Add Buildpack**.
- The order of the buildpacks is important, select `Python` first, then `Node.js` second. (if they are not in this order, you can drag them to rearrange them)

Heroku needs three additional files in order to deploy properly.

- requirements.txt
- Procfile
- runtime.txt

You can install this project's **requirements** (where applicable) using:

- `pip3 install -r requirements.txt`

If you have your own packages that have been installed, then the requirements file needs updated using:

- `pip3 freeze --local > requirements.txt`

The **Procfile** can be created with the following command:

- `echo web: node index.js > Procfile`

The **runtime.txt** file needs to know which Python version you're using:
1. type: `python3 --version` in the terminal.
2. in the **runtime.txt** file, add your Python version:
	- `python-3.12.2`

For Heroku deployment, follow these steps to connect your own GitHub repository to the newly created app:

Either:

- Select **Automatic Deployment** from the Heroku app.

Or:

- In the Terminal/CLI, connect to Heroku using this command: `heroku login -i`
- Set the remote for Heroku: `heroku git:remote -a app_name` (replace *app_name* with your app name)
- After performing the standard Git `add`, `commit`, and `push` to GitHub, you can now type:
	- `git push heroku main`

The frontend terminal should now be connected and deployed to Heroku!

### Local Deployment

This project can be cloned or forked in order to make a local copy on your own system.

For either method, you will need to install any applicable packages found within the *requirements.txt* file.

- `pip3 install -r requirements.txt`.

If using any confidential credentials, such as `CREDS.json` or `env.py` data, these will need to be manually added to your own newly created project as well.

#### Cloning

You can clone the repository by following these steps:

1. Go to the [GitHub repository](https://github.com/AshLaw96/weather-wise) 
2. Locate the Code button above the list of files and click it 
3. Select if you prefer to clone using HTTPS, SSH, or GitHub CLI and click the copy button to copy the URL to your clipboard
4. Open Git Bash or Terminal
5. Change the current working directory to the one where you want the cloned directory
6. In your IDE Terminal, type the following command to clone my repository:
	- `git clone https://github.com/AshLaw96/weather-wise.git`
7. Press Enter to create your local clone.

Alternatively, if using Gitpod, you can click below to create your own workspace using this repository.

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/AshLaw96/weather-wise)

Please note that in order to directly open the project in Gitpod, you need to have the browser extension installed.
A tutorial on how to do that can be found [here](https://www.gitpod.io/docs/configure/user-settings/browser-extension).

#### Forking

By forking the GitHub Repository, we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original owner's repository.
You can fork this repository by using the following steps:

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/AshLaw96/weather-wise)
2. At the top of the Repository (not top of page) just above the "Settings" Button on the menu, locate the "Fork" Button.
3. Once clicked, you should now have a copy of the original repository in your own GitHub account!

### Local VS Deployment

No differences were found between the local version and the live deployed version of the program.

## Credits

| Source | Location | Notes |
| --- | --- | --- |
| [Markdown Builder](https://tim.2bn.dev/markdown-builder) | README and TESTING | tool to help generate the Markdown files |
| [YouTube](https://www.youtube.com/watch?v=u51Zjlnui4Y) | PP3 terminal | tutorial for adding color to the Python terminal |
| [Chatgpt](https://chatgpt.com/c/66f43ff0-2720-8004-b795-ec70470e8df6) | question.py | used to generate randomly made multiple choice questions |
| [geeksforgeeks](https://www.geeksforgeeks.org/clear-screen-python/) | helpers.py | used for looking how to clear the terminal using the `os` library |
| [W3schools](https://www.w3schools.com/python/ref_string_format.asp) | helpers.py | used `format()` method to be able to center text |
| [geeksforkeeks](https://www.geeksforgeeks.org/sleep-in-python/) | helper.py | used to understand how to use the `sleep()` method with the imported `time` library |
| [Python Docs](https://docs.python.org/3/library/sys.html) | helpers.py | used to understand how to use the `quit()` method with the imported `sys` library |
| [W3Schools](https://www.w3schools.com/python/ref_random_sample.asp) | helpers.py | used to understand how to use `sample()` method from the `random` library |
| [Python Docs](https://docs.python.org/3/library/string.html) | helper.py | used to understand how to use `ascii_lowercase` method from the `string` library |
| [Python Docs](https://docs.python.org/3/whatsnew/3.8.html) | helpers.py | used to understand how to use the walrus operator `:=` |
| [Python Docs](https://docs.python.org/3/library/datetime.html) | helpers.py | used to understand how to use the `timestamp` method from the `datetime` library |
| [W3Schools](https://www.w3schools.com/python/python_datetime.asp) | helpers.py | understand how to use `now().strftime()` method from the `datetime` library |
| [geeksforgeeks](https://www.geeksforgeeks.org/python-staticmethod-function/) | checks.py | used to understand how to use `@staticmethod` in a `class` so that `__init__` is not required |
| [W3Schools](https://www.w3schools.com/python/ref_keyword_pass.asp) | run.py | used to understand how to use the `pass` keyword so that the program does not bring up a error |

### Media

| Source | Location | Type | Notes |
| --- | --- | --- | --- |
| [TinyPNG](https://tinypng.com) | entire site | image | tool for image compression |
| [GetEmoji](https://getemoji.com/#symbols) | helpers.py | used to add emoji's to the program |

### Acknowledgements

- I would like to thank my Code Institute mentor, [Tim Nelson](https://github.com/TravelTimN) for his support throughout the development of this project.
- I would like to thank the [Code Institute Slack community](https://code-institute-room.slack.com) for the moral support; it kept me going during periods of self doubt and imposter syndrome.
- I would like to thank my partner (Megan), for believing in me, and allowing me to make this transition into software development.

# MY PERSONAL APP
#### Video Demo:  <URL HERE>
#### Description:
- What is my project?
For this project I decided to make something that would help me achieve faster without resorting to normal ways.
In this app I made a Personal Translator, a Birthday Checker and a Reminder.

- The Personal Translator:
    - I decided to make a personal translator as I use Google Translate quite ofter to translate some languages(i.e. Korean, Portuguese, or other when needed) to English.
    - For this part, I used Google Translator API to translate sentences that the user inputs in the command line.
    - I tested between TextBlob and Google Translator and felt more comfortable using the Google one.

    #### How to use:
    ```
    python project translator
    or
    python project -t
    ```

    It will prompt the user for the sentence they wish to translate to English.


- Birthday Checker:
     As a person that doesn't use social platforms and prefer direct contact with friends or family, I decided to make an app that I can add birthdays and then check everytime I come to the computer and run the program it checks if I have any birthday that day.
     In this app I can add birthdays of friends/family, instead of using the normal datetime library I used another one that is also pretty popular called [Arrow](https://pypi.org/project/arrow/).
     Another library used is [Plyer](https://pypi.org/project/plyer/) to trigger a popup notification in Windows.
     The app then takes the day/month followed by the person's first and last name (i.e. 2305 Tino Hernandez)
     The birthday dates are saved in a .txt file.

    #### How to use:
    ```
    python project birthday
    or
    python project -b
    ```
    It will prompt the user for "add" or "check".
    - Add -> To insert a new birthday
    - Check -> To check if there is a birthday in the given day

    Once used check the program will open the .txt file and check if there is a birthday today.
    If there is a birthday that day, a Windows notification will appear telling the user which person's birthday is that day.

- Reminder:
    As a person that spends an alot of time in computer sometimes I forget tasks that I wanted to do or attend during that day, so I made a reminder to remember me about the given event.
    Using also [Arrow](https://pypi.org/project/arrow/) to calculate the time needed to trigger the notification by using the Time Library already incorporated in python, using time.sleep() to then activate the popup using [Plyer](https://pypi.org/project/plyer/).

    #### How to use:
    ```
    python project reminder
    or
    python project -r
    ```

    It will prompt the user for a hour in the 24 Hour Format(i.e. 19:20).
    Using arrow to check if the format is correct, otherwise it will raise an error.
    Note: The app needs to be running in background in order to trigger the reminder.

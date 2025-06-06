# Text Analyzer Challenge for Engeto's Python Academy

### Assignment

In this project, your goal is to create a text analyzer that can process text of any length and extract various information from it.
Before you begin, you'll work with pre-prepared texts. This will make it easier to check your code. Copy these texts into your file:

```python
TEXTS = [
    '''Situated about 10 miles west of Kemmerer,
    Fossil Butte is a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley
    to an elevation of more than 7500 feet
    above sea level. The butte is located just
    north of US 30 and the Union Pacific Railroad,
    which traverse the valley.''',
    '''At the base of Fossil Butte are the bright
    red, purple, yellow and gray beds of the Wasatch
    Formation. Eroded portions of these horizontal
    beds slope gradually upward from the valley floor
    and steepen abruptly. Overlying them and extending
    to the top of the butte are the much steeper
    buff-to-white beds of the Green River Formation,
    which are about 300 feet thick.''',
    '''The monument contains 8198 acres and protects
    a portion of the largest deposit of freshwater fish
    fossils in the world. The richest fossil fish deposits
    are found in multiple limestone layers, which lie some
    100 feet below the top of the butte. The fossils
    represent several varieties of perch, as well as
    other freshwater genera and herring similar to those
    in modern oceans. Other fish such as paddlefish,
    garpike and stingray are also present.'''
]
```

The program should:
1. Ask the user for their username and password
2. Check if the entered credentials match any registered users
3. If registered, greet them and allow them to analyze texts
4. If not registered, notify them and terminate the program

Your solution should be uploaded to a file named `main.py` (if you name the file differently, it won't be accepted). The repository should contain only one .py file with the output (if you split it into main_1.py and main_2.py, it won't be accepted). Each project has its own separate repository (one repository for project 1, another for the next project, etc.).

Registered users are:

```python
+------+-------------+
| user |   password  |
+------+-------------+
| bob  |     123     |
| ann  |   pass123   |
| mike | password123 |
| liz  |   pass123   |
+------+-------------+
```

The program should let the user choose between three texts stored in the `TEXTS` variable:
- If the user selects a text number that isn't in the assignment, the program should notify them and exit
- If the user enters input other than a number, the program should notify them and exit

For the selected text, calculate the following statistics:
- Number of words
- Number of words starting with a capital letter
- Number of words written in uppercase
- Number of words written in lowercase
- Number of numbers (not digits)
- Sum of all numbers (not digits) in the text

The program should display a simple bar graph representing the frequency of different word lengths in the text. For example:

```python
# ...
 7| * 1
 8| *********** 11
 9| *************** 15
10| ********* 9
11| ********** 10
```

When running, the process should look like this:

```bash
$ username:bob
$ password:123
----------------------------------------
Welcome to the app, bob
We have 3 texts to be analyzed.
----------------------------------------
Enter a number btw. 1 and 3 to select: 1
----------------------------------------
There are 54 words in the selected text.
There are 11 titlecase words.
There are 1 uppercase words.
There are 38 lowercase words.
There are 4 numeric strings.
The sum of all the numbers 8540
----------------------------------------
LEN|  OCCURENCES  |NR.
----------------------------------------
  1|*                   |1
  2|**********          |10
  3|*****               |5
  4|***********         |11
  5|************        |12
  6|***                 |3
  7|****                |4
  8|*****               |5
  9|*                   |1
 10|*                   |1
 11|*                   |1
```

If the user is not registered:
```bash
$ username:marek
$ password:123
$ unregistered user, terminating the program..
```

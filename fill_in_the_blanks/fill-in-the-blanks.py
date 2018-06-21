# IPND Stage 2 Final Project

# Fill-in-the-Blanks quiz
# Your quiz will prompt a user with a paragraph containing several blanks.
# The user should then be asked to fill in each blank appropriately to complete the paragraph.
# This can be used as a study tool to help you remember important vocabulary!

EASY = {'text':'''A common first thing to do in a language is display
'Hello __1__!'  In __2__ this is particularly easy; all you have to do
is type in:
__3__ "Hello __1__!"
Of course, that isn't a very useful thing to do. However, it is an
example of how to output to the user using the __3__ command, and
produces a program which does something, so it is useful in that capacity.

It may seem a bit odd to do something in a Turing complete language that
can be done even more easily with an __4__ file in a browser, but it's
a step in learning __2__ syntax, and that's really its purpose.''','answers':['world','Python','print','html']}

MEDIUM = {'text':'''A __1__ is created with the def keyword.  You specify the inputs a
__1__ takes by adding __2__ separated by commas between the parentheses.
__1__s by default returns __3__ if you don't specify the value to return.
__2__ can be standard data types such as string, integer, dictionary, tuple,
and __4__ or can be more complicated such as objects and lambda functions.''','answers':['function','arguments','None','list']}

HARD = {'text':'''When you create a __1__, certain __2__s are automatically
generated for you if you don't make them manually. These contain multiple
underscores before and after the word defining them.  When you write
a __1__, you almost always include at least the __3__ __2__, defining
variables for when __4__s of the __1__ get made.  Additionally, you generally
want to create a __5__ __2__, which will allow a string representation
of the method to be viewed by other developers.

You can also create binary operators, like __6__ and __7__, which
allow + and - to be used by __4__s of the __1__.  Similarly, __8__,
__9__, and __10__ allow __4__s of the __1__ to be compared
(with <, >, and ==).''','answers':['class','method','__init__','instance','__repr__','__add__','__sub__','__lt__','__gt__','__eq__']}

IMPOSSIBLE = {'text':'''A __1__ can be thought of as an equivalent of an array in other
programming languages.  A __1__ is indexed by __2__s of any __3__ type.  For example,
you can use __4__s, __5__s, or any __6__ as long as it does not contain a mutable object
such as a __7__.

To create an empty __1__ one starts with using a pair of __8__.  Each entry in a
__1__ is called a __2__:__9__ pair and one can check to see if a __2__ is in the
__1__ using the __10__ keyword.  In order to look up or set a __9__ under a __2__,
one uses __11__ brackets instead of __8__.  In order to substitute values in a dictionary,
one uses the __12__ operator for intergers and __13__ operator for strings.  Also,
one uses the __14__ operator in order to deletion a __2__:__9__ pair.  Keep in mind
that the __2__s of a __1__ are in a __15__ order.'''
,'answers':['dictionary','key','immutable','string','number','tuple','list','braces','value','in','square','%d','%s','del','random']}

def changePhrase(currentPhrase,currentAnswer,currentCount):
    '''
    updates CurrentPhrase input replacing currentCount input with currentAnswer input and outputs changedPhrase
    Args:
        currentPhrase: string of a phrase to be changed
        currentAnswer: string of correct answer to fill in part of the phrase
        currentCount: string with the field to be replaced
    Returns:
        changedPhrase: a string replacing the current missing text field currentCount with the currentAnswer
    '''
    changedPhrase = currentPhrase.replace(currentCount, currentAnswer)
    return changedPhrase

def checkTry(currentPhrase,currentAnswer,currentCount):
    '''
    allows user 5 tries to guess the correct answer to the current missing segment
    Args:
        currentPhrase: string of a phrase to be changed
        currentAnswer: string of correct answer
        currentCount: string with the field to be guessed
    Returns:
        if while loop returns, return
        if while loop runs out of guesses, exit program with statement
    '''
    tries_left = 5
    while tries_left > 0:
        tries_left -= 1
        guess = raw_input('''\r\n\r\nThe current paragraph reads as such:\r\n''' + str(currentPhrase) + '''\r\n\r\n\r\nWhat should be substituted in for ''' + currentCount + '''? ''')
        if guess.lower() == currentAnswer.lower():
            print '''\r\nCorrect!'''
            return
        if tries_left == 0:
            exit('''You've failed too many straight guesses!  Game over!''')
        print '''That isn't the correct answer!  Let's try again; you have ''' + str(tries_left) + ''' trys left!'''
    return

def playPhrase(initialPhrase,answers):
    '''
    plays through game using provided phrase and answers and fills in phrases as correct answers provided
    Args:
        initialPhrase: string chosen by difficulty level chosen by user
        answers: list of answers to complete the phrase
    Returns:
        returns if user completes the phrase correctly
    '''
    phrase = initialPhrase
    count = 1
    print '''You will get 5 guesses per problem'''
    for answer in answers:
        countString = '''__''' + str(count) + '''__'''
        checkTry(phrase,answer,countString)
        phrase = changePhrase(phrase,answer,countString)
        count += 1
    print phrase
    print '''\r\nYou won!\r\n'''
    return

def userPrompt(userQuery,validPrompts,errorMessage):
    '''
    requests user to provide an input and only returns a valid prompt
    Args:
        userQuery: a string with the question to pose to the user
        validPrompts: a list of acceptable strings to compare to the user input
        errorMessage: a string to display user if the user input does not match an acceptable string
    Returns:
        returns lowercase user input string of the difficulty chosen
    '''
    while True:
        print userQuery
        userInput = raw_input()
        for prompt in validPrompts:
            if prompt == userInput.lower():
                return userInput.lower()
        print errorMessage

def chooseMode():
    '''
    no inputs, provides user prompt and options and returns variable for level
    Returns:
        global dictionary name
    '''
    mode = userPrompt ('''Please select a game difficulty by typing it in!
Possible choices include easy, medium, hard and impossible.''',['easy','medium','hard','impossible'],
'''That's not an option!''')
    if mode == 'easy':
        print '''You have chosen ''' + mode + '''!\r\n'''
        return EASY
    elif mode == 'medium':
        print '''You have chosen ''' + mode + '''!\r\n'''
        return MEDIUM
    elif mode == 'hard':
        print '''You have chosen ''' + mode + '''!\r\n'''
        return HARD
    print '''You have chosen ''' + mode + '''!\r\n'''
    return IMPOSSIBLE

def playGame():
    #prompt user for difficulty level (easy, medium, hard), including error check
    gameMode = chooseMode()
    #plays game based on chosen difficulty
    playPhrase(gameMode['text'],gameMode['answers'])

playGame()
'''
#prompt user for difficulty level (easy, medium, hard, impossible), including error check
#Once a level is selected, game displays a fill-in-the-blank and a prompt to fill in the first blank.
#When player guesses correctly, new prompt shows with correct answer in the previous blank and a new prompt for the next blank
#When player guesses incorrectly, they are prompted to try again up to 5 times, then exits game if past 5 incorrect tries
'''

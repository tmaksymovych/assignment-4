import random
import json

words = ['apple','bread','candy','dream','eagle','flame',
         'grape','input','joker',"chair", "plant", "house",
           "dance", "sharp", "table"]

try:
    with open ("meaning.json", "r", encoding="utf-8") as file:
        meanings = json.load(file)
except FileNotFoundError:
    print("Reading 'meaning.json' eror:\n file not found")

def meaning (word):
    """
    Finds the meaning of a given word in the dictionary of meanings
    """
    if word in meanings:
        return meanings[word]

def difficulty (level_choice):
    """
    Users can choose the level of difficulty of the game. The number of attempts depends on it
    """
    if level_choice == "1" or level_choice == "easy":
        tries = 8
    elif level_choice == "2" or level_choice == "medium":
        tries = 6
    elif level_choice =="3" or level_choice == "hard":
        tries = 4
    else:
        tries = 8
    return tries

def guess_compare (guess:str, secret_word_list:list, hidden_list:list):
    """
    function checks, if in users guess any letters, that are similar to letters in guessed word and returns them to their proper places in hidden list. And says user that he wins if guess and secret word are similar. 
    """
    if guess == "".join(secret_word_list):
        return True
    else:
        for a in range(len(secret_word_list)):
            if guess[a] == secret_word_list[a]:
                hidden_list[a] = secret_word_list[a]
        return False
    
def first_game(first_game_bool:bool):
    """
    Checks if this firt game attempt. iF not, do not write "Welcome"
    """
    if first_game_bool == True:
        print("Welcome to Wordle!")
        print("-----------------------")
        first_game_bool = False
    else:
        print("-----------------------")



def game ():
    """
    Start the wordle game
    """
    first_game = True
    score = 0
    while True:

        if first_game == True:
            print("Welcome to Wordle!")
            print("-----------------------")
            print("You have to guess a 5-letter word using a hint\nGood luck!\n")
            first_game = False
        else:
            print("\n-----------------------")
            print(f"Your score: {score}")

        secret_word = random.choice(words)
        sw_list = list(secret_word)
        #print(secret_word)##

        level_choice = (input("Choose difficulty level: 1-easy | 2-medium | 3-hard\n" 
                            "difficulty:"))
        tries = difficulty(level_choice)

        print(f"You have {tries} tries.\n")
        wl = len(secret_word)
        hidden = ["_"] * wl
        
        print(f"Hint: {meaning(secret_word)}")
        
        finish = False

        while tries > 0:
            
            print(f"Mistery word: {hidden}\n")
            print(f"You have left {tries} tries")

            guess = input("Enter yor guess:\n").lower()
            win = guess_compare(guess, sw_list, hidden)

            if win:
                finish = True
                score += 1
                break
            else:
                tries -=1
        if finish:
            print("Congartulations, you won!!\n")
        else:
            print(f"You lose :/.\nThe word was:{secret_word}")

        again = input("Do you want to play again?\n")
        if again == ((("yes").lower()) or (("y").lower()) or (("так").lower()) or (("да").lower())):
            print("\nStarting a new game+:")
        else:
            print("Thanks for playing(❁´◡`❁)")
            break



game()
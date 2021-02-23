old_letters = []
def create_a_dictionary():
     """It's a function that builds the dictionary at the beginning of the game of man's situations
        :return: The dict situations of hung man 
        :rtype: dict
        
     """
     HANGMAN_PHOTOS = {0:  ("""x-------x """),1: ("""
1:
    x-------x
    |
    |
    |
    |
    |"""),2:  ("""2:
    x-------x
    |       |
    |       0
    |
    |
    |"""),3:("""3:
    x-------x
    |       |
    |       0
    |       |
    |
    |"""),4:("""4:
    x------- x
    |        |
    |        0
    |      | | |
    |
    |
             """),5:("""5:
    x-----------x
    |           |
    |           0
    |       |-- |-- |
    |      |
    |"""),6:(""" 6:
    x-------     x
    |            |
    |            0
    |       |----| ----|   
    |      |            |
    |
    """) }
     return HANGMAN_PHOTOS ;                           
def print_hangman (my_dict, num):
     """
     It's a function that print of man's situations during the game
     rtype : none
     """
     print (my_dict[num])
def check_valid_input(letter_guessed, old_letters_guessed):
     
     """
It's a function that halp to function "try_update_letter_guessed" and cheek if the guess is ligeal
and not geting call dirctly form main 
:param letter_guessed: guess of player
:param old_letters_guessed : all the guess that player did
:type letter_guessed : str
:type old_letters_guessed : list
:return : true if it ligeal and false if it not
:rtype : bool
    """
     list_lower =  map(lambda x:x.lower(),old_letters_guessed)
     user_guess = letter_guessed
     user_guess= user_guess.lower()
     size = len(user_guess)
     is_legal = user_guess.islower()
     if (size>1)or (is_legal == False):
        return False 
     else:
           
        if (user_guess in list_lower  ):
             return False ;
        return True
def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    """
     this function cheeking if the guess of user is ilegeal and print all the guess 
     and return true if legeal ant add the guess to old_letters_guessed
     using in function "check_valid_input"
:param letter_guessed: guess of player
:param old_letters_guessed : all the guess that player did
:type letter_guessed : str
:type old_letters_guessed : list
:return : true if it ligeal and false if it not
:rtype : bool
    """
    
   
    user_guess = letter_guessed
    user_guess= user_guess.lower()
    size = len(user_guess)
    is_legal = user_guess.islower()
    if not(check_valid_input(letter_guessed, old_letters_guessed)):
        print ("X")
        new = sorted(old_letters_guessed)
        print (("-> ".join(new)).lower())
        return False 
  
    else:
        old_letters.append(user_guess)
        return True
       



   
def show_hidden_word(secret_word, old_letters_guessed):
    """
The function prints the characters the player guessed and what is left
the function does not receive direct read from main but from check_win
:param secret_word: the secret_word that the player need to guess 
:param old_letters_guessed : all the guess that player did
:type secret_word : str
:type old_letters_guessed : list
:return : str that expresses the player's situation
:rtype : str 
    """
    
    secret_word = secret_word.lower() 
    game=""
    for x in secret_word :
        if x in old_letters_guessed :
            game = game + x + " "
        else:
             game = game + '_ '
             
    print (game)  
    return game
def check_win(secret_word, old_letters_guessed):
    """
A function that checks whether the player has won is doing so using the show_hidden_word function
:param secret_word: the secret_word that the player need to guess 
:param old_letters_guessed : all the guess that player did
:type secret_word : str
:type old_letters_guessed : list
:return : str that expresses the player's situation
:rtype : bool
    """
     
    if(len(old_letters_guessed) == 0):

        return False
    result = show_hidden_word (secret_word, old_letters_guessed)
    a = '_'
    if a in result :
        return False
    return True 
def unique(lst):
    """ Assumes lst is already sorted
A function that deletes all the words that appear multiple times
to know how many words the player has to choose from the file
param lst : list before the deletes
type lst : list
return : list whiout multiple word 
:rtype : lisr
"""
    unique_list = ['a']
    for el in lst:
        if el != unique_list[-1]:
            unique_list.append(el)
    unique_list.remove('a')
    
    return unique_list
def choose_word(file_path, index):
    """
A function that takes the place of the file from which to choose the secret word
and a number that defines the place of the secret word
param file_path : The location of the file
param index : the index of number form file
type file_path : str
type index : int
return : tuple that in 0 return the number of player options to choose a word and tow the secret_word
rtype : tuple 
    """
    my_file = open(file_path,'r')
    my_string = my_file.read()
    my_list = my_string.split()  
    new_list = sorted(my_list)
    new_list = unique(new_list) 
    size = len(unique(new_list))
    a = 0
    while a == 0 :
         
        if (index > len( my_list)):
            index = index - len( my_list)
        else:
            the_wors_choose = my_list[index - 1]
            a = 1
    
    return (size , the_wors_choose)
def func(secret_word):
     """
A function that returns false if each word is a character and verifies if there are invalid characters
param : secret_word this what i cheek
type : str
rtype: bool 
     """
     for x in secret_word:
          if x.isalpha():
               print("")
          else:
               return True
     return False      
    
def main():
    
    """<Your code here: start hangman game>"""
    

    HANGMAN_ASCII_ART=("""
  _    _                                         
 | |  | |                                        
 | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
 |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
 | |  | | (_| | | | | (_| | | | | | | (_| | | | |
 |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                      __/ |                      
                     |___/
     """)
# הפתחיה של המשחק
    print (HANGMAN_ASCII_ART)
    my_dict = {} 
    my_dict = create_a_dictionary()#יצירת המילון 
    MAX_TRIES= 7 #משתנה המבטא את מקסימום הנסיונות
    num_of_tries = 0 # משתנה שמבטע את מספר הנסינות של השחקן
    print("The number of guesses in the game is" , MAX_TRIES)
    my_tuple = ()
    file = input("Please enter the file location from which you select a word ")  
    try:#לבדוק שהקובץ קיים ואם לא לחזור מהתחלה למשחק 
        f = open(file,'r')
        
    except IOError:
        print("File not accessible")
        main() 
        
    
    my_tuple = choose_word(file,int (input("Please enter the secret word location ")) )
    
    secret_word = my_tuple[1]
    while (func(secret_word)):#לולאה שעוסדת עד שהמשתמש יבחר מתוך הקובץ מילה חוקית 
         print("worng please choose another ")
         my_tuple = choose_word(file,int (input("Please enter the secret word location ")))
         secret_word = my_tuple[1]
    print ("Let’s start!")
    while ( True ):#לולאה שעובדת כל הזמן עד שהמתמש ינחש או כל המילה או יפסיד המשחק 
         
        print_hangman(my_dict , num_of_tries)
        
        if (check_win(secret_word , old_letters)):
            print("Congratulations you won")
            break
        your_guess = input("plesee guess ")
        your_guess_is_legal = try_update_letter_guessed(your_guess, old_letters)    
        while( your_guess_is_legal == False ):#לולאה שעובדת עד שהמשתמש מכניס תו תקין ושלא ניחש כבר 
            your_guess = input("plesee guess ")
            your_guess_is_legal = try_update_letter_guessed(your_guess, old_letters)
        if (your_guess in  secret_word ):
            print("")
         
        else:    
            num_of_tries += 1
            if num_of_tries > 6 :
              print ("you are lozer and lost in the game")
              break
            
           
            
            
            
        
    print(secret_word)        
                
if __name__ == "__main__":
    main()

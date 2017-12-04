import os
import sys
import csv
import random


should_restart = 0 #BD Beter als een Boolean

#BD code block below really needs functions to make it more readable - quite some redundancy
while should_restart <= 0: #While loop which allows to return to the open file menu
    opened_file = 0 #While loop for opening file #BD Beter als Booleans
    editing = 0 #While loop for editing files
    start_quiz = 0 #While loop for the quiz

    #Open File
    print('Create a new file? press enter. / Existing file? type the name of the file.')
    name_file = input()
    #New file
    if name_file == '':
        print('Type the name of the new file + enter.')
        name_file = input().lower() #BD lower gives unexpected filename
        while opened_file <= 0:
            if os.path.exists(name_file + ".csv"): #Check whether filename exists
                print('This file already exists.')
                print('Type 1 to overwrite or enter to choose a new name.')
                user_choice = input()
                if user_choice == ('1'): #Overwrite existing file
                    with open (name_file + '.csv', 'w+') as f:
                        reader = csv.reader(f)
                        f.truncate()
                        word_list = list(reader)
                        f.close() #BD Closing file here => possible to still write to it?   
                        opened_file += 1
                else: #Retry to create a file
                    print('Type the name of the new file + enter.')
                    name_file = input().lower()
            else: #Create new file
                if name_file.strip() == (''): #blank input error
                    print('Field should not be blank. Choose another name for the new file + enter.')
                    name_file = input().lower()
                else: #New file opened
                    with open (name_file + '.csv', 'w+') as f:
                        reader = csv.reader(f)
                        word_list = list(reader)
                        f.close()
                        opened_file += 1
    #Existing file
    else:
        opened_file = 0
        while opened_file <= 0:
            if os.path.exists(name_file + ".csv"): #Check if file exists + open #BD adding .csv is counterintuitive; add a check if it is there or not
                with open (name_file + '.csv', 'r+') as f: #BD os.path.exists en r+, nice
                    reader = csv.reader(f)
                    word_list = list(reader)
                    f.close()
                    opened_file += 1
            else: #Error + option to create file
                print(name_file + ' does not exist. Do you want to open ' + name_file + ' as a new file? 1 = yes, enter = no.')
                user_answer = input().lower()
                if user_answer == '1': #Create new file from name input
                    if name_file.strip() == (''):
                        print('Field should not be blank. Choose another file + enter.')
                        name_file = input().lower()
                    else: 
                        with open (name_file + '.csv', 'w+') as f:
                            reader = csv.reader(f)
                            word_list = list(reader)
                            f.close()
                            opened_file += 1
                else: #Retry to find file
                    print('Try again: Type the name of the new file + enter.')
                    name_file = input().lower()
                
    #Check whether word_list is empty or not
    empty_wordlist = 1 
    if len(word_list) == 0:
        empty_wordlist -= 1 #BD empty_wordlist is verwarrend als variabelenaam
    else:
        pass #BD wat is hier het nut van? Mag weg
    print('')
    print('Currently working in ' + name_file + '.csv.')
    print(word_list)
    print('')
    print('Would you like to edit this file or start practicing?')
    print('Press enter to start practicing.')
    print('Type 1 to start editing.')
    user_choice = input('') #Input for editing menu 
    if empty_wordlist == 0 or user_choice == ('1'): #Is word list empty / does user want to edit? -> edit menu #BD perfect om hier functies van te maken
        while empty_wordlist <= 0 or user_choice ==('1'):
            if len(word_list) == 0:
                print('')
                print(name_file + ' is still an empty word list.')
                print('')
            else:
                pass

            #Editing menu
            while editing <= 0:
                print('Press enter + to save and/or quit editing mode.')
                print('Type 1 + enter to start removing items.')
                print('Type 2 + enter to start adding items.')
                print('')
                user_choice = input().lower().strip()
                print('')

                #Removing items
                if user_choice == ('1'):
                    done_removing = 0
                    while done_removing <= 0:
                        removedict = dict(enumerate(word_list)) #BD dict will scramble the order
                        print('')
                        print(removedict)
                        print('')
                        print('Type the number of the word pair you want to delete.')
                        print('Press enter to exit to the editing menu.')
                        print('')
                        remove_word = input('')
                        if remove_word.isdigit() == True:
                            if int(remove_word) > int(len(removedict)): #BD no need for int casting
                                print('Number is not in list.')
                            else:
                                word_list.pop(int(remove_word))
                        else:
                            done_removing += 1

                #Adding items    
                elif user_choice == ('2'):
                    done_adding = 0
                    while done_adding <= 0:
                        print('')
                        print('Type new word + enter or type 1 to return to the editing menu.')
                        new_word = input()
                        if new_word.lower().strip() == ('1'):
                            done_adding += 1
                        else:
                            print('Type translation + enter')
                            translation = input()
                            if new_word.strip() is '' and translation.strip() is '': #BD should be OR
                                print('')
                                print('No values entered, try again.')
                            else:
                                word_list.append([new_word, translation])

                #Saving and continuing / returning to the main menu                
                else:
                    if len(word_list) == 0: #Check if words have been added
                        print(name_file + ' is still empty.')
                        print('Press enter to continue editing.')
                        print('Type 1 to exit without saving and opening a new file.')
                        user_choice = input().lower().strip() 
                        if user_choice == ('1'): #Open new file instead
                            editing += 1
                            empty_wordlist += 1
                            start_quiz += 1
                            user_choice = ('')
                        else: #Continue editing
                            pass

                    else: #Save or exit without saving
                        empty_wordlist += 1
                        print('')
                        print(word_list)
                        print('')
                        print('To save and exit press enter.')
                        print('To exit without saving press 1.')
                        print('')
                        save_file = input() 
                        if save_file == ('1'):
                            with open (name_file + '.csv', 'r') as f:
                                reader = csv.reader(f)
                                check_csv = [] #Make sure added items are saved if file was empty
                                check_csv = list(reader)
                                f.close()
                                if check_csv == []: #Return to edit menu if file was orginally empty
                                    print('Empty files must be saved.')
                                    empty_wordlist -= 1
                                        
                                else: #Exit without saving
                                    editing += 1
                                    user_choice = ('')
                                    print('Your file has not been saved.')
                        else: #Save file
                            with open(name_file + '.csv','w+', newline='') as f:
                                f.truncate()
                                writer = csv.writer(f)
                                for pair in word_list:
                                    writer.writerow(pair)
                                f.close
                            editing += 1
                            user_choice = ('')
                            print('Your file has successfully been saved.')


    #Practice options
    while start_quiz <= 0: #Loop for practice options and quiz
        correct_input = 0
        while correct_input <= 0:
            shuffle = 1 #Variable for extra reshuffle at end of every quiz round
            print('How would you like to practice your word _list?')
            print('Type the corresponding number + enter.')
            print('1 = Standard order')
            print('2 = shuffled')
            print('3 = alphabetically')
            practice_method = input()
            if practice_method == '1': #Standard order
                correct_input += 1
            elif practice_method == '2': #Shuffle
                random.shuffle(word_list)
                correct_input += 1
                shuffle -= 1 
            elif practice_method == '3': #Sort alphabetically
                word_list.sort()
                correct_input += 1
            else:           #Wrong input
                print('Wrong input, try again.')

        #empty page (Otherwise the word list with answers is visible.)
        empty_page = 0        
        while empty_page <= 60:
            print('')
            empty_page += 1
        
        #Quiz
        print('Type the answer to the question + enter')
        numerator = len(word_list) #variables for end score
        denominator = len(word_list)
        unknown_words = word_list
        while len(unknown_words) > 0: #Loop over all word pairs until all 1 time correct
            still_unknown_words = []
            for question, correctanswer in unknown_words: #Run over all questions and answer + compare to user input
                answer = input(question + ' ').lower()
                if answer == correctanswer:
                    print('Correct!')
                else:
                    print('Wrong answer!')
                    numerator -= 1
                    still_unknown_words.append([question, correctanswer])
                if shuffle == 0: #Reshuffle if this options was chosen 
                    random.shuffle(still_unknown_words)
                unknown_words = still_unknown_words
            if len(unknown_words) == 0: #End of loop
                end_score = numerator / denominator * 100
                if end_score == 100:
                    print('Congratulations! You scored ' + str(round(end_score)) +'%!' )
                elif end_score >= 70:
                    print('Well done! your score is ' + str(round(end_score)) +'%.')
                elif end_score >= 50:
                    print('Your score is ' + str(round(end_score)) +'%.')
                else:
                    print('Too bad your score is ' + str(round(end_score)) +'%...')
                user_input = 0
                while user_input == 0: #Options after practicing the list
                    print('Do you want to practice this list again? Type 1 + enter.')
                    print('Do you want to open a new file? Type 2 + enter.')
                    print('Do you want exit the program? Type 3 + enter.')
                    user_choice = input()
                    if user_choice == '1': #Restart loop from practice options
                        user_input += 1
                        correct_input -= 1
                    elif user_choice == '2': #Restart loop from open file
                        start_quiz += 1
                        user_input += 1                      
                    elif user_choice == '3': #Close Program
                        sys.exit()
                        user_input += 1
                    else:           #Wrong input
                        print('Wrong input, try again.')
            

                    
                        
                
                    

                




   

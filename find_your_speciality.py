from ascii_logos import computer_logo

print(computer_logo)

print("Welcome to Find Your Speciality Game.")
print("Your mission is to answer relevant questions about Computer Engineering.") 
print("At the end of the game you will find out which area you are most interested in.")


choice1 = input("With which language did you start to software development? Type 'python', 'c#', 'javascript', 'java'. ").lower()

if choice1 == 'python':
    choice2 = input("Do you like to use this programming language? Type 'yes' or 'no' ").lower()

    if choice2 == 'yes':
        choice3 = input("Which one is more interesting for you? Type '1' for (Data Science, Artificial Intelligence, Big Data)  or  '2' for (Website Development) ").lower() 
        
        if choice3 == '1':
            print('You can apply to job postings titled Data Scientist, Data Analyst, Data Engineer or ML Engineer.') 
       
        elif choice3 == '2':
            print('You can apply to job postings titled Backend Developer or Full Stack Developer.')
        
        else:
            print('Incorrect Input.')
        
    else:
        print('You can do research on Frontend Development and Mobile App Development. I think this areas might be of interest to you.')


elif choice1 == 'c#':
    choice2 = input("Do you like to use this programming language? Type 'yes' or 'no' ").lower()
    
    if choice2 == 'yes':
        choice3 = input("Which one is more interesting for you? Type '1' for (Game Development, UX | UI Design)  or  '2' for (Website Development) ").lower()  

        if choice3 == '1':
            print('You can apply to job postings titled Unity Game Developer or Casual Mobile Developer.') 
       
        elif choice3 == '2':
            print('You can apply to job postings titled .NET Developer or Backend Developer.')
        
        else:
            print('Incorrect Input')

    else:
        print('You can do research on Frontend Development and Mobile App Development. I think this areas might be of interest to you.')


elif choice1 == 'javascript':
    choice2 = input("Do you like to use this programming language? Type 'yes' or 'no' ").lower()

    if choice2 == 'yes':
        choice3 = input("Which one is more interesting for you? Type '1' for (HTML&CSS, UX | UI Design)  or  '2' for (None) ").lower()  

        if choice3 == '1':
            print('You can apply to job postings titled React Developer, Frontend Developer or PHP Developer.') 
       
        elif choice3 == '2':
            print('You can do research on Backend Development and Mobile App Development. I think this areas might be of interest to you.')
        
        else:
            print('Incorrect Input') 

    else:
        print('You can do research on Backend Development and Mobile App Development. I think this areas might be of interest to you.')

elif choice1 == 'java':
    choice2 = input("Do you like to use this programming language? Type 'yes' or 'no' ").lower()

    if choice2 == 'yes':
        choice3 = input("Which one is more interesting for you? Type '1' for (Backend Development)  or  '2' for (Mobile App Development,  UX | UI Design) ").lower()  

        if choice3 == '1':
            print('You can apply to job postings titled Java Developer and Backend Developer.') 
       
        elif choice3 == '2':
            print('You can apply to job postings titled Mobile App Developer and Android Developer, Kotlin Developer.')
        
        else:
            print('Incorrect Input') 

    else:
         print('You can do research on Backend Development, Frontend Development and Game Development. I think this areas might be of interest to you.')

else:
    print('Wrong Answer.')
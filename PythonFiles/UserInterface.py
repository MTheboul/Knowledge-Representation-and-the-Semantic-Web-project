import MovieActorInformation

def __main__():
    print("\n************************\n****IMPORTANT NOTICE****\n************************")
    print("Currently there is no major User input error handling, some invalid errors happends and errors that are handeld in web ui.\n")
    print("************************\n****IMPORTANT NOTICE****\n************************")
    print("Welcome")
    print("To generate questions about Actors enter 1 for Movies enter 2 to exit enter 3.\n")
    
    choice = input()
    while("3" not in choice):
        if("1" in choice):
            print("Enter an Actor to get questions about.")
            try:
                json = MovieActorInformation.createQuizActor(input())
                print(json)
            except:
                print("Error due to input has occoured")
        elif("2" in choice):
            print("Enter an Movie to get questions about.")
            try:
                json = MovieActorInformation.createQuizMovie(input())
                print(json)
            except:
                print("Error due to input has occoured")
        else:
            print("Invalid input.")
        

        print("To generate questions about Actors enter 1 for Movies enter 2 to exit enter 3.\n")
        choice = input()

__main__()
import MovieActorInformation

def __main__():
    print("************************\n****IMPORTANT NOTICE****\n************************")
    print("Currently there is no major User input error handling, some invalid errors happends.\n")
    print("************************\n****IMPORTANT NOTICE****\n************************")
    print("Welcome")
    print("To generate questions about Actors enter 1 for Movies enter 2 to exit enter 3.\n")
    
    choice = input()
    while("3" not in choice):
        if("1" in choice):
            print("Enter an Actor to get questions about.")
            json = MovieActorInformation.createQuizActor(input())
            print(json)
        elif("2" in choice):
            print("Enter an Movie to get questions about.")
            json = MovieActorInformation.createQuizMovie(input())
            print(json)
        else:
            print("Invalid input.")
        

        print("To generate questions about Actors enter 1 for Movies enter 2 to exit enter 3.\n")
        choice = input()

__main__()
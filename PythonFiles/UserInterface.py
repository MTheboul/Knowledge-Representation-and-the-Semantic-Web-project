import MovieActorInformation

def __main__():
    print("Welcome")
    print("To generate questions about Actors enter 1 for Movies enter 2 to exit enter 3.\n")
    
    choice = input()
    while("3" not in choice):
        if("1" in choice):
            print("Enter an Actor to get questions about.")
            actor = input()
            json = MovieActorInformation.createQuizActor(actor)
        else:
            print("Enter an Movie to get questions about.")
            movie = input()
            json = MovieActorInformation.createQuizMovie(movie)
        print(json)

        print("To generate questions about Actors enter 1 for Movies enter 2 to exit enter 3.\n")
        choice = input()

__main__()
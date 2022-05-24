from mml_ratings import ratings as rateingsList
# to understand tuple-struckture: index[0] is title index[1] is artist
# index[2] is rating index[3] is distribution format(song, album)
ratingsFile = "MML\mml_ratings.py"
def sort_ratings(rate):
        return rate[2]
ratings = sorted(rateingsList, key=sort_ratings, reverse=True)
# @todo allow editing in main,  ...(implement binary search)

    # stuff for gettings input:
# gets the format and returns it
def getFORMAT(what):
    print(f"\nchoose a format to {what}"
        "\n                     - [song] -    "
        "\n                     - [album]   -    "
        "\n                     - [", end="")
    format = input().lower()
    if format == "song" or format == "album":
        return format
    else:
        print("invalid format")
        return False           
# gets the title of getFORMAT-result and returns it
def getTITLE(format):
    print(f"which [{format}]: - [", end="")
    return input()
# gets the artist of getTITLE-result and returns it
def getARTIST(title):
    print(f"who made [{title}]?: - [", end="")
    return input()
# gets input and return
def getNEW_ARTIST():
    print("which [artist]: - [", end="")
    return input()
# gets the rating of getTITLE and ARTIST-result and returns it + valuererror n' shadow realm
def getRATING(title, artist):
    try:
        print(f"choose a rating [0 - 100] for [{title} - {artist}]:   - [", end="")
        rating = int(input())
        if rating >= 0 and rating <= 100:
            return rating
        else:
            print("invalid rating") 
            return False           
    except ValueError:
        print("invalid rating")
        return False
# gets title + artist + format for specific arting
def getRATINGtpl():
    try:
        print("which [rating][0 - 100]: - [", end="")
        rating =int(input())
        if rating >= 0 and rating <= 100:
            return rating
        else:
            print("invalid rating")            
            return False           
    except ValueError:
        print("invalid rating")
        return False   
    
def add():
    # breaks while if invalid input
    allow = True
    add_while = True
    while add_while:
        format = getFORMAT("rate")
        if format == False:
            break
        title = getTITLE(format)
        artist = getARTIST(title)
        # checks if item is in tuples by iterating w/ for
        for i in ratings:
            if i[0] == title and i[1] == artist and i[3] == format:
                print(f"\n[{title} - {artist}] has already been rated as a [{i[2]}/100]!\n")
                allow = False
        if allow == False:
            break
        rating = getRATING(title, artist)
        if rating:  # bc there are objectively only ratings from [0-100] 
                    # allowed, any else returns false, names arent 
                    # objectively wrong thats why only here controlles
            with open(ratingsFile, 'a') as appender:
                # ads input to tuple w/ mentioned struckture onto file above
                appender.write(f'ratings.append(("{title}", "{artist}", {rating}, "{format}"))\n')
            print(f"\n[{title} - {artist}] has been added by as a {rating}/100!\n")
        # breaks while if user doesnt input "yes"
        else:
            break
        print("rate something else?: "
            "\n                      - [yes] - "
            "\n                      - [no]  - "
            "\n                      - [", end="")
        iffurther = input()
        if iffurther != "yes":
            add_while = False

def title():
    title_while = True
    while title_while:
        format = getFORMAT("check") 
        title = getTITLE(format)
        artist = getARTIST(title)
        for i in ratings:
            if i[0] == title and i[1] == artist and i[3] == format:
                print(f"\n[{i[0]} - {i[1]}] [{i[3]}] is a [{i[2]}]\n")
                break
            elif i == ratings[len(ratings)-1]:
                print(f"\n[{title} - {artist}] [{format}] is not rated... - consider adding it!\n")
                break            
        print("check another title?: "
            "\n                      - [yes] - "
            "\n                      - [no]  - "
            "\n                      - [", end="")
        iffurther = input()
        if iffurther != "yes":
            title_while = False
        
def rating():
    # if there are ratings w/ the wanted rating, appends tuple of rating
    # to respective list and prints it out later
    title_while = True
    while title_while:
        songs = []
        albums = []
        rating = getRATINGtpl()
        if rating:
            # checks the list of tuples to confirm existence and append to list
            for i in ratings:
                if i[2] == rating and i[3] == "song":
                    songs.append(i)
                elif i[2] == rating and i[3] == "album":
                    albums.append(i)
            if songs != []:
                print(f"\nsongs {rating}/100 are:")
                for i in songs:
                    print(f"    {i[0]} - {i[1]}")
            if albums != []:
                print(f"\nalbums {rating}/100 are:\n")
                for i in albums:
                    print(f"    {i[0]} - {i[1]}")
            if songs == [] and albums == []:
                print("\nthere is no music with this rating, consider adding some!")
        else:
            rating()
        print("\ncheck another rating?: "
            "\n                      - [yes] - "
            "\n                      - [no]  - "
            "\n                      - [", end="")
        iffurther = input()
        if iffurther != "yes":
            title_while = False

def artist():
    artist_added = []
    artist_while = True
    while artist_while:
        artist = getNEW_ARTIST()
        for i in ratings:
            if i[1] == artist:
                artist_added.append(i)
        if artist_added != []:
            print(f"from {artist}:\n")
            for i in artist_added:
                print(f"[{i[2]}] - [{i[0]} - {i[1]}]")
        else:
            print(f"there is no music rated from {artist}")
            break         
        print("\ncheck another artist?: "
            "\n                      - [yes] - "
            "\n                      - [no]  - "
            "\n                      - [", end="")
        iffurther = input()
        if iffurther != "yes":
            artist_while = False
 
def else_():
    # outputs all ratings first songs and albums second, descending from 100
    def all_ratings():
        print("\nsongs:\n")
        for i in ratings:
            if i[3] == "song":
                print(f"[{i[2]}] - [{i[0]} - {i[1]}]")
        print("\nalbums:\n")
        for i in ratings:
            if i[3] == "album":
                print(f"[{i[2]}] - [{i[0]} - {i[1]}]")

    # counts ++ for every tuple w/ the respective [3]
    def which_rated():
        sum_all = len(ratings)
        sum_songs = 0
        sum_albums = 0
        for i in ratings:
            if i[3] == "song":
                sum_songs += 1
            if i[3] == "album":
                sum_albums += 1
        print(f"\nyou have rated [overall]: {sum_all}"
              f"\nyou have rated [songs]: {sum_songs}"
              f"\nyou have rated [songs]: {sum_albums}")        

    print("\ncheck all your ratings with   - [all ratings] -"
          "\ncheck how many you rated with - [which rated] -"
          "\n                              - [", end="")
    else_action = input().lower()

    if else_action == "all ratings":
        all_ratings()
    elif else_action == "which rated":
        which_rated()

def main():
    further = True
    while further:
        # user chooses action
        print("\n"
              "you can extend your ratings with - [add]    -\n"
              "you can check your titles with   - [title]  - \n"
              "you can check your ratings with  - [rating] - \n"
              "you can check your artists with  - [artist] - \n"
              "                                 - [", end="")
        choice = input().lower()
        if choice == "add":
            add()
        elif choice == "rating":
            rating()
        elif choice == "title":
            title()
        elif choice == "artist":
            artist()
        else:
            else_()
        # user decides if he wants to continue
        print("\ndo you want to continue? - [yes] -"
              "\n                         - [no]  -"
              "\n                         - [", end="")
        Q_further = input().lower()
        if Q_further == "yes":
            pass
        else:
            further = False

main()

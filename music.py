# Import the Pygame mixer library
from pygame import mixer

# Starting the mixer
mixer.init()

file = open("songs.txt")  # file containing the list of songs
songs = {}
for i in file:
    a, b = i.strip("\n").split(", ")
    songs[a] = b

songs2 = songs.copy()

c = 1
q = []


# Function to print the header
def head():
    for i in range(80):
        print('*', end='')
    print()
    print('Music Player'.center(80))
    for i in range(80):
        print('*', end='')
    print()


# Function to print list of songs
def songslist(songs):
    global c
    c = 1
    print("   Title".ljust(23), "Artist")
    print("   -----".ljust(23), "-------")
    for i in songs.keys():
        print(str(c) + ")", i.ljust(20), songs[i])
        c += 1


# Function to play a selected song
def playmusic(song):
    song += ".mp3"
    mixer.music.load(song)
    mixer.music.set_volume(0.7)
    mixer.music.play()

    # Loop until the user stops or pauses the song
    while True:
        print()
        print("p - Pause      r - Resume      s - Stop")
        ch = input(">> ")

        if ch == 'p':
            mixer.music.pause()

        elif ch == 'r':
            mixer.music.unpause()

        elif ch == 's':
            mixer.music.stop()
            break


# Function to sort the list of songs
def sortmusic():
    global songs2
    print('''1. Sort by Title
2. Sort by Artist
3. Date Added''')

    while True:

        c1 = int(input('>> '))

        print('''1. Ascending
2. Descending''')

        c2 = int(input('>> '))

        if c1 not in [1, 2] and c2 not in [1, 2]:
            continue

        if c1 == 1:
            if c2 == 1:
                songs2 = dict(sorted(songs.items(), key=lambda x: x[0], reverse=False))
            else:
                songs2 = dict(sorted(songs.items(), key=lambda x: x[0], reverse=True))

        elif c1 == 2:
            if c2 == 1:
                songs2 = dict(sorted(songs.items(), key=lambda x: x[1], reverse=False))
            else:
                songs2 = dict(sorted(songs.items(), key=lambda x: x[1], reverse=True))

        elif c1 == 3:
            if c2 == 1:
                songs2 = songs
            else:
                songs2 = dict(reversed(list(songs.items())))

        break

    songslist(songs2)


# Function to add songs to the queue
def queue():
    global q
    songslist(songs)

    while True:
        t = int(input("Enter a song to add to the Queue: "))

        if t not in range(1, c + 1):
            print("Invalid Choice!")
            continue

        else:
            q.append(list(songs2)[t - 1])
            print(q)
            print("Successfully added to the Queue!!")

        break


# Function to play songs in the queue
def playqueue():
    global q
    if len(q) == 0:
        print("No songs are added to the Queue!")
    else:
        for i in q:
            playmusic(i)


# main function of the music player
def main():
    global songs2
    global q
    global c

    while True:
        head()

        print('''
                        1. Library
                        2. Sort Music
                        3. Add music to Queue
                        4. Play music from the Queue
                        5. Clear Queue
                        6. Exit Music Player''')
        ch = int(input("Enter your choice: "))

        if ch == 1:
            songslist(songs2)
            print()
            t = int(input("Enter a song to play: "))

            while t not in range(1, c):
                print('Invalid song!')
                t = int(input("Enter a song to play: "))

            playmusic(list(songs2)[t - 1])

        elif ch == 2:
            sortmusic()

        elif ch == 3:
            queue()

        elif ch == 4:
            playqueue()

        elif ch == 5:
            if len(q) == 0:
                print('No songs are added to the Queue!')
            else:
                q = []
                print("Queue successfully cleared!")

        elif ch == 6:
            print("Exiting....")
            break


# calling main
if __name__ == "__main__":
    main()

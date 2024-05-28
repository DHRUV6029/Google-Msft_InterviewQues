import collections
import random
songs = [ "A","B", "C", "D", "E" ]
k = 2

class MusicPlayer:
    def __init__(self) -> None:
        self.dict = collections.defaultdict(int)
        self.arr = [s for s in songs]
        for i in range(0,len(self.arr)):
            self.dict[self.arr[i]] = i 

        self.timer = []
        self.t = -1



    def getRandomSong(self):
        self.t+=1
        song = random.choice(self.arr)
        self.deleteSong(song)
        self.timer.append((song , self.t+k))
        return song


    def deleteSong(self, song):
        #tasks the song to the end of the array list popit and change the indexex at dict too
        i = self.dict[song]
        j = len(self.arr)-1

        song_at_last = self.arr[len(self.arr)-1]

        #exchange at the self.arr
        self.arr[i] , self.arr[j] = self.arr[j] , self.arr[i]
        self.arr.pop()

        self.dict.pop(song)

        self.dict[song_at_last] = i

    def insertAgainToPlay(self):
        if not self.timer:
            return
        
        if self.timer[0][1] <= self.t:
            song  = self.timer.pop(0)[0]
            self.arr.append(song)
            self.dict[song] = len(self.arr)-1



music_player = MusicPlayer()
a = music_player.getRandomSong()
b = music_player.getRandomSong()

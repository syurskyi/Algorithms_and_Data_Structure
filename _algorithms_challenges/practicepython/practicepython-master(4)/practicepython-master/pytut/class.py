

#this is to demonsrate the creation of a class and instantiaing it


class Song(object):
    def __init__(self,lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print line



#a class has been created above. now we will try to create different objects for it

happy_bday = Song(["Happy birthday to you",
"I dont want to get u sued",
"So I will stop right there"])

bulls_on_parade = Song(["They rally around the family",
        "With pocket full of shells"])

#here we will call the above 2 instatntiated objects

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

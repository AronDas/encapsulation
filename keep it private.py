class myclass:
    __privatevar = 27;


    def __privmeth(self):
        print("im in the class myclass")


    def hello(self):
        print("Private variable value:",myclass.__privatevar)

foo = myclass()
foo.hello()
foo.__privmeth
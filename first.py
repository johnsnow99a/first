import random
class game:
    def __init__(self):
        pass
    def gues_generate(self):
        self.x= random.randint(1,10)
        return self.x
    def user_guess(self):
        self.chose=input("please inter your guess")
        return self.chose
    def menu(self):
        print("hello and welcome to our game")
        print("=" * 70)
        print("please choose one number:\n1-enter the game\n2-game guide\n3-exit")
        ch=input("")
        if ch == "1":
            return self.compare()
        elif ch == "2":
            return self.guidee()
        elif ch == "3":
            return self.exitt()
        else:
            print("not correct value")
    def compare(self):
        flag=False
        a=int(self.gues_generate())
        print(a)
        b=int(self.user_guess())
        while not flag:
            if a == b:
                print("weldone")
                flag = True
                return self.exitt()
            elif a>b:
                print("my is bigger")
                b=int(self.user_guess())
            elif b > a:
                print("oh yours is bigger")
                b=int(self.user_guess())

    def guidee(self):
        print("hello dear friend in this game the pc guess a number and after it you should guess it")
    def exitt(self):
        print("thanks for doing this game see you later")

if __name__ == "__main__":
    gamee=game()
    gamee.menu()
    print("thanks for using this game")

            

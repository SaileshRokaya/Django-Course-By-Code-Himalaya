class First(object):
    def __init__(self):
        super(First, self).__init__()
        print("first")

    # def test():
    #     print("First method")


class Second(object):
    def __init__(self):
        super(Second, self).__init__()
        print("Second")
    
    def test():
        print("Second Method")

class Third(First,Second):
    def __init__(self):
        super(Third,self).__init__()
        print("Third")
    

class Forth(First):
    def __init__(self):
        super(Third, self).__init__()
        print('Forth')
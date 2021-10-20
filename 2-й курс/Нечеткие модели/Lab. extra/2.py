
class Books():
    def __call__(self, name="Books"):
        self.name = name
        print(name)


class Native(Books):
    def __call__(self, name="  Native"):
        super().__call__()
        self.name = name
        print(name)


class Foreign(Books):
    def __call__(self, name="  Foreign"):
        super().__call__()
        self.name = name
        print(name)


class Science(Books):
    def __call__(self, name="  Science"):
        super().__call__()
        self.name = name
        print(name)


class Art(Books):
    def __call__(self, name="  Art"):
        super().__call__()
        self.name = name
        print(name)


class Villa(Native, Art):
    def __call__(self, name="    Villa"):
        super().__call__()
        self.name = name
        print(name)


class NativeScience(Native, Science):
    def __call__(self, name="    Native science"):
        super().__call__()
        self.name = name
        print(name)


class ForeignArt(Foreign, Art):
    def __call__(self, name="    Foreign Art"):
        super().__call__()
        self.name = name
        print(name)


class ScienceFiction(Science, Art):
    def __call__(self, name="    Science fiction"):
        super().__call__()
        self.name = name
        print(name)


class ForeignScienceFiction(Foreign, ScienceFiction):
    def __call__(self, name="      Foreign science fiction"):
        super().__call__()
        self.name = name
        print(name)


obj1 = ForeignScienceFiction()
obj1()
obj2 = NativeScience()
obj2()

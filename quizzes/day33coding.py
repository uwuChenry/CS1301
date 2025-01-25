class Bookstore:
    def __init__(self,n):
        self.name = n
        self.titleList = []
    def addTitle(self,titleString):
        self.titleList.append(titleString)
    def countTitles(self, string):
        count = 0
        for things in self.titleList:
            if things[0].lower() == string.lower():
                count += 1
        return count


# testing code
store1 = Bookstore("Barnes and Noble")
store1.addTitle("Call of the Wild")
store1.addTitle("War and Peace")
store1.addTitle("Catcher in the Rye")
print(store1.countTitles("c"))  # should print 2
print(store1.countTitles("k"))  # should print 0
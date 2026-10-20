# Byoung Hartzel L. Kim             9 - Beryllium
# 2nd quarter second task

# publication class aka the main class
class Publication:
    # all the attributes of the publication class
    def __init__(self, booktitle, bookauthor):
        self.booktitle = booktitle
        self.bookauthor = bookauthor
    # title (will be used later on in the subclasses)
    def get_thetitle(self):
        return self.booktitle
    # author (will be used later on in the subclasses)
    def get_theauthor(self):
        return self.bookauthor
    # newtitle 
    def create_title(self, brandnewtitle):
        self.booktitle = brandnewtitle
    # newauthor 
    def create_author(self, brandnewauthor):
        self.bookauthor = brandnewauthor
    # display info (works for ever class that is connected to the publication class) 
    def display_info(self):
        print(f"Title: {self.booktitle}")
        print(f"Author: {self.bookauthor}")

class Book(Publication):
    def __init__(self, booktitle, bookauthor, numberofpages):
        super().__init__(booktitle, bookauthor)
        self.numberofpages = numberofpages
    # pages
    def get_numberofpages(self):
        return self.numberofpages
    # newpages
    def make_numberofpages(self, newnumberofpages):
        self.numberofpages = newnumberofpages

class Magazine(Publication):
    def __init__(self, booktitle, bookauthor, issuenumber):
        super().__init__(booktitle, bookauthor)
        self.issuenumber = issuenumber
    # issue number
    def get_issuenumber(self):
        return self.issuenumber
    # newissue number
    def make_issuenumber(self, newissuenumber):
        self.issuenumber = newissuenumber
# magazine is a subclass of publication and book is also a subclass of publication, so they are both connected to the publication class

# creating objects
publication1 = Publication("Journal of Experimental Psychology", "Ratchiff. R. & Van Dongen, H.")
book1 = Book("The Hobbit", "J.R.R. Tolkein", 310)
magazine1 = Magazine("National Geographic", "Various Authors", 202)
# printing the information
print("Publication Information:")
publication1.display_info()

print("\nBook Information:")
book1.make_numberofpages(-310) # setting invalid value on an attribute
book1.display_info()

print("\nMagazine Information:")
magazine1.display_info()
print(magazine1.get_issuenumber())

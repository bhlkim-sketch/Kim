# Byoung Hartzel L. Kim             9 - Beryllium
# 2nd quarter second task

# publication class aka the main class
class Publication:
    def __init__(self, booktitle, bookauthor):     # all the attributes of the publication class
        self.booktitle = booktitle
        self.bookauthor = bookauthor
    #@property
    def get_thetitle(self):      # title (will be used later on in the subclasses)
        return self.booktitle
    #@property
    def get_theauthor(self):      # author (will be used later on in the subclasses)
        return self.bookauthor
    #@get_thetitle.setter
    def create_title(self, brandnewtitle):      # create a new title
        self.booktitle = brandnewtitle
    #@get_theauthor.setter
    def create_author(self, brandnewauthor):    # create a new author
        self.bookauthor = brandnewauthor

    def display_info(self):      # display info (works for ever class that is connected to the publication class) 
        print(f"Title: {self.booktitle}")
        print(f"Author: {self.bookauthor}")
        if hasattr(self, 'numberofpages'):
            print(f"Number of pages: {self.numberofpages}")
        if hasattr(self, 'issuenumber'):
            print(f"Issue Number: {self.issuenumber}")

class Book(Publication):
    def __init__(self, booktitle, bookauthor, numberofpages):   # creating a subclass of publication called book, which has an additional attribute of number of pages
        super().__init__(booktitle, bookauthor)
        self.numberofpages = numberofpages

    #@property
    def get_numberofpages(self):   # get the number of pages
        return self.numberofpages

    #@get_numberofpages.setter
    def make_numberofpages(self, newnumberofpages):   # set the number of pages
        numbernew = int(newnumberofpages)   # convert the input to an integer
        if numbernew < 0:   # checks if the number of pages is negative, if it is, it will print an error message
            print("The number of pages must be positive.")
        else:
            self.numberofpages = numbernew

class Magazine(Publication):
    def __init__(self, booktitle, bookauthor, issuenumber):
        super().__init__(booktitle, bookauthor)
        self.issuenumber = issuenumber
    #@property
    def get_issuenumber(self):   # get the issue number
        return self.issuenumber
    #@get_issuenumber.setter
    def make_issuenumber(self, newissuenumber):   # set the issue number
        issuenew = int(newissuenumber)   # convert the input to an integer
        if issuenew < 0:   # checks if the issue number is negative, if it is, it will print an error message
            print("The issue number must be positive.")
        else:
            self.issuenumber = issuenew
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

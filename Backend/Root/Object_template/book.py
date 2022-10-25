class book ():
    def __init__(self,book_detail:tuple):
        self.__ISBN13=str(book_detail[0])
        self.__title=str(book_detail[1])
        self.__availiability=int(book_detail[2])
        self.__total=int(book_detail[3])

    @property
    def ISBN13(self):
        return self.__ISBN13

    @property
    def title(self):
        return self.__title

    @property
    def availiability(self):
        return self.__availiability

    @property
    def total(self):
        return self.__total

    @ISBN13.setter
    def ISBN13(self,value):
        self.__ISBN13=value

    @title.setter
    def title(self,value):
        self.__title=value

    @availiability.setter
    def availiability(self,value):
        self.__availiability=value

    @total.setter
    def total(self,value):
        self.__total=value










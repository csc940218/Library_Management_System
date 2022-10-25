class add_book ():
    def __init__(self,add_detail:tuple):
        self.__ISBN13=str(add_detail[0])
        self.__title=str(add_detail[1])
        self.__quantity=str(add_detail[2])
        self.__username=str(add_detail[3])
        self.__password=int(add_detail[4])

    @property
    def ISBN13(self):
        return self.__ISBN13


    @property
    def title(self):
        return self.__title

    @property
    def quantity(self):
        return self.__quantity

    @property
    def username(self):
        return self.__username

    @property
    def password(self):
        return self.__password
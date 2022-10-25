class return_book ():
    def __init__(self,return_detail:tuple):
        self.__ISBN13=str(return_detail[0])
        self.__username=str(return_detail[1])
        self.__password=int(return_detail[2])

    @property
    def ISBN13(self):
        return self.__ISBN13

    @property
    def username(self):
        return self.__username

    @property
    def password(self):
        return self.__password
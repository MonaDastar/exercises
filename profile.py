from datetime import datetime


class Profile:
    """ basic information of users and check its validation """

    def __init__(self, name: str=None, last_name: str=None, birth_date: int=None) -> None:
        self.name = name
        self.last_name = last_name
        self.birth_date = birth_date

    @property
    def name(self):
        """ get value of name """
        return self.__name

    @name.setter
    def name(self, value: str) -> None:
        """ set value of name

        Parameters
        ----------
        value: str :
        name of users


        """
        if isinstance(value, str):
            if value.isalpha():
                self.__name = value
            else:
                raise ValueError("name is non-alphabetic")
        else:
            raise ValueError(f"last_name must be string \
                            but it is {type(self.name)}")

    @property
    def last_name(self):
        """ get the last name"""
        return self.__last_name

    @last_name.setter
    def last_name(self, value: str) -> None:
        """ set the last

        Parameters
        ----------
        value: str :
        the last name must be string

        """
        if isinstance(value, str):
            if value.isalpha():
                self.__last_name = value
            else:
                raise ValueError("name is non-alphabetic")
        else:
            raise ValueError(f"last_name must be string but it is \
                  {type(self.last_name)}")

    @property
    def birth_date(self):
        """ set the date of birth"""
        return self.__birth_date

    @birth_date.setter
    def birth_date(self, value: int) -> None:
        """ set the birth date


        Parameters
        ----------
        value: int :
        must be a  positive integer


        """
        if isinstance(value, int) and value > 0:
            self.__birth_date = value
        else:
            raise ValueError("birth_date must be a positive integer ")

    def get_date(self) -> int:
        """ gets the year of birth

        Returns
        ----------
        integer : age of the user
        """

        current_year = int(datetime.today().strftime("%Y"))
        birth_year = self.__birth_date
        return (current_year-birth_year)

    def get_fullname(self) -> str:
        """ get full name

        Returns
        ----------
        string of users' name
        """
        return f'{self.__name},{self.__last_name}'

    def __str__(self):
        return f'{self.name}, {self.last_name}, {self.birth_date}'

    def __repr__(self):
        return f'{self.name}, {self.last_name}, {self.birth_date}'



if __name__ == '__main__':
    profile_test = Profile('Mona','Dastar', 1988)
    print(profile_test)
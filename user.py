import re
from profile import Profile
from typing import List


class User(Profile):
    """create user object with all its  and actions related to it """

    def __init__(
        self,
        user_name: str,
        password: str,
        name: str=None,
        last_name: str=None,
        birth_date: int=None
    ) -> None:

        self.user_name = user_name
        self.password = password
        super().__init__(name, last_name, birth_date)

    @property
    def user_name(self) -> str:
        """get the user name"""
        return self.__user_name

    @user_name.setter
    def user_name(self, value: str) -> None:
        """set the user name

        Parameters
        ----------
        value: str :
        the user name must be string typed
        """
        if value:
            self.__user_name = value
        else:
            raise ValueError("null value")

    @property
    def password(self) -> str:
        """ get the password"""
        return self.__password

    @password.setter
    def password(self, value: str) -> bool:
        """set the password based on the password pattern

        Parameters
        ----------
        value: str :
        value must be 8 characters and fit in the pattern


        """
        if self.check_strength_of_password(value):
                self.__password = value
                print("password accepted, welcome {}".format(self.user_name))
        else:
            raise ValueError("try another strong password ")



    @classmethod
    def check_strength_of_password(cls, value: str) -> bool:
        """ check_strength_of_password

        Parameters
        ----------
        password: str :
        input password
        Returns
        -------
        True if password is valid, False otherwise

        """
        password_pattern = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{8,18}$"  # noqa
        match_re = re.compile(password_pattern)
        strong = re.search(match_re, value)
        if (strong):
            return True
        else:
            return False


    def save_user_data(self, *args) -> None:
        """ saves the user data to the 'user_info.txt

        Parameters
        ----------
        *args :
        list of user information
        example: username, password, name,...



        """
        object_tools = [
            'user_name',
            'password',
            'name',
            'last_name',
            'birth_date'
        ]
        with open(args[0]+".txt", 'w') as txt_file:
            for i in range(len(args)):
                string = object_tools[i] + " : " + str(args[i]) + "\n"
                txt_file.write(string)

    @classmethod
    def read_from_user(cls, user_name: str, password: str) -> List[str]:
        """ read data from user's file which its
        name is the same as its username


        Parameters
        ----------
        user_name: str :
        shares the same name as the file name
        password: str :
        value must be 8 characters and fit in the pattern

        Returns
        -------
        list of users information

        """
        pattern = r":\s([\W\w\d].+)"
        object_list = []
        with open(user_name+".txt", 'r') as txt_file:
            for row in txt_file.readlines():
                object_list += re.findall(pattern, row)
                
        return object_list

    
    def create_user_data(self) -> None:
        """ creates a file in 'data' directory
        with the name of  "users_info.txt"
        keeps the usernames and passwords of the users
        for later authentications

        Parameters
        ----------
        user_name: str :
        shares the same name as the file name
        password: str :
        value must be 8 characters and fit in the pattern


        """
        path_users_data = "data/users_info.txt"
        with open(path_users_data, 'a') as data_file:
            string = "\n" + self.user_name + "\n" + self.password + "\n"
            data_file.write(string)

    def __str__(self) -> str:
        return f'welcome { self.user_name}'

    def authenticate(self) -> None:
        """ check if the username and
        passwords entered, exist in the file date/users_info.txt'
        if yes, reads their information from their files"""
        with open("data/users_info.txt", "r") as data_file:
            object_string = data_file.readlines()
            object_string = "".join(object_string)
            pattern = r"\n([\W\w\d].+)\n([\W\w\d].+)\n"
            print(re.findall(pattern, object_string, flags=re.M))
            if (self.user_name, self.password) in object_string:
                print(self.read_from_user(self.user_name, self.password))

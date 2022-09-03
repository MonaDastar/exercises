from user import User
from time import sleep
from utils import SiwssKnife

flag_on = False
while not flag_on:
    user_type = input("Are you a new member? (Y/n): ").lower()

    if user_type == 'y':
        # a new profile will be created for the user and the username
        # and password will be kept in user_info.txt for later
        # authentication
        user_name = input(" choose a user name for your account  ")
        go_on = False

        while not go_on:
            # a strong password will be accepted  for the user
            strong_password = input("Enter a strong password containing 8\
characters of lowercase, upper case \
and numbers and characters like '!@#$&*'  ")
            go_on = User.check_strength_of_password(strong_password)


        print("let's complete your profile information...")

        name = input('what is your first name please? ')
        last_name = input('and your last name? ')
        birth_date = int(input('and your birth date? '))
        user = User(user_name, strong_password,
            name, last_name, birth_date)
        user.create_user_data()
        # saves the profile information to a file
        user.save_user_data(
            user_name, strong_password,
            name, last_name, birth_date
        )
        

        sleep(2)
    # if the user is not new, first the username and password will be
    # checked and if they match with the data in users_info file
    # they can see their information like: name, lastname, etc
    elif user_type == 'n':
        user_name = input(" enter your user name:  ")
        go_on = False
        while not go_on:
            strong_password = input("enter your password: ")
            go_on = User.check_strength_of_password(strong_password)
            user_list = User.read_from_user(user_name, strong_password)
        sleep(2)
        SiwssKnife.clear_screen()
        user = User(
            user_name = user_list[0],
            password=user_list[1],
            name = user_list[2],
            last_name = user_list[3],
            birth_date=int(user_list[4])
            )
        print("user: ",user)
        print(user_list)
        print(f"welcome : {user_list[2]} with username : {user_list[0]} ")
        flag_on = True
        
        
        
        
# if __name__ == '__main__':
#     user1 = User('MD','Mona@123')
#     profile = Profile('mona', 'Dastar',1988)
#     print(user1)
import hashlib
import getpass
from time import sleep
from sql_manager import BankDB
from smtplib import SMTP
from smtplib import SMTPException
from mail_password import mail_pass
import random


class Bank():
    execute_program = True
    # dict_of_commands = {"register": Bank.register,
    #                     "login": Bank.login,
    #                     "help": Bank.helphommand,
    #                     "exit": Bank.exit_program,
    #                     "help_me": logged_help,
    #                     }
    number_of_unsuccessfull_tries_before_block = 5

    def main_menu():
        print(
            "Welcome to our bank service. You are not logged in. \nPlease register or login")

        while Bank.execute_program:
            command = input("$$$>")
            if command == 'login':
                Bank.dict_of_commands[command](
                    Bank.number_of_unsuccessfull_tries_before_block)
            elif command == "help" or command == "exit" or command == "register":
                Bank.dict_of_commands[command]()
            else:
                print("Not a valid command")
###################################################################

    def make_a_transaction(logged_user, operation, amount):
        if operation.lower() == "deposit":
            BankDB.make_a_transaction(amount)
        elif operation.lower() == "withdrow":
            pass
########################################################################

    def get_balance(logged_user):
        print("Your balance is {}".format(logged_user.get_balance))

    def exit_program():
        BankDB.execute_program = False

    def register():
        username = input("Enter your username: ")
        password = getpass.getpass('Enter your password:')
        if check_for_strong_pass(username, password):
            hashed_password = hash(pasword)
            BankDB.register(username, hashed_password)
            print("Registration Successfull")
        else:
            print("to weak password\n your password need to have:\n",
                  "Must have capital letters, and numbers and a special symbol",
                  "More then 8 symbols",
                  "Username is not in the password")

    def login(unsuccessful_tries):
        if unsuccessful_tries > 0:
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            if Bank.its_allready_hashed(password):
                logged_user = BankDB.login(username, password)
            else:
                hashed_password = Bank.password_to_hash(password)
                logged_user = BankDB.login(username, hashed_password)

            if logged_user:
                Bank.logged_menu(logged_user)
                return True
            else:
                print("Login failed\n ")
                print("you have {} tries left".format(unsuccessful_tries - 1))
                return Bank.login(unsuccessful_tries - 1)
        else:
            print("screw you hacker you are gonna wait 5 mins")
            sleep(300)  # Time in seconds.

    def its_allready_hashed(password):
        has_numbers = BankDB.check_for_numbers(password)
        has_40_symbols = False
        if len(password) == 40:
            has_40_symbols = True
        return has_numbers == has_40_symbols

    def password_to_hash(password):
        return hashlib.sha1(password.encode()).hexdigest()

    def logged_menu(logged_user):
        print("Welcome you are logged in as: " + logged_user.get_username())
        while True:
            command = input("Logged>>")

            if command == 'info':
                print("You are: " + logged_user.get_username())
                print("Your id is: " + str(logged_user.get_id()))
                print(
                    "Your balance is:" + str(logged_user.get_balance()) + '$')

            elif command == 'changepass':
                new_pass = input("Enter your new password: ")
                BankDB.change_pass(new_pass, logged_user)

            elif command == 'change-message':
                new_message = input("Enter your new message: ")
                BankDB.change_message(new_message, logged_user)

            elif command == 'show-message':
                print(logged_user.get_message())

            elif command == 'logout':
                logged_user.logout()

            elif command == 'help_me':
                Bank.logged_help()

    def system_pass_reset(logged_user):
        new_pass = Bank.generate_new_unique_pass()
        BankDB.change_pass(new_pass, logged_user)
        Bank.sent_mail(new_pass, logged_user.get_email)

    def logged_help():
        print("info - for showing account info")
        print("changepass - for changing passowrd")
        print("change-message - for changing users message")
        print("show-message - for showing users message")

    def check_for_strong_pass(username, password):
        if len(password) > 8:
            if check_for_capitals(password):
                if check_for_numbers(password):
                    if check_for_pass_in_username(username, password):
                        if check_for_special_symbols(password):
                            return True
                        else:
                            return False
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False

    def check_for_numbers(password):
        numbers = "0123456789"
        for char in password:
            if char in numbers:
                return True
        return False

    def check_for_special_symbols(password):
        special_symbol = "`~!@#$%^&*()_+=-|"
        for char in password:
            if char in special_symbol:
                return True
        return False

    def check_for_capitals(password):
        if password == password.lower():
            return False
        else:
            return True

    def check_for_pass_in_username(username, password):
        if password in username:
            return False
        else:
            return True

    def sent_mail(msg, receiver):
        SMTPserver = "smtp.gmail.com"
        port = 587
        #text_subtype = 'plain'
        content = """You new password is : {} \n Enter this code in our menu , to change it later """.format(
            msg)
        #subject = "Sent from Python"
        acc_name = "Google Mail (victor.vangelov)"
        USERNAME = "victor.vangelov@gmail.com"
        receivers = receiver
        PASSWORD = Bank.get_password()
        # try:
        conn = SMTP(SMTPserver, port)
        conn.ehlo()
        conn.starttls()
        conn.login(USERNAME, PASSWORD)
        conn.sendmail(USERNAME, receivers, content)
        conn.close()
        # except SMTPException:
            # print ("Error: unable to send email")

    def get_password():
        return mail_pass

    def generate_new_unique_pass():
        numbers_and_letters = "1234567890qwertyuiopasdfghjklzxcvbnm"
        new_pass = ""
        for x in range(0, 10):
            new_pass += random.choice(numbers_and_letters)
        return Bank.password_to_hash(new_pass)

    def have_enought_money_to_withdrow(logged_user, withdrow):
        if int(logged_user.get_balance) + int(withdrow) > 0:
            return True
        else:
            return False

    def transaction_menu(logged_user):
        transaction_method = input(
            "Choose to 'deposit' or 'withdrow' money or 'exit' to back in the menu ")
        method = transaction_method.split()
        if method[0].lower == "deposit":
            Bank.make_transaction(logged_user, method[1])
        elif method[0].lower == "withdrow":
            if Bank.have_enought_money_to_withdrow(logged_user, method[1]):
                Bank.make_transaction(logged_user, method[1])
            else:
                print("You dont have have_enought_money_to_withdrow")
        elif method[0].lower == "exit":
            Bank.logged_menu(logged_user)
        else:
            print("Wrong command!!!")
            transaction_method(logged_user)

    def make_withdrow_negativ(amount):
        return amount * (-1)

    def make_transaction(logged_user, amount):
        BankDB.make_transaction(amount, logged_user)


def main():
    BankDB.create_clients_table()
    #pswd = getpass.getpass('Password:')
    #print (pswd)


if __name__ == '__main__':
    main()

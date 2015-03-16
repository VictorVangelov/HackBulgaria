import sqlite3


class CreateCompany():

    def __init__(self):
        self.connection = sqlite3.connect('company')
        self.connection.row_factory = sqlite3.Row
        self.cursor = self.connection.cursor()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS company(id INTEGER PRIMARY KEY, name TEXT, monthly_salary INTEGER, yearly_bonus INTEGER, position TEXT)''')
        self.connection.commit()
        self.db_is_closed = False

    def add_employee(self):
        person_information = input("<name> <monthly_salary> <yearly_bonus> <position>")
        person_information = person_information.split()
        #need autogenerate forkey
        name = person_information[0]
        monthly_salary = person_information[1]
        yearly_bonus = person_information[2]
        position = person_information[3]
        self.cursor.execute('''INSERT INTO company(name, monthly_salary, yearly_bonus, position) VALUES(?, ?, ?, ?)''', (name, monthly_salary, yearly_bonus, position))
        self.connection.commit()

    def input_standart_info(self):
        users = [("Ivan Ivanov", 5000, 10000, "Software Developer"),
        ("Rado Rado", 500, 0, "Technical Support Intern"),
        ("Ivo Ivo", 10000, 100000, CEO),
        ("Petar Petrov", 3000, 1000, "Marketing Manager"),
        ("Maria Georgieva", 8000, 10000, "COO")]
        self.connection.executemany(''' INSERT INTO users(name, monthly_salary, yearly_bonus, position) VALUES(?,?,?,?)''', users)
        self.connection.commit()

    def list_employees(self):
        list_employees = self.cursor.execute("SELECT id, name, position FROM company")
        for row in list_employees:
            print(row["name"], row["position"])

    def monthly_spending(self):
        monthly_spending = self.cursor.execute("SELECT monthly_salary FROM company")
        all_salarys = 0
        for row in monthly_spending:
            all_salarys += row
        print(all_salarys)
        return all_salarys

    def yearly_spending(self):
        monthly_spending = self.monthly_spending()
        months_in_year = 12
        result = monthly_spending * months_in_year
        print (result)
        return result

    def delete_employee(self):
        self.list_employees()
        wanted_id = input("enter the wanted id to delete the whole row")
        self.cursor.execute('''DELETE FROM users WHERE id = {} '''.format(wanted_id,))
        self.connection.commit()

    def print_availabel_fields(self):
        result = self.cursor.execute("SELECT *FROM company")
        fields = result.keys()
        print(fields)

    def return_wanted_field(self):
        self.print_availabel_fields()
        wanted_field = input("enter wanted field name (only one field):")
        return (wanted_field)


#conn = sqlite3.connect(blabla)
#conn.row_factory = sqlite3.Row
#cursor = conn.cursor()
#result = cursor.execute("SELECT *FROM languages")
#for row in result:
#   print("{} - {} ".format(row["id"], row['language']))

    def update_employee(self):
        self.list_employees()
        wanted_id = input("enter the wanted id to update the whole row : ")
        wanted_field = self.return_wanted_field()
        modification = input("enter the new value: ")
        self.cursor.execute('''UPDATE company SET {} = {} WHERE id = {} '''.format(wanted_field, modification, wanted_id))
        self.connection.commit

    def close(self):
        self.connection.close()
        self.db_is_closed = True

    def print_available_commands(self):
        available_commands = "list_employees\nmonthly_spending\nyearly_spending\nadd_employee\ndelete_employee\nupdate_employee\nexit"

    def execute_command(self, command):
        if command == "list_employees":
            self.list_employees()
        elif command == "monthly_spending":
            self.monthly_spending()
        elif command == "yearly_bonus":
            self.yearly_spending()
        elif command == "add_employee":
            self.add_employee()
        elif command == "delete_employee":
            self.delete_employee()
        elif command == "update_employee":
            self.update_employee()
        elif command == "exit":
            self.close()
        else:
            print("wrong command , pls try again")

    def user_interface(self):
        while(self.db_is_closed is False):
            self.print_available_commands()
            command = input("enter command from this above:")
            self.execute_command(command)


def main():
    the_program = CreateCompany()
    the_program.user_interface()

if __name__ == '__main__':
    main()

import sqlite3

conn = sqlite3.connect("company.db")
conn.row_factory = sqlite3.Row
cursor = conn.cursor()

command = input("command> :")


def list_employees():
    info = cursor.execute("SELECT id, name, position FROM company")
    for row in info:
        print([row["id"], row["name"], row["position"]])


def monthly_spending():
    info = cursor.execute("SELECT monthly_salary FROM company")
    monthly_spending = sum([row["monthly_salary"] for row in info])
    print("The company is spending ${} every month!".format(monthly_spending))


def yearly_spending():
    info = cursor.execute("SELECT monthly_salary, yearly_bonus FROM company")
    total = sum(12 * row["monthly_salary"] + row["yearly_bonus"] for row in info)
    print (total)


def add_employee():
    name = input("name: ")
    salary = int(input("monthly_salary: "))
    bonus = int(input("yearly_bonus: "))
    position = input("position: ")
    cursor.execute("""INSERT INTO company(name, monthly_salary, yearly_bonus, position)
    VALUES(?,?,?,?)""", (name, salary, bonus, position))
    conn.commit()


def delete_employee(id):
    cursor.execute("""DELETE FROM company WHERE id = ?""", (id))
    conn.commit()


def update_employee(id):
    name = input("name:")
    salary = int(input("monthly_salary:"))
    bonus = int(input("yearly_bonus:"))
    position = input("position:")
    cursor.execute("""UPDATE company
        SET name = ?, monthly_salary = ?,
            yearly_bonus=?, position = ?
        WHERE id= ?""", (name, salary, bonus, position, id))
    conn.commit


commands = {
           "list_employees": list_employees,
           "monthly_spending": monthly_spending,
           "yearly_spending": yearly_spending,
           "add_employee": add_employee,
           "delete_employee": delete_employee,
           "update_employee": update_employee
           }


def main():
    user_command = command.split()[0]
    try:
        user_id = command.split()[1]
        commands[user_command](user_id)
    except:
        commands[user_command]()

if __name__ == '__main__':
    main()

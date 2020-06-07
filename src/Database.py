import sqlite3
from sqlite3 import Error
import src.Validation.Helper as helper
import locale
import os
from pathlib import Path

db_file = os.getcwd() + "\\dochazkadb2.db"


def create_database() -> None:
    """Create database file
    """
    print(db_file)
    print(os.getcwd())
    Path(db_file).touch()


def check_database() -> bool:
    """Checks if database exist or not
    Returns:
        bool: True if the database exist otherwise False
    """
    print("checking database")
    return os.path.exists(db_file)


def check_tables(conn: sqlite3.Connection, table: str) -> bool:
    """Checks if table is exist
    Args:
        conn: connection object
        table: table name

    Returns:
        bool: True if the database exist otherwise False
    """
    print("checking table " + table)
    # query = "SELECT name FROM sqlite_master WHERE type='table' AND name='{table_name}';"

    cur = conn.cursor()
    cur.execute("SELECT count(name) FROM sqlite_master WHERE type='table' AND name=?", (table,))

    row = cur.fetchall()
    if row[0][0] == 0:
        return False
    return True


def check_table_data(conn: sqlite3.Connection, table: str) -> bool:
    """Checks if table data exist
    Args:
        conn: connection object
        table: table name

    Returns:
        bool: True if the data is greater than zero otherwise False
    """
    cur = conn.cursor()
    cur.execute("SELECT count(*) FROM " + table)

    row = cur.fetchall()
    print("checking data from " + table + ": " + str(row[0][0]))
    if int(row[0][0]) > 0:
        return True
    return False


def create_tables():
    """Creating default tables if not exists
    """
    user_table = """ CREATE TABLE IF NOT EXISTS users (
                                                userId INTEGER PRIMARY KEY not null,
                                                username VARCHAR(255) not null,
                                                password VARCHAR(255) not null,
                                                firstName VARCHAR(255) not null,
                                                surname VARCHAR(255) not null,
                                                hireDate VARCHAR(10) not null,
                                                wagePerHour INT NOT NULL DEFAULT 100,
                                                isEmployer BOOLEAN NOT NULL DEFAULT 0
                                            ); """

    presence_table = """ CREATE TABLE IF NOT EXISTS presence (
                                                id INTEGER PRIMARY KEY not null,
                                                timeIn VARCHAR(5) null,
                                                timeOut VARCHAR(5) null,
                                                date VARCHAR(10) not null,
                                                userId int not null,
                                                FOREIGN KEY (userId) REFERENCES users(userId)
                                            ); """

    conn = create_connection()
    if conn is not None:
        # create projects table
        create_table(conn, user_table)
        create_table(conn, presence_table)

        seed_data(conn)

    else:
        print("Error! cannot create the database connection.")


def main():
    pass


def seed_data(conn):
    """Seed data to the database
    Args:
        conn: connection object
    """
    password_hash = "d3457ad5e96aa2727685b91b25b2d01c07e0bc8a33a868bda1b06b226e94fa7391db845be9b890af6b7f8c64be3f27927d391b7e832ba250c6568b8344ca64a1aa80003bb55101e6f960733b5bfee49281e276a76b314d7b3775651c43304938"
    if conn is not None:
        create_user(conn, ('dom53', password_hash, 'Dominik', 'Mandinec', '17.01.2019'))
        create_user(conn, ('admin', password_hash, 'Cristen', 'Klausen', '17.01.2019'))
        create_user(conn, ('atallis2', password_hash, 'Alicea', 'Tallis', '20.01.2019'))
        create_user(conn, ('mserris3', password_hash, 'Merwin', 'Serris', '07.01.2019'))
        create_user(conn, ('rfalkous4', password_hash, 'Ruddie', 'Falkous', '01.01.2019'))
        create_user(conn, ('vmaccaghan5', password_hash, 'Violante', 'MacCaghan', '05.01.2019'))
        create_user(conn, ('blamping6', password_hash, 'Brendin', 'Lamping', '13.01.2019'))
        create_user(conn, ('myearsley7', password_hash, 'Mervin', 'Yearsley', '26.01.2019'))
        create_user(conn, ('dtoffolini8', password_hash, 'Darcee', 'Toffolini', '20.01.2019'))
        create_user(conn, ('jfairnington9', password_hash, 'Jaymie', 'Fairnington', '11.01.2019'))
        create_user(conn, ('ecrannella', password_hash, 'Eilis', 'Crannell', '27.01.2019'))
        create_user(conn, ('gkennaghb', password_hash, 'Granger', 'Kennagh', '14.01.2019'))
        create_user(conn, ('ngirogettic', password_hash, 'Nell', 'Girogetti', '04.01.2019'))
        create_user(conn, ('bcoand', password_hash, 'Bethany', 'Coan', '24.01.2019'))
        create_user(conn, ('pjewise', password_hash, 'Paddy', 'Jewis', '04.01.2019'))


def get_presence_group_by_year_by_id(conn: sqlite3.Connection, user_id: int) -> list:
    """Return presence year by id
    Args:
        conn: connection object
        user_id: user id

    Returns:
        list: years from presence by id
    """
    cur = conn.cursor()
    cur.execute("SELECT substr(date,1,4) FROM presence WHERE userId=? group by substr(date,1,4)", (user_id,))

    rows = cur.fetchall()

    # for row in rows:
    #     print(row)
    print("group")
    print(type(rows))
    return rows


def select_user_by_id(conn: sqlite3.Connection, user_id: int):
    """Return user by id
    Args:
        conn:
        user_id:

    Returns:
        user by id
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE userId=?", (user_id,))

    row = cur.fetchall()
    # print(row)
    return row


def user_exist(conn: sqlite3.Connection, username: str) -> bool:
    """Checks if user exist
    Args:
        conn: connection object
        username: username

    Returns:
        bool: True if user exist otherwise False
    """
    print("db user")
    cur = conn.cursor()
    cur.execute("SELECT count(*) FROM users WHERE username=?", (username,))

    row = cur.fetchall()
    if row[0][0] == 0:
        return False
    return True


def check_pass(conn: sqlite3.Connection, password: str) -> bool:
    """Checks if the password matches
    Args:
        conn: connection object
        password: user password

    Returns:
        bool: True if the password matches otherwise False
    """
    print("db user")
    cur = conn.cursor()
    cur.execute("SELECT count(*) FROM users WHERE password=?", (password,))

    row = cur.fetchall()
    if row[0][0] == 0:
        return False
    return True


def exist_time_in(conn: sqlite3.Connection, user_id: int, date: str) -> bool:
    """Checks if entry already exist in database
    Args:
        conn: connection object
        user_id: user id
        date: date of arrival

    Returns:
        bool: True if entry already exist otherwise False
    """
    cur = conn.cursor()
    cur.execute("SELECT count(*) FROM presence WHERE userId=? AND date=?", (user_id, date,))

    row = cur.fetchall()
    if row[0][0] == 0:
        return False
    return True


def exist_time_out(conn: sqlite3.Connection, user_id: int, date: str) -> bool:
    """Checks if departure already exist in database
    Args:
        conn: connection object
        user_id: user id
        date: date of departure

    Returns:
        bool: True if entry already exist otherwise False
    """
    cur = conn.cursor()
    cur.execute("SELECT count(*) FROM presence WHERE userId=? AND date=? AND timeOut IS NULL", (user_id, date,))

    row = cur.fetchall()
    print(row[0][0])
    if row[0][0] == 1:
        return False
    return True


def select_presence_by_user_id(conn: sqlite3.Connection, user_id: int, year: str, month: str) -> list:
    """Return work presences by user id
    Args:
        conn: connection object
        user_id: user id
        year: year
        month: month

    Returns:
        list: List of user work presences
    """
    cur = conn.cursor()
    print("iid: " + str(id))
    print("ddate: " + year)
    print("mmonth: " + month)
    convert_month = helper.Validation.month_to_number(month)
    print(convert_month)
    # mesic = date + '-' + convert_month + '%'
    # print(mesic)
    cur.execute("SELECT * FROM presence WHERE userId= ? AND date LIKE ? ORDER BY date",
                (user_id, year + '-' + convert_month + '%',))

    rows = cur.fetchall()
    # print(row)
    return rows


def select_user_day_count(conn: sqlite3.Connection, user_id: int, date: str, month: str) -> int:
    """Return number of working days per month
    Args:
        conn: connection object
        user_id: user id
        date: date
        month: month

    Returns:
        int: Number of working days
    """
    cur = conn.cursor()
    convert_month = helper.Validation.month_to_number(month)
    # print(convert_month)
    cur.execute(
        "SELECT count(*) FROM presence WHERE userId= ? AND timeOut is not null AND date LIKE ? ORDER BY date",
        (user_id, date + '-' + convert_month + '%',))
    row = cur.fetchall()
    print("tp2")
    print(type(row[0][0]))
    return row[0][0]


def select_user_time(conn: sqlite3.Connection, user_id: int, date: str, month: str) -> str:
    """Return time of working days per month
    Args:
        conn:
        user_id:
        date:
        month:

    Returns:
        str: Time of working days
    """
    cur = conn.cursor()

    h: int = 0
    m: int = 0
    convert_month = helper.Validation.month_to_number(month)

    # convert_month = helper.Validation.month_to_number(month)
    # print(convert_month)
    cur.execute(
        "SELECT timeIn, timeOut FROM presence WHERE userId= ? AND timeOut is not null AND date LIKE ? ORDER BY date",
        (user_id, date + '-' + convert_month + '%',))
    rows: list = cur.fetchall()
    for x in rows:
        final_time = helper.Validation.number_of_hours(x[1], x[0])
        # print(celkovy_cas)
        h += int(final_time.split(":")[0])
        m += int(final_time.split(":")[1])

    # print(h)
    # print(m)
    # t = '{:02d}:{:02d}'.format(*divmod(m, 60))
    # print(helper.Validation.number_to_time(h, m))
    # print(celkovy_cas)
    # print(row)
    print("--->")
    print("h: " + str(h) + " - m: " + str(m))
    print("final -> " + str(helper.Validation.number_to_time(h, m)))
    print(type(h))
    print(type(m))
    return helper.Validation.number_to_time(h, m)


def select_user_wage(conn: sqlite3.Connection, user_id: int, date: str, month: str) -> str:
    """Return user wage per month by user id
    Args:
        conn: connection object
        user_id: user id
        date: date
        month: month

    Returns:
        str: user wage per month
    """
    time = select_user_time(conn, user_id, date, month)

    cur = conn.cursor()
    cur.execute("SELECT wagePerHour FROM users WHERE userId= ?", (user_id,))
    row = cur.fetchall()
    # print("time: " + time + ", mzda: " + str(row[0]))

    t = time
    (h, m) = t.split(':')
    result = int(h) * 3600 + int(m) * 60
    final_hours = result / 60 / 60
    # mzda = row[0]
    final_wage: float = float(final_hours) * float(row[0][0])

    locale.setlocale(locale.LC_ALL, '')
    mzd = locale.currency(round(final_wage, 2), grouping=True)

    return str(mzd)
    # return float(final_hours) * float(row[0])


def select_user_by_credentials(conn: sqlite3.Connection, username: str, password: str) -> list:
    """Return user by user credentials
    Args:
        conn: connection object
        username: user username
        password: user password

    Returns:
        list: user
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE username=? and password=?", (username, password))

    row = cur.fetchall()
    print("login user is:")
    print(type(row))
    print(row)
    return row

def select_user_by_credentials2(conn: sqlite3.Connection, username: str) -> list:
    """Return user by user credentials
    Args:
        conn: connection object
        username: user username

    Returns:
        list: user
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE username=?", (username,))

    row = cur.fetchall()
    print("login user is:")
    print(type(row))
    print(row)
    return row


def delete_user(conn: sqlite3.Connection, user_id: int):
    """Delete user by id
    Args:
        conn: connection object
        user_id: user id
    """
    sql = 'DELETE FROM users WHERE userId=?'
    cur = conn.cursor()
    cur.execute(sql, (user_id,))
    conn.commit()


def update_user(conn: sqlite3.Connection, task: tuple):
    """Update priority, begin_date, and end date of a task
    Args:
        conn: connection object
        task: data
    """
    sql = ''' UPDATE users
              SET wagePerHour = ?
              WHERE userId = ?'''
    cur = conn.cursor()
    cur.execute(sql, task)
    conn.commit()


def update_presence(conn: sqlite3.Connection, task: tuple):
    """Update presence
    Args:
        conn: connection object
        task: data
    """
    sql = ''' UPDATE presence
              SET timeIn = ?, timeOut = ?
              WHERE userId = ? AND id = ?'''
    cur = conn.cursor()
    cur.execute(sql, task)
    conn.commit()


def create_user(conn: sqlite3.Connection, project: tuple):
    """Create a new user
    Args:
        conn: connection object
        project: user data
    """
    sql = ''' INSERT INTO users(username,password,firstName,surname,hireDate)
              VALUES(?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, project)
    conn.commit()
    # return cur.lastrowid


def hire_user(conn: sqlite3.Connection, project: tuple):
    """Hire a new user
    Args:
        conn: connection object
        project: user data
    """
    sql = ''' INSERT INTO users(username,password,firstName,surname,hireDate,wagePerHour)
              VALUES(?,?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, project)
    conn.commit()
    # return cur.lastrowid


def create_presence(conn: sqlite3.Connection, project: tuple):
    """Create a new presence
    Args:
        conn: connection object
        project: presence data
    """
    sql = ''' INSERT INTO presence(id,timeIn,timeOut,date,userId)
              VALUES(?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, project)
    conn.commit()


def create_presence_in(conn: sqlite3.Connection, project: tuple):
    """Create a new presence (entry)
    Args:
        conn: connection object
        project: presence data
    """
    sql = ''' INSERT INTO presence(timeIn,date,userId)
              VALUES(?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, project)
    conn.commit()


def create_presence_out(conn: sqlite3.Connection, project: tuple):
    """Update presence (exit)
    Args:
        conn: connection object
        project: presence data
    """
    sql = ''' UPDATE presence
                  SET timeOut = ?
                  WHERE date = ? AND userId = ?'''
    cur = conn.cursor()
    cur.execute(sql, project)
    conn.commit()


def change_password(conn: sqlite3.Connection, project: tuple):
    """Change user password
    Args:
        conn: connection object
        project: user data
    """
    print("change type")
    print(type(project))
    sql = ''' UPDATE users
                  SET password = ?
                  WHERE userId = ?'''
    cur = conn.cursor()
    cur.execute(sql, project)
    conn.commit()


def create_table(conn: sqlite3.Connection, create_table_sql):
    """Create a table from the create_table_sql statement
    Args:
        conn: connection object
        create_table_sql: a CREATE TABLE statement
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


def create_connection():
    """Create a database connection to the SQLite database specified by db_file
    Returns:
        sqlite3.Connection: Open connection to the database file or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
        # raise Error
    return conn


if __name__ == '__main__':
    main()

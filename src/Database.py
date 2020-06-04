import sqlite3
from sqlite3 import Error
import src.Validation.Helper as helper
import locale
from datetime import datetime

conn = None
# db_file = r"C:\Users\dom53\Documents\_workspace\____new_project_here\_python-project\DochazkovySystem\_files\dochazkadb.db"
db_file = r"Y:\_workspace\dochazkovysystemv2-2\_files\dochazkadb.db"


def main():

    # conn = None
    # try:
    #     conn = sqlite3.connect(db_file)
    #     print(sqlite3.version)
    # except Error as e:
    #     print(e)
    # finally:
    #     if conn:
    #         conn.close()

    userTable = """ CREATE TABLE IF NOT EXISTS users (
                                            userId INTEGER PRIMARY KEY not null,
                                            username VARCHAR(255) not null,
                                            password VARCHAR(255) not null,
                                            firstName VARCHAR(255) not null,
                                            surname VARCHAR(255) not null,
                                            hireDate VARCHAR(10) not null,
                                            wagePerHour INT NOT NULL DEFAULT 100,
                                            isEmployer BOOLEAN NOT NULL DEFAULT 0
                                        ); """

    presenceTable = """ CREATE TABLE IF NOT EXISTS presence (
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
        create_table(conn, userTable)
        create_table(conn, presenceTable)

        # Insert data
        # user1 = ('test', 'test', 'David', 'Mašek', '20.05.2020', 1)
        # create_user(conn, user1)
        # create_user(conn, user1)
        # create_user(conn, user1)
        # create_user(conn, user1)
        # create_user(conn, user1)

        # Update data
        #update_user(conn, (120, 1))

        # Delete data
        #delete_user(conn, 2)

        # Select data by id
        #select_user_by_id(conn, 1)
        # select_user_by_credentials(conn, 'dom53', 'admin')

        seed_data(conn)

    else:
        print("Error! cannot create the database connection.")


def seed_data(connection):
    if connection is not None:
        create_user(connection, ('dom53', 'admin', 'Dominik', 'Mandinec', '17.01.2019'))
        create_user(connection, ('admin', 'admin', 'Cristen', 'Klausen', '17.01.2019'))
        create_user(connection, ('atallis2', 'admin', 'Alicea', 'Tallis', '20.01.2019'))
        create_user(connection, ('mserris3', 'admin', 'Merwin', 'Serris', '07.01.2019'))
        create_user(connection, ('rfalkous4', 'admin', 'Ruddie', 'Falkous', '01.01.2019'))
        create_user(connection, ('vmaccaghan5', 'admin', 'Violante', 'MacCaghan', '05.01.2019'))
        create_user(connection, ('blamping6', 'admin', 'Brendin', 'Lamping', '13.01.2019'))
        create_user(connection, ('myearsley7', 'admin', 'Mervin', 'Yearsley', '26.01.2019'))
        create_user(connection, ('dtoffolini8', 'admin', 'Darcee', 'Toffolini', '20.01.2019'))
        create_user(connection, ('jfairnington9', 'admin', 'Jaymie', 'Fairnington', '11.01.2019'))
        create_user(connection, ('ecrannella', 'admin', 'Eilis', 'Crannell', '27.01.2019'))
        create_user(connection, ('gkennaghb', 'admin', 'Granger', 'Kennagh', '14.01.2019'))
        create_user(connection, ('ngirogettic', 'admin', 'Nell', 'Girogetti', '04.01.2019'))
        create_user(connection, ('bcoand', 'admin', 'Bethany', 'Coan', '24.01.2019'))
        create_user(connection, ('pjewise', 'admin', 'Paddy', 'Jewis', '04.01.2019'))


def get_presence_groupby_year_by_id(conn, id):
    cur = conn.cursor()
    cur.execute("SELECT substr(date,1,4) FROM presence WHERE userId=? group by substr(date,1,4)", (id,))

    rows = cur.fetchall()

    # for row in rows:
    #     print(row)
    return rows

def select_user_by_id(conn, id):
    """
    Query tasks by priority
    :param conn: the Connection object
    :param priority:
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE userId=?", (id,))

    row = cur.fetchall()
    # print(row)
    return row

def user_exist(conn, username):
    print("db user")
    cur = conn.cursor()
    cur.execute("SELECT count(*) FROM users WHERE username=?", (username,))

    row = cur.fetchall()
    if(row[0][0] == 0):
        return False
    return True

def check_pass(conn, passw):
    print("db user")
    cur = conn.cursor()
    cur.execute("SELECT count(*) FROM users WHERE password=?", (passw,))

    row = cur.fetchall()
    if(row[0][0] == 0):
        return False
    return True


def exist_timeIn(conn, id, date):
    cur = conn.cursor()
    cur.execute("SELECT count(*) FROM presence WHERE userId=? AND date=?", (id, date,))

    row = cur.fetchall()
    if(row[0][0] == 0):
        return False
    return True
    #return row

def exist_timeOut(conn, id, date):
    cur = conn.cursor()
    cur.execute("SELECT count(*) FROM presence WHERE userId=? AND date=? AND timeOut IS NULL", (id, date,))

    row = cur.fetchall()
    print(row[0][0])
    if(row[0][0] == 1):
        return False
    return True

def select_presence_by_user_id(conn, id, date, month):

    cur = conn.cursor()
    print("iid: " + str(id))
    print("ddate: " + date)
    print("mmonth: " + month)
    convert_month = helper.Validation.month_to_number(month)
    print(convert_month)
    mesic = date+'-'+convert_month+'%'
    print(mesic)
    cur.execute("SELECT * FROM presence WHERE userId= ? AND date LIKE ? ORDER BY date", (id, date+'-'+convert_month+'%',))

    rows = cur.fetchall()
    # print(row)
    return rows

def select_user_day_count(conn, id, date, month):
    cur = conn.cursor()
    convert_month = helper.Validation.month_to_number(month)
    # print(convert_month)
    cur.execute(
        "SELECT count(*) FROM presence WHERE userId= ? AND timeOut is not null AND date LIKE ? ORDER BY date",
        (id, date + '-' + convert_month + '%',))
    row = cur.fetchall()

    return row[0][0]


def select_user_time(conn, id, date, month):

    cur = conn.cursor()

    h = 0
    m = 0
    convert_month = helper.Validation.month_to_number(month)

    # convert_month = helper.Validation.month_to_number(month)
    # print(convert_month)
    cur.execute("SELECT timeIn, timeOut FROM presence WHERE userId= ? AND timeOut is not null AND date LIKE ? ORDER BY date", (id, date+'-'+convert_month+'%',))
    rows = cur.fetchall()
    for x in rows:
        celkovy_cas = helper.Validation.pocet_hodin(x[1], x[0])
        # print(celkovy_cas)
        h += int(celkovy_cas.split(":")[0])
        m += int(celkovy_cas.split(":")[1])

    # print(h)
    # print(m)
    # t = '{:02d}:{:02d}'.format(*divmod(m, 60))
    #print(helper.Validation.number_to_time(h, m))
    #print(celkovy_cas)
    # print(row)
    return helper.Validation.number_to_time(h, m)


def select_user_mzda(conn, id, date, month):
    time = select_user_time(conn, id, date, month)

    cur = conn.cursor()
    cur.execute("SELECT wagePerHour FROM users WHERE userId= ?", (id,))
    row = cur.fetchall()
    # print("time: " + time + ", mzda: " + str(row[0]))


    t = time
    (h, m) = t.split(':')
    result = int(h) * 3600 + int(m) * 60
    final_hours = result / 60 / 60
    # print(str(int(final_hours) * float(row[0])) + ",-Kč")
    mzda = row[0]
    # print("minutes: ", result)
    # print("hodiny: ", final_hours)
    # print("mzda: ", row[0][0])
    # print(float(final_hours) * float(row[0][0]))
    celkova_mzda = float(final_hours) * float(row[0][0])

    locale.setlocale(locale.LC_ALL, '')
    mzd = locale.currency(round(celkova_mzda, 2), grouping=True)

    return str(mzd)
    #return float(final_hours) * float(row[0])


def select_user_by_credentials(conn, username, password):
    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE username=? and password=?", (username, password))

    row = cur.fetchall()
    print("login user is:")
    print(row)
    return row

def delete_user(conn, id):
    """
    Delete a task by task id
    :param conn:  Connection to the SQLite database
    :param id: id of the task
    :return:
    """
    sql = 'DELETE FROM users WHERE userId=?'
    cur = conn.cursor()
    cur.execute(sql, (id,))
    conn.commit()

def update_user(conn, task):
    """
    update priority, begin_date, and end date of a task
    :param conn:
    :param task:
    :return: project id
    """
    sql = ''' UPDATE users
              SET wagePerHour = ?
              WHERE userId = ?'''
    cur = conn.cursor()
    cur.execute(sql, task)
    conn.commit()

def update_presence(conn, task):
    """
    update priority, begin_date, and end date of a task
    :param conn:
    :param task:
    :return: project id
    """
    sql = ''' UPDATE presence
              SET timeIn = ?, timeOut = ?
              WHERE userId = ? AND id = ?'''
    cur = conn.cursor()
    cur.execute(sql, task)
    conn.commit()

def create_user(conn, project):
    """
    Create a new project into the projects table
    :param conn:
    :param project:
    :return: project id
    """
    sql = ''' INSERT INTO users(username,password,firstName,surname,hireDate)
              VALUES(?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, project)
    conn.commit()
    #return cur.lastrowid

def hire_user(conn, project):
    sql = ''' INSERT INTO users(username,password,firstName,surname,hireDate,wagePerHour)
              VALUES(?,?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, project)
    conn.commit()
    #return cur.lastrowid


def create_presence(conn, project):
    sql = ''' INSERT INTO presence(id,timeIn,timeOut,date,userId)
              VALUES(?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, project)
    conn.commit()

def create_presence_in(conn, project):
    sql = ''' INSERT INTO presence(timeIn,date,userId)
              VALUES(?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, project)
    conn.commit()

def create_presence_out(conn, project):
    sql = ''' UPDATE presence
                  SET timeOut = ?
                  WHERE date = ? AND userId = ?'''
    cur = conn.cursor()
    cur.execute(sql, project)
    conn.commit()

def change_password(conn, project):
    sql = ''' UPDATE users
                  SET password = ?
                  WHERE userId = ?'''
    cur = conn.cursor()
    cur.execute(sql, project)
    conn.commit()


def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

def create_connection():
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn


if __name__ == '__main__':
    main()
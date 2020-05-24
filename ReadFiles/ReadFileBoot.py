import sqlite3
from sqlite3 import Error

conn = None
db_file = r"C:\Users\dom53\Documents\_workspace\____new_project_here\_python-project\DochazkovySystem\_files\dochazkadb.db"


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
                                            wagePerHour INT NOT NULL DEFAULT 100
                                        ); """

    presenceTable = """ CREATE TABLE IF NOT EXISTS presence (
                                            id INTEGER PRIMARY KEY not null,
                                            timeIn VARCHAR(5) not null,
                                            timeOut VARCHAR(5) not null,
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
        user1 = ('test', 'test', 'David', 'Mašek', '20.05.2020', 1)
        create_user(conn, user1)
        create_user(conn, user1)
        create_user(conn, user1)
        create_user(conn, user1)
        create_user(conn, user1)

        # Update data
        #update_user(conn, (120, 1))

        # Delete data
        #delete_user(conn, 2)

        # Select data by id
        #select_user_by_id(conn, 1)
        select_user_by_credentials(conn, 'dom53', 'admin')

    else:
        print("Error! cannot create the database connection.")




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

def select_user_by_credentials(conn, username, password):
    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE username=? and password=?", (username,password))

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

def create_user(conn, project):
    """
    Create a new project into the projects table
    :param conn:
    :param project:
    :return: project id
    """
    sql = ''' INSERT INTO users(username,password,firstName,surname,hireDate,wagePerHour)
              VALUES(?,?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, project)
    conn.commit()
    #return cur.lastrowid


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
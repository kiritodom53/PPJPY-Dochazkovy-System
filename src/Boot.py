# import src.Dochazka as dochazka
import src.Database as db
import os

def main():
    print(db.check_database())
    conn = db.create_connection()
    # db.main()
    users = db.check_tables(conn, "users")
    presence = db.check_tables(conn, "presence")

    if(users == False or presence == False):
        print("main")
        db.main()
        # Seed dat

    # users_data = db.check_table_data(conn, "users")
    # presence_data = db.check_table_data(conn, "presence")

    # if(db.check_database()):
    #     if (db.check_tables(conn, "users")):
    #         if (db.check_table_data(conn, "users") == False):
    #             pass
    #             # ToDo: vytvořit data
    #     else:
    #         # ToDo: vytvořit tabulku
    #         # ToDo: vytvořit data
    #         pass
    #     if (db.check_tables(conn, "presence")):
    #         if (db.check_table_data(conn, "presence") == False):
    #             pass
    #             # ToDo: vytvořit data
    #     else:
    #         # ToDo: vytvořit tabulku
    #         # ToDo: vytvořit data
    #         pass
    # else:
    #     pass
    #     # ToDo: vytvořit db file
    #     # ToDo: vytvořit tabulky
    #     # ToDo: vytvořit data
    #
    # if(users and presence):
    #     print("v poho")
    # else:
    #     print("ne ne")

    # dochazka


if __name__ == '__main__':
    main()

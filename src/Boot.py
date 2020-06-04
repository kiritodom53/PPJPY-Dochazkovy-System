# import src.Dochazka as dochazka
import src.Data.SeedData as sd
import src.Database as db
import os

def main():
    # Vytvoří db, pokud neexistuje
    if(db.check_database() == False):
        print(db.check_database())
        db.create_database()

    conn = db.create_connection()
    # db.main()
    users = db.check_tables(conn, "users")
    presence = db.check_tables(conn, "presence")

    # Vytvoří tabulky, pokud neexistují
    if(users == False or presence == False):
        print("main")
        db.create_tables()
        sd.main()
        # Seed dat
    import src.Dochazka

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

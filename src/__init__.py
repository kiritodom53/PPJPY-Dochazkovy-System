import src.Data.SeedData as sd
import src.Database as db

def main():
    if(db.check_database() == False):
        print(db.check_database())
        db.create_database()

    conn = db.create_connection()
    users = db.check_tables(conn, "users")
    presence = db.check_tables(conn, "presence")

    # Vytvoří tabulky, pokud neexistují
    if(users == False or presence == False):
        print("main")
        db.create_tables()
        print("seed data - start")
        sd.main()
        print("seed data - end")
        print("start dochazka")
    import src.Dochazka


if __name__ == '__main__':
    main()

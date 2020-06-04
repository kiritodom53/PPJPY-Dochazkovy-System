import src.Database as db
import json

presence_json_file = r"C:\Users\dom53\Documents\_workspace\____new_project_here\_python-project\DochazkovySystem\_files\presence.json"
presence_json_file2 = r"C:\Users\dom53\Documents\_workspace\____new_project_here\_python-project\DochazkovySystem\_files\pres2.json"

def main():
    conn = db.create_connection()
    # insert_presence(conn,read_json(presence_json_file))
    # update_presence(conn,read_json(presence_json_file2))
    db.get_presence_groupby_year_by_id(conn, 1)


def insert_presence(conn, data):
    for item in data:
        print(item)
        presence = (item['id'], item['timeIn'], item['timeOut'], item['date'], item['userID'])
        db.create_presence(conn, presence)

def update_presence(conn, data):
    for item in data:
        print(item)
        # presence = (item['id'], item['timeIn'], item['timeOut'], item['date'], item['userID'])
        # db.create_presence(conn, presence)
        pr2 = (item['timeIn'], item['timeOut'], item['userId'], item['id'])
        db.update_presence(conn, pr2)

def read_json(path):
    with open(path) as json_file:
        data = json.load(json_file)
        return data
        # for p in data:
        #     print(p)

if __name__ == '__main__':
    main()
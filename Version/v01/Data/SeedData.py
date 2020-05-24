import Version.v01.Database as db
import json

presence_json_file = r"C:\Users\dom53\Documents\_workspace\____new_project_here\_python-project\DochazkovySystem\_files\presence.json"

def main():
    conn = db.create_connection()
    # insert_presence(conn,read_json())
    db.get_presence_groupby_year_by_id(conn, 1)


def insert_presence(conn, data):
    for item in data:
        print(item)
        presence = (item['id'], item['timeIn'], item['timeOut'], item['date'], item['userID'])
        db.create_presence(conn, presence)

def read_json():
    with open(presence_json_file) as json_file:
        data = json.load(json_file)
        return data
        # for p in data:
        #     print(p)

if __name__ == '__main__':
    main()
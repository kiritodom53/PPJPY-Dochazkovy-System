import src.Database as db
import json
import os
import urllib.request

__presence_json_file = os.getcwd() + r"\presence.json"
__url = 'https://lide.uhk.cz/fim/student/mandido1/pythondochazka/presence.json'
urllib.request.urlretrieve(__url, 'presence.json')


def main():
    print(__presence_json_file)
    conn = db.create_connection()
    __insert_presence(conn, __read_json(__presence_json_file))
    db.get_presence_groupby_year_by_id(conn, 1)


def __insert_presence(conn, data):
    for item in data:
        print(item)
        presence = (item['id'], item['timeIn'], item['timeOut'], item['date'], item['userID'])
        db.create_presence(conn, presence)


def __update_presence(conn, data):
    for item in data:
        print(item)
        pr2 = (item['timeIn'], item['timeOut'], item['userId'], item['id'])
        db.update_presence(conn, pr2)


def __read_json(path):
    with open(path) as json_file:
        data = json.load(json_file)
        return data

# if __name__ == '__main__':
#     main()

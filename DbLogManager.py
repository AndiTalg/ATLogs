import sqlite3
import csv


class DbLogManager:

    def __init__(self):
        self.db_path = '/Users/andibub/Library/Mobile Documents/com~apple~CloudDocs/Developer/Python/Garmin/ATLog.sqlite3'
        self.csv_path = '/Users/andibub/Library/Mobile Documents/com~apple~CloudDocs/Developer/Python/Garmin/Activities.csv'

    def load_data(self):

        try:
            with open(self.csv_path, newline='', encoding='utf-8') as csvfile:
                activities = csv.reader(csvfile)
                for row in activities:
                    print(row)
                # try:
                #     con = sqlite3.connect(self.db_path)
                #     cur = con.cursor()
                #     activity_sql = '''
                #     CREATE TABLE IF NOT EXISTS activities (
                #         timestamp text PRIMARY KEY,
                #         type text NOT NULL,
                #         title text,
                #         distance text,
                #         calories text
                #         duration text,
                #         average_hf text,
                #         average_speed,
                #         p
                #
                #         '''
                # except:
                #     print('Database Error')

        except:
            print('CSV file not found')




myDB = DbLogManager()

myDB.load_data()

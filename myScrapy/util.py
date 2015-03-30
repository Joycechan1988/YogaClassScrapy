import sqlite3

def login():
    conn = sqlite3.connect(r'C:\Users\hchen11\AppData\Local\Google\Chrome\User Data\Default\Cookies')
    c = conn.cursor()
    for row in c.execute('Select * From cookies where host_key = \'3.util.sinaapp.com\''):
        print(row)


if __name__ == '__main__':
    login()
import pymssql

def test_sqlserver_connection():
    conn = pymssql.connect(server='sqlserver', user='sa', password='1qaz@WSX3edc', database='master')
    cursor = conn.cursor()
    cursor.execute('SELECT 1')
    result = cursor.fetchone()
    conn.close()
    assert result[0] == 1

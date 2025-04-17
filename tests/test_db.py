import os
import pymssql

def test_sqlserver_connection():
    conn = pymssql.connect(server='sqlserver', user='sa', password=os.environ['MYSQL_SA_PASSWORD'], database='master')
    cursor = conn.cursor()
    cursor.execute('SELECT 1')
    result = cursor.fetchone()
    conn.close()
    assert result[0] == 1


def get_test_data():
    conn = pymssql.connect(server='sqlserver', user='sa', password=os.environ['MYSQL_SA_PASSWORD'], database='TestDB')
    cursor = conn.cursor()
    cursor.execute("SELECT id, a, b, c, expected_result FROM dbo.AdditionTests")
    rows = cursor.fetchall()
    conn.close()
    return rows

def test_addition_should_pass():
    data = get_test_data()
    for id, a, b, c, expected in data:
        if expected == 1:
            print(f"Testing PASS case: ID={id}, a={a}, b={b}, c={c}")
            assert a + b == c, f"Test ID {id}: {a} + {b} != {c}, but expected to pass"

def test_addition_should_fail():
    data = get_test_data()
    for id, a, b, c, expected in data:
        if expected == 0:
            print(f"Testing FAIL case: ID={id}, a={a}, b={b}, c={c}")
            assert a + b != c, f"Test ID {id}: {a} + {b} == {c}, but expected to fail"

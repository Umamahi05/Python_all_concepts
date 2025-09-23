import pymysql

connection = pymysql.connect(
    host = 'testtowork',
    user='root',
    password='Prosper@100%',
    database='world',
    cursorclass=pymysql.cursors.DictCursor
)

try:
    with connection.cursor() as cursor:
        #Create a table
        create_qry = '''
            CREATE TABLE IF NOT EXISTS emp (
            id int AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(20),
            dept VARCHAR(20)
            );
        '''

        cursor.execute(create_qry)

        insert_qry = "INSERT INTO emp(name,dept) VALUES (%s, %s)"
        values = [("John","IT"), ("Jeff","HR"),("Bob","Finance")]
        cursor.executemany(insert_qry,values)
        connection.commit()

        select_qry = "SELECT * from emp"
        cursor.execute(select_qry)
        result = cursor.fetchall()

        with open("Sample_output.txt","w") as fHnd:
            for row in result:
                fHnd.write(f"{row}\n")
finally:
    connection.close()

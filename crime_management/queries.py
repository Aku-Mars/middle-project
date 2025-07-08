# Criminal Query
INSERT_CRIMINAL_QUERY = 'INSERT INTO criminal VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
SELECT_ALL_CRIMINAL_COLUMN_QUERY = 'SELECT * FROM criminal'
SELECT_CRIMINAL_TABLE_PRIMARY_COLUMN = 'SELECT * FROM criminal WHERE '
DELETE_CRIMINAL_QUERY = 'DELETE FROM criminal WHERE Case_id=%s'
UPDATE_CRIMINAL_QUERY = '''
UPDATE criminal 
            SET 
                Criminal_no=%s,
                Criminal_name=%s,
                Nick_name=%s,
                arrest_date=%s,
                dateOfcrime=%s,
                address=%s,
                age=%s,
                occupation=%s,
                BirthMark=%s,
                crimeType=%s,
                fatherName=%s,
                gender=%s,
                wanted=%s 
            WHERE Case_id=%s
'''

# Users Query
SELECT_USER_TABLE_WITH_WHERE = "SELECT * FROM users WHERE username=%s AND password=%s"
INSERT_NEW_USER = "INSERT INTO users (username, password) VALUES (%s, %s)"
SELECT_ALL_USER_TABLE = "SELECT username, password FROM users"

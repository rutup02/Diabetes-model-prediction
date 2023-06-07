
import pymysql as pymysql
# Connect to the database
connection = pymysql.connect(
    host='127.0.0.1',
    user='root',
    password='tech@123',
    database='diabetes'
)

def mysqldata(prg, glc,bp,st,inl, bmi, dpf, age, prediction):
    mycursor = connection.cursor()
    query = "INSERT INTO DIABETES(PREGNANCIES, GLUCOSE, BLOODPRESSURE, SKINTHICKNESS, INSULIN, BMI, DIABETESPEDEGREEEFUNCTION, AGE, OUTCOME) VALUES(%s, %s,%s,%s,%s,%s,%s,%s,%s)"
    vals = (prg, glc, bp,st, inl, bmi,dpf, age, prediction)
    mycursor.execute(query,vals )
    connection.commit()
# Read data into a Pandas DataFrame
# df = pd.read_sql('SELECT * FROM diabetes', con=connection)



import MySQLdb
conexao = MySQLdb.connect(host='mysql.topskills.study', database='topskills01', user='topskills01', passwd='ts2019')

cursor=conexao.cursor()
cursor.execute('SELECT * FROM 01_MDG_PESSOA')
pessoas = cursor.fetchall()

for p in pessoas:
    print(p)
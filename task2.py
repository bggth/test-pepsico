import sqlite3
con = sqlite3.connect('task2.db')

def task_21():
	print('\ntask 2.1')
	cur = con.cursor()
	try:
		cur.execute('DROP TABLE table1')
		cur.execute('DROP TABLE table2')
	except:
		pass
		
	cur.execute('CREATE TABLE table1(EntityID, value)')
	cur.execute('''
		INSERT INTO table1 VALUES
			('1', 1001),
			('2', 1002),
			('3', 1003),
			('4', 1004),
			('5', 1005),
			('6', 1006),
			('7', 1007)
	''')

	cur.execute('CREATE TABLE table2(EntityID, value)')
	cur.execute('''
		INSERT INTO table2 VALUES
			('4', 1004),
			('5', 1005),
			('6', 1006),
			('7', 1007)
	''')

	con.commit()

	result = cur.execute('''SELECT table1.EntityID, table1.value FROM table1 
 			WHERE NOT EXISTS (SELECT EntityID FROM table2 WHERE EntityID=table1.EntityID)''')
	
	for x in result.fetchall():
		print(x)

def task_22():
	print('\ntask 2.2 table')
	cur = con.cursor()
	try:
		cur.execute('DROP TABLE table1')
		cur.execute('DROP TABLE table2')
	except:
		pass
		
	cur.execute('''CREATE TABLE table1(RequestID, PositionID, CatalogID, PositionQuantity, PositionPrice)''')
	cur.execute('''
		INSERT INTO table1 VALUES
			(109, 1, 1001, 5, 5000),
			(109, 2, 1002, 6, 6000),
			(109, 3, 1003, 6, 6000),
			(110, 1, 1001, 7, 7000),
			(110, 2, 1002, 8, 8000),
			(110, 3, 1003, 8, 8000),
			(111, 1, 1001, 9, 9000),
			(111, 2, 1001, 8, 8000),
			(111, 3, 1002, 7, 7000),
			(111, 4, 1003, 7, 7000),
			(111, 5, 1003, 8, 8000),
			(111, 6, 1004, 9, 9000),
			(112, 1, 1001, 7, 7000),
			(112, 2, 1002, 6, 6000),
			(112, 3, 1003, 6, 6000),
			(112, 4, 1004, 7, 7000)
			''')
	con.commit()

	result = cur.execute('SELECT * FROM table1')
	for x in result.fetchall():
		print(x)

	print('\ntask 2.2 result')
	result = cur.execute('''SELECT CatalogID, SUM(PositionQuantity * PositionPrice) FROM table1 WHERE RequestID = 111 GROUP BY CatalogID''')
	for x in result.fetchall():
		print(x)

	print('\ntask 2.3 result')
	#result = cur.execute('''SELECT CatalogID, sum FROM (SELECT CatalogID, SUM(PositionQuantity * PositionPrice) as sum FROM table1 WHERE RequestID = 111 GROUP BY CatalogID) WHERE sum > 100000''')
	result = cur.execute('''SELECT CatalogID, SUM(PositionQuantity * PositionPrice) as sum FROM table1 WHERE RequestID = 111 GROUP BY CatalogID''')
	for x in result.fetchall():
		print(x)

def task_23():
	pass

def main():
	task_21()
	task_22()
	task_23()

if __name__ == '__main__':
	main()
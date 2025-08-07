import sqlite3

def conectar():
	return sqlite3.connect("dados_mqtt.db")

def ler_dados(n=50):
	conn = conectar()
	cursor = conn.cursor()
	cursor.execute("SELECT timestamp, valor FROM dados ORDER BY id DESC LIMIT ?", (n,))
	dados = cursor.fetchall()
	conn.close()
	return dados[::-1]

def criar_banco():
	conn = conectar()
	cursor = conn.cursor()
	cursor.execute('''
		CREATE TABLE IF NOT EXISTS dados (
			id INTEGER PRIMARY KEY AUTOINCREMENT,
			timestamp TEXT,
			valor INTEGER
		)
	''')
	conn.commit()
	conn.close()

def inserir_dado(conn, timestamp, valor):
	cursor = conn.cursor()
	cursor.execute('INSERT INTO dados (timestamp, valor) VALUES (?, ?)', (timestamp, valor))
	conn.commit()


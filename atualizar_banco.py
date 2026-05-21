import sqlite3

conn = sqlite3.connect("manutencao.db")
cursor = conn.cursor()

cursor.execute("""
    ALTER TABLE equipamentos
    ADD COLUMN ultima_manutencao TEXT
""")

conn.commit()
conn.close()
print("Coluna adicionada com sucesso!")
import sqlite3

conn = sqlite3.connect("manutencao.db")
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS equipamentos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT,
        horas INTEGER,
        setor TEXT,
        status TEXT
    )
""")

dados_iniciais = [
    ("Forno 1",      850,  "Fundição",   "ALERTA"),
    ("Forno 2",      600,  "Fundição",   "ATENÇÃO"),
    ("Forno 3",      1100, "Fundição",   "CRÍTICO"),
    ("Bomba 1",      400,  "Utilidades", "OK"),
    ("Compressor 1", 730,  "Utilidades", "ALERTA")
]

cursor.executemany("""
    INSERT INTO equipamentos (nome, horas, setor, status)
    VALUES (?, ?, ?, ?)
""", dados_iniciais)

conn.commit()
conn.close()
print("Banco criado com sucesso!")
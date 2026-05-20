from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

def get_equipamentos():
    conn = sqlite3.connect("manutencao.db")
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM equipamentos")
    equipamentos = cursor.fetchall()
    conn.close()
    return equipamentos

@app.route("/")
def home():
    equipamentos = get_equipamentos()
    return render_template("index.html", equipamentos=equipamentos)

from flask import Flask, render_template, request, redirect, url_for

def verificar_status(horas):
    if horas > 1000:
        return "CRÍTICO"
    elif horas > 720:
        return "ALERTA"
    elif horas > 500:
        return "ATENÇÃO"
    else:
        return "OK"

@app.route("/excluir", methods=["POST"])
def excluir():
    id = int(request.form["id"])

    conn = sqlite3.connect("manutencao.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM equipamentos WHERE id = ?", (id,))
    conn.commit()
    conn.close()

    return redirect(url_for("home"))

@app.route("/adicionar", methods=["POST"])
def adicionar():
    nome  = request.form["nome"]
    horas = int(request.form["horas"])
    setor = request.form["setor"]
    status = verificar_status(horas)

    conn = sqlite3.connect("manutencao.db")
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO equipamentos (nome, horas, setor, status)
        VALUES (?, ?, ?, ?)
    """, (nome, horas, setor, status))
    conn.commit()
    conn.close()

    return redirect(url_for("home"))

@app.route("/atualizar", methods=["POST"])
def atualizar():
    id    = int(request.form["id"])
    horas = int(request.form["horas"])
    status = verificar_status(horas)

    conn = sqlite3.connect("manutencao.db")
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE equipamentos
        SET horas = ?, status = ?
        WHERE id = ?
    """, (horas, status, id))
    conn.commit()
    conn.close()

    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)
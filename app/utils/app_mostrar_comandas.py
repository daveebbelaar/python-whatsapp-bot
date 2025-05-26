from flask import Flask, request, jsonify, render_template_string
from datetime import datetime

app = Flask(__name__)
comandas = []

html_template = """
<!DOCTYPE html>
<html>
<head>
    <title>🧾 Tablero de Comandas - Cocina</title>
    <meta charset="UTF-8">
    <meta http-equiv="refresh" content="5">
    <style>
        body { font-family: sans-serif; background: #1e1e2f; color: white; margin: 0; padding: 0; }
        h1 { text-align: center; background: #333; padding: 20px 0; margin: 0; font-size: 2em; }
        .grid { display: flex; flex-wrap: wrap; padding: 20px; justify-content: center; gap: 20px; }
        .card {
            background: #2c2c3c;
            border-radius: 12px;
            padding: 20px;
            width: 300px;
            box-shadow: 0 0 10px rgba(0,0,0,0.4);
            transition: transform 0.3s;
        }
        .card:hover { transform: scale(1.03); }
        .cliente { font-size: 1.2em; margin-bottom: 10px; }
        .hora { font-size: 0.9em; color: #aaa; margin-bottom: 10px; }
        ul { padding-left: 20px; }
        li { margin-bottom: 5px; }
    </style>
</head>
<body>
    <h1>🧾 COMANDAS EN COCINA</h1>
    <div class="grid">
        {% for comanda in comandas %}
        <div class="card">
            <div class="cliente"><strong>👤 {{ comanda.cliente }}</strong></div>
            <div class="hora">🕒 {{ comanda.hora_pedido }}</div>
            <div><strong>📝 Pedido:</strong></div>
            <ul>
                {% for item in comanda.pedido %}
                <li>{{ item.cantidad }} x {{ item.producto }}</li>
                {% endfor %}
            </ul>
        </div>
        {% endfor %}
    </div>
</body>
</html>
"""

@app.route("/", methods=["GET"])
def ver_comandas():
    return render_template_string(html_template, comandas=comandas)

@app.route("/comandas", methods=["POST"])
def recibir_comanda():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data provided"}), 400

    # Agregar hora si no viene incluida
    if "hora_pedido" not in data:
        data["hora_pedido"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    comandas.append(data)
    return jsonify({"status": "comanda recibida"}), 200

if __name__ == "__main__":
    app.run(port=5001)
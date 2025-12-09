from flask import Flask, jsonify

app = Flask(__name__)

# Mock Data (Contoh produk)
produk_data = {
    "items": [
        {"id": 1, "nama": "Monitor 24 Inch", "harga": 1500000},
        {"id": 2, "nama": "Mouse Wireless", "harga": 250000}
    ],
    "server": "Server 1 (Utama)"
}

@app.route('/api/v1/produk', methods=['GET'])
def get_produk():
    # Logic untuk menampilkan data produk
    return jsonify(produk_data)

if __name__ == '__main__':
    # Server 1 berjalan di Port 5001
    app.run(host='0.0.0.0', port=5001)

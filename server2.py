from flask import Flask, jsonify

app = Flask(__name__)

# Mock Data (Contoh produk)
produk_data = {
    "items": [
        {"id": 3, "nama": "Keyboard Mekanik", "harga": 800000},
        {"id": 4, "nama": "Headset Bluetooth", "harga": 450000}
    ],
    "server": "Server 2 (Cadangan/Failover)"
}

@app.route('/api/v1/produk', methods=['GET'])
def get_produk():
    # Logic untuk menampilkan data produk
    return jsonify(produk_data)

if __name__ == '__main__':
    # Server 2 berjalan di Port 5002
    app.run(host='0.0.0.0', port=5002)

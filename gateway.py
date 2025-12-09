from flask import Flask, jsonify
import requests

app = Flask(__name__)

# Daftar server untuk Failover
SERVER_LIST = [
    'http://127.0.0.1:5001',  # Server Utama
    'http://127.0.0.1:5002'   # Server Cadangan
]

@app.route('/api/v1/produk', methods=['GET'])
def proxy_request():
    
    # Coba setiap server dalam daftar
    for url_server in SERVER_LIST:
        target_url = url_server + '/api/v1/produk'
        try:
            # Mengirim permintaan ke server target
            response = requests.get(target_url, timeout=2) # Timeout 2 detik
            
            # Jika respons berhasil (200 OK), kembalikan respons tersebut
            if response.status_code == 200:
                print(f"Berhasil terhubung ke: {url_server}")
                return jsonify(response.json())
                
        except requests.exceptions.RequestException as e:
            # Jika koneksi gagal, lanjutkan ke server berikutnya
            print(f"Gagal terhubung ke {url_server}. Mencoba server berikutnya...")
            continue
            
    # Jika semua server gagal
    return jsonify({"error": "Layanan tidak tersedia. Semua server down."}), 503

if __name__ == '__main__':
    # Gateway berjalan di Port 5000 (Akses publik)
    app.run(host='0.0.0.0', port=5000)

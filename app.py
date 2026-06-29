from flask import Flask, render_template, jsonify
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/balance', methods=['GET'])
def get_balance():
    # اینجا موجودی را از دیتابیس می‌خواند
    conn = sqlite3.connect('bot.db')
    c = conn.cursor()
    c.execute("SELECT balance FROM users WHERE id='1'") # آیدی کاربر را چک کن
    bal = c.fetchone()[0]
    conn.close()
    return jsonify({"balance": bal})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

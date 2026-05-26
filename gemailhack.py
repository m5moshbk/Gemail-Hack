from flask import Flask, jsonify, request
from datetime import datetime
import os

app = Flask(__name__)

# المتغيرات الأساسية
PAYLINK_SECRET = os.environ.get("PAYLINK_SECRET_KEY")

@app.route('/')
def index():
    return "نظام أحمد الجعفري: البوابة تعمل بنجاح!"

@app.route('/api/webhook/paylink', methods=['POST'])
def paylink_webhook():
    payload = request.get_json()
    if payload and payload.get("orderStatus") == "Paid":
        print(f"✅ عملية ناجحة: {payload.get('orderNumber')}")
        return jsonify({"status": "ok"}), 200
    return jsonify({"status": "pending"}), 200

# لا حاجة لـ app.run في Render لأن Gunicorn سيتولى المهمة
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

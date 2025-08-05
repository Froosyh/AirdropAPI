from flask import Flask, request, jsonify

app = Flask(__name__)

# 1) Endpoint: جلب رصيد المحفظة
@app.route('/get_balance', methods=['GET'])
def get_balance():
    address = request.args.get('address')
    # هنا المفروض تحط كود يجلب الرصيد الحقيقي من البلوكشين
    return jsonify({
        "address": address,
        "balance": 123.45,  # مثال
        "symbol": "USDT"
    })

# 2) Endpoint: جلب قائمة الإيردروبات
@app.route('/get_airdrops', methods=['GET'])
def get_airdrops():
    data = [
        {
            "name": "Project Alpha",
            "project_url": "https://example.com/alpha",
            "reward": "100 Tokens",
            "deadline": "2025-12-31"
        },
        {
            "name": "Project Beta",
            "project_url": "https://example.com/beta",
            "reward": "50 Tokens",
            "deadline": "2025-11-15"
        }
    ]
    return jsonify(data)

# 3) Endpoint: تحليل الإيردروب
@app.route('/analyze_airdrop', methods=['POST'])
def analyze_airdrop():
    project_url = request.json.get('project_url')
    # هنا تكتب منطق التحليل
    return jsonify({
        "project_url": project_url,
        "score": 85,
        "verdict": "Good Potential",
        "notes": "Strong community and active development"
    })

if __name__ == '__main__':
    import os
port = int(os.environ.get("PORT", 5000))
app.run(host='0.0.0.0', port=port)


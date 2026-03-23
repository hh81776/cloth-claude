import os
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
# 設定照片存放路徑
UPLOAD_FOLDER = 'static/uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# 模擬資料庫
wardrobe_data = []

@app.route('/')
def index():
    # 計算統計數據
    stats = {
        "summer": len([i for i in wardrobe_data if i['season'] == '夏裝']),
        "winter": len([i for i in wardrobe_data if i['season'] == '冬裝'])
    }
    return render_template('index.html', items=wardrobe_data, stats=stats)

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files.get('image')
    name = request.form.get('name', '未命名衣物')
    
    if file:
        filename = file.filename
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        
        # 簡易 AI 辨識邏輯：根據名稱關鍵字判斷
        # 之後可在此處串接 Google Vision API 達成真正辨識
        season = "冬裝" if any(k in name for k in ["厚", "毛", "冬", "羽絨", "長袖"]) else "夏裝"
        
        wardrobe_data.append({
            "name": name,
            "season": season,
            "path": f"uploads/{filename}"
        })
    return redirect(url_for('index'))

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
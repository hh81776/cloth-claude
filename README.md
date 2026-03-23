# 衣櫥管家 👗

AI 智能衣物管理 App — 拍照自動識別冬衣／夏衣／冬褲／夏褲

## 功能

- 📸 **AI 智能識別** — 拍照或上傳衣物照片，Claude AI 自動分類
- 🗂 **衣物管理** — 冬衣、夏衣、冬褲、夏褲四大分類
- 📊 **統計面板** — 數量統計、季節比例、顏色分布
- 🎨 **顏色標記** — 10 種顏色標籤
- 📱 **行動裝置優先** — 支援手機相機直拍

## 本地開發

```bash
npm install
npm start
# 開啟 http://localhost:3000
```

## 部署到 Railway

1. Fork 或 clone 此 repo 到你的 GitHub
2. 前往 [railway.app](https://railway.app) 並登入
3. 點擊 **New Project** → **Deploy from GitHub repo**
4. 選擇此 repo，Railway 會自動偵測 Node.js 並部署
5. 部署完成後，點擊 **Generate Domain** 取得網址

### 環境需求

- Node.js ≥ 18
- 無需資料庫（資料存於瀏覽器 localStorage）

## 技術架構

- **後端**: Node.js + Express（靜態檔案伺服器）
- **前端**: 純 HTML/CSS/JS（無框架）
- **AI**: Anthropic Claude API（圖片識別）
- **儲存**: 瀏覽器 localStorage

## 注意事項

AI 識別功能使用 Anthropic Claude API，需要在有 API Key 的環境下才能使用（claude.ai 內建支援）。

若要在自己的 Railway 環境中完整使用 AI 功能，可以：
1. 在前端加入你的 Anthropic API Key（注意安全性）
2. 或在 Express server 建立 `/api/analyze` proxy endpoint

---

Made with ❤️ using Claude AI

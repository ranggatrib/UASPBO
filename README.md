# 🚀 Bootcamp Final Project

## 📄 Resume Bootcamp
https://seen-guava-b40.notion.site/Resume-22e593e4804c8097b072c2c70156a281?pvs=141

## 🧪 Final Project

### 🔧 **Project 1: Building an API Service**

#### 🎯 Fitur:
- ✅ Register
- ✅ Login
- ✅ Get User Data
- ✅ Update User Data
- ✅ Set User Status: Active / Inactive
- ✅ Soft Delete User (non-permanen)

#### 🛠️ Teknologi:
- 🟩 Node.js / Express
- 🍃 MongoDB / 🐬 MySQL
- ♻️ PM2 (background service)
- 🌐 nginx (`proxy_pass`)
- 🌍 Ngrok (untuk local server / WSL)
  
  #### 🚀 Deployment:
- 💻 Lokal (via Ngrok untuk WSL)
- ☁️ Publik (via VPS dengan nginx + PM2)
  
## ⚙️ Cara Menjalankan Project

#### 1. Clone Repository
```bash
git clone https://github.com/ranggatrib/Final-Bootcamp.git
cd Final-Bootcamp/api-service
```
### 2. Install Dependencies
```bash
npm install
```

### 4. Konfigurasi `.env`
```env
PORT=3000
MONGODB_URI=mongodb://localhost:27017/api_service
JWT_SECRET=supersecretjwtkey
```

### 4. Start MongoDB
```bash
mongod --dbpath /data/db
```

### 5. Jalankan Project
```bash
node app.js
```

### 6. Jalankan API dengan PM2
```bash
pm2 start app.js --name api-service
```

### 7. Gunakan Ngrok (jika di WSL)
```bash
ngrok http 3000
```

## 🔁 Endpoint API

| Method | Endpoint                | Deskripsi                    |
|--------|-------------------------|------------------------------|
| POST   | `/api/register`         | Registrasi user              |
| POST   | `/api/login`            | Login dan dapatkan JWT       |
| GET    | `/api/user`             | Ambil data user              |
| PUT    | `/api/user`             | Update data user             |
| PATCH  | `/api/user/status`      | Ubah status user (aktif/non) |
| DELETE | `/api/user`             | Soft delete data user        |

> 🔐 Semua endpoint kecuali `/register` dan `/login` memerlukan JWT di header:
```
Authorization: Bearer <your_token>
```

## 🌐 Deployment
🛠️ PM2: untuk menjalankan project di background
🌐 NGINX: untuk akses publik via domain (proxy ke localhost)
🌍 Ngrok: jika menggunakan WSL / lokal dan ingin expose ke publik

## ⚙️ PM2 Status
<img src="pm2.png" width="700"/>

# 🌱 FarmAz (farmaz.info)

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![Django](https://img.shields.io/badge/Django-4.0+-green.svg)

---

## 📖 Haqqında

**FarmAz** platforması, fermerlərə müəyyən illər aralığındakı statistikanı analiz edərək maksimum gəlir əldə etməyə kömək edən **AI dəstəkli** bir sistemdir.  

Bizim sistemimiz fermer məhsullarının tarixi verilənlərini təhlil edərək gələcəkdəki trend və qiymət dəyişikliklərini proqnozlaşdırır.  
Bu da fermerlərə daha düzgün qərarlar verməyə və gəlirlərini artırmağa şərait yaradır.

---

## ⚡ Quraşdırma və işə salma

Layihəni lokal mühitinizdə işə salmaq üçün aşağıdakı addımları izləyin:

```bash
# 1. Repository-ni klonlayın
git clone <repo-link>
cd FarmAz

# 2. Virtual mühit yaradın
python -m venv .venv

# 3. Virtual mühiti aktivləşdirin
# Linux / MacOS
source .venv/bin/activate
# Windows
.venv\Scripts\activate

# 4. Asılılıqları quraşdırın
pip install -r requirements.txt

# 5. .env faylını yaradın
# Linux / MacOS
cp .env.example .env
# Windows
copy .env.example .env

# Lazımi dəyişənləri .env faylında doldurun


## 🚀 Layihəni işə salmaq

```bash
python manage.py migrate
python manage.py runserver

Sonra brauzerdə açın:
👉 http://localhost:8000

URL: http://localhost:8000/admin
İstifadəçi adı: admin
Parol: admin

from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
# সব সূরা ও তাদের অডিও লিংক
surahs = [
  {"number": 1, "name": "Al-Fatiha", "audio": "http://server1.iloveallaah.com/recitation/mishary/001.mp3"},
  {"number": 2, "name": "Al-Baqara", "audio": "http://server1.iloveallaah.com/recitation/mishary/002.mp3"},
  {"number": 3, "name": "Aal-E-Imran", "audio": "http://server1.iloveallaah.com/recitation/mishary/003.mp3"},
  {"number": 4, "name": "An-Nisa", "audio": "http://server1.iloveallaah.com/recitation/mishary/004.mp3"},
  {"number": 5, "name": "Al-Ma'idah", "audio": "http://server1.iloveallaah.com/recitation/mishary/005.mp3"},
  {"number": 6, "name": "Al-An'am", "audio": "http://server1.iloveallaah.com/recitation/mishary/006.mp3"},
  {"number": 7, "name": "Al-A'raf", "audio": "http://server1.iloveallaah.com/recitation/mishary/007.mp3"},
  {"number": 8, "name": "Al-Anfal", "audio": "http://server1.iloveallaah.com/recitation/mishary/008.mp3"},
  {"number": 9, "name": "At-Tawba", "audio": "http://server1.iloveallaah.com/recitation/mishary/009.mp3"},
  {"number": 10, "name": "Yunus", "audio": "http://server1.iloveallaah.com/recitation/mishary/010.mp3"},
  {"number": 11, "name": "Hud", "audio": "http://server1.iloveallaah.com/recitation/mishary/011.mp3"},
  {"number": 12, "name": "Yusuf", "audio": "http://server1.iloveallaah.com/recitation/mishary/012.mp3"},
  {"number": 13, "name": "Ar-Ra'd", "audio": "http://server1.iloveallaah.com/recitation/mishary/013.mp3"},
  {"number": 14, "name": "Ibrahim", "audio": "http://server1.iloveallaah.com/recitation/mishary/014.mp3"},
  {"number": 15, "name": "Al-Hijr", "audio": "http://server1.iloveallaah.com/recitation/mishary/015.mp3"},
  {"number": 16, "name": "An-Nahl", "audio": "http://server1.iloveallaah.com/recitation/mishary/016.mp3"},
  {"number": 17, "name": "Al-Isra", "audio": "http://server1.iloveallaah.com/recitation/mishary/017.mp3"},
  {"number": 18, "name": "Al-Kahf", "audio": "http://server1.iloveallaah.com/recitation/mishary/018.mp3"},
  {"number": 19, "name": "Maryam", "audio": "http://server1.iloveallaah.com/recitation/mishary/019.mp3"},
  {"number": 20, "name": "Taha", "audio": "http://server1.iloveallaah.com/recitation/mishary/020.mp3"},
  {"number": 21, "name": "Al-Anbiya", "audio": "http://server1.iloveallaah.com/recitation/mishary/021.mp3"},
  {"number": 22, "name": "Al-Hajj", "audio": "http://server1.iloveallaah.com/recitation/mishary/022.mp3"},
  {"number": 23, "name": "Al-Mu'minun", "audio": "http://server1.iloveallaah.com/recitation/mishary/023.mp3"},
  {"number": 24, "name": "An-Nur", "audio": "http://server1.iloveallaah.com/recitation/mishary/024.mp3"},
  {"number": 25, "name": "Al-Furqan", "audio": "http://server1.iloveallaah.com/recitation/mishary/025.mp3"},
  {"number": 26, "name": "Ash-Shu'ara", "audio": "http://server1.iloveallaah.com/recitation/mishary/026.mp3"},
  {"number": 27, "name": "An-Naml", "audio": "http://server1.iloveallaah.com/recitation/mishary/027.mp3"},
  {"number": 28, "name": "Al-Qasas", "audio": "http://server1.iloveallaah.com/recitation/mishary/028.mp3"},
  {"number": 29, "name": "Al-Ankabut", "audio": "http://server1.iloveallaah.com/recitation/mishary/029.mp3"},
  {"number": 30, "name": "Ar-Rum", "audio": "http://server1.iloveallaah.com/recitation/mishary/030.mp3"},
  {"number": 31, "name": "Luqman", "audio": "http://server1.iloveallaah.com/recitation/mishary/031.mp3"},
  {"number": 32, "name": "As-Sajda", "audio": "http://server1.iloveallaah.com/recitation/mishary/032.mp3"},
  {"number": 33, "name": "Al-Ahzab", "audio": "http://server1.iloveallaah.com/recitation/mishary/033.mp3"},
  {"number": 34, "name": "Saba", "audio": "http://server1.iloveallaah.com/recitation/mishary/034.mp3"},
  {"number": 35, "name": "Fatir", "audio": "http://server1.iloveallaah.com/recitation/mishary/035.mp3"},
  {"number": 36, "name": "Ya-Sin", "audio": "http://server1.iloveallaah.com/recitation/mishary/036.mp3"},
  {"number": 37, "name": "As-Saffat", "audio": "http://server1.iloveallaah.com/recitation/mishary/037.mp3"},
  {"number": 38, "name": "Sad", "audio": "http://server1.iloveallaah.com/recitation/mishary/038.mp3"},
  {"number": 39, "name": "Az-Zumar", "audio": "http://server1.iloveallaah.com/recitation/mishary/039.mp3"},
  {"number": 40, "name": "Ghafir", "audio": "http://server1.iloveallaah.com/recitation/mishary/040.mp3"},
  {"number": 41, "name": "Fussilat", "audio": "http://server1.iloveallaah.com/recitation/mishary/041.mp3"},
  {"number": 42, "name": "Ash-Shura", "audio": "http://server1.iloveallaah.com/recitation/mishary/042.mp3"},
  {"number": 43, "name": "Az-Zukhruf", "audio": "http://server1.iloveallaah.com/recitation/mishary/043.mp3"},
  {"number": 44, "name": "Ad-Dukhan", "audio": "http://server1.iloveallaah.com/recitation/mishary/044.mp3"},
  {"number": 45, "name": "Al-Jathiya", "audio": "http://server1.iloveallaah.com/recitation/mishary/045.mp3"},
  {"number": 46, "name": "Al-Ahqaf", "audio": "http://server1.iloveallaah.com/recitation/mishary/046.mp3"},
  {"number": 47, "name": "Muhammad", "audio": "http://server1.iloveallaah.com/recitation/mishary/047.mp3"},
  {"number": 48, "name": "Al-Fath", "audio": "http://server1.iloveallaah.com/recitation/mishary/048.mp3"},
  {"number": 49, "name": "Al-Hujurat", "audio": "http://server1.iloveallaah.com/recitation/mishary/049.mp3"},
  {"number": 50, "name": "Qaf", "audio": "http://server1.iloveallaah.com/recitation/mishary/050.mp3"},
  {"number": 51, "name": "Adh-Dhariyat", "audio": "http://server1.iloveallaah.com/recitation/mishary/051.mp3"},
  {"number": 52, "name": "At-Tur", "audio": "http://server1.iloveallaah.com/recitation/mishary/052.mp3"},
  {"number": 53, "name": "An-Najm", "audio": "http://server1.iloveallaah.com/recitation/mishary/053.mp3"},
  {"number": 54, "name": "Al-Qamar", "audio": "http://server1.iloveallaah.com/recitation/mishary/054.mp3"},
  {"number": 55, "name": "Ar-Rahman", "audio": "http://server1.iloveallaah.com/recitation/mishary/055.mp3"},
  {"number": 56, "name": "Al-Waqia", "audio": "http://server1.iloveallaah.com/recitation/mishary/056.mp3"},
  {"number": 57, "name": "Al-Hadid", "audio": "http://server1.iloveallaah.com/recitation/mishary/057.mp3"},
  {"number": 58, "name": "Al-Mujadila", "audio": "http://server1.iloveallaah.com/recitation/mishary/058.mp3"},
  {"number": 59, "name": "Al-Hashr", "audio": "http://server1.iloveallaah.com/recitation/mishary/059.mp3"},
  {"number": 60, "name": "Al-Mumtahina", "audio": "http://server1.iloveallaah.com/recitation/mishary/060.mp3"},
  {"number": 61, "name": "As-Saff", "audio": "http://server1.iloveallaah.com/recitation/mishary/061.mp3"},
  {"number": 62, "name": "Al-Jumua", "audio": "http://server1.iloveallaah.com/recitation/mishary/062.mp3"},
  {"number": 63, "name": "Al-Munafiqoon", "audio": "http://server1.iloveallaah.com/recitation/mishary/063.mp3"},
  {"number": 64, "name": "At-Taghabun", "audio": "http://server1.iloveallaah.com/recitation/mishary/064.mp3"},
  {"number": 65, "name": "At-Talaq", "audio": "http://server1.iloveallaah.com/recitation/mishary/065.mp3"},
  {"number": 66, "name": "At-Tahrim", "audio": "http://server1.iloveallaah.com/recitation/mishary/066.mp3"},
  {"number": 67, "name": "Al-Mulk", "audio": "http://server1.iloveallaah.com/recitation/mishary/067.mp3"},
  {"number": 68, "name": "Al-Qalam", "audio": "http://server1.iloveallaah.com/recitation/mishary/068.mp3"},
  {"number": 69, "name": "Al-Haqqa", "audio": "http://server1.iloveallaah.com/recitation/mishary/069.mp3"},
  {"number": 70, "name": "Al-Maarij", "audio": "http://server1.iloveallaah.com/recitation/mishary/070.mp3"},
  {"number": 71, "name": "Nuh", "audio": "http://server1.iloveallaah.com/recitation/mishary/071.mp3"},
  {"number": 72, "name": "Al-Jinn", "audio": "http://server1.iloveallaah.com/recitation/mishary/072.mp3"},
  {"number": 73, "name": "Al-Muzzammil", "audio": "http://server1.iloveallaah.com/recitation/mishary/073.mp3"},
  {"number": 74, "name": "Al-Muddathir", "audio": "http://server1.iloveallaah.com/recitation/mishary/074.mp3"},
  {"number": 75, "name": "Al-Qiyama", "audio": "http://server1.iloveallaah.com/recitation/mishary/075.mp3"},
  {"number": 76, "name": "Al-Insan", "audio": "http://server1.iloveallaah.com/recitation/mishary/076.mp3"},
  {"number": 77, "name": "Al-Mursalat", "audio": "http://server1.iloveallaah.com/recitation/mishary/077.mp3"},
  {"number": 78, "name": "An-Naba", "audio": "http://server1.iloveallaah.com/recitation/mishary/078.mp3"},
  {"number": 79, "name": "An-Nazi'at", "audio": "http://server1.iloveallaah.com/recitation/mishary/079.mp3"},
  {"number": 80, "name": "Abasa", "audio": "http://server1.iloveallaah.com/recitation/mishary/080.mp3"},
  {"number": 81, "name": "At-Takwir", "audio": "http://server1.iloveallaah.com/recitation/mishary/081.mp3"},
  {"number": 82, "name": "Al-Infitar", "audio": "http://server1.iloveallaah.com/recitation/mishary/082.mp3"},
  {"number": 83, "name": "Al-Mutaffifin", "audio": "http://server1.iloveallaah.com/recitation/mishary/083.mp3"},
  {"number": 84, "name": "Al-Inshiqaq", "audio": "http://server1.iloveallaah.com/recitation/mishary/084.mp3"},
  {"number": 85, "name": "Al-Buruj", "audio": "http://server1.iloveallaah.com/recitation/mishary/085.mp3"},
  {"number": 86, "name": "At-Tariq", "audio": "http://server1.iloveallaah.com/recitation/mishary/086.mp3"},
  {"number": 87, "name": "Al-Ala", "audio": "http://server1.iloveallaah.com/recitation/mishary/087.mp3"},
  {"number": 88, "name": "Al-Ghashiya", "audio": "http://server1.iloveallaah.com/recitation/mishary/088.mp3"},
  {"number": 89, "name": "Al-Fajr", "audio": "http://server1.iloveallaah.com/recitation/mishary/089.mp3"},
  {"number": 90, "name": "Al-Balad", "audio": "http://server1.iloveallaah.com/recitation/mishary/090.mp3"},
  {"number": 91, "name": "Ash-Shams", "audio": "http://server1.iloveallaah.com/recitation/mishary/091.mp3"},
  {"number": 92, "name": "Al-Lail", "audio": "http://server1.iloveallaah.com/recitation/mishary/092.mp3"},
  {"number": 93, "name": "Ad-Duhaa", "audio": "http://server1.iloveallaah.com/recitation/mishary/093.mp3"},
  {"number": 94, "name": "Ash-Sharh", "audio": "http://server1.iloveallaah.com/recitation/mishary/094.mp3"},
  {"number": 95, "name": "At-Tin", "audio": "http://server1.iloveallaah.com/recitation/mishary/095.mp3"},
  {"number": 96, "name": "Al-Alaq", "audio": "http://server1.iloveallaah.com/recitation/mishary/096.mp3"},
  {"number": 97, "name": "Al-Qadr", "audio": "http://server1.iloveallaah.com/recitation/mishary/097.mp3"},
  {"number": 98, "name": "Al-Bayyina", "audio": "http://server1.iloveallaah.com/recitation/mishary/098.mp3"},
  {"number": 99, "name": "Az-Zalzala", "audio": "http://server1.iloveallaah.com/recitation/mishary/099.mp3"},
  {"number": 100, "name": "Al-Adiyat", "audio": "http://server1.iloveallaah.com/recitation/mishary/100.mp3"},
  {"number": 101, "name": "Al-Qaria", "audio": "http://server1.iloveallaah.com/recitation/mishary/101.mp3"},
  {"number": 102, "name": "At-Takathur", "audio": "http://server1.iloveallaah.com/recitation/mishary/102.mp3"},
  {"number": 103, "name": "Al-Asr", "audio": "http://server1.iloveallaah.com/recitation/mishary/103.mp3"},
  {"number": 104, "name": "Al-Humaza", "audio": "http://server1.iloveallaah.com/recitation/mishary/104.mp3"},
  {"number": 105, "name": "Al-Fīl", "audio": "http://server1.iloveallaah.com/recitation/mishary/105.mp3"},
  {"number": 106, "name": "Quraysh", "audio": "http://server1.iloveallaah.com/recitation/mishary/106.mp3"},
  {"number": 107, "name": "Al-Maun", "audio": "http://server1.iloveallaah.com/recitation/mishary/107.mp3"},
  {"number": 108, "name": "Al-Kauthar", "audio": "http://server1.iloveallaah.com/recitation/mishary/108.mp3"},
  {"number": 109, "name": "Al-Kafirun", "audio": "http://server1.iloveallaah.com/recitation/mishary/109.mp3"},
  {"number": 110, "name": "An-Nasr", "audio": "http://server1.iloveallaah.com/recitation/mishary/110.mp3"},
  {"number": 111, "name": "Al-Lahab", "audio": "http://server1.iloveallaah.com/recitation/mishary/111.mp3"},
  {"number": 112, "name": "Al-Ikhlas", "audio": "http://server1.iloveallaah.com/recitation/mishary/112.mp3"},
  {"number": 113, "name": "Al-Falaq", "audio": "http://server1.iloveallaah.com/recitation/mishary/113.mp3"},
  {"number": 114, "name": "An-Nas", "audio": "http://server1.iloveallaah.com/recitation/mishary/114.mp3"}

]

@app.route('/')
def home():
    return jsonify({
        "message": "Welcome to the Quran Audio API",
        "usage": {
            "all_surahs": "/api/arbi_surah",
            "single_surah": "/api/arbi_surah/<number>"
        }
    })

@app.route('/api/arbi_surah')
def all_surah():
    return jsonify(surahs)

@app.route('/api/arbi_surah/<int:number>')
def single_surah(number):
    surah = next((s for s in surahs if s["number"] == number), None)
    if surah:
        return jsonify(surah)
    return jsonify({"error": "Surah not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)

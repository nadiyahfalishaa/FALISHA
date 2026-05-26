from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template ("index.html")

@app.route("/klik", methods=["POST"])
def aksi_tombol():
    return ( "<h1>NADIYAH FALISHA ADRIANSANTOSA</h1>"
"<p>Hai nama lengkap aku Nadiyah Falisha Adrianisantosa, panggilannya Falisha, atau biasanya orang-orang panggilnya fal, palisa, pal, pale, nana, nad, nadiyah, apa ajadeh bebas. Lahir di Bandung tanggal 3 April 2008, aku anak pertama dari tiga bersaudara, perempuan semuanya. Hobi aku baca buku, scroll tiktok atau instagram, nonton youtube, foto-foto, bikin video/ngevlog, yapping, main sama temen-temen, dan sekarang lagi pengen belajar ngoding karena ayah baru beli laptop ⸜(｡˃ ᵕ ˂ )⸝♡. Beberapa detail singkat lainnya tentang aku adalah hasil MBTI aku INTP, suka warna hijau, suka semua seri mobil Mercedes-Benz!, udah sih kayanya segitu dulu aja, makasi uda baca sampe sini ദ്ദി◝ ⩊ ◜.ᐟ </p>"
"<a href='https://linktr.ee/nadiyahfalishaa'>Sosial Media<a/>"
)
if __name__ == "__main__":
    app.run(debug=True)
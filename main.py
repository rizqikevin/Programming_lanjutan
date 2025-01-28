from flask import Flask,render_template, request

app = Flask(__name__)

@app.route("/")
def main():
    return render_template("index.html", web_title="Home")

@app.route("/about")
def about():
    return render_template("about.html", web_title="About")

@app.route("/cek_usia", methods=["GET", "POST"])
def cek_usia():
    if request.method == "POST":
        tahun_lahir = request.form["tahun_lahir"]
        tahun_sekarang = 2024
        usia = tahun_sekarang - int(tahun_lahir)
        print(cek_usia)
        return render_template("cek_usia.html", usia=usia)
    return render_template("cek_usia.html", usia=None)

if __name__ == "__main__":
    app.run(host='localhost', port=1234, debug=True)
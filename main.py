from flask import Flask,render_template, request
from datetime import datetime
from groq import Groq
import os

app = Flask(__name__)

client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)

def ai_call(year):
    try:
        chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": f"berikan satu fakta menarik maupun kejadian penting yang terjadi pada tahun {year}"
        }
    ],
    model="llama-3.2-1b-preview",
    stream=False
)
        ai_response = chat_completion.choices[0].message.content
        return ai_response
    
    except Exception as e:
        return str(e)

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
        tahun_sekarang = datetime.now().year
        usia = tahun_sekarang - int(tahun_lahir)
        ai_output = ai_call(tahun_lahir)
        
        print(ai_output)
       
        return render_template("cek_usia.html", usia=usia, tahun_lahir = tahun_lahir, ai_output=ai_output)
    return render_template("cek_usia.html", usia=None)

if __name__ == "__main__":
    app.run(host='localhost', port=1234, debug=True)
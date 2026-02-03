from flask import Flask, render_template, request
import requests
import pdfplumber
from bs4 import BeautifulSoup

app = Flask(__name__)

BOTPRESS_TOKEN = "bp_pat_nqci3iVNox0NCc8z9SKZm8KoPQqrmuowvYez"
BOT_ID = "230d7486-c63a-440a-b008-d6b03b3dc11a"


def send_to_botpress(content):
    url = f"https://api.botpress.cloud/v1/bots/{BOT_ID}/knowledge"
    headers = {
        "Authorization": f"Bearer {BOTPRESS_TOKEN}",
        "Content-Type": "application/json"
    }
    data = {
        "title": "Team Upload",
        "content": content
    }
    requests.post(url, headers=headers, json=data)


@app.route("/", methods=["GET", "POST"])
def index():
    message = ""
    if request.method == "POST":
        content = ""
        pdf_file = request.files.get("pdf")
        if pdf_file:
            with pdfplumber.open(pdf_file) as pdf:
                for page in pdf.pages:
                    content += page.extract_text() or ""
        elif request.form.get("url"):
            r = requests.get(request.form.get("url"))
            soup = BeautifulSoup(r.text, "html.parser")
            content = soup.get_text()
        elif request.form.get("text"):
            content = request.form.get("text")
        if content:
            send_to_botpress(content)
            message = "Uploaded to Botpress successfully!"
    return render_template("index.html", message=message)


if __name__ == "__main__":
    app.run(debug=True)

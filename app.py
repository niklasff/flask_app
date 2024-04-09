# app.py

from flask import Flask, render_template, request, url_for
app = Flask(__name__)


def sana_haku(input_text):
    import re

    replaced_words = []

    with open("sanat.txt", "r", encoding="utf-8") as file:
        suomisanat = file.read()

    with open("sanat_pilkku.txt", "r", encoding="utf-8") as file:
        suomisanat_pilkku = file.read()
    
    with open("sanat_piste.txt", "r", encoding="utf-8") as file:
        suomisanat_piste = file.read()

    for word in input_text.split():
        if "�" in word:
            korvaus_a = re.sub(r"�","ä",word)
            korvaus_b = re.sub(r"�","ö",word)

            if korvaus_a in suomisanat:
                replaced_words.append(f"{word};{korvaus_a}")
            elif korvaus_b in suomisanat:
                replaced_words.append(f"{word};{korvaus_b}")

    for word in input_text.split():
     if "," and "�" in word:
            korvaus_c = re.sub(r"�","ä",word)
            korvaus_d = re.sub(r"�","ö",word)

            if korvaus_c in suomisanat_pilkku:
                replaced_words.append(f"{word};{korvaus_c}")
            elif korvaus_d in suomisanat_pilkku:
                replaced_words.append(f"{word};{korvaus_d}")

    for word in input_text.split():
        if "." and "�" in word:
            korvaus_e = re.sub(r"�","ä",word)
            korvaus_f = re.sub(r"�","ö",word)

            if korvaus_e in suomisanat_piste:
                replaced_words.append(f"{word};{korvaus_e}")
            elif korvaus_f in suomisanat_piste:
                replaced_words.append(f"{word};{korvaus_f}")


    with open("replace_patterns2.txt", "w", encoding="utf-8") as output_file:
        for replaced_word in replaced_words:
            output_file.write(replaced_word + "\n")

    return replaced_words

def sana_korvaus(input_text):
    replace_patterns = {}
    with open("replace_patterns2.txt", "r", encoding="utf-8") as file:
        for line in file:
            parts = line.strip().split(";")
            if len(parts) == 2:
                vaara_sana, oikea_sana = parts
                replace_patterns[vaara_sana] = oikea_sana

        for word in input_text.split():
            if word in replace_patterns: 
                input_text = input_text.replace(word, replace_patterns[word])

    return input_text

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/index', methods=['GET', 'POST'])
def cat(): 
    return render_template('index.html')

@app.route('/tietoa', methods=['GET', 'POST'])
def tieto():
    return render_template("tietoa.html")

@app.route("/fix_text", methods=["POST"])
def fix_text_route():
    input_text = request.form["input1"]
    replaced_words = sana_haku(input_text)
    corrected_text = sana_korvaus(input_text)
    return render_template(
        "index.html", corrected_text=corrected_text, replaced_words=replaced_words
    )


if __name__ == "__main__":
    app.run(debug=True)

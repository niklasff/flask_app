# app.py

from flask import Flask, render_template, request, url_for
app = Flask(__name__)


def sana_haku(input_text):
    import re

    replaced_words = []

    with open("sanat.txt", "r", encoding="utf-8") as file:
        suomisanat = file.read().split()

    with open("sanat_pilkku.txt", "r", encoding="utf-8") as file:
        suomisanat_pilkku = file.read().split()
    
    with open("sanat_piste.txt", "r", encoding="utf-8") as file:
        suomisanat_piste = file.read().split()

    for word in input_text.split():
        if "�" in word:
            korvaus_a = word.replace(r"�","ä")
            korvaus_b = word.replace(r"�","ö")

            if korvaus_a in suomisanat:
                replaced_words.append(f"{word};{korvaus_a}")
            if korvaus_b in suomisanat:
                replaced_words.append(f"{word};{korvaus_b}")

    for word1 in input_text.split():
     if "," and "�" in word1:
            korvaus_c = re.sub(r"�","ä",word1)
            korvaus_d = re.sub(r"�","ö",word1)

            if korvaus_c in suomisanat_pilkku:
                replaced_words.append(f"{word1};{korvaus_c}")
            elif korvaus_d in suomisanat_pilkku:
                replaced_words.append(f"{word1};{korvaus_d}")

    for word2 in input_text.split():
        if "." and "�" in word2:
            korvaus_e = re.sub(r"�","ä",word2)
            korvaus_f = re.sub(r"�","ö",word2)

            if korvaus_e in suomisanat_piste:
                replaced_words.append(f"{word2};{korvaus_e}")
            elif korvaus_f in suomisanat_piste:
                replaced_words.append(f"{word2};{korvaus_f}")

    for char in input_text.split():
            x = char.count("�")
            if "�" in char:
             if x > 0:
                muutettu_a = char.replace("�", "ä")
                muutettu_b = char.replace("�", "ö")
            
                for capital in muutettu_a:
                    etsi_iso_kirjain = capital.isupper()
                    if etsi_iso_kirjain == True:
                        muutettu_eka = muutettu_a.lower()
                        if muutettu_eka in suomisanat:
                            valmis_sana = muutettu_eka.capitalize()
                            replaced_words.append(f"{char};{valmis_sana}")

                for capital in muutettu_b:
                    etsi_iso_kirjain2 = capital.isupper()
                    if etsi_iso_kirjain2 == True:
                        muutettu_eka2 = muutettu_b.lower()
                        if muutettu_eka2 in suomisanat:
                            valmis_sana2 = muutettu_eka2.capitalize()
                            replaced_words.append(f"{char};{valmis_sana2}")


    with open("replace_patterns.txt", "w", encoding="utf-8") as output_file:
        for replaced_word in replaced_words:
            output_file.write(replaced_word + "\n")

    return replaced_words

def sana_korvaus(input_text):
    replace_patterns = {}
    with open("replace_patterns.txt", "r", encoding="utf-8") as file:
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

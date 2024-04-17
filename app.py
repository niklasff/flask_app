from flask import Flask, render_template, request
from itertools import product
import string

app = Flask(__name__)

def preprocess_word(word):
    return word.rstrip(string.punctuation)

def sana_haku(input_text):
    replaced_words = []

    with open("sanat.txt", "r", encoding="utf-8") as file:
        suomisanat = set(file.read().split())

    for word in input_text.split():
        positions = [pos for pos, c in enumerate(word) if c == "�"]
        if positions:
            print(f'Found in word: {word}, "�" found at positions: {positions}')

            replacements = []

            for replacement_combination in product(["ä", "ö"], repeat=len(positions)):
                replaced_word = word
                for pos, replacement_char in zip(positions, replacement_combination):
                    replaced_word = replaced_word[:pos] + replacement_char + replaced_word[pos + 1:]
                replacements.append(replaced_word)

            print(f'All possible replacements: {replacements}')

            word_processed = preprocess_word(word)

            for muutettu_word in replacements:
                muutettu_word_processed = preprocess_word(muutettu_word)
                if muutettu_word_processed.lower() in suomisanat or muutettu_word_processed.capitalize() in suomisanat:
                    replaced_words.append(f"{word};{muutettu_word}")
                    print(f'Final version {muutettu_word} has been added to "replaced_words"')

    with open("replace_patterns.txt", "w", encoding="utf-8") as output_file:
        for replaced_word in replaced_words:
            output_file.write(replaced_word + "\n")

    return replaced_words

def sana_korvaus(input_text):
    replace_patterns = {}
    unreplaced_words = []
    with open("replace_patterns.txt", "r", encoding="utf-8") as file:
        for line in file:
            parts = line.strip().split(";")
            if len(parts) == 2:
                vaara_sana, oikea_sana = parts
                replace_patterns[vaara_sana] = oikea_sana

    corrected_words = []
    words = input_text.split()
    for word in words:
        if word in replace_patterns:
            corrected_words.append(replace_patterns[word])
        else:
            corrected_words.append(word)
            if '�' in word:
                unreplaced_words.append(word)

    corrected_text = ' '.join(corrected_words)
    
    print("Corrected text:", corrected_text)

    return corrected_text, unreplaced_words

@app.route("/") 
def index():
    return render_template("index.html")

@app.route('/tietoa', methods=['GET', 'POST'])
def tieto():
    return render_template("tietoa.html")

@app.route('/kotisivu', methods=["GET", "POST"])
def kotisivu():
    return render_template("index.html")

@app.route("/fix_text", methods=["POST"])
def fix_text_route():
    input_text = request.form["input1"]
    replaced_words = sana_haku(input_text)
    corrected_text, unreplaced_words = sana_korvaus(input_text)
    return render_template(
        "index.html", corrected_text=corrected_text, replaced_words=replaced_words, unreplaced_words = unreplaced_words
    )


if __name__ == "__main__":
    app.run(debug=True)
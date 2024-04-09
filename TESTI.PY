import re

replaced_words = []

with open("sanat.txt", "r", encoding="utf-8") as file:
    suomisanat = file.read().split()

with open("input.txt", "r", encoding="utf-8") as read_files:
    content = read_files.read()

for char in content.split():
        x = char.count("�")
        if "�" in char:
            print(f'löydetty sanasta: {char}, {x} kappale "�" -merkkejä')
        
        if x > 0:
            muutettu = char.replace("�", "ä")
            print(f'korvataan: {char} sanasta "�" -merkit kirjaimella "ä" -> {muutettu}')
        if x > 0:
            muutettu_eka = muutettu.lower()
            print(f'valmis sana korvaamaan: {muutettu_eka}')  

            if muutettu_eka in suomisanat:
                replaced_words.append(f"{char};{muutettu_eka}")

with open("replace_patterns.txt", "w", encoding="utf-8") as output_file:
        for replaced_word in replaced_words:
            output_file.write(replaced_word + "\n")
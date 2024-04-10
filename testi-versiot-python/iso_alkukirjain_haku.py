def iso_kirjain():
    
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
            muutettu_a = char.replace("�", "ä")
            muutettu_b = char.replace("�", "ö")
            print(f'korvataan: {char} sanasta "�" -merkit kirjaimella "ä" -> {muutettu_a}')
            print(f'korvataan: {char} sanasta "�" -merkit kirjaimella "ö" -> {muutettu_b}')

            for capital in muutettu_a:
                etsi_iso_kirjain = capital.isupper()
                if etsi_iso_kirjain == True:
                    muutettu_eka = muutettu_a.lower()
                    print(f'sanan {char} eka kirjain muutettu pieneksi: {muutettu_eka} ja tallennettu sana muuttujaan "muutettu_eka"')  
                    if muutettu_eka in suomisanat:
                        valmis_sana = muutettu_eka.capitalize()
                        print(f'jos sana {muutettu_eka} oli sanat.txt tiedostossa, muutetaan takaisin iso kirjain -> {valmis_sana} "')
                        replaced_words.append(f"{char};{valmis_sana}")
                        print(f'valmis versio {valmis_sana} on tallennettu muuttujaan -> "replaced_words"')

            for capital in muutettu_b:
                etsi_iso_kirjain2 = capital.isupper()
                if etsi_iso_kirjain2 == True:
                    muutettu_eka2 = muutettu_b.lower()
                    print(f'sanan {char} eka kirjain muutettu pieneksi: {muutettu_eka2} ja tallennettu sana muuttujaan "muutettu_eka"')  
                    if muutettu_eka2 in suomisanat:
                        valmis_sana2 = muutettu_eka2.capitalize()
                        print(f'jos sana {muutettu_eka2} oli sanat.txt tiedostossa, muutetaan takaisin iso kirjain -> {valmis_sana2} "')
                        replaced_words.append(f"{char};{valmis_sana2}")
                        print(f'valmis versio {valmis_sana2} on tallennettu muuttujaan -> "replaced_words"')

with open("replace_patterns.txt", "w", encoding="utf-8") as output_file:
        for replaced_word in replaced_words:
            output_file.write(replaced_word + "\n")
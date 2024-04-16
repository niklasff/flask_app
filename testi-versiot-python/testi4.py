def iso_kirjain():
    replaced_words = []

    with open("sanat.txt", "r", encoding="utf-8") as file:
        suomisanat = file.read().split()

    with open("input.txt", "r", encoding="utf-8") as read_files:
        content = read_files.read()

    for char in content.split():
        positions = [pos for pos, c in enumerate(char) if c == "�"]
        if positions:
            print(f'löydetty sanasta: {char}, "�" -merkki löytyy sijainneista: {positions}')

            if len(positions) > 1:
                position_2 = positions[1]

                muutettu_a = char[:positions[0]] + "ä" + char[positions[0] + 1:position_2] + "ö" + char[position_2 + 1:]
                muutettu_b = char[:positions[0]] + "ö" + char[positions[0] + 1:position_2] + "ä" + char[position_2 + 1:]
            else:
                muutettu_a = char.replace("�", "ä")
                muutettu_b = char.replace("�", "ö")
                
            print(f'korvataan: {char} sanasta "�" -merkit kirjaimella "ä" -> {muutettu_a}')
            print(f'korvataan: {char} sanasta "�" -merkit kirjaimella "ö" -> {muutettu_b}')

            for muutettu_word in [muutettu_a, muutettu_b]:
                if muutettu_word[0].isupper() and muutettu_word.lower() in suomisanat:
                    muutettu_word = muutettu_word.lower().capitalize()

                if muutettu_word in suomisanat:
                    replaced_words.append(f"{char};{muutettu_word}")
                    print(f'valmis versio {muutettu_word} on tallennettu muuttujaan "replaced_words"')

    with open("replace_patterns.txt", "w", encoding="utf-8") as output_file:
        for replaced_word in replaced_words:
            output_file.write(replaced_word + "\n")

iso_kirjain()

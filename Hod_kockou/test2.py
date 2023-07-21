

body = 0
player_input2 = "?"
while True:
    player_input = input("Povedz keď budeš pripravený. Press A or Q ").lower()
    if player_input == "q":
        print("Ďakujeme, zahráme si nabudúce")
        quit()
    else:
        while True:
            if player_input2 == "q":
                print("Ako myslíš, možno to bolo aj dobre, máš", body, "bodov :D")
                print("")
                break
            else:
                cube_number = random.randint(1, 6)
                if cube_number == 1:
                    print("BOHUŽIAL SI hodil si 1 a prehral si s", body, "bodmi")
                    print("")
                    break
                else:
                    body += 1
                    print("Hodil si kockou číslo", cube_number, "a už máš", body, "body")
                    print("")
            player_input2 = str(input("Pokračujeme? Press A or Q ").lower())












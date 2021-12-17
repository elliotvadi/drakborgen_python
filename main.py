import time
import datetime
import random

class color_bold:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'


class color_italic:
    PURPLE = '\x1B[95m'
    CYAN = '\x1B[96m'
    DARKCYAN = '\x1B[36m'
    BLUE = '\x1B[94m'
    GREEN = '\x1B[92m'
    YELLOW = '\x1B[93m'
    RED = '\x1B[91m'
    ITALIC = '\x1B[1m'
    END_ITALIC = '\x1B[0m'

# Variablerna kontrollerar vilket monster man stöter på.
what_monster = 0
encountered_monster = 0


# Player starting stats
player_starting_health = 0
player_starting_strength = 0
player_starting_luck = 0
player_starting_armour = 0
player_starting_agility = 0

# Player Stats
player_health = player_starting_health
player_strength = player_starting_strength
player_luck = player_starting_luck
player_agility = player_starting_agility
player_armour = player_starting_armour

# Denna variabeln bestämmer håller koll på vilken karaktär spelaren valt. 
# Aelfric = 1
# Bardhor = 2
# Sigeir = 3
# Rohan = 4
chosenCharacter = 0

# Den här variabeln håller koll på vilken specialattack spelaren har
# Aelfric = "C"
# Bardhor = "B"
# Sigeir = "A"
# Rohan = "B"
specialAttack = 0

# Antal pilar för armborst
crossBowBolts = 4

# Monster; Först i listan är Styrka, näst Vighet, näst Tur, näst Rustning, näst KP, näst namn
Svartalv = [3, 9, 7, 3, 2, "Svartalv"]
Bergstroll = [11, 3, 4, 5, 6, "Bergstroll"]
Skelett = [5, 6, 8, 4, 4, "Skelett"]
Orch = [7, 5, 4, 6, 4, "Orch"]


# Inventarie och föremål
player_weapons = ["Långsvärd", "Spikklubba", "Armborst", "Kortsvärd", "Dubbelyxa"]
player_equipment = ["Stav", "Träsköld", "Lädersköld", "Järnsköld", f"{crossBowBolts} Pil(ar)"]

treasures_room_search = ["Dräktsmycke (Värde 350 gm)", "Dräktsmycke (Värde 200 gm)", "Ring (Värde 90 gm)", "Mynt (Värde 10 gm)"]
treasures_chest = ["Mynt (Värde 50 gm)", "Dolk (Värde 250 gm)", "Smycke (Värde 100 gm)", "Armring (Värde 120 gm)"]
treasures_fallen_warrior = ["Mynt (Värde 60 gm", "Halskedja (Värde 150 gm)"]
treasures_treasure_chamber = ["Ädelstenar, (Värde 400 gm", "Spira (Värde 1000 gm)", "Litet skrin (Värde 450 gm)", 
"Jätterubin (Värde 700 gm)", "Guldäpple, (Värde 2000 gm)", "Bägare (Värde 600 gm)", "Trolleribok (2500 gm)"]
generalItems = ["Liten flaska"]

inventory = []


# Placeholder för pilar och armborst. Siffran är antalet pilar
crossBow = {
    "Armborst": 4
}

# Du stöter på ett monster
def monster_encounter():
    global encountered_monster
    global what_monster
    what_monster = random.randint(1, 4)
    if what_monster == 1:
        encountered_monster = Svartalv
    elif what_monster == 2:
        encountered_monster = Bergstroll
    elif what_monster == 3:
        encountered_monster = Skelett
    elif what_monster == 4:
        encountered_monster = Orch


# Strid
def combat(encountered_monster):
    global player_move

    print("Vill du använda attack A, B eller C? Skriv \"slump\" om du vill slumpa din attack.")
    player_attack = input("")
    if player_attack == "A":
        player_move = "A"
    elif player_attack == "B":
        player_move = "B"
    elif player_attack == "C":
        player_move = "C"
    elif player_attack == "slump":
        player_move_random = random.randint(1, 3)
        if player_move_random == 1:
            player_move = "A"
        elif player_move_random == 2:
            player_move = "B"
        elif player_move_random == 3:
            player_move = "C"


# § Rum
# Nytt rum
def moveToRoom():
    global inventory
    global roomContent
    global encountered_monster
    global player_health
    print("Du går...")
    roomContent = random.randint(1, 20)
    if roomContent >= 1 and < 5:
        emptyRoom()
    elif roomContent >= 6 and <= 10: 
        print(f"Du stöter på ett monster... {encountered_monster}")
        monster_encounter()
    elif roomContent == 11: 
        print("Du hittar en liten flaska")
        inventory.append(generalItems[0])
    elif = roomContent == 12:
        print("""Du ser ur golvet öppnar sig och du hinner inte reagera innan du faller ner i den 
            bottenlösa brunnen...""")
        player_health = 0
        exit()
    elif roomContent == 13 or 14:
        fallenWarrior()
    elif roomContent == 


def emptyRoom():
    print("Rummet är tomt. Det ligger lite döda råttor utströdda över golvet och, du känner att luften är kvav.")
    print("Framför dig öppnar ser du en stor dörröppning som leder till ett annat rum. Du har inget annat val än att gå in.")
    moveToRoom()


def fallenWarrior():
    global inventory
    global player_health
    global player_luck
    global treasures_fallen_warrior
    local_scorpionDamage = random.randint(1, 6)
    local_scorpionDamage = local_scorpionDamage - 2
    localWarriorSearch = random.randint(1, 7)
    localSkeletonAmbush = random.randint(1, 6)
    print("""Du ryggar till när du ser det skelettet på golvet. Det är täckt i de trasiga resterna av kläder. 
        Det är uppenbart att det är en stupad krigare, men du har ingen aning om hur länge den har legat här. 
        Du sväljer tungt när du inser att du kan sluta på samma sätt om du inte är försiktig.""")
        localChoice = input("Vill du söka igenom den döde krigaren? (J/N)")
        if localChoice == "J":
            if localWarriorSearch == 1:
                print("Du hittar en liten flaska. Innehållet är okänt.")
                keep = input("Vill du behålla den? (J/N)")
                if keep == "J":
                    inventory.append(generalItems[0])
                else:
                    print("Du lägger tillbaks flaskan och övertygar dig själv om att det säkert ändå var gift.")
            elif localWarriorSearch == 2:
                print(f"""Du söker igenom den stupade krigaren, men du hittar inget. Den lilla, gyllene skorpionen
                    hittar dock dig, specifikt din tumme. Du förlorar {local_scorpionDamage} KP som skada. """)
                player_health = player_health - local_scorpionDamage
            elif localWarriorSearch == 3 or 5:
                print("""Du känner en mindre känsla av besvikelse när du inser att krigaren inte har något av värde.
                    Kanske har någon varit här före dig...""")
            elif localWarriorSearch == 4:
                print(f"Du hittar några gamla {treasures_fallen_warrior[0]}")
                keep = input("Vill du behålla den? (J/N)")
                if keep == "J":
                    inventory.append(treasures_fallen_warrior[0])
            elif localWarriorSearch == 6:
                print(f"Du hittar en {treasures_fallen_warrior[1]}")
                keep = input("Vill du behålla den? (J/N)")
                if keep == "J":
                    inventory.append(treasures_fallen_warrior[1])
        else:
            print("""När tanken om att det är så här du skulle kunna sluta börjar bita sig fast
                så känner du att du kommer att bli alldeles demoraliserad om du stannar i rummet något mer.
                Inte nog med det, men du vet att i den här borgen förblir inte skelett livlösa särksilt länge.
                Du skynder dig ut samtidigt som du ber till gudarna att det inte ska vakna och överfalla dig... """)
                if localSkeletonAmbush > player_luck:
                    print("""Gudarna hör dig inte inifrån den här djävulska borgen, och du svär för dig själv när du
                        hör ljudet av benknotor bakom dig. Du greppar ditt vapen och kan bara hoppas att denna
                        strid inte blir din sista.""")
                        # Combat
                else: 
                    print("""Gudarna måste vara välvilliga idag, för till din stora förvåning så vaknar inte
                        den döde krigaren...""")
        
def roomChest():
    global inventory
    global player_health
    global player_luck
    local_chestTrapDamage = random.randint(1, 12)
    localTreasureSearch = random.randint(1, 9)
    print("Du har hittat en kista. Den är dammig och ser ut att vara väldigt gammal.")
    localChoice = input("Vill du öppna kistan? (J/N)")
    if localChoice == "J":
        if localTreasureSearch == 1:
            print(f"Du hittar några gamla {treasures_chest[0]}")
            keep = input("Vill du behålla dem? (J/N)")
            if keep == "J":
                inventory.append(treasures_chest[0])
            else:
                print("Du lämnar mynten i kistan. Locket faller ner med ett brak och låser sig med ett ljudligt klick.")
        elif localTreasureSearch == 2 or 6:
            print("Vassa metallspikar tränger in i handen när du öppnar kistlocket. En fälla!")
            print(f"Du förlorar {player_health - local_chestTrapDamage - player_luck} KP i skada.")
            player_health = player_health - local_chestTrapDamage
            player_health = player_health - player_luck
        elif localTreasureSearch == 3:
            print("Du öppnar kistans lock men finner bara damm. Den är tom.")
        elif localTreasureSearch == 4:
            print(f"I kistan hittar du en {treasures_chest[1]}")
            keep = input("Vill du behålla den? (J/N)")
            if keep == "J":
                inventory.append(treasures_chest[1])
            else:
                print("Du lämnar dolken i kistan. Locket faller ner med ett brak och låser sig med ett ljudligt klick.")
        elif localTreasureSearch == 5:
            print("""Till din förfäran stirrar ett par mörka ögonhålor på dig när du öppnar kistan. Du har hittat 
                benknotor. Du funderar på ett ögonblick på hur en människa hamnade i den här kistan, men å andra sidan 
                vill du inte riktigt veta. Du tar dock ett djupt andetag av lättnad eftersom just detta skelett
                inte kommit till liv igen. Än så länge...""")
        elif localTreasureSearch == 7:
            print(f"Du hittar ett {treasures_chest[2]}")
            keep = input("Vill du behålla den? (J/N)")
            if keep == "J":
                inventory.append(treasures_chest[2])
        elif localTreasureSearch == 8:
            print("Du hittar en liten flaska. Innehållet är okänt.")
            keep = input("Vill du behålla den? (J/N)")
            if keep == "J":
                inventory.append(generalItems[0])
            else: 
                print("Du lämnar flaskan och glömmer snabbt bort den i borgens mörka korridorer...")
                return
        elif localTreasureSearch == 9:
            print(f"Du hittar en {treasures_chest[3]}")
            keep = input("Vill du behålla den? (J/N)")
            if keep == "J":
                inventory.append(treasures_chest[3])
        else: 
            print("""Du bestämmer dig för att låta bli att öppna kistan. Du har dock en oförklarlig känsla av ett
                den inte längre kommer vara där när du lämnar rummet...""")


def roomSearch():
    global inventory
    global player_health
    global treasures_room_search
    local_centipedeDamage = random.randint(1, 12)
    roomSearch = random.randint(1, 11)
    if roomSearch == 1:
        print("Du hittar en Ring (Värde 90 gm)")
        keep = input("Vill du behålla den? (J/N)")
        if keep == "J":
            inventory.append(treasures_room_search[2])
        else:
            print("Du lämnar ringen och glömmer snabbt bort den i borgens mörka korridorer...")
            return
    elif roomSearch == 2 or 5:
        print("Det är tomt. Du hittar ingenting.")
        return
    elif roomSearch == 3:
        print(f"""Du känner en förskräcklig smärta i handen. Tusenfotingens gift tränger in i dig och du
            förlorar {local_centipedeDamage} KP i skada...""")
        player_health = player_health - local_centipedeDamage
    elif roomSearch == 4: 
        print("Du hittar en liten flaska. Innehållet är okänt.")
        keep = input("Vill du behålla den? (J/N)")
        if keep == "J":
            inventory.append(generalItems[0])
        else: 
            print("Du lämnar flaskan och glömmer snabbt bort den i borgens mörka korridorer...")
            return
    elif roomSearch == 6:
        print("Du hittar ett Dräktsmycke (Värde 350 gm)")
        keep = input("Vill du behålla den? (J/N)")
        if keep == "J":
            inventory.append(treasures_room_search[0])
        else:
            print("Du lämnar dräktsmycket och glömmer snabbt bort det i borgens mörka korridorer...")
            return
    elif roomSearch == 7: 
        print("Du hittar några gamla Mynt (Värde 10 gm)")
        keep = input("Vill du behålla den? (J/N)")
        if keep == "J":
            inventory.append(treasures_room_search[3])
        else:
            print("Du lämnar mynten och glömmer snabbt bort dem i borgens mörka korridorer...")
            return
    elif roomSearch == 8: 
        print("Du hittar ett Dräktsmycke (Värde 200 gm)")
        keep = input("Vill du behålla den? (J/N)")
        if keep == "J":
            inventory.append([1])
        else: 
            print("Du lämnar dräktsmycket och glömmer snabbt bort det i borgens mörka korridorer...")
            return
    elif roomSearch == 9: 
        print("""Du hinner nätt och jämt hoppa undan för att undvika skelettet som plötsligt kastar sig mot dig.
            Du har blivit överrumplad och du har nu inget annat val än att slåss för ditt liv.""")
        # Combat-funktion
    elif roomSearch == 10 or 11:
        print("Du hittar en lönndörr. Du inser att du inte har något annat val än att gå igenom den.")
            moveToRoom()


















# Inventarie
def inventory():
    print(f"Med dig har du: {inventory}")

# Om spelaren dricker en flaska
def bottle():
    global bottle_result
    global player_health
    global player_strength
    global player_luck
    global player_starting_health
    bottle_result = random.randint(1, 12)
    if bottle_result == 1:
        print("Dödligt gift, du dör omedelbart.")
        player_health = 0
    elif bottle_result == 2:
        print("Kraftigt gift, din KP halveras nedåt.")
        player_health = player_health / 2
    elif bottle_result == 3:
        print("Gift, du förlorar 2 KP.")
        player_health = player_health - 2
    elif bottle_result == 4:
        print("Du är blir förvirrad och stöter på en fälla")
        # Fälla här
    elif bottle_result == 5:
        print("Den har en smak av...Hallonsaft? Ja, definitivt hallonsaft.")
        print("Inget händer.")
    elif bottle_result == 6:
        print("Osynlighetsdryck, du är osynlig. Inget monster (förutom drake) kan anfalla dig på tre rundor.")
    elif bottle_result == 7:
        print("Styrkedryck, du får +1 SF.")
        player_strength = player_strength + 1
    elif bottle_result == 8:
        print("Turdryck, du får +1 TF.")
        player_luck = player_luck + 1
    elif bottle_result == 9:
        print("Stärkande dryck, du läker 2 KP.")
        player_health = player_health + 2
    elif bottle_result == 10:
        print("Helande dryck, du läker 1/3  av dina förlorade KP.")
        player_health = player_health * 1.33
    elif bottle_result == 11:
        print("Kraftigt helande dryck, du läker 2/3 av dina förlorade KP.")
        player_health = player_health * 1.66
    else:
        print("Hjältedryck, du helas fullständigt")
        player_health = player_starting_health



# Valbara karaktärer och tillhörande "kort"
# Aelfric Brunkåpa
def aelfric_info_card():
    print(f"""{color_bold.BOLD}Aelfric Brunkåpa{color_bold.END}
    {color_bold.BOLD}Vapen:{color_bold.END} Spikklubba, stav
    {color_bold.BOLD}SF:{color_bold.END} 4
    {color_bold.BOLD}VF:{color_bold.END} 7
    {color_bold.BOLD}RF:{color_bold.END} 4
    {color_bold.BOLD}TF:{color_bold.END} 8
    {color_bold.BOLD}KP:{color_bold.END} 15
    {color_bold.BOLD}Specialattack:{color_bold.END} C""")

# Bardhor Bågman
def bardhor_info_card():
    print(f"""{color_bold.BOLD}Bardhor Bågman{color_bold.BOLD}
    {color_bold.BOLD}Vapen:{color_bold.END} Armborst, kortsvärd, träsköld
    {color_bold.BOLD}SF:{color_bold.END} 3
    {color_bold.BOLD}VF:{color_bold.END} 8
    {color_bold.BOLD}RF:{color_bold.END} 5
    {color_bold.BOLD}TF:{color_bold.END} 7
    {color_bold.BOLD}KP:{color_bold.END} 11
    {color_bold.BOLD}Specialattack:{color_bold.END} B""")

# Sigeir Skarpyxe
def sigeir_info_card():
    print(f"""{color_bold.BOLD}Sigeir Skarpyxe{color_bold.BOLD}
    {color_bold.BOLD}Vapen:{color_bold.END} Dubbelyxa, Lädersköld
    {color_bold.BOLD}SF:{color_bold.END} 7
    {color_bold.BOLD}VF:{color_bold.END} 5
    {color_bold.BOLD}RF:{color_bold.END} 6
    {color_bold.BOLD}TF:{color_bold.END} 5
    {color_bold.BOLD}KP:{color_bold.END} 16
    {color_bold.BOLD}Specialattack:{color_bold.END} A""")

# Riddar Rohan
def rohan_info_card():
    print(f"""{color_bold.BOLD}Riddar Rohan{color_bold.BOLD}
    {color_bold.BOLD}Vapen:{color_bold.END} Långsvärd, järnsköld
    {color_bold.BOLD}SF:{color_bold.END} 6
    {color_bold.BOLD}VF:{color_bold.END} 4
    {color_bold.BOLD}RF:{color_bold.END} 9
    {color_bold.BOLD}TF:{color_bold.END} 4
    {color_bold.BOLD}KP:{color_bold.END} 17
    {color_bold.BOLD}Specialattack:{color_bold.END} B""")


# Introduktion
def intro():
    print("""\x1B[3mFör länge, länge sedan härskade den stora trollkarlen T’siraman över ett helt rike. Han var vida
    beryktad för den jättelika och ointagliga fästning där han bodde; en svart borg uppe på en bergstopp.
    Tusen och femhundra år har passerat sedan hans rike föll samman, och T’siraman är numera
    bara ett namn och en legend. Men hans väldiga borg – den urgamla Drakborgen – står kvar ännu,
    lika orubblig som en del av berget självt. Den levde vidare långt efter sin herres död, som om den
    hade ett alldeles eget liv. Vissa hävdar att monstren som nu vandrar i Drakborgens salar en gång var
    T’siramans väktare. Andra menar att de drogs dit efter trollkarlens fall. Några få menar att det är före
    detta lycksökare som irrat sig in i Drakborgen i jakt på skatter, men som nu vandrar dess salar som
    borgens tjänare.
    Otaliga är legenderna om de trolska skatter som gömmer sig i borgens inre, om den fasansfulla
    drake som vaktar dem, och om borgens evigt föränderliga skepnad. De få som har vågat sig in en bit
    för att sen ta sig ut igen, berättar att inget är sig likt från dag till dag. Några har hört legender om folk
    som gått in och kommit ut med konungsliga skatter. Många fler är berättelserna om äventyrare som
    gått in och aldrig setts åter.
    Likt en uråldrig jätte har Drakborgen överlevt många tidsåldrar. För ett tag tycktes det som om borgen slumrade, 
    då berättelserna om rum som vred sig inför ögonen på folk och det eviga vandrandet i
    Drakborgens underjord avtog och istället ersattes av historier om jättespindlar som härjade i salarna,
    om gigantiska demoner och minotaurer. Ett tag spreds ryktet att draken själv hade blivit gammal, då
    man från flera källor fick höra berättelser om folk som faktiskt hade sett henne vaken och arg - och
    ändå kommit tillbaka för att kunna berätta om det.
    Den tiden tycks vara förbi. Alla byar i närheten kände stöten när Något hände. Vissa svär att de
    hörde en drakes skrik för sitt liv. Sedan dess vågar sig ingen i närheten. Drakborgens återtog sin
    forna sits som en skräckinjagande fästning av svart sten, lika otämjbar som ogästvänlig. 
    \033[1mDrakborgen hade vaknat ur sin slummer.\033[0m
    \x1B[3mDe skämtande fyllesagorna om att vilken bonde som helst kunde ta sig in i Drakborgen och ut
    igen tystnade, och ersattes av storögda berättelser om guld som glimmade från spirorna, delar av
    silversmycken som föll ut från de mörka skottgluggarna, och otaliga monsters hånskrattande vrål från
    salarnas inre. Det var nästan som om Drakborgen vill locka folk att kliva in i dess gap. Alltför många
    har antagit den återväckta Drakborgens utmaning och begett sig in. Ingen har återvänt.
    Som så många andra äventyrare före dig har du valt att trotsa Drakborgens faror, lockad av skatterna som väntar i 
    dess inre. Din familj och hemby är i stor nöd, och även en bråkdel av de skatter
    som sägs finnas i Drakborgen skulle kunna rädda liv. Så här står du, i det blodröda gryningsljuset
    nedanför Drakborgens skräckinjagande fasad. Du vet att du måste vara ute före solnedgången, för
    när natten kommer vaknar fasor som ingen dödlig kan överleva. Du sväljer hårt, fullt medveten om att
    det här kan vara sista gången du ser solen gå upp.\x1B[0m""")

# Kör introt
intro()
print("")


# Olika stats
print(f"""Följande stats finns i spelet: 
 {color_bold.BOLD}Styrka{color_bold.END}, förkortat {color_bold.BOLD}SF{color_bold.END}
 {color_bold.BOLD}Vighet{color_bold.END}, förkortat {color_bold.BOLD}VF{color_bold.END}
 {color_bold.BOLD}Rustning{color_bold.END}, förkortat {color_bold.BOLD}RF{color_bold.END}
 {color_bold.BOLD}Tur{color_bold.END}, förkortat {color_bold.BOLD}TF{color_bold.END}
 {color_bold.BOLD}Kroppspoäng{color_bold.END}, förkortat {color_bold.BOLD}KP{color_bold.END}
 """)


# Berätta spelets stridssytem
print(f"""{color_bold.BOLD}Spelets stridssystem{color_bold.END} fungerar väldigt likt \"Sten Sax Påse\". 
Alla spelarkaraktärer och monster har tre närstridsattacker: A, B och C. 
Detta fungerar som så att A slår B, B slår C och C slår A. Vid lyckad attack dras 1 Kroppspoäng 
(KP) från motståndaren. Denna skada dras dock endast om den går igenom spelarens eller monstrets 
rustning, vilket spelet kontrollerar genom att digitalt slå en T20. Om resultatet är högre än 
spelarens eller monstrets (Rustningsfaktor) RF så bryter attacken igenom rustningen, varpå 
skada dras. 
Aelfric Brunkåpas spikklubba har dock dubbelt så hög chans att bryta igenom rustning.
Spelarkaraktärer har även en specialattack, vilken, om den lyckas, ger dunbbelt i skada.
Om både spelare och monster skulle använda samma attack mot varandra så blir det ett dråpslag; 
både spelare och monster förlorar 1 KP.
""")

# Förklara möte med monster
print(f"""Vid möte med monster har spelaren tre val:
{color_bold.BOLD}1. Fly{color_bold.END}
Om spelaren väljer att fly så kommer denne automatiskt att gå tillbaka till närmaste rum.
{color_bold.BOLD}2. Avvakta{color_bold.END}
Om spelaren väljer att avvakta så kommer en av två saker hända: 
Monstret attackerar eller monstret flyr.
{color_bold.BOLD}3. Anfalla
Om spelaren väljer att anfalla så kommer spelaren påbörja strid med monsret, förutsatt att
monstret inte flyr.
Om spelaren har otur kommer denne dock att råka ut för ett {color_bold.BOLD}Överfall{color_bold.END}.
Vid ett överfall kommer strid automatiskt att påbörjas. Spelaren kan med andra ord inte välja att
avvakta, anfalla eller fly. Om spelaren vill fly så måste denne göra detta efter att striden påbörjats.
Vid ett överfall kan Bardhor Bågman inte heller använda sin armborst. Sköldar kan heller inte 
användas vid monstrets {color_bold.BOLD}första{color_bold.END} attack vid ett överfall.
""")

# Visa spelaren vilka karaktärer som finns och fråga spelaren vilken denne vill spela som
show_characters = print(f"""Vilken karaktär vill du spela som?
Följande karaktärer finns: """)
aelfric_info_card()
print("")
bardhor_info_card()
print("")
sigeir_info_card()
print("")
rohan_info_card()
print("")
what_character = input("Välj en karaktär (Skriv Aelfric, Bardhor, Sigeir eller Rohan): ")

# Om spelaren väljer karaktärer
if what_character == "Aelfric":
    player_starting_health = 15
    player_starting_strength = 4
    player_starting_agility = 7
    player_starting_luck = 8
    player_starting_armour = 4
    inventory.append(player_weapons[1], player_equipment[0])
    chosenCharacter = 1
    specialAttack = "C"
    #
    while chosenCharacter == 1:


elif what_character == "Bardhor":
    player_starting_health = 11
    player_starting_strength = 3
    player_starting_agility = 8
    player_starting_luck = 7
    player_starting_armour = 5
    inventory.append(player_weapons[2, 3], player_equipment[1, 4])
    chosenCharacter = 2
    specialAttack = "B"
    #
    while chosenCharacter == 2:


elif what_character == "Sigeir":
    player_starting_health = 16
    player_starting_strength = 7
    player_starting_agility = 5
    player_starting_luck = 5
    player_starting_armour = 6
    inventory.append(player_weapons[4], player_equipment[2])
    chosenCharacter = 3
    specialAttack = "A"
    #
    while chosenCharacter == 3:



elif what_character == "Rohan":
    player_starting_health = 17
    player_starting_strength = 6
    player_starting_agility = 4
    player_starting_luck = 4
    player_starting_armour = 9
    inventory.append(player_weapons[0], player_equipment[3])
    chosenCharacter = 4
    specialAttack = "B"
    #
    while chosenCharacter == 4:



else:

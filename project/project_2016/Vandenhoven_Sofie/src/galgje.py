import random

def play_galgje (credits): #definitie om aan te roepen in gamecarousel
	play_galgje_kost = 4
	play_galgje_win_1_guess = 24
	play_galgje_win_2_5_guess = 14
	play_galgje_win_other_guess = 9
	print("Welkom bij galgje! Elk spelletje galgje kost", play_galgje_kost, "credits.")
	woordenlijst = ["aansteker", "aardappel", "aardbei", "abonnement", "abrikoos", "adres", "afwasmiddel", "amandel", "ananas", "anjer", "aperitief", "apotheek", "apotheker", "appel", "appelflap", "appelsap", "artisjok", "asperge", "aubergine", "augurk", "avocado", "baard", "babyvoeding", "badjas", "badpak", "bakker", "banaan", "bank", "bankkaart", "behangpapier", "belgisch", "benzine", "benzinepomp", "benzinestation", "beschuit", "betalen", "biefstuk", "bier", "bieslook", "bikini", "bloem", "bloemist", "bloemkool", "bloempot", "bloemstuk", "boek", "boeket", "boon", "boormachine", "borstel", "bosbes", "boter", "boterkoek", "braambes", "brief", "briefje", "brievenbus", "bril", "brillendoos", "broccoli", "broek", "broek", "brood", "broodje", "buikpijn", "bushalte", "cadeau", "cadeaubon", "cadeauwinkel", "cake", "champagne", "champignon", "chips", "chocoladekoek", "chocolademelk", "citroen", "cola", "contactlens", "courgette", "croissant", "dadel", "das", "deodorant", "dessert", "doos", "drank", "druif", "druppel", "duif", "eend", "eetlepel", "eieren", "envelop", "erwt", "everzwijn", "fazant", "fietsslot", "fles", "fles", "framboos", "frieten", "fruit", "fruitsap", "gans", "garnalen", "geboorte", "gebraad", "gehakt", "gehaktbal", "geldautomaat", "geneesmiddel", "gereedschap", "geschenk", "glas", "granen", "groen", "groente", "haardroger", "haarspeld", "hak", "hamburger", "hamer", "handschoenen", "handtekening", "hemd", "hersenen", "hert", "hoed", "honing", "hoofddoek", "hoofdpijn", "huiduitslag", "ijs", "inktvis", "jas", "jeans", "jurk", "kaart", "kaas", "kabeljauw", "kalfsvlees", "kalkoen", "kam", "kapper", "kapsel", "karaf", "kassa", "keelpijn", "kelner", "kers", "ketchup", "keukenrol", "kip", "kipfilet", "kippenbout", "kiwi", "kleding", "kleingeld", "koeken", "koffie", "koffielepel", "kokosnoot", "komkommer", "konijn", "kool", "koorts", "thermometer", "kostuum", "kotelet", "kousen", "kraan", "krab", "krant", "krantenwinkel", "krasbiljet", "kraslot", "kreeft", "kriek", "kroketten", "krokus", "kruiden", "krultang", "laarzen", "laarzen", "ladder", "lamp", "lamsvlees", "lelie", "lens", "lepel", "lever", "lijm", "limoen", "limonade", "lippenstift", "loket", "maag", "macaroni", "magazine", "mandarijn", "mango", "mantelpak", "mascara", "mayonaise", "melk", "meloen", "menu", "mes", "mineraalwater ", "moer", "mosselen", "mozzarella", "munt", "muntstuk", "muts", "nachtkleed", "nachtpon", "nagelknipper", "nagelschaartje", "nagelvijl", "nagerecht", "narcis", "nectarine", "neusdruppels", "nier", "ober", "oesters", "okkernoot", "olie", "olijf", "onderbroek", "ondergoed", "onderhemd", "oogschaduw", "oorpijn", "opsturen", "opticien", "oranje", "orchidee", "overschrijving", "paardenvlees", "paars", "pak", "pakje", "paling", "pannenkoek", "panty", "papaja", "papier", "paprika", "pasta", "peer", "pen", "peper", "perron", "perzik", "pet", "phone-card", "pil", "pincobetaalpas", "pint", "pintje", "pistolet", "pizza", "plant", "plat", "pleister", "pompelmoes", "pompoen", "pompstation", "postcopostzegel", "postkantoor", "potlood", "prei", "prijs", "pruim", "pudding", "raap", "rabarber", "radijs", "regenjas", "rekening", "ribbetjes", "riem", "rijst", "rijst", "rits", "robiet", "rok", "rood", "roos", "roze", "rugpijn", "rundvlees", "safe", "salade", "salami", "sandaal", "sandwich", "saus", "scampi", "schaar", "schapenvlees", "scheermes", "scheerschuim", "schelpdieren", "schoen", "schoenen", "schoenmaker", "schoensmeer", "schoonmaakmiddel", "schroef", "schroevendraaier", "schuurmachine", "serveerster", "shampoo", "short", "sigaren", "sigaretten", "sinaasappelsap", "siroop", "siroop", "sjaal", "sla", "slager", "slagroom", "slakken", "sleutel", "slip", "slot", "slotenmaker", "smeerkaas", "snack", "snoep", "snor", "soep", "sokken", "spaghetti", "spaghetti", "sparen", "spek", "spierpijn", "spijker", "spoor", "spruitje", "spuitwater", "staart", "station", "sterkedrank", "stokbrood", "strip", "stripverhaal", "struisvogel", "suiker", "suikerbrood", "taart", "tabak", "tablet", "tandenborstel", "tandpasta", "tandpijn", "tankstation", "telefoonkaart", "thee", "tijdschrift", "tobacco", "toiletpapier", "tomaat", "tondeuse", "tong", "tortilla", "tramhalte", "trui", "t-shirt", "tube", "tuinkers", "ui", "uittreksel", "vaas", "varkensvlees", "verf", "verjaardag", "verkoudheid", "vervoer", "videocassette", "vijg", "vis", "vitamine", "vlecht", "vlees", "vleeswaren", "voeding", "voorschrift", "vork", "vruchtensap", "vuilniszak", "walnoot", "wasmiddel", "water", "water", "waterkers", "watermeloen", "waterpas", "wattenstaafjes", "wijn", "wisselgeld", "wond", "woord", "woord", "woord", "worst", "wortel", "yoghurt", "zaag", "zakdoek", "zalf", "zalm", "zeep", "zonnebloem", "zonnebril", "zool", "zout", "zuivelafdeling", "zwembroek"] 
	
	speel_opnieuw = "ja"
	while speel_opnieuw == "ja":
		credits = credits - play_galgje_kost
		te_raden_woord = random.choice(woordenlijst) #woord dat geraden moet worden
		gok = 0 #aantal gokken staat op 0 bij het begin van het spel
		guessed_letters = '' #welke letters zijn er al geraden? lege lijst bij het begin van het spel
		print("Het woord bevat", len(te_raden_woord), "letters") #hoelang is het woord
		geheim_woord = '-' * len(te_raden_woord) #het te raden woord in -
		wrong_guesses = ''

		while gok < 10 and te_raden_woord != geheim_woord: #als je nog niet 10x gegokt hebt en het te raden woord is niet gelijk aan wat er op de - staat
			print("Momenteel geraden:", geheim_woord, ".") #dan print je wat er al geraden is
			print("Foute letters:", wrong_guesses)	
			if gok == 0: #BD beter != 0 en dan redundantie hieronder weg
				print("Zeg een letter.")
				letter = (input()).lower()
			else:
				print("Wil je het volledige woord gokken?")
				antwoord_gokken = input("Ja of nee?")
				if antwoord_gokken.lower() == "ja":
					jouw_gegokt_antwoord = input("Jouw gegokt woord is:")
					geheim_woord = jouw_gegokt_antwoord
					break
				else:
					print("\n")
					print("Zeg een letter.")
					letter = (input()).lower() #de input moet in lowercase gezet worden en in de variabele letter
			print("\n")
			if len(letter) == 1 and letter in "abcdefghijklmnopqrstuvwxyz":  #als de input slechts 1 karakter bevat én het komt voor in het alfabet
				if letter not in guessed_letters: #als de input (1 letter) niet voorkomt in de lijst van al geraden letters
					guessed_letters = guessed_letters + letter #dan mag de lijst guessed_letters geüpdate worden met deze letter
					if letter in te_raden_woord: #als de input (1 letter) in het woord dat geraden moet worden staat
						print(letter.upper(), "komt voor in het woord!")  #dan print juist
						for letterpositie in range(len(te_raden_woord)): #voor elke letterpositie in het te raden woord (e.g banaan: [0,1,2,3,4,5,6])
							if te_raden_woord[letterpositie] == letter: #als de letter op een bepaalde positie in het te raden woord gelijk is aan de ingegeven letter
								geheim_woord = geheim_woord[:letterpositie] + letter + geheim_woord[letterpositie + 1:] #dan moet het woord met de - aangepast worden: alles voor de geraden letter blijft -, de letter vervangt een - en alles wat na de letter komt blijft -
					else: #als de input (1 letter) niet in het te raden woord voorkomt
						print(letter.upper(), "is helaas fout.")
						wrong_guesses = wrong_guesses + letter
					gok = gok + 1
					if te_raden_woord != geheim_woord:	
						print("Je kan nog", 10 - gok, "keer raden.")
					else:
						print("Je hebt het woord geraden!")
				else: #als de letter al eerder is geraden en dus in lijst guessed_letters staat
					print("Je hebt", letter, "al geraden.")
			else: #als de input ofwel meerdere tekens bevat ofwel geen deel uitmaakt van het alfabet
				print("Je mag slechts 1 letter invullen.")
			

			
		if te_raden_woord == geheim_woord: #als alle streepjes ingevuld zijn en het komt overeen met het te geraden woord
			print("Het woord was inderdaad", te_raden_woord.upper(), "!")
			print("Nice!")
		else: #als je meer dan 10x hebt moeten gokken en je hebt het antwoord nog niet
			print("Het woord dat we zochten was", te_raden_woord.upper(), ". Helaas heb je dit niet gevonden.")
			print("Game over.")
			#BD hier zou het script ook moeten eindigen. Als je verkeerd antwoord, krijg je toch credits alsof je juist geraden had
	
		if gok == 1:
			print("Waw, supergoed gedaan! Je wint", play_galgje_win_1_guess, "extra credits." )
			credits = credits + 24
		elif gok < 5:
			print("Dat is indrukwekkend. Je wint", play_galgje_win_2_5_guess, "extra credits.")
			credits = credits +  14
		elif gok <= 9:
			print("Niet slecht! Je wint", play_galgje_win_other_guess, "extra credits.")
			credits = credits +  9
		else:
			print("Jammer. Je wint geen credits.")
			credits = credits +  0
			
		speel_opnieuw = input("Nog eens spelen?")
		
	if credits < play_galgje_kost and speel_opnieuw == "ja":
		print("Je hebt niet genoeg credits om dit spel te spelen.")
	else:
		print("Bye.")
	return credits
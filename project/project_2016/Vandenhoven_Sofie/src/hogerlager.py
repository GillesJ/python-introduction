import random 

def play_hoger_lager(credits): #definitie om aan te roepen in gamecarousel
	play_hoger_lager_kost = 2
	play_hoger_lager_win = 3
	print("\n")
	print("Welkom bij hoger lager! Elk spelletje hoger lager kost", play_hoger_lager_kost, "credits.")
	
	speel_opnieuw = "ja"
	while speel_opnieuw == "ja":
		credits = credits - play_hoger_lager_kost #credits - kostprijs
		huidig_nummer = random.randint(0, 20)
		print("\n")
		print ("Het spel gaat van 0 tot en met 20.")
		print ("Je nummer is", huidig_nummer) 
		print ("Hoger of lager?") 
		answer = input()
		nieuw = random.randint(0, 20) #random nummer genereren
		print("\n")
		print("Je nummer is", nieuw)
		if nieuw > huidig_nummer and answer == "hoger" or nieuw < huidig_nummer and answer == "lager": #situaties: correct
			print("Goed gedaan! Je wint", play_hoger_lager_win, "extra credits!")
			credits = credits + play_hoger_lager_win #x credits bij
			speel_opnieuw = input("Nog eens spelen?")
		elif nieuw > huidig_nummer and answer == "lager" or nieuw < huidig_nummer and answer == "hoger": #situaties: foutief
			print("Jammer, volgende keer beter! Je wint geen coins!")
			#geen credits bij, maar wel -2 van regel 10
			speel_opnieuw = input("Nog eens spelen?")
		else: 
			if answer != "hoger" or answer != "lager":
				print("Je moet hoger of lager invullen! Je krijgt je credits terug. Probeer het opnieuw (:")
				credits = credits + play_hoger_lager_kost
				speel_opnieuw = "ja"
			else:
				print("Oh, bad luck, de nummers zijn gelijk!")
				speel_opnieuw = input("Nog eens spelen?")

	if credits < play_hoger_lager_kost and speel_opnieuw == "ja": #als je minder dan 3 #BD 2 credits hebt en je wilt opnieuw spelen
		print("Je hebt niet genoeg credits om dit spel te spelen.")
	else:
		print("Bye.")
		
	return credits
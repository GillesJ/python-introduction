import random

def play_kop_of_munt (credits): #definitie om aan te roepen in gamecarousel
	play_kop_of_munt_kost = 2
	play_kop_of_munt_win = 3
	
	keuzes = ['kop', 'munt']
	print("Welkom bij kop of munt! Elk spelletje kop of munt kost", play_kop_of_munt_kost, "credits.")
	speel_opnieuw = "ja" #BD liever Boolean, maar logische keuze gezien dit soms een user input is
	while speel_opnieuw == "ja":
		credits = credits - play_kop_of_munt_kost #credits - kostprijs #BD -= shortcut
		print("\n")
		print("Wat denk je? Kop of munt?")
		answer = input() #ik denk kop of munt
		kant_muntstuk = random.choice(keuzes)
		print("\n")
		print(kant_muntstuk) #het is kop of munt
		
		if kant_muntstuk == "kop" and answer == "kop" or kant_muntstuk == "munt" and answer == "munt": #BD beter: check kant_muntstuk == answer
			print("Het is", kant_muntstuk, ". Goed gedaan! Je wint", play_kop_of_munt_win, "credits.")
			credits = credits + play_kop_of_munt_win #x credits bij
			speel_opnieuw = input("Nog eens gooien?")
		if kant_muntstuk == "kop" and answer == "munt" or kant_muntstuk == "munt" and answer == "kop": #BD kant_munstuk moeten verbeteren
			print("Het is", kant_muntstuk, ". Jammer! Je wint geen coins.")
			#geen credits bij, maar wel -2 van regel 10
			speel_opnieuw = input("Nog eens gooien?")
		else:
			print("Je moet kop of munt invullen. Je krijgt je credits terug. Probeer het opnieuw! (:")
			credits = credits + play_kop_of_munt_kost
			speel_opnieuw = "ja"
		
	if credits < play_kop_of_munt_kost and speel_opnieuw == "ja": #als je minder dan 3 credits hebt en je wilt opnieuw spelen
		print("Je hebt niet genoeg credits om dit spel te spelen.")
	else:
		print("Bye.")
		
	return credits
		

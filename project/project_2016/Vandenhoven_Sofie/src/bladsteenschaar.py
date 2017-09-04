import random

def play_blad_steen_schaar (credits): #definitie om aan te roepen in gamecarousel
	play_blad_steen_schaar_kost = 2
	play_blad_steen_schaar_win = 3
	print("\n")
	print("Welkom bij Blad steen schaar! Elk spelletje kost", play_blad_steen_schaar_kost, "credits.")
	
	keuzes = ['blad', 'steen', 'schaar']

	speel_opnieuw = "ja"
	while speel_opnieuw == "ja":
		credits = credits - play_blad_steen_schaar_kost #credits - kostprijs
		print("Oké, hier gaan we. Blad, steen of schaar?")
		
		answer = input() #ik denk B, St, Sch
		keuze_computer = random.choice(keuzes)
		print(keuze_computer) #het is B,ST of SCH
		
		if keuze_computer == "blad" and answer == "blad": #BD kon korter: if keuze_computer == answer
			print("Het is", keuze_computer, "tegen", answer, ". Het is gelijkspel! Je krijgt je", play_blad_steen_schaar_kost, "credits terug!")
			credits = credits + play_blad_steen_schaar_kost
			speel_opnieuw = input("Nog eens spelen?")
		elif keuze_computer == "blad" and answer == "steen":
			print("Het is", keuze_computer, "tegen", answer, ". De computer heeft je verslagen! Je wint geen credits.")
			speel_opnieuw = input("Nog eens spelen?")
		elif keuze_computer == "blad" and answer == "schaar":
			print("Het is", keuze_computer, "tegen", answer, ". Jij wint, goed gedaan! Je wint", play_blad_steen_schaar_win, "extra credits.")
			credits = credits + play_blad_steen_schaar_win
			speel_opnieuw = input("Nog eens spelen?")	
		elif keuze_computer == "steen" and answer == "blad":
			print("Het is", keuze_computer, "tegen", answer, ". Jij wint, goed gedaan! Je wint", play_blad_steen_schaar_win, "extra credits.")
			credits = credits + play_blad_steen_schaar_win
			speel_opnieuw = input("Nog eens spelen?")
		elif keuze_computer == "steen" and answer == "steen":
			print("Het is", keuze_computer, "tegen", answer, ". Het is gelijkspel! Je krijgt je", play_blad_steen_schaar_kost, "credits terug!")
			credits = credits + play_blad_steen_schaar_kost
			speel_opnieuw = input("Nog eens spelen?")
		elif keuze_computer == "steen" and answer == "schaar":
			print("Het is", keuze_computer, "tegen", answer, ". De computer heeft je verslagen! Je wint geen credits.")
			speel_opnieuw = input("Nog eens spelen?")
		elif keuze_computer == "schaar" and answer == "blad":
			print("Het is", keuze_computer, "tegen", answer, ". De computer heeft je verslagen! Je wint geen credits.")
			speel_opnieuw = input("Nog eens spelen?")
		elif keuze_computer == "schaar" and answer == "steen":
			print("Het is", keuze_computer, "tegen", answer, ". Jij wint, goed gedaan! Je wint", play_blad_steen_schaar_win, "extra credits.")
			credits = credits + play_blad_steen_schaar_win
			speel_opnieuw = input("Nog eens spelen?")
		elif keuze_computer == "schaar" and answer == "schaar":
			print("Het is", keuze_computer, "tegen", answer, ". Het is gelijkspel! Je krijgt je", play_blad_steen_schaar_kost, "credits terug!")
			credits = credits + blad_steen_schaar_kost
			speel_opnieuw = input("Nog eens spelen?")
		else:
			print("Er is iets foutgegaan.")
			speel_opnieuw = input("Wil je nog eens proberen?")
	if credits < play_blad_steen_schaar_kost and speel_opnieuw == "ja":
		print("Je hebt niet genoeg credits om dit spel te spelen.")
	else:
		print("Bye.")
		
	return credits #credits wordt geüpdate en doorgegeven aan gamecarousel


		

import random
from hogerlager import play_hoger_lager #BD NICE!
from kopofmunt import play_kop_of_munt
from bladsteenschaar import play_blad_steen_schaar
from quiz import play_quiz
from galgje import play_galgje

welk_spel = 0
credits = 10
while welk_spel != 6:
	if credits <= 2: #niet meer mogelijk om een spel te 'betalen' #BD in principe zou het < ipv <= moeten zijn
		print("Sorry, je hebt geen credits meer. De carousel is gesloten voor jou!")
		break
	else:
		print("\n")
		print("Welkom in de game carousel! Je hebt momenteel", credits, "credits.")
		print("\n")
		print("Welk spel wil je spelen?")
		print("Je kan kiezen tussen:") 
		print("1. Hoger lager")
		print("2. Kop of Munt")
		print("3. Blad Steen Schaar")
		print("4. Quiz")
		print("5. Galgje")
		print("6. Exit")
		print("\n")
		welk_spel = input("Kies [1,2,3,4,5 of 6]: ")
		######HOGER LAGER
		if welk_spel == "1": #BD Knap hoe elke functie de overblijvende credits returnt
			credits = play_hoger_lager(credits) #credits worden geassigned en teruggegeven in het .py bestand gamecarousel

		###########KOP OF MUNT
		elif welk_spel == "2":
			credits = play_kop_of_munt(credits)

		###########BLAD STEEN SCHAAR
		elif welk_spel == "3":
			credits = play_blad_steen_schaar(credits)
			
		###########QUIZ
		elif welk_spel == "4":
			credits = play_quiz(credits)
			
		###########GALGJE
		elif welk_spel == "5":
			credits = play_galgje(credits)
		
		###########EXIT
		elif welk_spel == "6":
			print ("See you soon.")

		###########ANDER CIJFER
		else:
			print("Sorry, dit spel kennen we niet.")
import codecs

def play_quiz(credits): #definitie om aan te roepen in gamecarousel
	f = codecs.open('quiz.csv', 'r', 'UTF-8') ##importeer csv file met de vragen
	lines = f.readlines()
	collection_questions = [] #lege verzameling waar alle vragen moeten inkomen

	#vraag en antwoord in een lijst, per lijn
	for line in lines: 
		line = line.strip()
		question_answer = line.split(";")
		collection_questions.append(question_answer)

	play_quiz_kost = 5
	play_quiz_win_10 = 55
	play_quiz_win_7 = 35
	play_quiz_win_5 = 10
	print("Welkom bij de quiz! Dit spelletje kost je", play_quiz_kost, "credits.")
	print("\n")
			
	speel_opnieuw = "ja"
	#hier zijn alle lijstjes met vragen en antwoorden in één grote lijst
	while speel_opnieuw == "ja" and credits >= play_quiz_kost:
		credits = credits - play_quiz_kost
		from random import randrange
		random_q_a = randrange(0,len(collection_questions))##random_q_a = alle vragen vanaf de eerste tot en met de laatste

		#hoe de vragen eruit moeten zien
		question = (collection_questions[random_q_a][0]) 
		correct_answer = (collection_questions[random_q_a][1])
		punten = 0
		amount_questions = 0

		print(question)
		answer = input()
		
		if (answer).lower() == (correct_answer).lower():
			punten = punten + 1 
			amount_questions = amount_questions + 1
			print((correct_answer).upper() , "is correct!")
		else:
			amount_questions = amount_questions + 1
			print("Sorry,", (answer).upper() , "is niet correct. We zochten het antwoord" , (correct_answer).upper())
		print(punten, "/ 10")
		print("\n")

		while amount_questions < 10:
			random_q_a = randrange(0,len(collection_questions)) #random vraag oproepen
			question = (collection_questions[random_q_a][0])  #eerste element is de vraag
			correct_answer = (collection_questions[random_q_a][1]) #tweede element is het bijhorende antwoord
			print(question)
			answer = (input()).lower() #lower om geen foute antwoorden aan te rekenen met hoofdletters
			if (answer).lower() == (correct_answer).lower():
				punten = punten + 1 
				amount_questions = amount_questions + 1
				print((correct_answer).upper() , "is correct!")
			else:
				amount_questions = amount_questions + 1
				print("Sorry," , (answer).upper() , "is niet correct. We zochten het antwoord" , (correct_answer).upper())
			print(punten, "/", amount_questions)
		print ("eindscore:", punten, "/", amount_questions)	
	
		if punten == 10:
			print("Waw, perfecte score! Daarvoor krijg je", play_quiz_win_10, "extra credits." )
			credits = credits + 25
		elif punten > 7:
			print("Je was echt goed bezig! Volgende keer 10/10? Hiervoor krijg je", play_quiz_win_7, "extra credits.")
			credits = credits +  15
		elif punten >= 5:
			print("Niet slecht! Je wordt beloond met", play_quiz_win_5, "extra credits.")
			credits = credits +  10
		else:
			print("Je haalde net niet de helft. Jammer :( Je wint geen credits.")
			
		speel_opnieuw = input("Wil je opnieuw spelen?")
		
	if credits < play_quiz_kost and speel_opnieuw == "ja":
		print("Je hebt niet genoeg credits om dit spel te spelen.")
	else:
		print("Bye.")
		
	return credits
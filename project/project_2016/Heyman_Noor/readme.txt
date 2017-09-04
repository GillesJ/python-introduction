Dit deelproject had drie doelen:

1) een bestand (txt) met woordenschat en woordniveau's omzetten in een dictionary 
2) in een bestand (txt) met lemma's en frequenties van die lemma's kunnen opzoeken welke woorden frequenter zijn dan andere
3) in een bestand met woordenschat kunnen opzoeken welke woorden er al in het bestand zaten.

Alle code werd initieel opgeroepen via Sublime Text, maar opdracht 3 moest worden aangeroepen in het cmdvenster of in een notebook. 

Deel 1: dictionary_niveaulijst.py, op basis van UGent nivealijst

Input was een tekstbestand met woorden en woordniveau's gescheiden door tabs.
Ik heb het tekstbestand eerst gesplit op tabs en dan omgezet in een dictionary. De woordniveau's werden gecast als strings, omdat bij de eindvalues
uiteindelijk niets meer moest worden toegevoegd. Het belangrijkste resultaat is gewoon het printen van de value

Deel 2: frequentielijst.py, op basis van CREA_freq

Input was een zeer groot tekstbestand met lemma's en de frequenties van die lemma's.

Eerste probleem: het bestand openen in Sublime Text. Het stond niet in utf-8, dus werd (door jouw suggestie) in lijn 3 utf-8 aangepast naar latin1,
en werd er nog een lijn code helemaal bovenaan toegevoegd om de code te doen werken op alle computers. Ik heb lijn 5 nog niet verwijderd, omdat ik dacht dat 
dat ook makkelijker was voor jullie om dat zo te testen.

Tweede probleem: het indelen van de frequenties. Je had terecht opgemerkt dat de initiële verdeling niet echt correct was. In plaats van de
indeling wiskundig te berekenen, ben ik handmatig gaan kijken in het originele bestand tot waar de hoogste waarden lagen, en dan heb ik de 
frequenties ingedeeld in 'extremely frequent' etc. Initieel was mij gevraagd om van de indeling 'very frequent' etc. een tweede value te maken in een dictionary
met de woorden als keys en de frequentie en de genormaliseerde waarde als values, maar daar zat ik op vast.

Daarom heb ik ervoor gekozen om te werken met een for loop en om de lemma's steeds te laten toevoegen aan een lijst.

Deel 3: dictionary_seenorunseen.py, op basis van UGent niveaulijst

Het was de bedoeling om te testen of bepaalde woorden voorkwamen in het bestand of niet. Ik heb het tekstbestand omgezet in een dictionary op dezelfde manier als bij
de twee andere opdrachten. Ik dacht eerst met een for loop te werken, maar dan kreeg ik inderdaad alle keys terug - en dat was niet de bedoeling.

In de plaats heb ik gewerkt met een input die ik heb getest via de notebook. Nu krijg ik enkel het woord terug dat ik wil terugkrijgen. 


Conclusie:

Ik heb gemerkt dat ik niet echt aanleg heb voor programmeren, maar ik ben toch aardig in de buurt geraakt van wat ik wou bereiken. Ik hoop dat 
prof Goethals hier iets aan heeft, of dat ik toch een basis heb gelegd die nuttig kan zijn. De scope van het project had misschien nog wat groter 
mogen zijn. 

#BD Het was leuk geweest als alledrie de functies in een overkoepelend script werden aangeroepen voor een gegeven lemma (met import)
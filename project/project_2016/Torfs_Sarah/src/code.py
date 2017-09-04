import codecs
f_in = codecs.open('test_source.txt', 'r', 'utf-8') # Het bronbestand wordt geopend.
source_text = f_in.read() # Het bronbestand wordt ingelezen.
f_in.close()

f_in = codecs.open('test_target.txt', 'r', 'utf-8') # Het doelbestand wordt geopend.
target_text = f_in.read() # Het doelbestand wordt ingelezen.
f_in.close()

source_list = source_text.split("\r\n") # Het bronbestand wordt gesplitst in lijnen die worden toegevoegd aan de lijst source_list. Elke lijn is een bronsegment.
target_list = target_text.split("\r\n") # Het doelbestand wordt gesplitst in lijnen die worden toegevoegd aan de lijst target_list. Elke lijn is een doelsegment.

segment_pairs = list(zip(source_list, target_list)) # De twee lijsten worden samengevoegd in een ziplijst.

def fix_uppercase(segment_pair): # De eerste fix-functie wordt gedefinieerd: bronsegmenten die volledig in hoofdletters staan, moeten in het doelsegment ook in hoofdletters gezet worden (als dat nog niet het geval is).
	source_segment, target_segment = segment_pair # Elke combinatie van bron- en doelsegment uit de gezipte lijst wordt hier weer opgesplitst in bronsegment en doelsegment.
	if source_segment == source_segment.upper(): # Voorwaarde: als het bronsegment in hoofdletters staat...
		result = target_segment.upper() # ... dan moet het doelsegment ook in hoofdletters staan. De variabele 'result' bevat dus het doelsegment in hoofdletters.
	if source_segment != source_segment.upper(): # Voorwaarde: als het bronsegment niét in hoofdletters staat... #BD dit kon ook met een else, maar is sowieso overbodig 
		result = target_segment # ... dan verandert er niets aan het doelsegment. De variabele 'result' bevat dus het originele doelsegment.
	return (source_segment, result) # Deze functie geeft de combinatie terug van bronsegment en de inhoud van 'result'. Uiteindelijk hebben we in de doeltekst enkel het 'result' nodig, maar op deze manier kunnen meerdere fix-functies na elkaar worden toegepast.

def fix_uppercase_untranslatable(segment_pair): # De tweede fix-functie wordt gedefinieerd: bronwoorden die niet vertaald (kunnen) worden en die in hoofdletters staan, moeten in de doeltekst ook in hoofdletters staan.
	source_segment, target_segment = segment_pair # Elke combinatie van bron- en doelsegment uit de gezipte lijst wordt hier weer opgesplitst in bronsegment en doelsegment, net als in de vorige functie.
	source_words = source_segment.split() # Het bronsegment wordt opgesplitst in woorden die worden toegevoegd aan de lijst 'source_words'.
	uppercase_source_words = [] # Een lege lijst wordt gedefinieerd waarin alle woorden zullen worden toegevoegd die in de brontekst volledig in hoofdletters staan.
	for source_word in source_words: # De functie loopt over alle woorden in 'source_words'.
		if source_word == source_word.upper(): # Voorwaarde: als het woord in de brontekst in hoofdletters staat...
			uppercase_source_words.append(source_word) # ... dan wordt dat woord toegevoegd aan de eerder gedefinieerde lijst 'uppercase_source_words'. #BD List comprehension was hier mooi geweest
	target_words = target_segment.split() # Het doelsegment wordt opgesplitst in woorden die worden toegevoegd aan de lijst 'target_words'.
	for target_word in target_words: # De functie loops over alle woorden in 'target_words'.
		if target_word.upper() in uppercase_source_words: # Voorwaarde: als het woord in de lijst 'uppercase_source_words' voorkomt (en dus in de brontekst in hoofdletters staat)...
			target_segment = target_segment.replace(target_word, target_word.upper()) # ... dan wordt dit woord in de string 'target_segment' ook in hoofdletters gezet.
	return (source_segment, target_segment) # De functie geeft de gefixte combinatie van bron- en doelsegment terug.

def fix_numbers(segment_pair): # De derde fix-functie wordt gedefinieerd: wanneer de doeltekst een getal bevat dat niet letterlijk in de brontekst voorkomt, moet een waarschuwing gegeven worden voor de post-editor.
	source_segment, target_segment = segment_pair # Elke combinatie van bron- en doelsegment uit de gezipte lijst wordt hier weer opgesplitst in bronsegment en doelsegment.
	source_words = source_segment.split() # Het bronsegment wordt opgesplitst in woorden die worden toegevoegd aan de lijst 'source_words'.
	source_numbers = [] # Een lege lijst wordt gedefinieerd waarin alle 'woorden' uit de brontekst zullen worden toegevoegd die enkel uit cijfers bestaan.
	for source_word in source_words: # De functie loopt over alle woorden in 'source_words'.
		if source_word == source_word.isdigit(): # Voorwaarde: als het woord in de brontekst enkel uit cijfers bestaat... #BD geen equivalence test doen hier
			source_numbers.append(source_word) # ... dan wordt het toegevoegd aan de lijst 'source_numbers'.
	target_words = target_segment.split() # Het doelsegment wordt opgesplitst in woorden die worden toegevoegd aan de lijst 'target_words'.
	for target_word in target_words: # De functie loopt over alle woorden in 'target_words'.
		if target_word == target_word.isdigit() and target_word.isdigit() not in source_numbers: # Voorwaarde: als het woord in de doeltekst enkel uit cijfers bestaat en niet voorkomt in de lijst 'source_numbers' (het getal staat dus niet in de brontekst)... #BD target_word not in...
			result = target_segment + " Warning! Check if all numbers were transferred correctly." # ... dan zou de variabele 'result' het doelsegment en een waarschuwing moeten geven, maar de waarschuwing blijft uit. #BD ipv target_segment aan te passen, beter een warning hier en target_segments laten zoals ze zijn. Onderstaande regel wordt dan overbodig. 
		if target_word != target_word.isdigit() or target_word.isdigit() in source_number: # Voorwaarde: als het woord in de doeltekst niet uit cijfers bestaat of als het uit cijfers bestaat maar wel voorkomt in de lijst 'source_numbers'...
			result = target_segment # ... dan geeft de variabele 'result' het oorspronkelijke doelsegment terug.
	return (source_segment, result) # De functie geeft oorspronkelijke combinatie van bron- en doelsegment terug, máár met een opmerking erbij als er getallen voorkomen die niet overeenkomen en gecontroleerd moeten worden door de post-editor.

corrected_segment_pairs = [] # Een lege lijst wordt gedefinieerd.

for segment_pair in segment_pairs: # Er wordt geloopt over alle segmentparen in de gezipte lijst 'segment_pairs'
	corrected_segment_pair = fix_uppercase(segment_pair) # Voor elk segmentpaar wordt een variabele gedefinieerd die het resultaat bevat van de 'fix_uppercase' functie, toegepast op het segmentpaar in kwestie.
	corrected_segment_pair = fix_uppercase_untranslatable(corrected_segment_pair) # In dezelfde variabele worden de eerder toegevoegde segmentparen nu vervangen door dezelfde segmentparen waarop de 'fix_uppercase_untranslatable' functie is toegepast.
	corrected_segment_pair = fix_numbers(corrected_segment_pair) # In dezelfde variabele worden de eerder toegevoegde segmentparen vervangen door dezelfde segmentparen waarop de 'fix_numbers' functie is toegepast.
	corrected_segment_pairs.append(corrected_segment_pair) # Nadat alle fix-functies uitgevoerd zijn, worden de resulterende segmentparen toegevoegd aan de eerder gedefinieerde lijst 'corrected_segment_pairs'.

#BD alles hieronder mocht ook een functie zijn
corrected_target_segments = [] # Een lege lijst wordt gedefinieerd.

for source_segment, target_segment in corrected_segment_pairs: # Er wordt geloopt over alle bron- en doelsegmenten in 'corrected_segment_pairs'.
	corrected_target_segments.append(target_segment) # Enkel de doelsegmenten worden toegevoegd aan de hierboven gedefinieerde lijst 'corrected_target_segments'.

f_out = codecs.open('testoutput.txt', 'w', 'utf-8') # Een nieuw tekstbestand wordt gecreëerd waarin de gecorrigeerde doelsegmenten zullen worden ingeschreven.
for target_segment in corrected_target_segments: # Er wordt geloopt over de doelsegmenten in de lijst met gecorrigeerde doelsegmenten.
    f_out.write(target_segment + "\n") # Elk segment wordt in het nieuwe tekstbestand op een nieuwe lijn geschreven. Anders zouden we gewoon een lijst terugkrijgen.
f_out.close()
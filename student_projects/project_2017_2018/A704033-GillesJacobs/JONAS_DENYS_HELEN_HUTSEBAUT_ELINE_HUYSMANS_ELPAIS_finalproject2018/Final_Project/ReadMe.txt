The ReadMe file explains how all separate files work, however, to run the whole program, you can just run the document 'project_main.py'.

1. Webscraping 

1_webscraping.py

- With this script, we scrape the 5 most recent articles from the Economía pages of the El Pais website. For each article, we scrape the following elements:
- Title 
- URL
- Date of publication
- Subtitle 
- Introduction (If applicable. If no introduction is found “no hay introduccion” is shown) 
- All this data is written into .txt files (one per article, with all data of that article) 
- output = article1.txt, article2.txt, article3.txt, article4.txt, article5.txt 

2. Treetagger

2_tagging_docs.py

The TreeTagger is a tool for annotating text with part of speech and lemma information. For this project, we will especially focus on verbs, nouns, adverbs and adjectives and leave out functional words like prepositions, articles and conjunctions. We used the Spanish parameter file trained on the Ancora corpus that was provided on the website of TreeTagger itself.

The input of the TreeTagger will be the .txt files that include the articles from El País. We wanted to run only one script and thus run the programme on five (or more) files at the same time.

The output of the TreeTagger is also a .txt file with three columns: one with the word, one with its part of speech and one with its lemma. If you want to know what the abbreviations in the part of speech column stand for, you can read the added document ‘morfologia_tagset’.


3. Sentiment Analysis 

3_sorting_tagged_text_and_separating_lemmata.py

- This script sorts the treetagger output:
1. Reading the output and assigning the output to tagged_text
2. Creating a list: ver_sus_adj_adv
3. For every line in tagged_text, if the line contains ‘NC’ or ‘ADJ’ or ‘VLfin’ or ‘VLinf’ or ‘ADV, the word is appended to the list ‘ver_sus_adj_adv’. This data is written to a separate file, for each article. (article1_ver_sus_adj_adv, article2_....) 
- We only need the lemmata (no conjugated verb forms or inflected adjective forms) since the lexicon only contains lemmata. 
1. For every line in the list ver_sus_adj_adv, the script appends the third word (the lemma) to the lemmata list.
2. Writing lemmata list to a separate file. For each article, a separate file is generated. 

4_matching_lemmata_to_pos-neg.py

- Reading pos_words
- Reading neg_words
- Reading lemmata
- Creating an output list + setting counter
	- For every lemma in lemmata: 
		- if it is in pos_words: 
			- the script appends “the lemma itself + +-sign” to output
			- The counter increases with 1
		- If it is in neg_words: 
			- The script appends “the lemma itself + - sign” to output
			- The counter decreases with 1.
		- If it is not in pos_words and not in neg_words, the script appends “Lemma is not in one of the lexicons” to output.
			- Write output and final count to file
This final value displays wether the article has a positive or negative connotation: we start from 0 and the counter goes up or down according to the sentiment each word has. This means that, if the end value is above zero, the connotation of the article is positive. If the value is below zero, the connotation is negative. 


REMARKS
- Our code is a lexicon-based approach, which means the code only checks the word itself and not its context, while the context often is a very important factor for determining the value of a word. 
	Eg.:	Las ganancias bajan (de inkomsten dalen) - negative
			Las deudas bajan (de schulden dalen) - positive
	
To solve this problem, we would have to make sure that the code checks multiple words (in order to create context) at the same time, to see if the phrase has a positive or negative connotation. Unfortunately we were not able to program our code in this way, as this requires a more experienced knowledge of Python. 

       
- Remark concerning Proposal
		- part 3B & 4A: we intended to analyze the 20 most common words and include them in the output, with their value. As we noticed most input is not much longer than 20 words (as there is often no introduction), this seems a bit useless. We therefore omitted this part. 
		- part 3C: "If the word is not in the dictionary/list yet, add it, so it will be taken into account for future analysis." Unfortunately, we did not (yet) find a way to let our program automatically assign a connotation to unknown words (= words that are not in the lexicon). We did, however, expand the lexicon manually with a limited number of lemmata that we were certain of, e.g. ‘no’, ‘nunca’.

- Instead of creating a new lexicon, we used a lexicon that was available on the internet. We downloaded two polarity lexicons (Sentiment Lexicons in Spanish) that have been automatically or semi-automatically generated. Then we split up the lexicon into one positive-words-lexicon and one negative-words-lexicon. The problem with this lexicon is, however, that it does not take into account diacritic marks, such as accents. Our system does include these marks, which means that words in our final output might not be recognized in the lexicon and thus not be appended with a positive or negative tag.

Reference: Veronica Perez Rosas, Carmen Banea, Rada Mihalcea, Learning Sentiment Lexicons in Spanish, in Proceedings of the International Conference on Language Resources and Evaluations (LREC 2012), Istanbul, Turkey, May 2012.
JAPANESE GLOSSARY EXTRACTOR
===========================

1. HOW TO USE
2. REQUIREMENTS
3. PROCESS
	Reference file generation
	Tokenization
	Token level check
	Text level check
	Reading level filter
	Jisho API lookup
	Docx output generation




1. HOW TO USE
=============
To generate a glossary, first paste a Japanese text into a .txt file.
Make sure that the .txt file is located in the input folder and that it has a proper name.
A proper filename consists of the actual title, a reference and a level.
--> TITLE_REFERENCE_LEVEL.txt

TITLE:	
	You can give your file any title, as long as they do not contain any underscores
REFERENCE:
	For the reference, you can choose between a number of options:
	"JLPT" 		for the official Japanese language grading system
	"Genki" 	for the Genki I and II handbooks (BEWARE: Genki is a beginner level book and contains not much vocab!)
	"Minna" 	for the Minna no Nihongo handbook
	In the future, Intermediate Japanese will also be an option.
LEVEL:
	Level is either a number or in the case of JLPT, an N-level (N5 > N1)
	If do not enter a number, the script will determine the level of the text instead of generating a glossary.

Once your file with the correct title is in the correct location, activate the script in the src folder.
No further input is needed, as the filename will be used as a key to determine the script's function.

----------------------------------------------------------------------------------------------------
IMPORTANT: the lower the reading level, the more items have to be glossed, and the longer it takes!
----------------------------------------------------------------------------------------------------



2. REQUIREMENTS --> (the requirements file can be found in the src folder)
===============
- Python
- Standard Python packages:
	os
	codecs
	requests
	JSON
	re
- Standalone Python packages:
	janome 0.3.6
	python-docx 0.8.6



3. PROCESS
==========

Reference file generation
-------------------------
To access the data files efficiently throughout the runtime of the script, a list of reference files is created.
The files need to be iterated through, so they need a fixed and correct order that can work for various reference types.
There is a number of factors preventing the files from being sorted simply on the basis of their filenames:
- The list allows only the files to be sorted and stored that are relevant for a single run, which is more efficient.
- Not all files have the same title format. Usually, the difficulty increases when the level number is higher.
  For JLPT, the order is reversed, and the level is denoted by N5 > N1 from easy to difficult. This makes sorting more difficult.
- Kanji and vocabulary files do not necessarily correspond. A word can be more or less difficult than the sum of its components.
  For this reason, words have to be looked up in vocab lists, and components in kanji lists.
- Not all levels exist. E.g. Genki only starts teaching kanji at chapter 3, and not all books have an equal amount of chapters.
- By default, files will not be sorted lexicographically, 
For these reasons, it is easier to define a list of vocab files and an list of kanji files that can sort all reference files.
The script uses the index of every level to do calculations, and can also use it to find the name of the reference in the lists.

index 			0				 	1					->		-1
JLPT:			[ JLPT_N5_vocab.txt ,	JLPT_N5_vocab.txt -> JLPT_N1_vocab.txt ]
Genki vocab: 	[ Genki_1_vocab.txt ,	Genki_2_vocab.txt -> Genki_23_vocab.txt]
Genki kanji: 	[ Genki_3_kanji.txt ,	Genki_4_kanji.txt -> Genki_23_kanji.txt]

Practically speaking, the scrips loops through the data files and filters all files matching the reference in the input file title.
It then either appends them to the list, or inserts them from the front if JLPT is the reference.
NOTE: All reference files are made available online and free from charge by several internet users.


Tokenization
------------
The tokenization process is done in two steps. 
In the first step, the raw text contained in the input file is tokenized by Janome (蛇の目, Bull's-eye).
Janome is a tokenizer and PoS tagger written in pure Python with an integrated dictionary (mecab-ipadic-2.7.0-20070801) and language model.
It has several sub-functions that help define its main function (for more info, see the Janome documentation).
The RegexReplaceCharFilter removes all punctuation, numerals and roman letters before the tokenisation.
The POSStopFilter suppresses particles (助詞), auxiliaries and verb inflections (助動詞) and other symbols (記号).
Janome outputs a list with strings: 
["表層形,	品詞, 品詞細分類1, 品詞細分類2, 品詞細分類3, 活用型, 活用形, 基本形, 読み, 表層形", ""]
["surface	PoS, PoS_detail_1, PoS_detail_2, PoS_detail_3, infl_type, infl_form, lemma, reading, pronunciation", ""]

In the second stage, the output is manipulated to a dictionary with a list of features.
To avoid miscalculations due to irregular input or data formats when pulling the data from the API, placeholder items are created.
This is also done to anticipate Jisho's inability to recognize proper names. If they are not found, the original reading and "name" tag can be kept.
{"lemma" = [alternatives (empty), PoS (empty), level (empty), reading (backup), meaning (backup)}


Token Level Check
---------------------
Now that each token has a dictionary entry, the next function will try to find each word and insert its level into the dictionary.
As long as the "level" field in the dictionary is empty, the script will loop through all the files in the vocab reference list from easy to hard.
If the item is found in a particular file, the index of this file in the reference list is used to find and inject the actual name of the level.
First, all vocab files are looped over. When the end is reached, the word is looked up in the kanji files, because some tokens are one-kanji words.
To initiate the change to a different file, a counter is used. When the counter exceeds the number of files, an IndexError is caught to continue.
If the word was not found, the script iterates over all its characters, looping over and checking every kanji file; and then every vocab file.
If a character is a syllabic character (kana), the lowest level is set; since they are the first characters anyone learns.
If the character is found in a kanji or vocab file, the level is determined based on the index. 
Any time a character is rated level than a previous one, it overwrites the level of the word; so that the word is as hard as the hardest component.
Since the reference files are official, a character that it not found means that it is beyond the highest available reference level.


Text Level Check
----------------
Depending on the filename, the script can either check the level of a text if no level filer was provided, or it can proceed to the glossary stage.
If the text is to be checked for its level, it loops through all the dictionary items, and stores how many items are present of each level.
The real level is provided in the dictionary entry for each token, but since no ranking is required, its index in the files is of no importance here.
Verb endings and particles were filtered out at an earlier stage, so that all remaining tokens now have an accurate representation of their level.
The level with the highest amount of words is appended to the original file title to give the user an indication of how hard the text is.
WARNING: this level is determined ONLY on the basis of individual words. It does NOT take any other factors into account!


Reading Level Filter
--------------------
If the input file contains a level, the filter function iterates over every dictionary item, and copies those with a higher level to a new dictionary.
Most files are filtered on the basis of their surface level; files with a JLPT reference undergo a slightly different path to achieve the same result.
The new dictionary only contains items that have a harder or equal difficulty than the specified level.


Jisho API Lookup
-----------------
For every item in the dictionary, a request is sent to Jisho.org's API, which returns all data for the query in a JSON format. 
Jisho.org is a large database, and unwanted data is filtered by adding (or not adding) the data to lists prior to injecting them into the dictionary.
Every word returns a number of hits which each have a different content and amount of parameters. Within each parameter, different values can be present. As a result, if not filtered, an item could end up with dozens of identical values, while missing other values. It's all very complex.
The JSON structure looks as follows:
Data
	[								this equals a hit or variation of the word
		Is_common					
		Japanese
			Word:						hits can have alternate spellings								--> overwrites alternatives
			Reading:					hits can have multiple readings									--> overwrites readings
		Senses:
			English definition:			hits have multiple definitions									--> overwrites definition 
			PoS:						hits can have multiplt PoS and PoS depends on the meaning		--> overwrites PoS 
	]
As demonstrated above, the different features of each variation are scrambled for simplicity's sake, but, nonetheless, all data is present.
In most cases, the empty placeholders are overwritten. In cases where Jisho cannot provide data (usually names), the reading and proper name tag provided by janome are left unaltered, which results in a correct representation of almost all proper names.
At this stage, all features of the dictionary are filled in. For simplicity's sake, the number of readings are limited to 2; and definitions to 5.
{"lemma" = [lemma(alternatives), PoS, level, reading, meaning}
NOTE: Jisho is built on several online dictionaries that are also used to create the janome tokenizer, JLPT reference files and much more!
	This means that all these functions are compatible and should not interfere with each other.
NOTE: Jisho is open-source and free to use. 


Word File Generation
--------------------
This function relies on the .docx module to generate a Word file. It generates a title and table, with inbetween them an empty paragraph. 
I plan to add a function later on that would reprodoce the input file contents here. For now, the user has the option to paste the text here.
Due to the mechanics of the Py2Docx Script, the columns and rows have to be iterated through to fill in and style the entire table.
At this stage, the user can decide which values of the dictionary to output. By default, the alternatives, reading and meanings are represented.
If desired, the script can be changed to add or remove an additional column, or change the displayed features. The table style can also be changed.
+---------------------+
| Title (level)       |
|---------------------|
|                     |
|_____________________|
|word|reading|meanings|
|____|_______|________|
|____|_______|________|
|____|_______|________|
|____|_______|________|
|____|_______|________|
|____|_______|________|
|____|_______|________|

The docx file is saved in the root folder with an appropriate filename and title.


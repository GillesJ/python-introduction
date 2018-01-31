Project: check blog texts on lexical variety and suggest synonyms

Before you can run the code, you first need to insert a URL in the r = requests.get("URL") from the Blog page on the website of Femma.
TreeTagger and OpenDutchWordnet need to be installed on your computer to make the code work.

When you run the code, these steps will be executed:
- First, the website will be scraped to get the content between the p-tags. This code will be written to the file output_webscraping.txt
- Then, TreeTagger will tag the output_webscraping.txt file and write into a new file: output_webscraping_tag_cap.txt.
- In a next step, the TreeTagger output is cleaned and each line (word1, wordclass1, lemma1 ; word2, wordclass2, lemma2...) is put into a list to be able to work with this information. These lists are put into a bigger list: wordlist.
- Next, the programme makes a frequency dictionary of all the lemmas (freq_lem) and we filter out the word classes we want to use (by adding these to search_pos).
- In part 4, we write the dictionary to a file with JSON: clean_tt_output.
- Then the word frequency percentage of the lemmas is calculated. When it is higher than 1%, the lemma is added to the list high_freq. If there are no frequently used words, it will print: "Proficiat, uw tekst is gevarieerd!".
- If there are terms in high_freq, the programme uses OpenDutchWordnet to print synonyms for each of these words.
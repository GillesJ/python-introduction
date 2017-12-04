Bedoeling van het project:

Met dit project probeer ik een aantal frequente problemen op te lossen die opdoken in de automatische vertalingen geproduceerd door mijn KantanMT vertaalsysteem (gecreëerd voor de module Machine Translation & Post-editing).
Dit waren de problemen:
1) Sommige zinnen die in de brontekst volledig in hoofdletters stonden, werden in de doeltekst met kleine letters geschreven.
2) Sommige woorden die in de brontekst in hoofdletters stonden, werden in de vertaling met kleine letters geschreven.
3) Sommige getallen waren foutief overgezet in de doeltekst. Ofwel waren de cijfers volledig verkeerd, ofwel werden er spaties of interpunctietekens toegevoegd of weggelaten.

Probleem 1 kan worden opgelost met de fix-functie 'fix_uppercase'.
Probleem 2 kon ik niet oplossen omdat ik de code niet kan vertellen welk doeltaalwoord met welk brontaalwoord overeenkomt.
--> Ik heb het probleem daarom beperkt tot onvertaalbare woorden (die dus in bron- en doeltekst hetzelfde zijn). Deze kunnen gecorrigeerd worden met de fix-functie 'fix_uppercase_untranslatable'.
Probleem 3 heb ik niet kunnen oplossen. Ik heb een poging gedaan en de code toegevoegd aan het bestand, maar er zit nog een fout in die ik niet vind.
--> Het was oorspronkelijk de bedoeling om getallen meteen te corrigeren, maar omdat er vaak meerdere getallen in een segment staan en die niet noodzakelijk in dezelfde volgorde voorkomen, moet de post-editor de getallen alsnog controleren.
--> Daarom heb ik geprobeerd om de functie een waarschuwing te doen teruggeven als er in de doeltekst getallen voorkwamen die niet in de brontekst stonden. Dit is echter ook niet gelukt. De .isdigits() code lijkt niet te werken.

KantanMT geeft een simpel tekstbestand terug met de vertaling. De code kan worden toegepast door zowel het bronbestand (als .txt) als het doelbestand in te lezen en de fix-functies erop toe te passen.
De bron- en doelbestanden in de map data, bevatten acht lijnen. Lijnen 1-3 werden gebruikt om de code te testen tijdens het schrijven ervan. Lijnen 4-8 zijn afkomstig uit de erste KantanMT-vertaling die mijn systeem opleverde.
De kwaliteit van de doelzinnen is slecht, maar ze tonen aan dat fix-functies 1 (lijnen 1,4,6 en 8) en 2 (lijnen 2 en 5) correct worden toegepast. Lijnen 3 en 7 tonen aan dat fix-functie 3 niét correct wordt toegepast.
Na een aantal bijkomende bouwfases in KantanMT kwamen fouten als deze gelukkig niet meer voor in de uiteindelijke testvertaling.
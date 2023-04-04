# README data directory

The data directory contains word lists that can be used to form 
anagrams.  

The number of anagrams that can be produced, as well as 
their quality, depends partly on the word list.  A short word list 
like `1-1000.txt` (1000 very common English words) tends to produce 
very few anagrams, but any it produces will consist of common words. 
`wordlist.10000.txt` contains 10,000 words, including many uncommon 
short words.  It tends to build anagrams from those uncommon 
two-letter words.   File `ngsl.csv`, taken from a "new general 
service list" for second language learners of English, seems to strike a 
reasonable balance between comprehensiveness and quality.  

`ngsl.csv` is taken from the 
[New General Service List](http://www.newgeneralservicelist.org/) 
and reused under an Attribution-ShareAlike (CC BY-SA) license.  

<a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-sa/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/">Creative Commons Attribution-ShareAlike 4.0 International License</a>.
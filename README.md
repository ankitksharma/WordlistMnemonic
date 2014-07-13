WordlistMnemonic
================

This python script fetches Mnemonics of the wordlist provided from mnemonicdictionary.com and dump the data into a csv file.

####project.py file
This file contains the code to perform the mentioned task.


####Wordlist file
words.csv contains comma seperated list of words you want to set. I've already provided some of he more important GRE words. Edit this file as per the need.

####Result file
This file will contain the output of the script. The schema for the output would be

word$Definition$Mnemonic

Dependencies
------------
This script uses BeautifulSoup 4 so install it either via pip or easy_install

    $pip install beautifulsoup4
    -----
    $easy_install beautifulsoup4
    
How to use this project?
------------------------
 - Download the repository or clone it

>git clone https://github.com/ankitksharma/WordlistMnemonic.git

 - Edit the words.csv file
 - Run the project.py script

>python project.py

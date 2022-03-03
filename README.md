# Wanna complete wordle huh?
This simple py script can help you.

### Installation 
Can run in Python 3.9.2.
Copy repository:
```sh
$ git clone https://github.com/lalapopa/wordle_cracker.git
```
### Usage
Can solve word with length ≤ 9.
Run script.
```sh
$ python3 main.py [OPTION]
```
In OPTION you can specify word length, by default 5.

Follow output instruction.
In first output it gives you a random word from list words_alpha.txt.
In 'y/n?' you should input y or n and press Enter.
In 'What letter gray?' question if you don't have any of it you just can press Enter for skiping, otherwise you'll should input grey letters without any spaces:
```sh
...
What letter in gray?
abc⏎
Gray symbols: ['a', 'b', 'c']
...
```
If you have multiple same letters in yellow or green color you'll should input their positions without spaces:
```sh
Do you have yellow letter?
y/n?y⏎
What letter in yellow?
acw⏎
In what position letter A?
Begin from 1:23⏎
In what position letter C?
Begin from 1:5⏎
In what position letter W?
Begin from 1:1⏎
```
After 'My guess...' output you can find your won word.

Huge thanks for https://github.com/dwyl/english-words you guys did amazing work.


from sound import play
from muncher import munch
from pyfiglet import Figlet
from termcolor import colored
import random

figlet_slant = Figlet(font='slant')
figlet_standard = Figlet(font='standard')



score = 0
word_list = '''amino
anemometers
antennas
ash
beam
benches
brayed
chalk
chicken
cliff
constellation
crowd
depot
finish
fumble
gallop
gnaw
jangled
Mars
modern
Monday
Nepal
Pakistan
plaid
police
pond
pranks
punting
salamanders
secret
shepherd
stubborn
Tabasco
test
utensils
vinyl
Wednesday
workhorse'''.splitlines()

random.shuffle(word_list)

print(figlet_slant.renderText('Welcome to'))
print(colored(figlet_standard.renderText('SPELL TO ME!'),'green'))
print()
print('THE GAME WITH WORDS AND SPELLING BUT NO BEES...')
print('-----------------------------------------------')
play(f'welcome.wav')
input('Press enter to continue...')
print()


for i, word in enumerate(word_list):
    for guess_num in range(3):
        if guess_num == 0:
            play('spelltome.wav')
        else:
            play('tryagain.wav')
        play(f'words/{word}.wav', wait=False)
        munched_word = munch(word, fraction=0.2, vowel_bias=0.8)
        print(f'Word #{i+1}: {munched_word}')
        guess = input('Spell this word: ' )
        if guess == word:
            score = score + len(word) - guess_num
            print(colored(figlet_standard.renderText('Good Job!'), 'green'))
            print(colored(f'{score=}\n','blue'))
            play(f'good.wav')
            break        
        else:
            print(colored('\tNot quite, please try again... :(','red'))
            play(f'bad.wav')

play(f'end.wav')
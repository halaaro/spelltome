import sounddevice as sd
import soundfile as sf
import time

fs = 44100
word_path = 'words'
word_seconds = 1.3
sentence_path = 'sentences'
sentence_seconds = 5

def record(filename, seconds):
    print('recording...', end='', flush=True)

    recording = sd.rec(int(seconds*fs), samplerate=fs, channels=1)

    sd.wait()
    print('done!')

    sf.write(filename, recording, samplerate=fs)

    return recording

def play(filename, wait=True):
    audio, samplerate = sf.read(filename)
    sd.play(audio, samplerate)
    if wait:
        sd.wait()

def record_word(word):
    filename = f'{word_path}/{word}.wav'
    record(filename, word_seconds)
    time.sleep(1)
    play(filename)

def record_sentence(word):
    filename = f'{sentence_path}/{word}.wav'
    record(filename, sentence_seconds)
    time.sleep(1)
    play(filename)

def main():
    while True:
        word = input("Enter word: ")
        time.sleep(1)
        record_word(word)

        #more = input("Record sentence? (Y/n) ")
        #if not (more == '' or more == 'Y' or more == 'y'): continue
        #time.sleep(1)
        #record_sentence(word)

if __name__ == '__main__':
    import sys
    args = sys.argv[1:]
    if args[0] == 'play':
        play(args[1])
    elif args[0] == 'record':
        record(args[1],float(args[2]))
    elif args[0] == 'recorder':
        main()


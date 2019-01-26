import markovify
import sys
import lyricsgenius
import os

genius = lyricsgenius.Genius("4jhbha5yph1BCGNuTLVnfXl05CeUJConx4VsrqAk5O5dUiQqADdwnZ4PcSY48a9Q")
def mark(file):
    with open(file) as f:
        text = f.read()
    return markovify.Text(text, state_size=1)


def createSong(file, verse, bridge, chorus):
    model = mark(file)
    corus = ["\n"]
    for i in range(chorus):
        corus.append(model.make_sentence())
        #print (model.make_sentence())
    bidge = ["\n"]
    for i in range(bridge):
        bidge.append(model.make_sentence())
    verse1 = ["\n"]
    for i in range(verse):
        verse1.append(model.make_sentence())
    verse2 = ["\n"]
    for i in range(verse):
        verse2.append(model.make_sentence())
    print ('\n'.join(corus))
    #print ('\n')
    print ('\n'.join(verse1))
    print ("\n".join(bidge))
    #print ("\n")
    print ("\n".join(corus))
    #print ("\n")
    print ("\n".join(verse2))
    #print ("\n")
    print ("\n".join(bidge))
    print ("\n".join(corus))

def scrapeLyrics(artist, lyrics):
    art = lyrics.search_artist(artist, max_songs=15)
    art.save_lyrics(filename = artist+'.txt', format_='txt')
    return artist +'.txt'

if len(sys.argv) < 2:
    name = 'xxxtentacion.txt'
elif sys.argv[1] + '.txt' not in os.listdir():
    name = scrapeLyrics(sys.argv[1], genius)
else:
    name = sys.argv[1] + '.txt'
createSong(name, 8, 2, 4)

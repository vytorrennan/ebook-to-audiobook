from os import system
from slugify import slugify
from bs4 import BeautifulSoup
import ebooklib
from ebooklib import epub


ebookLocation = "./algoritms.epub"
quality = "medium"
language = "en_US"
voice = "joe"


def chapterToString(chapter):
    soup = BeautifulSoup(chapter.get_body_content(), "html.parser")
    text = [p.get_text() for p in soup.find_all("p")]
    return (" ".join(text)).replace(";", "").replace('"', '\\"')


book = epub.read_epub(ebookLocation)
chapters = list(book.get_items_of_type(ebooklib.ITEM_DOCUMENT))

chapterStrings = []
for c in chapters:
    chapterStrings.append(chapterToString(c))

#text = open("text.txt", "r").read()
currentPart = 0
totalOfParts = len(chapterStrings) - 1
for text in chapterStrings:
    currentPart = currentPart + 1
    if currentPart == totalOfParts:
        text = text + ". ESTE É O FIM DO TEXTO."
    filename = f"part{currentPart}"

    system(f"echo '{text}' | piper \
  --model {language}-{voice}-{quality} \
  --output_file audiobook/{filename}.wav")

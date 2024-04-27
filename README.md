# ebook-to-audiobook
Turn your EPUB ebooks into audiobooks

---

#### *In the futere the script will have an interface*
#### *Still in development*

---
### How it works

The app reads the epub with the ebooklib library and uses the fast [piper](https://github.com/rhasspy/piper) library to turn every part of it into an audiobook using an AI voice


### How to use the script

- Install all the requirements with:
```pip install -r requirements.txt```

- The first variable in the script is called "ebookLocation". Change it to the location of your epub file

- Then just execute the script with:
```python textToSpeech.py```

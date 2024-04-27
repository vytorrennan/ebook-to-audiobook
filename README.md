# ebook-to-audiobook
Turn your EPUB ebooks into audiobooks

---

#### *Still in development*
#### *In the futere the script will have an interface*

---
### How it works

The app reads the epub with the ebooklib library and uses the fast [piper](https://github.com/rhasspy/piper) library to turn every part of it into an audiobook using an AI voice


### How to use the script

- Install all the requirements with:
```pip install -r requirements.txt```

- The first variable in the script is called "ebookLocation". Change it to the location of your epub file

- You can also change a some other configurations like *quality, language and the voice*, these configs are right bellow the "ebooklocation", you can check all the possible options [here](https://github.com/rhasspy/piper/blob/master/VOICES.md), just change the variables to the specific config and it will automatically download everything it needs

- Then just execute the script with:
```python textToSpeech.py```

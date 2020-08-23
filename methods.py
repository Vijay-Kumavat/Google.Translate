from googletrans import Translator,LANGUAGES
# print(LANGUAGES)

class Mytranslator :
    def __init__(self):
        self.langs=list(LANGUAGES.values())
    
    def run(self,txt='Type text here...',src='english',dest='hindi'):
        self.translator=Translator()
        self.txt=txt
        self.src=src
        self.dest=dest
        try:
            self.translated=self.translator.translate(self.txt,src=self.src,dest=self.dest)
        except:
            self.translated=self.translator.translate(self.txt)
        self.ttext=self.translated.text
        return self.ttext
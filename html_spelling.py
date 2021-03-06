import fileinput
import enchant
from enchant.tokenize import get_tokenizer
from enchant.tokenize import HTMLChunker
__metaclass__=type

class HTMLSpellChecker():
	def __init__(self, lang='en_US'):
		"""
		Setup tokenizer..
		Create a new tokenizer based on lang.
		This lets us skip the HTML and only care
		about our contents
		"""
		self.lang=lang
		self._dict=enchant.Dict(self.lang)
		self._tk=get_tokenizer(self.lang, chunkers=(HTMLChunker,))

	def __call__(self, line):
		for word, off in self._tk(line):
			if not self._dict.check(word):
				yield word, self._dict.suggest(word)

if __name__=='__main__':
	try:
		check=HTMLSpellChecker()
		for line in fileinput.input():
			for word, suggestions in check(line):
				print("error on line %d (%s) in file %s." % (fileinput.filelineno(), word, fileinput.filename()))
				print("did you mean %s? " % ', '.join(suggestions))
	except :
		pass
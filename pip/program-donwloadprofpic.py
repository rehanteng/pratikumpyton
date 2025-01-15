from googletrans import Translator
tl = Translator()

text = input("masukan teks : ")
result = tl.translate(text, dest='en')
print(result.text)
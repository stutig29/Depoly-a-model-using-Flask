
import spacy 
  
# Load English tokenizer, tagger,  
# parser, NER and word vectors 
nlp = spacy.load("en_core_web_sm") 
   
def pos_tag(data):
	text = str(data)
	doc = nlp(text)
	t= []
	# Token and Tag 
	for token in doc: 
  		t.append([token, token.pos_]) 
  
	# You want list of Verb tokens 
	#print("Verbs:", [token.text for token in doc if token.pos_ == "VERB"]) 
	return t

if __name__=="__main__":
	#text = ("""My name is Shaurya Uppal.
	#I enjoy writing articles on GeeksforGeeks checkout 
	#my other article by going to my profile section.""") 

	text = "I am Stuti."
	print(pos_tag(text))
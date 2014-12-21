import random
def converse():
	while(True):
		this = raw_input("YOU: ")
		print ""
		print "QUINN: " + conversationTree(this)
		print ""
	
	
	
def conversationTree(input):
	g = open("greetings.txt","r")
	eq = open("emotional_questions.txt","r")
	er = open("emotional_response.txt", "r")
	ynq = open("yes_no_questions.txt","r")
	ynr = open("yesno_response.txt","r")
	c = open("certainty.txt","r")

	greetings = g.readlines()
	emotionalq = eq.readlines()
	emotionalr = er.readlines()
	yesNoq = ynq.readlines()
	yesNor = ynr.readlines()
	certainty = c.readlines()

#stereotypically, a conversation will start with some kind of greeting		
	for line in greetings:
		if input in line:
			response = random.choice(greetings).strip("\n\r")
			return response

#Questions are either emotional, factual, or true/false (yes or no)			
	if "?" in input:
		input = input.strip("?")
		
		#if it's an emotional question, respond with an emotion
		for line in emotionalq:
			line = line.strip("\n\r")
			if line in input:
				response = "I'm "+random.choice(certainty).strip("\n\r")+" "+random.choice(emotionalr).strip("\n\r")
				return response
				
		#if it's a yes or no, respond with yes or no
		for line in yesNoq:
			line = line.strip("\n\r")
			if line in input:
				response = random.choice(yesNor).strip("\n\r")
				return response
				
				
	return "Punctuation matters... or you're a terrible conversationalist"
				
				


if __name__ == "__main__":
    converse()
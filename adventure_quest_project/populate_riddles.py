import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'adventure_quest_project.settings')
import django
django.setup()
from adventureQuest.models import Riddle
from adventureQuest.models import Quest

def populate():

	# Test_Quest Riddle
	add_riddle(question="When you have me you want to share me, if you share me you no longer have me.....what am I?",answer="secret",instruction="This question is just a fun riddle to do while you have your first drink",hint="You might want to whisper me...",quest_name="test_quest",question_id=0)

	add_riddle(question="What gets wetter as it dries.....?", answer="towel",instruction="This question is just a fun riddle to do while you have your first drink",hint="Starts with 'T'", quest_name="test_quest", question_id=1)

	add_riddle(question="When I am born, I fly, When I am alive, I lie, When I die I run....what am I?", answer="snowflake",instruction="This question is just a fun riddle to do while you have your first drink",hint="I usually only seen in the winter",  quest_name="test_quest", question_id=2)

	add_quest(name="test_quest", description = "Fun quest", difficulty = 5, age_limit = 10 )

	add_quest(name="Finnieston_Quest", description="Fun quest starting in Finnieston that takes you through some of the 'trendiest' bars in Glasgow.", difficulty=3, age_limit=18)

	add_riddle(
		question="What is greater than God, more evil than the devil, the poor have it, the rich need it, and if you eat it, you'll die?",
			   answer="nothing", instruction="This question is just a fun riddle to do while you have your first drink",
			   hint="abstract", quest_name="Finnieston_Quest", question_id=0)

	add_riddle(
		question="What has a head and a tail but no body?",
		answer="A coin", instruction="This question is just a fun riddle to do while you have your first drink",
		hint="The Queen", quest_name="Finnieston_Quest", question_id=1)

	add_riddle(
		question="What is behind the woman in the painting of the battle?",
		answer="A lizard", instruction="You will have to explore to find the answer",
		hint="It's by the bathroom", quest_name="Finnieston_Quest", question_id=2)

	add_riddle(
		question="What is the tallest mountain in the United Kingdom!",
		answer="Ben Nevis", instruction="The answer to this riddle is your next destination",
		hint="Don't go to the actual mountain you wally!", quest_name="Finnieston_Quest", question_id=3)

	add_riddle(
		question="How many mirrors are there in the whole pub?",
		answer="8", instruction="You will have to explore to find the answer",
		hint="Don't go to the actual mountain you wally!", quest_name="Finnieston_Quest", question_id=4)

	add_riddle(
		question="Who makes it, has no need of it. Who buys it has no use for it. Who uses it can neither see nor feel it. What is it?",
		answer="A coffin", instruction="Riddle me this!",
		hint="claustrophobics hate these!", quest_name="Finnieston_Quest", question_id=5)

	add_riddle(
		question="Count how many people are in the paintings",
		answer="21", instruction="You will have to explore to find the answer",
		hint="It's a number", quest_name="Finnieston_Quest", question_id=6)

	add_riddle(
		question="Count how many people are in the paintings",
		answer="21", instruction="You will have to explore to find the answer",
		hint="It's a number", quest_name="Finnieston_Quest", question_id=6)

	add_riddle(
		question="The name of the next bar is an anagram of a supermarket and what you do on a chair",
		answer="Distill", instruction="answer the two questions and then rearrange the letters to find the name of the next bar",
		hint="Lidl", quest_name="Finnieston_Quest", question_id=7)

	add_riddle(
		question="How many rums do they serve here?",
		answer="30", instruction="Find out the answer",
		hint="Ask the bar staff", quest_name="Finnieston_Quest", question_id=8)

	add_riddle(
		question="How old is this bar?",
		answer="5", instruction="Find out the answer",
		hint="Ask the bar staff", quest_name="Finnieston_Quest", question_id=9)

	add_riddle(
		question="What kind of room has no doors or windows?",
		answer="A mushroom", instruction="Riddle me this!",
		hint="pun", quest_name="Finnieston_Quest", question_id=10)

	add_riddle(
		question="What can travel around the world while staying in a corner?",
		answer="A stamp", instruction="Riddle me this!",
		hint="The Queen", quest_name="Finnieston_Quest", question_id=11)


	add_riddle(
		question="The next bar is a place for 'Big white blokes'",
		answer="The Big Lebowski", instruction="It's an annagram!",
		hint="Cool Dudes go here", quest_name="Finnieston_Quest", question_id=12)

	add_riddle(
		question="'I can't blow that far'",
		answer="The bunny", instruction="Riddle me this!",
		hint="Drinks menu", quest_name="Finnieston_Quest", question_id=13)

	add_riddle(
		question="What breaks when its name is spoken?",
		answer="Silence", instruction="Riddle me this!",
		hint="Ssh", quest_name="Finnieston_Quest", question_id=14)

	add_riddle(
		question="How many pictures of the Dude are there?",
		answer="3", instruction="You will have to explore to find the answer",
		hint="there's some in the toilets", quest_name="Finnieston_Quest", question_id=15)

	add_riddle(
		question="Shared between two, \nMost often to woo,\nSometimes hot and sometimes cold,\nThe beginning of us all,\nYoung an old.",
		answer="A kiss", instruction="Riddle me this!",
		hint="mwah", quest_name="Finnieston_Quest", question_id=16)

	add_riddle(
		question="Which country has more cellphones than there are people in the U.S.?",
		answer="China", instruction="Riddle me this!",
		hint="Asia", quest_name="Finnieston_Quest", question_id=17)

	add_riddle(
		question="The next bar is an anagram of the previous two ansers!",
		answer="Chinaskis", instruction="Riddle me this!",
		hint="one of the words stays in the same order", quest_name="Finnieston_Quest", question_id=18)

	add_riddle(
		question="How many horses can you find?",
		answer="5", instruction="You will have to explore to find the answer",
		hint="Check downstairs", quest_name="Finnieston_Quest", question_id=19)

	add_riddle(
		question="When I am alive you sing, when I die you clap your hands. What am I?",
		answer="candles", instruction="Riddle me this!",
		hint="for he's a jolly good fellow!", quest_name="Finnieston_Quest", question_id=20)

	add_riddle(
		question="Cut my skin out, I won't cry! But you will. What am I?",
		answer="an onion", instruction="Riddle me this!",
		hint="I'm making a lasagne...for one.", quest_name="Finnieston_Quest", question_id=21)

	add_riddle(
		question="What tastes better than it smells?",
		answer="a tongue", instruction="Riddle me this!",
		hint="It's pink", quest_name="Finnieston_Quest", question_id=22)

	add_riddle(
		question="Relaxing with 'incense' makes me feel very 'lazy'",
		answer="nice n sleazy", instruction="The answer will tell you your next location",
		hint="It's an anagram", quest_name="Finnieston_Quest", question_id=23)

	add_riddle(
		question="When is 99 more than 100?",
		answer="on a microwave", instruction="Riddle me this!",
		hint="I live in the kitchen", quest_name="Finnieston_Quest", question_id=24)

	add_riddle(
		question="What asks but never answers?",
		answer="an owl", instruction="Riddle me this!",
		hint="whoo-whoo", quest_name="Finnieston_Quest", question_id=25)

	add_riddle(
		question="Feed me I will survive, give me a drink and I will die",
		answer="fire", instruction="Riddle me this!",
		hint="calcifer", quest_name="Finnieston_Quest", question_id=26)

	add_riddle(
		question="What runs but never gets tired",
		answer="water", instruction="Riddle me this!",
		hint="wet", quest_name="Finnieston_Quest", question_id=27)

	add_riddle(
		question="Where is the final destination?",
		answer="firewater", instruction="The last two answers should let you know your next location",
		hint="earthwind", quest_name="Finnieston_Quest", question_id=28)

	add_riddle(
		question="Find the secret message",
		answer="I have riddle brain", instruction="You'll have to explore",
		hint="behind the bar", quest_name="Finnieston_Quest", question_id=29)

	add_riddle(
		question="What loses its head in the morning and gets it back at night?",
		answer="a pillow", instruction="Riddle me this!",
		hint="not technically 'its' head", quest_name="Finnieston_Quest", question_id=30)

	add_riddle(
		question="What has a single eye but cannot see?",
		answer="a needle", instruction="Riddle me this!",
		hint="Doe a dear a female deer...", quest_name="Finnieston_Quest", question_id=31)

	add_riddle(
		question="What is the centre of gravity?",
		answer="V", instruction="Riddle me this!",
		hint="literal", quest_name="Finnieston_Quest", question_id=32)

	add_riddle(
		question="OMG THE BIG FINALE IT SHOULD BE MORE EXCITING",
		answer="ADVENTUREQUEST", instruction="Riddle me this!",
		hint="team name", quest_name="Finnieston_Quest", question_id=33)

def add_riddle(question, answer, instruction, hint, quest_name, question_id):
	r=Riddle.objects.get_or_create(question=question, answer=answer, instruction=instruction, hint=hint,  quest_name=quest_name, question_id=question_id)[0]
	r.save()
	return r
	
	
def add_quest(name, description, difficulty, age_limit):
	q=Quest.objects.get_or_create(name=name, description=description, difficulty=difficulty, age_limit=age_limit)[0]
	q.save()
	return q


	
# Start Execution
if __name__ == '__main__':
	print("Starting AdventureQuest population script...")
	populate()
	
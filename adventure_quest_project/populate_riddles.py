import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'adventure_quest_project.settings')
import django
django.setup()
from adventureQuest.models import Riddle
from adventureQuest.models import Quest

def populate():

	# Test_Quest Riddle
	add_riddle(question="When you have me you want to share me, if you share me you no longer have me.....what am I?", answer="secret", quest_name="test_quest", question_id=0)
	add_riddle(question="What gets wetter as it dries.....?", answer="towel", quest_name="test_quest", question_id=1)
	add_riddle(question="When I am born, I fly, When I am alive, I lie, When I die I run....what am I?", answer="snowflake", quest_name="test_quest", question_id=2)
	add_quest(name="test_quest", description = "Fun quest", difficulty = 5, age_limit = 10 )

	# Real Riddle



def add_riddle(question, answer, quest_name, question_id):
	r=Riddle.objects.get_or_create(question=question, answer=answer, quest_name=quest_name, question_id=question_id)[0]
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
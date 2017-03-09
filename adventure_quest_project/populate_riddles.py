import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'adventure_quest_project.settings')


django.setup()

from rango.models import Riddle
from rango.models import Quest

def populate():

	test_riddles = [
		{"question":"When you have me you want to share me, if you share me you no longer have me.....what am I?",
		"answer": "secret", "quest_name":"test_quest", "question_id":1},
		{"question":"What gets wetter as it dries.....?",
		"answer": "towel", "quest_name":"test_quest", "question_id":2},
		{"question":"When I am born, I fly, When I am alive, I lie, When I die I run....what am I?",
		"answer": "snow flake", "quest_name":"test_quest", "question_id":3}]
		
		
	
	testerquest =[
		{"name":"test_quest", "description":"A fun test quest", "difficulty":"2", "age_limit":10}]

# Going through the riddle dictionary
	for riddle, riddle_data in test_riddles.iteritems():
		r=add_riddle(riddle.riddle_data["question"],riddle_data["answer"],riddle_data["id"],riddle_data["question_id"])
		
	# Going through the quest dictionary
	for quest, quest_data in testerquest.iteritems():
		q=add_quest(quest.quest_data["name"],quest_data["description"],quest_data["difficulty"],quest_data["age_limit"])
	

def add_riddle(question, answer, id, question_id):
	r=Riddle.objects.get_or_create(question=question, answer=answer, id=id, question_id=question_id)[0]
	r.save()
	return r
	
	
def add_quest(name, description, difficulty, age_limit):
	q=Riddle.objects.get_or_create(name=name, description=description, difficulty=difficulty, age_limit=age_limit)[0]
	q.save()
	return q


	
# Start Execution
if __name__ == '__main__':
	print("Starting AdventureQuest population script...")
	populate()
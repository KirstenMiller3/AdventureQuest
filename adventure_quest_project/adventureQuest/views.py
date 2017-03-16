from django.shortcuts import render
from django.http import HttpResponse
from adventureQuest.forms import UserForm, UserProfileForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from adventureQuest.forms import RiddleForm
from adventureQuest.models import Quest, Riddle, UserProfile


# Create your views here.

# The home page
def index(request):
	return render(request, 'adventureQuest/index.html')

# About page for one quest maybe we should make this generalizable the way pages were in rango as seems silly to have to
# make a new one of these for each quest. Same for riddle pages!!!!!!
def quest1_about(request):
    return render(request, 'adventureQuest/quest1_about.html')


# riddle page
def answer_riddle(request):
    form = RiddleForm()

    if request.method == 'POST':
        form = riddle(request.POST)
        if form.is_valid():
            # If valid save to database???? not sure if we should be doing that with riddle answers?
            form.save(commit=True)
            # instead of saving we need a check to see if answer was correct
            return index(request)
        else:
            print(form.errors)

    return render(request, 'adventureQuest/test_quest.html')


def register(request):
    # A boolean value for telling the template
    # whether the registration was successful.
    # Set to False initially. Code changes value to
    # True when registration succeeds.
    registered = False

    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        # Note that we make use of both UserForm and UserProfileForm.
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        # If the two forms are valid...
        if user_form.is_valid() and profile_form.is_valid():
            # Save the user's form data to the database.
            user = user_form.save()

            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.
            user.set_password(user.password)
            user.save()

            # Now sort out the UserProfile instance.
            # Since we need to set the user attribute ourselves,
            # we set commit=False. This delays saving the model
            # until we're ready to avoid integrity problems.
            profile = profile_form.save(commit=False)
            profile.user = user

            # Did the user provide a profile picture?
            # If so, we need to get it from the input form and
            # put it in the UserProfile model.
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            # Now we save the UserProfile model instance.
            profile.save()

            # Update our variable to indicate that the template
            # registration was successful.
            registered = True
        else:
            # Invalid form or forms - mistakes or something else?
            # Print problems to the terminal.
            print(user_form.errors, profile_form.errors)
    else:
        # Not a HTTP POST, so we render our form using two ModelForm instances.
        # These forms will be blank, ready for user input.
        user_form = UserForm()
        profile_form = UserProfileForm()

    # Render the template depending on the context.
    return render(request,
                  'adventureQuest/register.html',
                  {'user_form': user_form,
                   'profile_form': profile_form,
                   'registered': registered})




def my_account(request):
    context_dict = {'hi'}
    if request.user.is_authenticated():
        name = request.user.username
        #pic = request.user.picture


    return render(request, 'adventureQuest/my_account.html',context_dict)





def user_login(request):
    context_dict = {}
    # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':
        # Gather the username and password provided by the user.
        # This information is obtained from the login form.
        # We use request.POST.get('<variable>') as opposed
        # to request.POST['<variable>'], because the
        # request.POST.get('<variable>') returns None if the
        # value does not exist, while request.POST['<variable>']
        # will raise a KeyError exception.
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Use Django's machinery to attempt to see if the username/password
        # combination is valid - a User object is returned if it is.
        user = authenticate(username=username, password=password)

        # If we have a User object, the details are correct.
        # If None (Python's way of representing the absence of a value), no user
        # with matching credentials was found.
        if user:
            # Is the account active? It could have been disabled.
            if user.is_active:
                # If the account is valid and active, we can log the user in.
                # We'll send the user back to the homepage.
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                # An inactive account was used - no loggin in!
                return HttpResponse("Your adventureQuest account is disabled.")
        else:
            # Bad login details were provided. So we can't log the user in.
            print("Invalid login details: {0}, {1}".format(username, password))
            context_dict['invalid_deets'] = True
            return render(request, 'adventureQuest/login.html', context_dict)

    # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.
    else:
        # No context variables to pass the template system, hence the
        # blank dictionary object...
        return render(request, 'adventureQuest/login.html', {})



@login_required
def restricted(request):
    return render(request, 'adventureQuest/restricted.html')


# Use the login_required() decorator to ensure only those logged in can access the view
@login_required
def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)
    # Take the user back to the homepage.
    return HttpResponseRedirect(reverse('adventureQuest./index.html'))


# test_Quest view
def quest(request):
    global name
    name = 'test_quest'
    return render(request, 'adventureQuest/test_quest.html')

import json
ridQID = 0
ridAID = 0
correctNo = 0
name = ''

def quest_ajax(request):

    # Set the global variables
    global ridAID
    global ridQID
    global correct
    global correctNo
    global name



    #quest = Quest.name

    # count how many riddles in this quest
    listRiddles = list(Riddle.objects.filter(quest_name='test_quest'))
    numberRiddles= len(listRiddles)
    print('This is the number of riddles'+str(numberRiddles)+' '+name)
    print(name)

    # Get the user answer
    user_answer = request.GET.get('answer')

    # Set the current question and answer from the database
    for row in Riddle.objects.filter(quest_name='test_quest', question_id=ridAID):
        textAnswer = row.answer
        print(row.answer)

    for row in Riddle.objects.filter(quest_name='test_quest', question_id=ridQID):
        textQuestion = row.question
        print(row.question)

    # Create Response data vairable
    response_data = {}

# If the users answer is correct then get the next question from the database unless this is the last question
    if correctNo < numberRiddles:
        if user_answer == textAnswer:
            ridQID += 1
            correctNo += 1
            ridAID += 1
            for row in Riddle.objects.filter(quest_name='test_quest', question_id=ridQID):
                textQuestion = row.question
                print(row.question)
                response_data['answer'] = textQuestion
            if correctNo == numberRiddles:
                response_data['answer'] = 'Congratualtions you finished the quest!'
                ridQID = 0
                ridAID = 0
                correctNo = 0
    # If the user answer is incorrect
        else:
            for row in Riddle.objects.filter(quest_name='test_quest', question_id=ridQID):
                textQuestion = row.question
            response_data['answer'] = 'try again: '+textQuestion
    # If the users answer is
     #   elif correct == True:
         #   response_data['answer'] = 'try again: ' + textQuestion

    return HttpResponse(json.dumps(response_data), content_type="application/json")


	
	
	


	
	
	
	
	
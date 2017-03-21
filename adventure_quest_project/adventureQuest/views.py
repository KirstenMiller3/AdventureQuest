
from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponse

from django.shortcuts import render
from adventureQuest.forms import UserForm, UserProfileForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from adventureQuest.models import Quest, Riddle
from django.shortcuts import redirect
from adventureQuest.models import Quest, Riddle, UserProfile, UserScores
from django.core.signals import request_finished
from .forms import PostForm
from .models import Quest, Riddle, UserProfile, Post


# Create your views here.

# The home page
def index(request):
    return render(request, 'adventureQuest/index.html')


# The about page for the Finnieston Quest.
def finnieston_about(request):
    context_dict = {}
    for row in Quest.objects.filter(name="finnieston_quest"):
        context_dict['descr'] = row.description
        context_dict['age_limit'] = row.age_limit
        context_dict['difficulty'] = row.difficulty
        context_dict['start'] = row.start_point
        context_dict['questurl'] = reverse(finnieston_quest)
        context_dict['questmappos'] = "55.868273, -4.292110" 
    check_url(request)
    return render(request, 'adventureQuest/finnieston_about.html', context_dict)


# The about page for the Glasgow University quest.
def glasgow_uni_about(request):
    context_dict = {}
    for row in Quest.objects.filter(name="glasgow_uni_quest"):
        context_dict['descr'] = row.description
        context_dict['age_limit'] = row.age_limit
        context_dict['difficulty'] = row.difficulty
        context_dict['start'] = row.start_point
        context_dict['questurl'] = reverse(glasgow_uni_quest)
        context_dict['questmappos'] = "55.871950, -4.288233"
        
    check_url(request)
    return render(request, 'adventureQuest/glasgow_uni_about.html', context_dict)


# The about page for the Southside quest.
def southside_about(request):
    context_dict = {}
    for row in Quest.objects.filter(name="southside_quest"):
        context_dict['descr'] = row.description
        context_dict['age_limit'] = row.age_limit
        context_dict['difficulty'] = row.difficulty
        context_dict['start'] = row.start_point
        context_dict['questurl'] = reverse(southside_quest)
        context_dict['questmappos'] = "55.850538, -4.259042"
    check_url(request)
    return render(request, 'adventureQuest/southside_about.html', context_dict)


# The about page for the City Centre quest.
def city_centre_about(request):
    context_dict = {}
    for row in Quest.objects.filter(name="city_centre_quest"):
        context_dict['descr'] = row.description
        context_dict['age_limit'] = row.age_limit
        context_dict['difficulty'] = row.difficulty
        context_dict['start'] = row.start_point
        context_dict['questurl'] = reverse(city_centre_quest)
        context_dict['questmappos'] = "55.863422, -4.252970"
    check_url(request)
    return render(request, 'adventureQuest/city_centre_about.html', context_dict)


# The about page for the Kids quest.
def kids_about(request):
    context_dict = {}
    for row in Quest.objects.filter(name="kids_quest"):
        context_dict['descr'] = row.description
        context_dict['age_limit'] = row.age_limit
        context_dict['difficulty'] = row.difficulty
        context_dict['start'] = row.start_point
        context_dict['questurl'] = reverse(kids_quest)
        context_dict['questmappos'] = "55.868786, -4.290196"
    check_url(request)
    return render(request, 'adventureQuest/kids_about.html', context_dict)


# The about page for the ?MyStErY? quest.
def mystery_about(request):
    context_dict = {}
    for row in Quest.objects.filter(name="mystery_quest"):
        context_dict['descr'] = row.description
        context_dict['age_limit'] = row.age_limit
        context_dict['difficulty'] = row.difficulty
        context_dict['start'] = row.start_point
        context_dict['questurl'] = reverse(mystery_quest)
        context_dict['questmappos'] = "55.874692, -4.292962"
    check_url(request)
    return render(request, 'adventureQuest/mystery_about.html', context_dict)


# The view for the congratulations page
def congratulations(request):
    # In this view we need to add their high score to the correct user field!!
    return render(request, 'adventureQuest/congratulations.html')


# The view for the registration page.
def register(request):
    # Tells us if registration was successful or not.
    registered = False
    # It's a form so POST
    if request.method == 'POST':
        # Try to get form data from users
        #user_form = UserForm(data=request.POST)
        #profile_form = UserProfileForm(data=request.POST)
        user_form = UserForm(request.POST or None, request.FILES or None)
        profile_form = UserProfileForm(request.POST or None, request.FILES or None)
        # If the two forms are valid:
        if user_form.is_valid() and profile_form.is_valid():
            # Save the user's form data to the database.
            user = user_form.save()

            # Hash the users password and then update the user object.
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
            print(str(request.FILES))
            if 'picture' in request.FILES:
                picture = request.FILES.get('picture', False)
                print("Entered")
                profile.picture = picture

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
    context_dict = {}
    user = request.user
    #if request.user.is_authenticated():
    #name = request.user.username
    #pic = request.user.picture
    for row in UserProfile.objects.filter(user=user):
        context_dict['user'] = row.picture
        context_dict['pic'] = str(row.picture)



        context_dict['mystery_quest'] = 'n/a'
        context_dict['finnieston_quest'] = 'n/a'
        context_dict['glasgow_uni_quest'] = 'n/a'
        context_dict['southside_quest'] = 'n/a'
        context_dict['city_centre_quest'] = 'n/a'
        context_dict['kids_quest'] = 'n/a'

    for row in UserScores.objects.filter(user=request.user):
        context_dict[row.quest.name] = row.score




    return render(request, 'adventureQuest/my_account.html',context_dict)


# The view for login page.
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


# THINK THIS CAN BE DELETED
@login_required
def restricted(request):
    return render(request, 'adventureQuest/restricted.html')


# Use the login_required() decorator to ensure only those logged in can access the view
@login_required
def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)
    # Take the user back to the homepage.
    return HttpResponseRedirect(reverse('index'))

#Hall of Fame view from which quest can be selected
def hall_of_fame(request):
    return render(request, 'adventureQuest/hall_of_fame.html')


#add login_required
def post_create(request):

    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))

    form = PostForm(request.POST or None, request.FILES or None)

    myHint = None

    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user

        for quest_post in Quest.objects.filter(name=instance.quest):
            myQuest = quest_post

        for score_row in UserScores.objects.filter(user=request.user, quest=myQuest):
            myHint = score_row.score

        if myHint != None:
            instance.hints = myHint
        instance.save()

        # message success
        messages.success(request, "Post was created")
        return HttpResponseRedirect(reverse('post_list'))

    context = {
        "form": form,
    }
    return render(request, 'adventureQuest/post_form.html', context)


def post_list(request):
    objects_post = Post.objects.order_by('hints')[:100]
   # print(objects_post[0].title)

    context = {
        "object_list": objects_post,
        "title": "List",
       # "page_request_var": page_request_var
    }
    return render(request, 'adventureQuest/post_list.html', context)


# test_Quest view
def mystery_quest(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))
    else:
        get_current_quest(request)
        return render(request, 'adventureQuest/mystery_quest.html')

def finnieston_quest(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))
    else:
        get_current_quest(request)
        return render(request, 'adventureQuest/finnieston_quest.html')

def glasgow_uni_quest(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))
    else:
        get_current_quest(request)
        return render(request, 'adventureQuest/glasgow_uni_quest.html')


def southside_quest(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))
    else:
        get_current_quest(request)
        return render(request, 'adventureQuest/southside_quest.html')


def city_centre_quest(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))
    else:
        get_current_quest(request)
        return render(request, 'adventureQuest/city_centre_quest.html')


def kids_quest(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))
    else:
        get_current_quest(request)
        return render(request, 'adventureQuest/kids_quest.html')

# Method that would reset the quest if the user leaves half way through...not working, maybe need a quit button
def check_url(request):
    request.session['riddleQuestionID'] = 0
    request.session['riddleAnswerID'] = 0
    request.session['riddleCorrectNo'] = 0
    request.session['riddleCorrectNo'] = 0
    request.session['numberHint'] = 0
    request.session['questName'] = 0
    #original_path = '/adventureQuest/quest_ajax/'

   # print('This is the url that is compared too' + request.get_full_path(request))
   # if original_path not in request.get_full_path(request):
     #   print('TEST!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')



# incrementors
def quest_cookies(request, inc, hint):
    riddleQuestionID = int(get_server_side_cookie(request,  'riddleQuestionID', '0'))
    if inc == True:
        riddleQuestionID +=1
    request.session['riddleQuestionID'] = riddleQuestionID

    riddleAnswerID = int(get_server_side_cookie(request, 'riddleAnswerID', '0'))
    if inc == True:
        riddleAnswerID += 1
    request.session['riddleAnswerID'] = riddleAnswerID

    riddleCorrectNo = int(get_server_side_cookie(request, 'riddleCorrectNo', '0'))
    if inc == True:
        riddleCorrectNo += 1
    request.session['riddleCorrectNo'] = riddleCorrectNo

    numberHint = int(get_server_side_cookie(request, 'numberHint', '0'))
    if hint == True:
        numberHint += 1
    request.session['numberHint'] = numberHint

    numberRiddles = int(get_server_side_cookie(request, 'numberRiddles', '0'))
    request.session['numberRiddles'] = numberRiddles

# server side cookie
def get_server_side_cookie(request, cookie, default_val = None):
    val = request.session.get(cookie)
    if not val:
        val = default_val
    return val


def get_current_quest(request):
    current_path = request.get_full_path()
    questName ="".join(current_path.split('/')[2:])
    trimmed = questName
    print("HEEEEEELOOOOOO" + trimmed)
    quest_name = str(get_server_side_cookie(request, 'questName', trimmed))
    request.session['questName'] = quest_name

def add_score(user, quest, score):
	q=UserScores.objects.get_or_create(user=user, quest=quest, score=score)[0]
	q.save()
	return q

import json
def quest_ajax(request):
    response_data = {}
    questName = request.session['questName']
    print("HEY" + questName)
    # Set session variables
    quest_cookies(request, False, False)
    ridQID = request.session['riddleQuestionID']
    ridAID = request.session['riddleAnswerID']
    correctNo = request.session['riddleCorrectNo']

    response_data['currentQ'] = ridQID

    # count how many riddles in this quest
    listRiddles = list(Riddle.objects.filter(quest_name=questName))
    numberRiddles= len(listRiddles)
    response_data['noRiddles'] = numberRiddles
    print('This is the number of riddles'+str(numberRiddles))
    print('This is the question ID' + str(ridQID) + 'This is the answer ID' + str(ridAID))
    print('this is the quest name: '+questName)

    # Get the user answer

    input_answer = request.GET.get('answer')

    if input_answer != None:
        user_answer = input_answer.lower()
        print('this should be the answer in lower case'+user_answer)
    else:
        user_answer = ''

    # Set the current question and answer from the database
    for row in Riddle.objects.filter(quest_name=questName, question_id=ridAID):
        textAnswer = row.answer
        print(row.answer)

    for row in Riddle.objects.filter(quest_name=questName, question_id=ridQID):
        textQuestion = row.question
        textHint = row.hint
        textInstruction = row.instruction
        print(row.question)

    # Create Response data vairable

    # Hint file
    if request.GET.get('click', False):
        print('testing button')
        response_data['hint'] = textHint
        quest_cookies(request, False, True)
        no_hints = request.session['numberHint']
        response_data['hintNo'] = no_hints
        response_data['hint_available'] = 'false'
        print(no_hints)

    #response_data['instruction'] = textInstruction




# If the users answer is correct then get the next question from the database unless this is the last question
    if correctNo <= numberRiddles:
        print('************** '+str(correctNo))
        if textAnswer in user_answer:
            response_data['hint'] = 'Your hint will appear here....but remember you will loose 5 points for each hint!'
            quest_cookies(request, True, False)
            ridQID = request.session['riddleQuestionID']
            ridAID = request.session['riddleAnswerID']
            response_data['hint_available'] = 'true'
            correctNo = request.session['riddleCorrectNo']
            response_data['correct'] = True
            print('This should be True' + str(response_data['correct']))

            #Adding final score to the database
            if correctNo == numberRiddles:
                # get quest id
                id = Quest.objects.filter(name=questName).values('id')[0]['id']
                for quest_row in Quest.objects.filter(name=questName):
                    add_score(user=request.user,quest=quest_row, score=request.session['numberHint'])


            for row in Riddle.objects.filter(quest_name=questName, question_id=ridQID):
                textQuestion = row.question
                textAnswer = row.answer
                textInstruction = row.instruction
                print(row.question)
                print(row.answer)
                response_data['answer'] = textQuestion
                response_data['instruction'] = textInstruction



                        #somehowsave



        # If the user answer is incorrect
        else:
            for row in Riddle.objects.filter(quest_name=questName, question_id=ridQID):
                textQuestion = row.question
            response_data['answer'] = 'try again: '+textQuestion
            response_data['correct'] = False
            print('This should be false'+str(response_data['correct']))

    return HttpResponse(json.dumps(response_data), content_type="application/json")












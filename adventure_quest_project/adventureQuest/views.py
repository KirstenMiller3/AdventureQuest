from django.shortcuts import render
from django.http import HttpResponse
from adventureQuest.forms import UserForm, UserProfileForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from adventureQuest.forms import RiddleForm
from adventureQuest.models import Quest, Riddle, UserProfile
from django.core.signals import request_finished


from .forms import RiddleForm, PostForm
from .models import Quest, Riddle, UserProfile, Post


# Create your views here.

# The home page
def index(request):
    return render(request, 'adventureQuest/index.html')


def finnieston_about(request):
    check_url(request)
    return render(request, 'adventureQuest/finnieston_about.html')


def glasgow_uni_about(request):
    check_url(request)
    return render(request, 'adventureQuest/glasgow_uni_about.html')


def southside_about(request):
    check_url(request)
    return render(request, 'adventureQuest/southside_about.html')


def city_centre_about(request):
    check_url(request)
    return render(request, 'adventureQuest/city_centre_about.html')


def kids_about(request):
    check_url(request)
    return render(request, 'adventureQuest/kids_about.html')

# About page for one quest maybe we should make this generalizable the way pages were in rango as seems silly to have to
# make a new one of these for each quest. Same for riddle pages!!!!!!
def quest1_about(request):
    check_url(request)
    return render(request, 'adventureQuest/quest1_about.html')


def congratulations(request):
    # In this view we need to add their high score to the correct user field!!
    return render(request, 'adventureQuest/congratulations.html')



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
    context_dict = {}
    if request.user.is_authenticated():
        name = request.user.username
        #pic = request.user.picture

    for row in UserProfile.objects.all():
        context_dict['score1'] = row.quest1Score
        context_dict['score2'] = row.quest2Score
        context_dict['score3'] = row.quest3Score
        context_dict['score4'] = row.quest4Score
        context_dict['score5'] = row.quest5Score

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
    return HttpResponseRedirect(reverse('index'))

#Hall of Fame view from which quest can be selected
def hall_of_fame(request):
    return render(request, 'adventureQuest/hall_of_fame.html')


#add login_required
def post_create(request):
    form = PostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        # message success
        messages.success(request, "Post was created")
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "form": form,
    }
    return render(request, 'adventureQuest/post_form.html', context)

def post_list(request):
    objects_post = Post.objects.all()
    print(objects_post[0].title)
    # paginator = Paginator(queryset_list, 10)
    # page_request_var = "page"
    # page = request.GET(page_request_var)
    # try:
    #         queryset = paginator.page(page)
    # except PageNotAnInteger:
    #         # If not an int, deliver first page
    #         queryset = paginator.page(1)
    # except EmptyPage:
    #         # If page is out of range, deliver last page
    #         queryset = paginator.page(paginator.num_pages)


    context = {
        "object_list": objects_post,
        "title": "List",
       # "page_request_var": page_request_var
    }
    return render(request, 'adventureQuest/post_list.html', context)

# test_Quest view
def test_quest(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('adventureQuest/login.html'))
   # check_url(request)
    # Set up session variables
    get_current_quest(request)
    return render(request, 'adventureQuest/test_quest.html')


def finnieston_quest(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('adventureQuest/login.html'))
    get_current_quest(request)
    return render(request, 'adventureQuest/finnieston_quest.html')

def glasgow_uni_quest(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('adventureQuest/login.html'))
    get_current_quest(request)
    return render(request, 'adventureQuest/glasgow_uni_quest.html')


def southside_quest(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('adventureQuest/login.html'))
    get_current_quest(request)
    return render(request, 'adventureQuest/southside_quest.html')


def city_centre_quest(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('adventureQuest/login.html'))
    get_current_quest(request)
    return render(request, 'adventureQuest/city_centre_quest.html')


def kids_quest(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('adventureQuest/login.html'))
    get_current_quest(request)
    return render(request, 'adventureQuest/kids_quest.html')

# Method that would reset the quest if the user leaves half way through...not working, maybe need a quit button
def check_url(request):
    original_path = '/adventureQuest/quest_ajax/'
    print('This is the url that is compared too' + request.get_full_path(request))
    if original_path not in request.get_full_path(request):
        print('TEST!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
        request.session.flush()

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

import json
def quest_ajax(request):


    questName = request.session['questName']
    print("HEY" + questName)
    # Set session variables
    quest_cookies(request, False, False)
    ridQID = request.session['riddleQuestionID']
    ridAID = request.session['riddleAnswerID']
    correctNo = request.session['riddleCorrectNo']



    # count how many riddles in this quest
    listRiddles = list(Riddle.objects.filter(quest_name=questName))
    numberRiddles= len(listRiddles)
    print('This is the number of riddles'+str(numberRiddles))
    print('This is the question ID' + str(ridQID) + 'This is the answer ID' + str(ridAID))
    print('this is the quest name: '+questName)

    # Get the user answer
    user_answer = request.GET.get('answer')

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
    response_data = {}
    # Hint file
    if request.GET.get('click', False):
        print('testing button')
        response_data['hint'] = textHint
        quest_cookies(request, False, True)
        no_hints = request.session['numberHint']
        response_data['hintNo'] = no_hints
        response_data['hint_available'] = 'false'
        print(no_hints)

    response_data['instruction'] = textInstruction



# If the users answer is correct then get the next question from the database unless this is the last question
    if correctNo < numberRiddles:
        if user_answer == textAnswer:
            response_data['hint'] = 'Your hint will appear here....but remember you will loose 5 points for each hint!'
            quest_cookies(request, True, False)
            ridQID = request.session['riddleQuestionID']
            ridAID = request.session['riddleAnswerID']
            correctNo = request.session['riddleCorrectNo']
            response_data['hint_available'] = 'true'
            response_data['instruction']=textInstruction

            for row in Riddle.objects.filter(quest_name=questName, question_id=ridQID):
                textQuestion = row.question
                textAnswer = row.answer
                print(row.question)
                print(row.answer)
                response_data['answer'] = textQuestion
            if correctNo == numberRiddles:
                response_data['answer'] = 'Congratualtions you finished the quest!'
                request.session.flush()
    # If the user answer is incorrect
        else:
            for row in Riddle.objects.filter(quest_name=questName, question_id=ridQID):
                textQuestion = row.question
            response_data['answer'] = 'try again: '+textQuestion

    return HttpResponse(json.dumps(response_data), content_type="application/json")












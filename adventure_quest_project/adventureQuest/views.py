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
from .forms import PostForm, CommentForm
from .models import Quest, Riddle, UserProfile, Post, Comment
import re
import json

#############################################
#   This is the views for Adventure Quest   #
#############################################


# The home page, has info about Adventure Quest and links to the other
# parts of the application.
def index(request):
    return render(request, 'adventureQuest/index.html')


# Quest comments
def comment(request):
    objects_comment = Comment.objects.all()
    context={
        "comment_list": objects_comment,
    }
    return render(request, 'adventureQuest/comment.html', context)


# Adding comments
def add_comment(request):
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.save()
            return redirect('comment')
    else:
        form = CommentForm()
    return render(request, 'adventureQuest/comment_form.html', {'form': form})


# The about page for the Finnieston Quest displays information about the
# Quest, a map of the starting location and a link to begin the quest.
def finnieston_about(request):
    context_dict = {}
    context_dict['questurl'] = reverse(finnieston_quest)
    context_dict['questmappos'] = "55.868273, -4.292110" 
    for row in Quest.objects.filter(name="finnieston_quest"):
        context_dict['descr'] = row.description
        context_dict['age_limit'] = row.age_limit
        context_dict['difficulty'] = row.difficulty
        context_dict['start'] = row.start_point

    check_url(request)
    return render(request, 'adventureQuest/finnieston_about.html', context_dict)


# The about page for the Glasgow University Quest displays information about the
# Quest, a map of the starting location and a link to begin the quest.
def glasgow_uni_about(request):
    context_dict = {}
    context_dict['questurl'] = reverse(glasgow_uni_quest)
    context_dict['questmappos'] = "55.871950, -4.288233"
    for row in Quest.objects.filter(name="glasgow_uni_quest"):
        context_dict['descr'] = row.description
        context_dict['age_limit'] = row.age_limit
        context_dict['difficulty'] = row.difficulty
        context_dict['start'] = row.start_point
    check_url(request)
    return render(request, 'adventureQuest/glasgow_uni_about.html', context_dict)


# The about page for the Southside Quest displays information about the
# Quest, a map of the starting location and a link to begin the quest.
def southside_about(request):
    context_dict = {}
    context_dict['questurl'] = reverse(southside_quest)
    context_dict['questmappos'] = "55.840240, -4.267360"
    for row in Quest.objects.filter(name="southside_quest"):
        context_dict['descr'] = row.description
        context_dict['age_limit'] = row.age_limit
        context_dict['difficulty'] = row.difficulty
        context_dict['start'] = row.start_point
    check_url(request)
    return render(request, 'adventureQuest/southside_about.html', context_dict)


# The about page for the City Centre Quest displays information about the
# Quest, a map of the starting location and a link to begin the quest.
def city_centre_about(request):
    context_dict = {}
    context_dict['questurl'] = reverse(city_centre_quest)
    context_dict['questmappos'] = "55.859986, -4.252588"
    for row in Quest.objects.filter(name="city_centre_quest"):
        context_dict['descr'] = row.description
        context_dict['age_limit'] = row.age_limit
        context_dict['difficulty'] = row.difficulty
        context_dict['start'] = row.start_point
    check_url(request)
    return render(request, 'adventureQuest/city_centre_about.html', context_dict)


# The about page for the Kids Quest displays information about the
# Quest, a map of the starting location and a link to begin the quest.
def kids_about(request):
    context_dict = {}
    context_dict['questurl'] = reverse(kids_quest)
    context_dict['questmappos'] = "55.868786, -4.290196"
    for row in Quest.objects.filter(name="kids_quest"):
        context_dict['descr'] = row.description
        context_dict['age_limit'] = row.age_limit
        context_dict['difficulty'] = row.difficulty
        context_dict['start'] = row.start_point
    check_url(request)
    return render(request, 'adventureQuest/kids_about.html', context_dict)


# The about page for the Mystery Quest displays information about the
# Quest, a map of the starting location and a link to begin the quest.
def mystery_about(request):
    context_dict = {}
    context_dict['questurl'] = reverse(mystery_quest)
    context_dict['questmappos'] = "55.874692, -4.292962"
    for row in Quest.objects.filter(name="mystery_quest"):
        context_dict['descr'] = row.description
        context_dict['age_limit'] = row.age_limit
        context_dict['difficulty'] = row.difficulty
        context_dict['start'] = row.start_point
        
    check_url(request)
    return render(request, 'adventureQuest/mystery_about.html', context_dict)


# The view for the congratulations page
def congratulations(request):
    return render(request, 'adventureQuest/congratulations.html')


# The view for the registration page. Allows users to register with a username,
# email and password and an optional profile pciture.
def register(request):
    # Tells us if registration was successful or not.
    registered = False
    # Try and get form info with POST.
    if request.method == 'POST':
        user_form = UserForm(request.POST or None, request.FILES or None)
        profile_form = UserProfileForm(request.POST or None, request.FILES or None)
        # If the two forms are valid:
        if user_form.is_valid() and profile_form.is_valid():

            # Save the user's form data to the database.
            user = user_form.save()

            # Hash the users password and then update the user object.
            user.set_password(user.password)
            user.save()

            # Set commit=False to avoid integrity problems.
            profile = profile_form.save(commit=False)
            profile.user = user

            # Check if user uploaded a profile picture.
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            # Now we save the UserProfile model instance.
            profile.save()

            # Update variable as registration was successful.
            registered = True
        else:
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
                   'registered': registered, })



# The My Account page view. This view allows information to be displayed about the
# quests the user has completed and their high scores, their profile picture and
# any hall of fame posts they have made.
def my_account(request):
    # Get current user.
    user = request.user

    # Get all the hall of fame posts made by user and order them by number of hints used low-high.
    objects_filter = Post.objects.filter(user=user)
    objects_post = objects_filter.order_by('hints')[:100]

    # Add the posts to the context dictionary.
    context_dict = {"object_list": objects_post,}

    # Initialise each quest so that if they haven't completed the quest n/a will appear.
    context_dict['mystery_quest'] = 'n/a'
    context_dict['finnieston_quest'] = 'n/a'
    context_dict['glasgow_uni_quest'] = 'n/a'
    context_dict['southside_quest'] = 'n/a'
    context_dict['city_centre_quest'] = 'n/a'
    context_dict['kids_quest'] = 'n/a'

    # Get the user information to be displayed on the page.
    for row in UserProfile.objects.filter(user=user):
        context_dict['user'] = row.user
        context_dict['pic'] = str(row.picture)

    # Order the number of hints so that best scores are at the top.
    all_scores = UserScores.objects.filter(user=request.user)
    ordered_scores = all_scores.order_by('-score')

    # Get the least amount of hints used for each quest and update context dictionary.
    for row in ordered_scores.filter(user=request.user):
        context_dict[row.quest.name] = row.score

    return render(request, 'adventureQuest/my_account.html',context_dict)


# The view for login page. Authenticates users who provide valid log in details.
def user_login(request):
    context_dict = {}
    # If the request is a POST, try to get the information.
    if request.method == 'POST':
        # Get the username and password provided by the user.
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Check if the username/password combination is valid,
        # a User object is returned if it is.
        user = authenticate(username=username, password=password)

        # Check if a User object was returned.
        if user:
            # Check user hasn't been disabled.
            if user.is_active:
                # log user in and redirect them to the homepage
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                # Account has been disabled so don't log them in.
                return HttpResponse("Your adventureQuest account is disabled.")
        else:
            # User object wasn't returned so user details weren't authenticated.
            print("Invalid login details: {0}, {1}".format(username, password))
            context_dict['invalid_deets'] = True
            return render(request, 'adventureQuest/login.html', context_dict)
    else:
        return render(request, 'adventureQuest/login.html', {})


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

# This allows users to create a post in the Hall of Fame.
def post_create(request):
    # If user is not authenticated, redirect them to login.
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))

    # Try and get the information from the POST
    form = PostForm(request.POST or None, request.FILES or None)

    # Initalise hints as None.
    my_hint = None

    # If form is valid
    if form.is_valid():
        # Set commit=False to avoid integrity problems.
        instance = form.save(commit=False)
        # Save the post user.
        instance.user = request.user
        # Save the quest the post is associated with.
        for quest_post in Quest.objects.filter(name=instance.quest):
            my_quest = quest_post
        # Save the score the user got for that quest.
        for score_row in UserScores.objects.filter(user=request.user, quest=my_quest):
            my_hint = score_row.score
        # If they have completed the quest update the number of hints used.
        if my_hint != None:
            instance.hints = my_hint
        # Now save the post.
        instance.save()

        # The post was a success!
        messages.success(request, "Post was created")
        return HttpResponseRedirect(reverse('hall_of_fame'))

    # Else the post wasn't successful so return form.
    context = {"form": form,}

    return render(request, 'adventureQuest/post_form.html', context)


# This is the view for the mystery quest hall of fame. Posts from that quest will
# be displayed here in order of number of hints used low-high.
def mystery_quest_hall_of_fame(request):

    context = hall_of_fame_helper("mystery_quest")

    return render(request, 'adventureQuest/mystery_quest_post_list.html', context)


# This is the view for the finnieston quest hall of fame. Posts from that quest will
# be displayed here in order of number of hints used low-high.
def finnieston_quest_hall_of_fame(request):

    context = hall_of_fame_helper("finnieston_quest")

    return render(request, 'adventureQuest/finnieston_quest_post_list.html', context)


# This is the view for the Glasgow University quest hall of fame. Posts from that quest will
# be displayed here in order of number of hints used low-high.
def glasgow_uni_quest_hall_of_fame(request):

    context = hall_of_fame_helper("glasgow_uni_quest")

    return render(request, 'adventureQuest/glasgow_uni_quest_post_list.html', context)


# This is the view for the Southside University quest hall of fame. Posts from that quest will
# be displayed here in order of number of hints used low-high.
def southside_quest_hall_of_fame(request):

    context = hall_of_fame_helper("southside_quest")

    return render(request, 'adventureQuest/southside_quest_post_list.html', context)


# This is the view for the City Centre University quest hall of fame. Posts from that quest will
# be displayed here in order of number of hints used low-high.
def city_centre_quest_hall_of_fame(request):

    context = hall_of_fame_helper("city_centre_quest")

    return render(request, 'adventureQuest/city_centre_quest_post_list.html', context)


# This is the view for the Kids University quest hall of fame. Posts from that quest will
# be displayed here in order of number of hints used low-high.
def kids_quest_hall_of_fame(request):

    context = hall_of_fame_helper("kids_quest")

    return render(request, 'adventureQuest/kids_quest_post_list.html', context)


# Helper method for Hall Of Fame posts that gets the posts associated with said quest.
def hall_of_fame_helper(quest_name):
    # Get the quest object
    for quest_row in Quest.objects.filter(name=quest_name):
        my_quest = quest_row
    # Get all the hall of fame posts associated with that quest.
    objects_filter = Post.objects.filter(quest=my_quest)
    # Order them by hints used low-high.
    objects_post = objects_filter.order_by('hints')[:100]
    # Add the posts to a dictionary.
    context = {"object_list": objects_post,}
    # return the dictionary of posts.
    return context


# This is the view for the mystery quest. This is where riddles for that quest are shown.
def mystery_quest(request):
    # Redirected if not logged in as only users can play quests.
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))
    else:
        # helper method which gets the quest name and adds it as a session variable.
        get_current_quest(request)
        return render(request, 'adventureQuest/mystery_quest.html')


# This is the view for the finnieston quest. This is where riddles for that quest are shown.
def finnieston_quest(request):
    # Redirected if not logged in as only users can play quests.
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))
    else:
        # helper method which gets the quest name and adds it as a session variable.
        get_current_quest(request)
        return render(request, 'adventureQuest/finnieston_quest.html')


# This is the view for the Glasgow uni quest. This is where riddles for that quest are shown.
def glasgow_uni_quest(request):
    # Redirected if not logged in as only users can play quests.
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))
    else:
        # helper method which gets the quest name and adds it as a session variable.
        get_current_quest(request)
        return render(request, 'adventureQuest/glasgow_uni_quest.html')


# This is the view for the southside quest. This is where riddles for that quest are shown.
def southside_quest(request):
    # Redirected if not logged in as only users can play quests.
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))
    else:
        # helper method which gets the quest name and adds it as a session variable.
        get_current_quest(request)
        return render(request, 'adventureQuest/southside_quest.html')


# This is the view for the city centre quest. This is where riddles for that quest are shown.
def city_centre_quest(request):
    # Redirected if not logged in as only users can play quests.
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))
    else:
        # helper method which gets the quest name and adds it as a session variable.
        get_current_quest(request)
        return render(request, 'adventureQuest/city_centre_quest.html')


# This is the view for the kids quest. This is where riddles for that quest are shown.
def kids_quest(request):
    # Redirected if not logged in as only users can play quests.
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))
    else:
        # helper method which gets the quest name and adds it as a session variable.
        get_current_quest(request)
        return render(request, 'adventureQuest/kids_quest.html')


# Helper method that resets the quest if the user leaves half way through
def check_url(request):
    request.session['riddleQuestionID'] = 0
    request.session['riddleAnswerID'] = 0
    request.session['riddleCorrectNo'] = 0
    request.session['riddleCorrectNo'] = 0
    request.session['numberHint'] = 0
    request.session['questName'] = 0


# Helper method that increments cookies for the quest.
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


# Helper method that gets cookies.
def get_server_side_cookie(request, cookie, default_val = None):
    val = request.session.get(cookie)
    if not val:
        val = default_val
    return val

# Helper method
def get_current_quest(request):
    current_path = request.get_full_path()
    questName ="".join(current_path.split('/')[2:])
    trimmed = questName
    quest_name = str(get_server_side_cookie(request, 'questName', trimmed))
    request.session['questName'] = quest_name

def add_score(user, quest, score):
	q=UserScores.objects.get_or_create(user=user, quest=quest, score=score)[0]
	q.save()
	return q

def quest_ajax(request):
    response_data = {}
    questName = request.session['questName']

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


    # Get the user answer

    input_answer = request.GET.get('answer')

    if input_answer != None:
        user_lower = input_answer.lower()
        user_answer = re.sub('[^A-Za-z0-9]+', '', user_lower)

    else:
        user_answer = '@'

    # Set the current question and answer from the database
    for row in Riddle.objects.filter(quest_name=questName, question_id=ridAID):
        textAnswer = row.answer


    for row in Riddle.objects.filter(quest_name=questName, question_id=ridQID):
        textQuestion = row.question
        textHint = row.hint
        textInstruction = row.instruction


    # Create Response data vairable

    # Hint file
    if request.GET.get('click', False):
        response_data['hint'] = textHint
        quest_cookies(request, False, True)
        no_hints = request.session['numberHint']
        response_data['hintNo'] = no_hints
        response_data['hint_available'] = 'false'





# If the users answer is correct then get the next question from the database unless this is the last question
    if correctNo <= numberRiddles:

        if user_answer in textAnswer:
            response_data['hint'] = 'Remember the number of hints you use will be recorded!'
            quest_cookies(request, True, False)
            ridQID = request.session['riddleQuestionID']
            ridAID = request.session['riddleAnswerID']
            response_data['hint_available'] = 'true'
            correctNo = request.session['riddleCorrectNo']
            response_data['correct'] = True

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
                response_data['answer'] = textQuestion
                response_data['instruction'] = textInstruction


        # If the user answer is incorrect
        else:
            for row in Riddle.objects.filter(quest_name=questName, question_id=ridQID):
                textQuestion = row.question
            response_data['answer'] = 'try again: '+textQuestion
            response_data['correct'] = False

    return HttpResponse(json.dumps(response_data), content_type="application/json")





######################
#   Helper methods   #
######################






# Helper method to add a user to database.
def add_user(username, email):
    u = User.objects.get_or_create(username=username, email=email)[0]
    u.save()
    u.set_password('123456')
    u.save()
    p = UserProfile.objects.get_or_create(user=u)
    return u


# Helper method to add a quest to database.
def add_quest(name):
    q = Quest.objects.get_or_create(name=name)[0]
    q.description = 'this is a test'
    q.difficulty = 1
    q.age_limit = 4
    q.start_point = 'here'
    q.save()
    return q


# Helper method to add users high score to a quest to the database.
def add_user_scores(user, quest, score):
    us = UserScores.objects.get_or_create(user=user,quest=quest)[0]
    us.score = score
    us.save()
    return us


# Helper method to add a post to database.
def add_post(u, quest, title, content, hints):
    path = os.path.abspath('cat.jpg')
    path = path[:3]
    p = Post.objects.get_or_create(user=u,quest=quest,title = title, image = SimpleUploadedFile(name='cat.jpg', content=open(path+'cat.jpg').read()))[0]
    p.content = content
    p.hints = hints
    p.height_field = 10
    p.width_field = 10
    p.updated = timezone.now()
    p.timestamp = timezone.now()
    p.save()
    return p
from django.core.management.base import BaseCommand
from ask.models import User, Ask
import random


class Command(BaseCommand):

    def handle(self, *args, **options):
        user_range = 10
        ask_range = 10

        f_name = [
            'Red', 'Mad', 'Dummy', 'Crazy', 'Big', 'Black', 'Lonely', 'Shiz', 'Drunken',
            'Wicked', 'Brainless', 'Rich', 'Stubborn', 'Stupid', 'Fat', 'Wooden', 'Donald'
        ]
        l_name = [
            'Sailor', 'Rat', 'Man', 'Rabbit', 'Donkey', 'Policeman', 'Child', 'Penguin', 'Joker',
            'Lawmaker', 'Judge', 'Iron', 'President', 'Trump', 'Duck', 'Timmy', 'Kartman', 'Kenny'
            'Orc',
        ]

        for i in range(0, user_range):
            username = u'{0}{1}'.format(
                f_name[random.randrange(0, len(f_name))],
                l_name[random.randrange(0, len(l_name))]
            )
            email = u'{0}@e-corp.com'.format(username)

            password = u'{0}123'.format(username)

            try:
                User.object.create_user(username=username, email=email, password=password)
            except:
                username = u'{0}{1}'.format(username, i)
                email = u'{0}@e-corp.com'.format(username)
                User.object.create_user(username=username, email=email, password=password)

        f_question = ['How to', 'Why to', 'Can I']
        l_question = ['fly', 'run', 'jump', 'degrade']

        users = User.object.all()
        users_count = len(users)

        for i in range(0, ask_range):
            ask = Ask()
            random_pk = random.randrange(1, users_count)
            ask.author = users[random_pk]
            ask.question = u'{0} {1}'.format(
                f_question[random.randrange(0, len(f_question))],
                l_question[random.randrange(0, len(l_question))]
            )
            ask.text = u'{0} question by {1}'.format(
                ask.question, ask.author.username
            )
            ask.save()
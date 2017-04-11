from django.core.management.base import BaseCommand
from ask.models import User, Ask, Answer, Tag
import random


class Command(BaseCommand):

    def handle(self, *args, **options):
        user_range = 25
        ask_range = 37
        answers_range = 97

        f_name = [
            'Red', 'Mad', 'Dummy', 'Crazy', 'Big', 'Black', 'Lonely', 'Shiz', 'Drunken',
            'Wicked', 'Brainless', 'Rich', 'Stubborn', 'Stupid', 'Fat', 'Wooden', 'Donald',
            'American', 'Dead', 'Lucky', 'Night'
        ]
        l_name = [
            'Sailor', 'Rat', 'Man', 'Rabbit', 'Donkey', 'Policeman', 'Child', 'Penguin', 'Joker',
            'Lawmaker', 'Judge', 'Iron', 'President', 'Trump', 'Duck', 'Timmy', 'Kartman', 'Kenny',
            'Orc', 'Illuminati', 'Band', 'Slave', 'Coffee', 'Aviato', 'Redneck', 'Camper', 'King'
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

        tags_list = [
            'LOL', 'mad', 'wazzzup', 'DonaldTrump', 'luxury', 'shaurma', 'Skynet',
            'TheyAreWatchingYou', 'illuminati', 'Futurama', 'Bender', 'BlackJack',
            'TacoBell', 'BreakingBad',
        ]

        for tag in tags_list:
            try:
                new_tag = Tag()
                new_tag.title = tag
                new_tag.save()
            except:
                pass

        f_question = ['How to', 'Why to', 'Can I', 'What if']
        l_question = ['fly', 'run', 'jump', 'degrade', 'capture the world']

        users = User.object.all()
        users_count = len(users)

        tags_list = Tag.objects.all()
        tags_count = len(tags_list)

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

            ask_tags = []
            tags_range = random.randrange(1, 4)
            for i in range(0, tags_range):
                ask_tags.append(tags_list[random.randrange(0, tags_count)])

            ask.rating = random.randrange(-10, 30) # temporary remove later by UserVote
            ask.save()
            ask.tags = set(ask_tags)
            ask.save()

        asks = Ask.objects.all()
        asks_count = len(asks)

        f_answer = ['Just', 'I dont', 'May be', 'You should']
        l_answer = ['do it', 'know', 'know', 'forget it']

        for i in range(0, answers_range):
            answer = Answer()

            random_pk = random.randrange(1, users_count)
            answer.author = users[random_pk]

            ask_pk = random.randrange(1, asks_count)
            answer.ask = asks[ask_pk]

            answer.text = u'{0} {1}'.format(
                f_answer[random.randrange(0, len(f_answer))],
                l_answer[random.randrange(0, len(l_answer))]
            )
            answer.save()
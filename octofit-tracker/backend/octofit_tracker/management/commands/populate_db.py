from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Workout, Activity, Leaderboard
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()
        Workout.objects.all().delete()

        # Create Teams
        marvel = Team.objects.create(name='Team Marvel', description='Marvel superheroes')
        dc = Team.objects.create(name='Team DC', description='DC superheroes')

        # Create Users
        users = [
            User(email='tony@stark.com', username='IronMan', team=marvel),
            User(email='steve@rogers.com', username='CaptainAmerica', team=marvel),
            User(email='bruce@wayne.com', username='Batman', team=dc),
            User(email='clark@kent.com', username='Superman', team=dc),
        ]
        for user in users:
            user.save()

        # Create Workouts
        pushups = Workout.objects.create(name='Pushups', description='Upper body workout', difficulty='Easy')
        running = Workout.objects.create(name='Running', description='Cardio workout', difficulty='Medium')
        yoga = Workout.objects.create(name='Yoga', description='Flexibility workout', difficulty='Easy')

        # Create Activities
        Activity.objects.create(user=users[0], workout=pushups, date=timezone.now().date(), duration=30, calories_burned=200)
        Activity.objects.create(user=users[1], workout=running, date=timezone.now().date(), duration=45, calories_burned=400)
        Activity.objects.create(user=users[2], workout=yoga, date=timezone.now().date(), duration=60, calories_burned=150)
        Activity.objects.create(user=users[3], workout=pushups, date=timezone.now().date(), duration=20, calories_burned=120)

        # Create Leaderboard
        Leaderboard.objects.create(team=marvel, total_points=600, rank=1)
        Leaderboard.objects.create(team=dc, total_points=270, rank=2)

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data.'))

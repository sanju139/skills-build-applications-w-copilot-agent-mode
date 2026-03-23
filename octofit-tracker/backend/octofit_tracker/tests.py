# Basic tests for the Octofit Tracker API
from django.test import TestCase
from .models import User, Team, Workout, Activity, Leaderboard

class BasicModelTest(TestCase):
    def test_team_creation(self):
        team = Team.objects.create(name='Test Team')
        self.assertEqual(str(team), 'Test Team')

    def test_user_creation(self):
        team = Team.objects.create(name='Test Team')
        user = User.objects.create(email='test@example.com', username='testuser', team=team)
        self.assertEqual(str(user), 'testuser')

    def test_workout_creation(self):
        workout = Workout.objects.create(name='Pushups', description='Pushups workout', difficulty='Easy')
        self.assertEqual(str(workout), 'Pushups')

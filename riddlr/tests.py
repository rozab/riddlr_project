from django.test import TestCase
from riddlr.models import Riddle, UserProfile
# Create your tests here.




class CreateRiddle(TestCase):
	def test_for_user_creation(self):
		guy = UserProfile(user=('username','james@james.com','jsjsjs'))
		guy.save()
		self.assertEqual((guy.karma==0), true)

	def test_to_ensure_rating_is_zero(self):
		guy = UserProfile(user='james')
		riddle = Riddle(question='How many are you', answers='two',author=guy)
		riddle.save()
		self.assertEqual((riddle.rating == 0), true)
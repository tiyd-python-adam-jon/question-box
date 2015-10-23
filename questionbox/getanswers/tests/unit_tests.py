from django.test import TestCase
from getanswers.models import Question, Answer

# Create your tests here.
class AnswerPostTestCase(TestCase):

    def setUp(self):
        Question.objects.create(title="First Question", qtext="What?")
        Question.objects.create(title="Second Question", qtext="Who?")

    def tearDown(self):
        Question.objects.all().delete()
        Answer.objects.all().delete()

    def test_add_answer(self):
        self.setUp()
        resp = self.client.post('/questions/1/answers/add',
                                form={'atext': 'An answer'})
        self.assertEqual(resp.status_code, 201)
        self.tearDown()

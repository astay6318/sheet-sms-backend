from django.db import models

#create the tables for form, questions,answers and response
class Form(models.Model):
    form_id = models.AutoField(primary_key=True)
    form_name = models.CharField(max_length=255)

#each question is linked to a form 
class Question(models.Model):
    question_id = models.AutoField(primary_key=True)
    form = models.ForeignKey(Form,on_delete=models.CASCADE)
    question_text = models.TextField()
    SINGLE_CHOICE = 'single_choice'
    MULTIPLE_CHOICE = 'multiple_choice'
    question_type_choices = (
        (SINGLE_CHOICE,'Single Choice'),
        (MULTIPLE_CHOICE,'Multi-Select')
    )
    question_type = models.CharField(max_length=20, choices = question_type_choices,default=SINGLE_CHOICE)

#answer is linked to the question and form using foreign key
class Answer(models.Model):
    answer_id = models.AutoField(primary_key=True)
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    answer_text = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)

#response is connected to the form and question using foreign key
class Response(models.Model):
    user_id = models.IntegerField()
    form = models.ForeignKey(Form,on_delete=models.CASCADE)
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    answers =  models.TextField()

    def get_selected_answers(self):
        import json
        return json.loads(self.answers)


from django.db import models

class Form(models.Model):
    form_id = models.AutoField(primary_key=True)
    form_name = models.CharField(max_length=255)

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

class Answer(models.Model):
    answer_id = models.AutoField(primary_key=True)
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    answer_text = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)

class Response(models.Model):
    user_id = models.IntegerField()
    form = models.ForeignKey(Form,on_delete=models.CASCADE)
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    answers =  models.TextField()

    def get_selected_answers(self):
        import json
        return json.loads(self.answers)


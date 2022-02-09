from datetime import  datetime
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.http import HttpResponseRedirect
from .models import Question,Choice
from django.views import View


class index(View):

    def get(self, request):
        latest_question_list = Question.objects.order_by('-pub_date')
    
        context = {
            'latest_question_list': latest_question_list,
        }
    
        return render(request, 'polls/index.html', context)


class vote(View):
       
    def post(self, request, question_id):    
        question = get_object_or_404(Question, pk=question_id)
        try:    
            selected_choice = question.choice_set.get(pk=request.POST['choice'])
        except (KeyError, Choice.DoesNotExist):
            # Redisplay the question voting form.
            return render(request, 'polls/details.html', {
                'question': question,
                'error_message': "You didn't select a choice.",
            })
        else:
            selected_choice.votes += 1
            selected_choice.save()
            # Always return an HttpResponseRedirect after successfully dealing
            # with POST data. This prevents data from being posted twice if a
            # user hits the Back button.
            return HttpResponseRedirect(reverse('results', args=(question.id,)))
    
    
class detail(View):

    def get(self, request, question_id):
        question = get_object_or_404(Question, pk=question_id)
        return render(request, 'polls/details.html', {'question': question})


class results(View):

    def get(self, request, question_id):
        question = get_object_or_404(Question, pk=question_id)
        return render(request, 'polls/results.html', {'question': question})


class create(View):

    def get(self, request):
        return render(request, 'polls/create.html')


class save(View):

    def post(self, request):
        if request.method == "POST":
            question = request.POST['question']
        for question1 in Question.objects.values_list('question_text'):
            print(question1[0])
            if question == question1[0]:
                
                return render(request, 'polls/create.html', {'message':'Question alreay exists'})

        q = Question(question_text=question, pub_date=datetime.today())
        q.save()   
        question = Question.objects.get(question_text=question)
        return render(request, 'polls/options.html', {'question':question})


class options(View):

    def post(self, request, question_id):
        if request.method == "POST":
            question = get_object_or_404(Question, pk=question_id)
            choice = request.POST['option']   
            c=Choice(choice_text=choice, question=question)
            c.save()
                
            return render(request, 'polls/options.html', {'question':question})
       
       
class choice(View):

    def get(self, request, question_id):
        question = get_object_or_404(Question, pk=question_id)
        return render(request, 'polls/options.html', {'question':question})

    



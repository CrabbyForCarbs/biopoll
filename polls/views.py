# polls/views.py

from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Question, Choice

def index(request):
    # Get your question with id=1 from the database
    question = get_object_or_404(Question, pk=1)
    # Send the question to the template
    return render(request, 'polls/index.html', {'question': question})

def results(request, question_id):
    # Get the question and display the results page
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        # request.POST['choice'] gets the ID of the choice selected by the user
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # If no choice was selected, show the poll form again with an error
        return render(request, 'polls/index.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        # Add one vote and save the change to the database
        selected_choice.votes += 1
        selected_choice.save()
        # Redirect to the results page after a successful vote.
        # reverse() helps build the URL like '/polls/1/results/'
        return HttpResponseRedirect(reverse('results', args=(question.id,)))
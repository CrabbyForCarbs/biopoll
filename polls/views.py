# polls/views.py

from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse
from django.db.models import F
from django.db import transaction
from .models import Question, Choice
import os

# This is the NEW homepage view that was missing.
# It will render your homepage.html template.
def homepage(request):
    return render(request, 'polls/homepage.html')

# This is your view for a specific profile page like /your-name/
# I have removed the duplicate and kept the one that matches your urls.py
def index(request, username):
    # This line is for debugging if you need it
    print(f"Fetching data for user: {username}")
    
    question = get_object_or_404(Question, pk=1)
    return render(request, 'polls/index.html', {'question': question})

# This decorator ensures all database operations within the function are safe
# Your vote function is correct, no changes are needed here.
@transaction.atomic
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    
    try:
        # Get the ID of the choice the user just clicked
        selected_choice_id = int(request.POST.get('choice'))
    except (KeyError, TypeError, ValueError):
        return JsonResponse({'success': False, 'error': 'Invalid choice.'}, status=400)

    session_key = f'voted_on_question_{question.id}'
    previous_choice_id = request.session.get(session_key)

    # Case 1: User is changing their vote from a previous one
    if previous_choice_id is not None and previous_choice_id != selected_choice_id:
        # Decrement the old choice and increment the new one
        Choice.objects.filter(pk=previous_choice_id).update(votes=F('votes') - 1)
        Choice.objects.filter(pk=selected_choice_id).update(votes=F('votes') + 1)
    
    # Case 2: User is voting for the first time
    elif previous_choice_id is None:
        Choice.objects.filter(pk=selected_choice_id).update(votes=F('votes') + 1)

    # Case 3: User clicked the same choice again (previous_choice_id == selected_choice_id)
    # We do nothing in this case.

    # After any changes, update the user's session to remember the latest vote
    request.session[session_key] = selected_choice_id
    
    # Return the latest vote counts for all choices on the question
    all_choices = question.choice_set.all()
    vote_counts = {choice.id: choice.votes for choice in all_choices}
    return JsonResponse({'success': True, 'votes': vote_counts})
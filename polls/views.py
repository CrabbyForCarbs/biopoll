# polls/views.py

from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse
from django.db.models import F
from django.db import transaction
from .models import Question, Choice

# ... (your homepage and index views remain the same) ...
def homepage(request):
    # ... (no changes needed here)
    try:
        latest_question = Question.objects.latest('pub_date')
    except Question.DoesNotExist:
        latest_question = None
    context = {
        'question': latest_question,
    }
    return render(request, 'polls/homepage.html', context)

def index(request, username):
    # ... (no changes needed here)
    print(f"Fetching data for user: {username}")
    question = get_object_or_404(Question, pk=1)
    return render(request, 'polls/index.html', {'question': question})


# THIS IS THE CORRECTED VOTE FUNCTION
@transaction.atomic
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    
    try:
        selected_choice_id = int(request.POST.get('choice'))
    except (KeyError, TypeError, ValueError):
        return JsonResponse({'success': False, 'error': 'Invalid choice.'}, status=400)

    session_key = f'voted_on_question_{question.id}'
    previous_choice_id = request.session.get(session_key)

    # First, update the session with the new choice.
    # This ensures it's set even on the very first vote.
    request.session[session_key] = selected_choice_id

    # Now, handle the database updates
    # Lock the choices to prevent race conditions
    choices_to_update = Choice.objects.select_for_update().filter(question=question)

    # Case 1: The user is changing their vote
    if previous_choice_id is not None and previous_choice_id != selected_choice_id:
        # Increment the new choice
        choices_to_update.filter(pk=selected_choice_id).update(votes=F('votes') + 1)
        # Decrement the old choice
        choices_to_update.filter(pk=previous_choice_id).update(votes=F('votes') - 1)
    
    # Case 2: The user is voting for the first time
    elif previous_choice_id is None:
        choices_to_update.filter(pk=selected_choice_id).update(votes=F('votes') + 1)

    # Case 3: The user clicked the same choice again (do nothing)
    
    # Get the fresh, updated vote counts
    all_choices = question.choice_set.all()
    vote_counts = {choice.id: choice.votes for choice in all_choices}
    
    return JsonResponse({'success': True, 'votes': vote_counts})
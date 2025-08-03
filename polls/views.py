from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse(
        "<p>Hey, everyone. I ask you to vote in this poll very politely.</p>"
        "<p>This is a poll for my Instagram bio, as I can't decide which one I should put there.</p>"
        "<p>To give you some context about me, I am a very extroverted and candid person, so go ham!</p>"
    )
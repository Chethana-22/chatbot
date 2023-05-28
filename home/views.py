from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
import os
import openai

openai.api_key = "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"

# Create your views here.

def home(request):
    return render(request, "index.html")


def chatAPI(request):
  if request.method =="POST":
     prompt = request.POST["prompt"]
     response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
        )
     print(response)
     return JsonResponse(response)
  return HttpResponse("Bad Request")
from datetime import datetime

from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .models import Challenge
from keys.openAIKey import OPEN_AI_VAR

# Create your views here.
class ChallengeView(TemplateView):
    template_name = 'challenges/challenges.html'
    
    def get(self, request):
        context = {'challenges' : Challenge.objects.filter(sustainer=request.user.sustainer, completionStatus=False)}
        return render(request, self.template_name, context)
    
    def post(self, request):
        if request.POST.get('location') == None or request.POST.get('location') == "Enter your location":
            support_cause = request.POST.get('support-dropdown')
            hours_to_help = request.POST.get('hours-dropdown')
            # Do something with the values
            import openai
            openai.api_key = OPEN_AI_VAR

            alignmentPrompt = """
            You are a 1-hour challenge generator for an app called 'sustain' to create a more happy and sustainable world.
            The challenges should be short and easy to complete.
            They should not include posting on social media, as the app requires you to post a picture of your completed challenge.
            You only give 1-2 sentence challenges in the following format:
            Hi User,
            Your challenge is: {insert_challenge_here}
            Go Forth and sustain!
            """

            time_limit = hours_to_help
            cause = support_cause
            UserPrompt = f"Create a challenge to help the following cause:{cause} with a time limit of ${time_limit}"

            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": alignmentPrompt},
                    {"role": "user", "content": UserPrompt}
                ]
            )

            rawChallenge = response['choices'][0]['message']['content']
            try:
                parsedChallenge = rawChallenge.splitlines()[1].strip().split("is: ")[1]
            except:
                parsedChallenge = rawChallenge
            print(rawChallenge)
            print(parsedChallenge)
            print(response['usage'])
            
            new = Challenge(cause=cause, description=parsedChallenge, points=time_limit, sustainer=request.user.sustainer)
            new.save()
            context = {
                'challenges': Challenge.objects.filter(sustainer=request.user.sustainer),
            }
            

            return render(request, self.template_name, context)
        else:
            challenge_location = request.POST.get('location')
            challenge_picture = request.POST.get('profile-picture')
            curr_pk = request.POST.get('challenge_pk')
            challenge = Challenge.objects.get(id=curr_pk)
            challenge.latitude = float(challenge_location.split(",")[0].strip())
            challenge.longitude = float(challenge_location.split(",")[1].strip())
            challenge.time = datetime.now()
            challenge.completionStatus = True
            challenge.save()
            return redirect('challenges:challenges')
        
    
    
class ChallengeDeleteView(TemplateView):
    
    def get(self, request, pk):
        challenge = Challenge.objects.get(id=pk)
        challenge.delete()
        return redirect('challenges:challenges')
        

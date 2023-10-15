from datetime import datetime

from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .models import Challenge
from keys.openAIKey import OPEN_AI_VAR
from django.core.files.storage import default_storage


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
            
            new = Challenge(cause=cause, description=parsedChallenge, points=time_limit, sustainer=request.user.sustainer, time=datetime.now(), completionStatus=False)
            new.save()
            context = {
                'challenges': Challenge.objects.filter(sustainer=request.user.sustainer, completionStatus=False),
            }
            

            return render(request, self.template_name, context)
        else:
            import urllib.request
            import os
            curr_pk = request.POST.get('challenge_pk')
            print(curr_pk)
            print('test')
            challenge = Challenge.objects.get(id=curr_pk)
            challenge_location = request.POST.get('location')
            if 'picture' in request.FILES:
                challenge_picture = request.FILES['picture']
                folder_path = 'static/challenge_images'
                filename = f'{challenge.pk}.jpg'
                file_path = os.path.join(folder_path, filename)
                with open(file_path, 'wb+') as destination:
                    for chunk in challenge_picture.chunks():
                        destination.write(chunk)
                print(challenge_picture)
                challenge.image = challenge_picture  # Move this line here
            else:
                print("NO PICTURE")

            challenge.latitude = float(challenge_location.split(",")[0].strip())
            challenge.longitude = float(challenge_location.split(",")[1].strip())
            # challenge.image = challenge_picture
            challenge.time = datetime.now()
            challenge.completionStatus = True
            request.user.sustainer.challenges_completed += 1
            challenge.save()
            request.user.sustainer.save()
            return redirect('challenges:challenges')
        
    
    
class ChallengeDeleteView(TemplateView):
    
    def get(self, request, pk):
        challenge = Challenge.objects.get(id=pk)
        challenge.delete()
        return redirect('challenges:challenges')
        

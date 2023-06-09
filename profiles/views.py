from django.shortcuts import render
from profiles.models import Profile


""" Sed placerat quam in pulvinar commodo. Nullam laoreet consectetur ex, sed\n
consequat libero pulvinar eget. Fusc faucibus, urna quis auctor pharetra,\n
massa dolor cursus neque, quis dictum lacus d"""


def profiles_index(request):
    profiles_list = Profile.objects.all()
    context = {'profiles_list': profiles_list}
    return render(request, 'profiles_index.html', context)


"""Aliquam sed metus eget nisi tincidunt ornare accumsan eget lac laoreet\n
neque quis, pellentesque dui. Nullam facilisis pharetra vulputate. Sed\n
tincidunt, dolor id facilisis fringilla, eros leo tristique lacus, it. Nam\n
aliquam dignissim congue. Pellentesque habitant morbi tristique senectus et\n
netus et males"""


def profile(request, username):
    profile = Profile.objects.get(user__username=username)
    context = {'profile': profile}
    return render(request, 'profile.html', context)

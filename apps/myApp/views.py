from django.shortcuts import render


def services(request):
	return render(request,"services.html")

def about_us(request):
	return render(request,"about_us.html")

def our_team(request):
	return render(request,"our_team.html")

def results(request):
	return render(request,"results.html")

def tsp(request):
	return render(request,"tsp.html")

def shortest_path(request):
	return render(request,"shortest_path.html")


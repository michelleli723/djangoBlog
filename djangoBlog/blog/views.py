from django.shortcuts import render
from django.http import HttpResponse

posts = [
	{
		'author' : 'Michelle',
		'title' : 'Blog Post 1',
		'content' : 'First post content',
		'date_posted' : 'October 21, 2018'
	},
	{
		'author' : 'Richard',
		'title' : 'Blog Post 2',
		'content' : 'Second post content',
		'date_posted' : 'October 22, 2018'
	}
]

# Create your views here.
def home(request):
	context = {
		'posts' : posts
	}
	return render(request, 'blog/home.html', context)

def about(request):
	return render(request, 'blog/about.html', {'title' : 'About'})
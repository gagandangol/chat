from django.shortcuts import render

def index(reqest):
	return render(reqest,'index.html',{})

def room (reqest,room_name):
	return render(reqest,'chatroom.html',{})

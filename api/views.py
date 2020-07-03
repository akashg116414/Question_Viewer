from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from question_viewer.settings import CDN_DOMAIN

from .models import Question, Group
from .forms import AddDocument


def add_documents(request):
	form = AddDocument(request.POST or None, request.FILES or None)
	errors = None
	if form.is_valid():
			# saving the details in the db
		group_obj = Group.objects.filter(name=form.cleaned_data.get('name')).first()
		if not group_obj:
			group_obj = Group.objects.create(
					name = form.cleaned_data.get('name')
				)
		print("comment-",form.cleaned_data.get('comment'),"question-",form.cleaned_data.get('question'))


		# # uploading the first document with same id
		# query = Document.objects.latest('id')
		obj1 = Question.objects.create(
					group_id = group_obj.id,
					comment = form.cleaned_data.get('comment'),
					question = form.cleaned_data.get('question'),
				)
       
			
			# looping through all other documents and uploading with same id
		for i in range(2,6):
			extra = 'question' + str(i)
			if (str(form.cleaned_data.get(extra)) != 'None'):
				obj1 = Question.objects.create(
					group_id = group_obj.id,
					comment = form.cleaned_data.get('comment'),
					question = form.cleaned_data.get(extra),)
		return redirect('view_all')
			
	if form.errors:
		errors = form.errors

	template_name = 'documents/add_documents.html'
	context = {"form":form, "errors":errors}
	return render(request, template_name, context)

def display_documents(request):
	template_name = 'documents/display_documents.html'

	# querying Document table from db
	queryset1 = Group.objects.all().order_by('-pk')

	# querying DocumentUpload table from db
	queryset2 = Question.objects.all()

	# domain of CDN where the documents will be uploaded
	cdn = CDN_DOMAIN

	context = {"object_list": queryset1, "document_list":queryset2, "cdn":cdn}
	return render(request, template_name, context)

def display_documents_google(request):
	template_name = 'documents/display_documents_google.html'

	# querying Document table from db
	queryset1 = Group.objects.all().order_by('-pk')

	# querying DocumentUpload table from db
	queryset2 = Question.objects.all()

	# domain of CDN where the documents will be uploaded
	cdn = CDN_DOMAIN

	context = {"object_list": queryset1, "document_list":queryset2, "cdn":cdn}
	return render(request, template_name, context)


def group_question(request, pk):
	template_name = 'documents/display_documents.html'

	# querying Document table from db
	queryset1 = Group.objects.filter(id=pk)

	# querying DocumentUpload table from db
	queryset2 = Question.objects.all().order_by('-pk')

	# domain of CDN where the documents will be uploaded
	cdn = CDN_DOMAIN

	context = {"object_list": queryset1, "document_list":queryset2, "cdn":cdn}
	return render(request, template_name, context)
from django import forms
from django.core.validators import FileExtensionValidator

class AddDocument(forms.Form):
	comment = forms.CharField()
	name =  forms.CharField()
	question 	= forms.FileField(validators=[FileExtensionValidator(
												allowed_extensions=['pdf', 'odt', 'txt','docx','jpg','png','jpeg']
												)])
	question2 	= forms.FileField(validators=[FileExtensionValidator(
												allowed_extensions=['pdf', 'odt', 'txt','docx','jpg','png','jpeg']
												)], required=False)
	question3	= forms.FileField(validators=[FileExtensionValidator(
												allowed_extensions=['pdf', 'odt', 'txt','docx','jpg','png','jpeg']
												)], required=False)
	question4 	= forms.FileField(validators=[FileExtensionValidator(
												allowed_extensions=['pdf', 'odt', 'txt','docx','jpg','png','jpeg']
												)], required=False)
	question5	= forms.FileField(validators=[FileExtensionValidator(
												allowed_extensions=['pdf', 'odt', 'txt','docx','jpg','png','jpeg']
												)], required=False)
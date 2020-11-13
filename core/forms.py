from django import forms


class EmailListForm(forms.Form):
    email_list = forms.CharField(label="Enter emails i.e. email_1@abc.com, email_2@abc.com")
    html_file = forms.FileField(label="HTML file")


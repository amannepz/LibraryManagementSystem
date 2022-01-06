from django import forms
class DateInput(forms.DateInput):
    input_type='date'
class NewBookForm(forms.Form):
        name=forms.CharField(label='BookName',max_length=100)
        number=forms.IntegerField(label='Book No')
        author=forms.CharField(label='Author',max_length=50)
        date=forms.DateField(label='Date',widget=DateInput)
        price=forms.FloatField(label='Price')
        quantity=forms.IntegerField(label='Quantity')

class searchform(forms.Form):
        name=forms.CharField(label='Name',max_length=100)

class issuebookform(forms.Form):
        studentid=forms.CharField(label='StudentId',max_length=10)
        sname=forms.CharField(label='StudentName',max_length=100)
        bnumber=forms.IntegerField(label='Book Number')
        bname=forms.CharField(label='BookName',max_length=100)
        author=forms.CharField(label='Author',max_length=50)
        issuedate=forms.DateField(label='IssueDate',widget=DateInput)
        returndate=forms.DateField(label='ReturnDate',widget=DateInput)
        aquantity=forms.IntegerField(label='AvailableQuantity')

class returnbookform(forms.Form):
        studentid=forms.CharField(label='StudentID',max_length=10)
        sname=forms.CharField(label='StudentName',max_length=100)
        bname=forms.CharField(label='BookName',max_length=100)
        bnumber=forms.IntegerField(label='Book Number')
        author=forms.CharField(label='Author',max_length=50)
        issuedate=forms.DateField(label='IssueDate',widget=DateInput)
        returningdate=forms.DateField(label='ReturningDate',widget=DateInput)
        returneddate=forms.DateField(label='ReturnedDate',widget=DateInput)
        latefee=forms.FloatField(label='LateFee')

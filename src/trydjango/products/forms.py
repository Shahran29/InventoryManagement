from django import forms

from .models import Product

#this is where I build my inventory forms
class ProductForm(forms.ModelForm):
	name = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Product Name"}))
	# description = forms.CharField(required=False, widget=forms.Textarea(attrs={
	# 	"class": "new-class-name two",
	# 	"id": "my-id-for-textarea",
	# 	"rows": 20,
	# 	"cols": 50
	# 	}))
	price = forms.DecimalField(initial=199.99)
	quantity = forms.IntegerField(initial=1)
	status = forms.CharField(required=False)
	class Meta:
		model = Product
		fields = [
		'name',
		'price',
		'quantity',
		'status'
		]
	# def clean_title(self, *args, **kwargs):
	# 	title = self.cleaned_data.get("title")
	# 	if not "CFE" in title:
	# 		raise forms.ValidationError("This is not a valid title")
	# 	if not "news" in title:
	# 		raise forms.ValidationError("This is not a valid title")
	# 	return title

# class RawProductForm(forms.Form):
# 	title = forms.CharField(label='', widget=forms.TextInput(attrs={"placeholder": "Your Title"}))
# 	description = forms.CharField(required=False, widget=forms.Textarea(attrs={
# 		"class": "new-class-name two",
# 		"id": "my-id-for-textarea",
# 		"rows": 20,
# 		"cols": 50
# 		}))
# 	price = forms.DecimalField(initial=199.99)
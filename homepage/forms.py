from django import forms

from .models import PCR_Polymerase


class PCR_PolymeraseForm(forms.ModelForm):
	class Meta:
		model = PCR_Polymerase
		fields = ["seqNo", "name", "price", "unit", "category", "factory", "lifetime", "pro_date"]
	def get_product_name(self):
		product_name = self.cleaned_data.get('name')
		return product_name
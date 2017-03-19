from django.core.exceptions import ValidationError
from django.core.validators import URLValidator


def validate_url(value):
	url_validator = URLValidator()
	is_valid_url = True
	try:
		url_validator(value)
	except:
		is_valid_url = False

	if is_valid_url == False:
		raise ValidationError('Invalid URL for this field')
	return value

def validate_dot_com(value):
	if not 'com' in value:
		raise ValidationError('This is not valid because of no .com')
	return value

from django.shortcuts import render
from .models import Case
# Create your views here.


def charts(request):
	case_list = []
	case = {
		'x':0,
		'y':0,
		'r':0
	}
	obj = Case.objects.all()
	for i in obj:
		case = {
			'x':int(str(i.doj).split("-")[0]),
			'y':int(str(i.doj).split("-")[1]),
			'r':len(i.mentions.split(","))
		}
		print case
		case_list.append(case)

	print(case_list)

	

	return render(request, 'index.html', {"case_list":case_list,"cases":obj})
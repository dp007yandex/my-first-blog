from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse

from .models import Pdf
from .forms import PdfForm

# Create your views here.
def pdf_list(request):
    pdfItems = Pdf.objects.all
    return render(request, 'reports_project/pdf_list.html', {'pdfItems': pdfItems})

def pdf_detail(request, pk):
    pdfItem = get_object_or_404(Pdf, pk=pk)
    return render(request, 'reports_project/pdf_detail.html', {'pdfItem': pdfItem})

def pdf_edit(request, pk):
    pdf = get_object_or_404(Pdf, pk=pk)
    if request.method == "POST":
        form = PdfForm(request.POST, instance=pdf)
        if form.is_valid():
            pdf = form.save(commit=False)
            pdf.save()
            return redirect('pdf_detail', pk=pdf.pk)
    else:
        form = PdfForm(instance=pdf)
    return render(request, 'reports_project/pdf_edit.html', {'form': form})

def pdf_get_file(request, pk):
    pdf = get_object_or_404(Pdf, pk=pk)

    data = pdf.get_pdf_file()

    if data.status_code == 200:
        response = HttpResponse(data)
        #response['Content-Type'] = 'application/pdf; charset=utf-8'
        response['Content-Disposition'] = 'attachment; filename=' + pdf.report_name + '.' + pdf.file_format
        pdf.rawData = ""
    else:
        pdf.rawData = data.text
        raise Exception(data.text)
    
    pdf.save()

    return response
    
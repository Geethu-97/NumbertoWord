

from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html',{"data":"NUMBER TO WORD CONVERTER"})

def convert(request):
    number = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
    nty = ["", "", "Twenty", "Thirty", "Fourty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninty"]
    tens = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen",
            "Nineteen"]
    val = int(request.POST['num'])

    if val > 999999 or val=="":
        d="Cant solve for more than 6 digits"
        return render(request, 'result.html', {'res': d})
    else:
        d = [0, 0, 0, 0, 0, 0, ]
        i = 0
        numb = ""
        while val > 0:
            d[i] = val % 10
            i += 1
            val = val // 10

        if d[5] != 0:
            numb += number[d[5]] + " Lakh "

        if d[4] != 0:
            if (d[4] == 1):
                numb += tens[d[3]] + " Thousand "
            else:
                numb += nty[d[4]] + " " + number[d[3]] + " Thousand "
        else:
            if d[3] != 0:
                numb += number[d[3]] + " Thousand "
        if d[2] != 0:
            numb += number[d[2]] + " Hundred "
        if d[1] != 0:
            if (d[1] == 1):
                numb += tens[d[0]]
            else:
                numb += nty[d[1]] + " " + number[d[0]]
        else:
            if d[0] != 0:
                numb += number[d[0]]



    return render(request,'result.html',{'res':numb})
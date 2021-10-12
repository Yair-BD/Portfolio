from django.shortcuts import render


def myself(reqest):
    return render(reqest, "myself/cv_page.html")

class MySelf :
    pass

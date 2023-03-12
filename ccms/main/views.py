from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(response):
    return HttpResponse("<h1>Creating and Mapping Views Activity</h1>")

def mission(response):
    return HttpResponse("<h1>CCMS Mission</h1><br>The College of Computing and Multimedia Studies shall produce competent and innovative professionals or Technopreneurs in the Information and Communication Technology (ICT) industry adequately prepared in the practice of their profession supportive of national development goals and standards of global excellence.")
def vision(response):
    return HttpResponse("<h1>CCMS Vision</h1><br>The College of Computing and Multimedia Studies shall be a center of excellence in delivering Computing and Multimedia education.")
def objectives(response):
    return HttpResponse("""<h1>
                        CCMS Objectives </h1><br>
    1. Be employed and demonstrate professionalism, competence and passion in solving contemporary comuting problems by developing or utilizing innovative IT solutions. <br>
    2. Embark in lifelong learning or research to attune to the continuous innovation in the IT industry in order to adapt to the changing demands of the global market. <br>
    3. Exhibit leadership and teamwork, and commitment to their respective local or global organizations.
    """)

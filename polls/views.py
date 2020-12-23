from django.shortcuts import render
from django.http.response import HttpResponse
import requests,xmltodict

def rss(request):
    response = xmltodict.parse(requests.get(request.GET.get("url")).text)
    num=0
    for j in response["rss"]["channel"]["item"]:
        if("pubDate" in j):
            pubDate=response["rss"]["channel"]["item"][num]["pubDate"]
            if(pubDate[10]=="T"):
                pubDate=response["rss"]["channel"]["item"][num]["pubDate"].split("T")
                pubDate=pubDate[0].replace("-","/")+" "+pubDate[1][0:8]
            else:
                pubDate=response["rss"]["channel"]["item"][num]["pubDate"].split()
                pubDate=pubDate[3]+"/"+pubDate[2].replace("Jan","1").replace("Feb","2").replace("Mar","3").replace("Apr","4").replace("May","5").replace("Jun","6").replace("Jul","7").replace("Aug","8").replace("Sep","9").replace("Oct","10").replace("Nov","11").replace("Dec","12")+"/"+pubDate[1]+" "+pubDate[4]
        
            response["rss"]["channel"]["item"][num]["pubDate"]=pubDate
        num=num+1
    data = {
        "data": response
    }
    return render(request, "rss.html", data)

def index(request):
    return render(request, "index.html")
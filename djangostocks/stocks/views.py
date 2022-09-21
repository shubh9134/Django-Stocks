from django.http import HttpResponse
from django.shortcuts import render,HttpResponse
import finnhub

# Create your views here.
def trade(request):
    if(request.method == "POST"):
        ticker = request.POST["ticker"].upper()
        finnhub_client = finnhub.Client(api_key="c9jag72ad3idg7p56prg")
        res = finnhub_client.quote(ticker)
        print(res)
        if(res["c"]==0):
            res = "Error"
    else:
        ticker = "AAPL"
        finnhub_client = finnhub.Client(api_key="c9jag72ad3idg7p56prg")
        res = finnhub_client.quote(ticker)
    return render(request,"home.html",{"api":res,"ticker" : ticker })











def about(request):
    return render(request,"about.html",{})

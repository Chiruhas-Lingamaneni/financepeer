from django.shortcuts import render,redirect
import json
from .models import JsonData
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

def saveData(request,json_data):
    for x in json_data:
        #modeluser=request.user.username
        objjsondata=JsonData(modeluser=request.user,user_id=x['userId'],input_id=x['id'],title=x['title'],body=x['body'])
        objjsondata.save()

@login_required
def fileinput(request):
    username=None
    if request.method=="POST":
        valid_file=1
        check_format={'userId':0,'id':0,'title':0,'body':0}
        uploaded_file=request.FILES['documentone']
        data=uploaded_file.read()
        json_data=None
        if uploaded_file.content_type!='application/json':
            valid_file=2
        else:
            try:
                json_data=json.loads(data)
                for x in json_data:
                    if x.keys()!=check_format.keys():
                        valid_file=3
                        break
            except:
                valid_file=3
        if valid_file==1:
            saveData(request,json_data)
        request.FILES['documentone']=None
        return render(request,'fileupload/fileupload.html',{'valid_file':valid_file,'username':username})
    username = request.user.username
    return render(request,'fileupload/fileupload.html',{'valid_file':0,'username':username})

@login_required
def userData(request):
    data=JsonData.objects.all().filter(modeluser=request.user)
    return render(request,'fileupload/data.html',{'data':data})

@login_required
def userLogout(request):
    logout(request)
    return redirect('/')
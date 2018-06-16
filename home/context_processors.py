from home.models import userInfo

def owner(request):
    try:
        ownername=userInfo.objects.all().last().chefName
    except:
        ownername="Empty"
    return {'owner':ownername}
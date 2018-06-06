from home.models import userInfo

def owner(request):
    ownername=userInfo.objects.all().last().chefName
    return {'owner':ownername}
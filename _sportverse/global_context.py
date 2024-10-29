from datetime import date

def username(request):
    if request.user.is_authenticated:
        # print(request.user.first_name)
        return{'name': request.user.username.upper()} 
    return {}

def time_of_day(request):
    return{'date': date.today}
from django.shortcuts import render

# Create your views here.
def home_view(request):
    return render(request, 'npapp/result.html')

def movie_view(request):
    news1='KG3 will be a blockbuster'
    news2='Daali Dhananjaya in love?'
    news3='Daali Krishna and Milana Nagaraj got engaged'
    news4='Sunny Leone will come to Bengaluru for an item song'
    news5='Darshan and Sudeep friendship is like Chaddidosti'
    my_dict={'news1':news1,'news2':news2,'news3':news3,'news4':news4,'news5':news5}
    return render(request, 'npapp/mnews.html', my_dict)

def sports_view(request):
    spnews1='Kohli and Gambir: who is wrong?'
    spnews2='Whhen will RCB win IPL Trophy?'
    spnews3='Who will will today"s match and what their statics tell'
    spnews4='Who is this cute SRH owner girl?'
    spnews5='Fans waiting for RCB win the trphy'
    my_dict1={'news1':spnews1,'news2':spnews2,'news3':spnews3,'news4':spnews4,'news5':spnews5}
    return render(request, 'npapp/spnews.html', my_dict1)

def politics_view(request):
    pnews1='Who is the candidate gainst Modi in 2024 general election?'
    pnews2='When will Ukrain and Russia war will end?'
    pnews3='Economy will be down to a record level due to Warlike situation around the world'
    pnews4='What you can do for a better world?'
    pnews5='The people see the future with worried eyes!!'
    my_dict2={'news1':pnews1,'news2':pnews2,'news3':pnews3,'news4':pnews4,'news5':pnews5}
    return render(request, 'npapp/pnews.html', my_dict2)
from django.shortcuts import render, redirect
from apps.new.models import *
from .forms import RegisterForm

def home(request):
    main =  Main.objects.latest('id')
    abouts = About.objects.all()
    about_pro = AboutPro.objects.all()
    about_pro_photo = AboutProPhoto.objects.all()
    about_photos = AboutPhoto.objects.latest('id')

    experts = AboutExperts.objects.all()
    participent_numbers = ParticipantNumbers.objects.all()

    help_marketing = HelpMarketing.objects.latest('id')

    picture_marketing = PictureMarketing.objects.all()

    marketing_head = MarketingHead.objects.latest('id')
    marketing_box = MarketingBox.objects.all()

    service = Service.objects.latest('id')
    service_list = ServiceList.objects.all()
    review_list = ReviewList.objects.all()
    review_phrases = ReviewPhrases.objects.all()


    goods = Goods.objects.latest('id')
    photo_goods = GoodsPicture.objects.all()

    adress = Adresses.objects.all()

    blog = Blog.objects.latest('id')
    blog_picture = BlogPicture.objects.all()

    nagiv = NavigBar.objects.all()

    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect ('home')

    else:
        form = RegisterForm()

    return render(request, 'index_2.html', locals())
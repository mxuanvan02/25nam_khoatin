from django.shortcuts import render
# from django.views.generic import
from .models import Cooperate, Image, Join, Activity, MailAdmin, Title, Link_QRCode
from .forms import ATTEND_CHOICES, JoinForm, ImageForm, YEAR_CHOICES


from django.conf import settings
from django.core.mail import send_mail, send_mass_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.paginator import Paginator



def multiple_forms(request):
    form = JoinForm()
    img = ImageForm()
    image = Image.objects.all()
    activity = Activity.objects.all()
    cooperate = Cooperate.objects.all()
    filters = YEAR_CHOICES
    admin = MailAdmin.objects.all()
    title = Title.objects.all()
    link_qrcode = Link_QRCode.objects.all()

    join_list = Join.objects.order_by('year')
    paginator = Paginator(join_list, 5)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    

    if request.method == "POST":
        if 'formm' in request.POST:
            form = JoinForm(request.POST or None)
            
            

            subject = 'Cảm ơn đã phản hồi!'
            message = render_to_string('email.html', {'name': form['name'].value()})
            plain_message = strip_tags(message)
            recepient = str(form['email'].value())
            
            subject_admin = 'Kỉ niệm 25 năm khoa tin'
            message_admin = render_to_string('email_admin.html', {'name': form['name'].value()})
            plain_message_admin = strip_tags(message_admin)
            for adm in admin:
                recepient_admin = str(adm.email)

            datatuple = (
                            (subject, plain_message, settings.EMAIL_HOST_USER, [recepient]),
                            (subject_admin, plain_message_admin, settings.EMAIL_HOST_USER, [recepient_admin]),
                        )

            send_mass_mail(datatuple, fail_silently=False)



            if form.is_valid():
                form.save()
                form = JoinForm()






        elif 'imgg' in request.POST:
            img = ImageForm(data=request.POST, files=request.FILES)
            if img.is_valid():
                img.save()
                img = ImageForm()


            subject_admin = 'Someone upload images to the 25th anniversary'
            message_admin = render_to_string('email_admin_img.html', {})
            plain_message_admin = strip_tags(message_admin)
            for adm in admin:
                recepient_admin = str(adm.email)
            send_mail(subject_admin, plain_message_admin, settings.EMAIL_HOST_USER, [recepient_admin])
        


    else:
        form = JoinForm()
        img = ImageForm()





    context = {
        'form': form,
        'img': img,
        'filters': filters,
        'image': image,
        'cooperate': cooperate,
        'activity': activity,
        'page_obj': page_obj,
        'title': title,
        'link_qrcode': link_qrcode,
        }

    return render(request, 'index.html', context)






from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponse
from django.conf import settings

from django.core.files import File
from django.core.files.base import ContentFile
from django.http import FileResponse


from events.forms import PlantationEventForm
from events.models import PlantationEventModel
from user.models import PlantationUser
from notifications.models import PlantationNotificationsModel

import qrcode, json, uuid, os



def is_stuff(user):
    return user.is_superuser or user.is_staff

# Create your views here.
@login_required(login_url='/users/login/')
@user_passes_test(is_stuff)
def event_list_view(request):
    events = PlantationEventModel.objects.all()
    return render(request, "events.html", { "events": events })

@login_required(login_url='/users/login/')
@user_passes_test(is_stuff)
def event_create_view(request):
    form = PlantationEventForm()
    if request.method == "POST":
        form = PlantationEventForm(request.POST)

        if form.is_valid():
            event = form.save(commit=False)
            # form_sent = True
            event.host = request.user
            event.save()

            users = PlantationUser.objects.filter(is_staff=False).filter(is_superuser=False)
            for user in users:
                # notification = PlantationNotificationsModel.objects.create(user = user, event = event)
                # notification.save()

                notification, created = PlantationNotificationsModel.objects.get_or_create(user=user, event=event)
                if created:
                    notification.viewed = False  # Set any other initial values as needed
                    notification.rsvped = False
                    notification.attended = False
                    notification.save()
                


            return redirect("events")
    return render(request, "create-events.html", {"form": form})


@login_required(login_url='/users/login/')
def event_detail_view(request, pk):
    event = get_object_or_404(PlantationEventModel, pk = pk)
    return render(request, "event-detail.html", { "event": event })


def download_event_qr_view(request, pk):
    try:
        notification = get_object_or_404(PlantationNotificationsModel, pk = pk)
        # return redirect("event", event.pk)
        user = get_object_or_404(PlantationUser, pk = request.user.pk)

        data = {
            "name": user.get_name(),
            "event": notification.event.title,
            "ticket_id": "0000" + str(notification.pk)
        }
    
         # Create a QR code instance
        data_as_json = json.dumps(data)
    
        # Create a QR code instance
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(data_as_json)
        qr.make(fit=True)
    
        # Create an image object
        img = qr.make_image(fill_color="black", back_color="white")

        # Construct the image file path
        image_filename = f"qr_code_{data['ticket_id']}.png"  # You can define the file name as needed
        # Check and create the media directory if it doesn't exist
        # if not os.path.exists(settings.MEDIA_ROOT):
        #     os.makedirs(settings.MEDIA_ROOT)

        image_path = os.path.join(settings.MEDIA_ROOT, image_filename)


        # Save the image to the images folder
        # img.save(image_path)

         # Open the image file and read its content
        with open(image_path, 'rb') as image_file:
            # Create a File object from the image data
            # image_content = File(image_file)
            image_content = ContentFile(image_file.read())

            notification.qr_image.save(image_filename, image_content)
            
            # Assign the image to the ImageField
            # notification.qr_image = image_content

            print("notification file saved")
    
        notification.save()
        # Create a response with the image content type
        response = HttpResponse(content_type="image/png")
        img.save(response, "PNG")
        
        return response
    except Exception as e:
        print(e)
        return redirect("main:main")
    

def rsvp_event(request, pk):
    try:
        notification = get_object_or_404(PlantationNotificationsModel, pk = pk)

        if request.method == "POST":
            data = request.POST.get("ticket", None)

            if data:
                if data == "general":
                    notification.bought_vip = False
    except Exception as e:
        pass

def download_qr(request, pk):
    # Build the full file path to your image
    notification = get_object_or_404(PlantationNotificationsModel, pk = pk)
    # image_path = os.path.join(settings.MEDIA_ROOT, 'your_image_directory', image_filename)
    if not notification:
        return redirect("main:main")
    
    # Open the image file and create a FileResponse
    # image_path = os.path.join(settings.MEDIA_ROOT, notification.qr_image.url)

    with notification.qr_image.open('rb') as image_file:
        print(image_file)
        response = FileResponse(image_file, as_attachment=True)
    
    return response

def event_detail_view(request, pk):
    event = get_object_or_404(PlantationEventModel, pk=pk)
    notifications = PlantationNotificationsModel.objects.all()
    return render(request, "event-detail.html", { "event": event, "notifications": notifications })
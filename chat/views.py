from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import MessageForm, LoginForm, Upload
from .models import message 
from django.contrib.auth import authenticate, login
from django.views.generic.edit import FormView
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q
from Crypto.PublicKey import RSA
from registration.models import SiteUser
import ast

@csrf_exempt
def messageform(request):
    if 'loggedIn' not in request.session:
        request.session['loggedIn'] = False
    if request.session['loggedIn'] == False:
        form = LoginForm()
        return render(request, 'logintemp.html', {'form': form})

    if request.method == 'POST':

        form = MessageForm(request.POST)
        if form.is_valid():
            new_message = message()

            new_message.message_recipient = form.cleaned_data['recipient']
            new_message.message_content = form.cleaned_data['content']
            new_message.message_encrypted = form.cleaned_data['encrypted']
            # new_message.message_content = request.POST.get("content")
            # print(new_message.message_content)
            # new_message.message_sender = request.user.username
            # new_message.message_encrypted = request.POST.get("encrypted")
            new_message.save()
            # print(new_message.message_content)
            # print(new_message.message_encrypted)

            if new_message.message_encrypted:
                print("here")
                u=SiteUser.objects.get(username=new_message.message_recipient)
                pub_key= u.public_key
                publickeyOBJ = RSA.importKey(pub_key)

                #mes = str(publickeyOBJ.encrypt(new_message.message_content.encode('utf-8'),32))
                mes = publickeyOBJ.encrypt(new_message.message_content.encode('utf-8'),32)

                print(mes)
                new_message.message_content = mes
            #enc_data = pub_key.encrypt(new_message.message_content, 32)
                #dont know how to access recipient public key
            # new_message.message_content = enc_data
                new_message.save()


            new_message.save()

            return render(request, 'cmp_home.html')
        else:
            error_string = ""
            for field in form:
                error_string += field.errors + ", "
            print(error_string)
            return render(request, 'createMessage.html', {'form': form})

        # Go back to appropriate home page
        if request.user.user_type == "CMP_USR":
             return render(request, 'cmp_home.html')
        else:
             return render(request, 'inv_home.html')

    elif request.method == "GET":
        form = MessageForm()
        return render(request, 'createMessage.html', {'form': form})


@csrf_exempt
def viewMessages(request):
    if 'loggedIn' not in request.session:
        request.session['loggedIn'] = False
    if request.session['loggedIn'] == False:
        form = LoginForm()
        return render(request, 'logintemp.html', {'form': form})

    recipient = request.user.username

    print(recipient)

    # only display message sent to the current user
    messages = message.objects.filter(Q(message_recipient__iexact=recipient))
    user = request.user
    messages.noMessages = True
    #u = SiteUser.objects.get(username=new_message.message_recipient)
    for chat in messages:
        messages.noMessages = False


        print(chat.message_recipient)
        print(chat.message_sender)
        #if chat.message_encrypted == True:
        #   decMes = str(user.public_key.decrypt(chat.message_content))
            #print(decMes)
        print(chat.message_content)

    return render(request, 'viewMessages.html', {'messages': messages, 'form': Upload() })

def decrypt(request, message_id):
    if request.method == 'POST':

        form = Upload(request.FILES)
        if form.is_valid():
            file = request.FILES.get('file_field')
            print(file.name)

            #with open(file, 'rb') as in_file:
            readkey = file.read()
            print(eval(readkey))
            key = RSA.importKey(eval(readkey))
            message1 = message.objects.get(pk=message_id)
            # user = request.user
            # u = SiteUser.objects.get(username=new_message.message_recipient)
            encoded = message1.message_content
            #print(encoded)
            message2 = key.decrypt(ast.literal_eval(encoded))
            #readkey = file.read()
            print(encoded)

            print(file.name)

            #key = RSA.importKey(eval(readkey))

            return render(request, 'decrypt.html', {'message': message2})



        #files = request.FILES.get('file_field')


@csrf_exempt
def deleteMessage(request, message_id):

    message.objects.filter(id=message_id).delete()

    recipient = request.user.username

    # only display message sent to the current user
    messages = message.objects.filter(Q(message_recipient__iexact=recipient))

    return render(request, 'viewMessages.html', {'messages': messages})


















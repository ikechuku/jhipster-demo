from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import permission_classes
from ...models.user import User
from ...models.customer import Customer
from ...models.vendor import Vendor
from django.core.mail import send_mail
from decouple import config
from ...utils.helper import random_string_generator

class ForgotPassword(APIView):
    def post(self, request):
        data = request.data
        token = random_string_generator()
        user_name=data['user_name']
        users = User.objects.filter(user_name = user_name)
        user=""
        if users.count() == 1:
            user = users[0]
            user_id = user.id
            user_type = user.user_type
            if user_type=="customer":
                email = Customer.objects.get(user_id = user_id).email

            elif user_type == "vendor":
                email = Vendor.objects.get(user_id = user_id).email

            user.forgot_password_token = token

        else:
            return Response(dict(error="This user_name does not exist"), status=status.HTTP_400_BAD_REQUEST)

        subject = 'Bouncer Password Reset'

        to = [email]
        from_email = config("EMAIL_SENDER")
        reset_password_url = config("RESET_PASSWORD_URL")
        html_content ='Complete your password reset by clicking the link below'
        link_message = f'Reset your password </br> <h6>Token: {token}</h6> </br>  Click on this <a href={reset_password_url}?token={token} ">Link</a> to set a new password'
        message = "A password reset Link has been sent to your Email address"
        msg= send_mail(subject, html_content,from_email,to, fail_silently=False,  html_message=link_message)
        if msg:
            user.save()

            return Response({"message":message}, status=status.HTTP_200_OK)
        return Response({"message":"Error in delivering email"}, status=status.HTTP_400_BAD_REQUEST)
        
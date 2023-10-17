from django.shortcuts import render,redirect
from django.views.generic.base import TemplateView
from django.contrib.auth.models import User, auth
from django.db.models import Sum
from club.models import Club, HomeSlider,Event, Registrations
from django.urls import reverse
# Create your views here.
class Index(TemplateView):
    template_name = "club/index.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['clubs'] = Club.objects.all()
        context['slider'] = HomeSlider.objects.all()[0]
        context['events'] = Event.objects.all()
        return context

class ClubSingle(TemplateView):
    template_name = "club/club-single.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['clubs'] = Club.objects.all()
        id = self.kwargs.get('id')
        context['datas'] = Club.objects.get(id=id)
        return context
class Clubreg(TemplateView):
    template_name = "club/clubreg.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['clubs'] = Club.objects.all()
        return context
    def post(self, request, *args, **kwargs):
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        username=email.split('@')[0]
        selected_values = request.POST.getlist('club')
        user = User.objects.filter(username = username)
        if not user:
            User.objects.create(
                first_name = name,
                username = username,
                email=email,
                password=password
                )
        items = Club.objects.filter(id__in=selected_values)
        total_amount = items.aggregate(total_amount=Sum('reg_fee'))['total_amount']
        print(name,email,password,total_amount)
        # 'checkbox_name' should be replaced with the actual name attribute of your checkbox input

        # Process the selected values
        param1 = total_amount
        registration= Registrations.objects.create(
            user= request.user,

            )
        registration.club.set(selected_values)
        url = reverse('payment') + f'?param1={param1}&param2={registration.id}'
        for value in selected_values:
            print(value)
        return redirect(url)
class Dashboard(TemplateView):
    template_name = "club/dashboard.html"
class Payment(TemplateView):
    template_name = "club/payment.html"
    def post(self, request, *args, **kwargs):
        number = request.POST.get('number')
        trxid= request.POST.get('trxid')
        amount= request.POST.get('amount')
        method= request.POST.get('method')
        regid = request.POST.get('regid')
        print(number,trxid,amount,method,regid)
        my_model_instance = Registrations.objects.get(id=regid)

        # Set new values for the attributes
        my_model_instance.amount = amount
        my_model_instance.payment_number = number
        my_model_instance.trx_id = trxid
        my_model_instance.payment_method = method
        my_model_instance.payment_status = "Completed"
        my_model_instance.save()

        return redirect('index')
class Login(TemplateView):
    template_name = "club/pages-login.html"
    def post(self, request, *args, **kwargs):
        username = request.POST['username']
        password = request.POST['pass']
        print(username)
        print(password)
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('dashboard')
        else:
            return redirect('login')
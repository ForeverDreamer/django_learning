from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.utils.http import is_safe_url
from django.views.generic import CreateView, FormView

from .forms import LoginForm, RegisterForm, GuestForm
from .models import GuestEmail
from .signals import user_logged_in


def guest_register_view(request):
    form = GuestForm(request.POST or None)
    context = {
        "form": form
    }
    next_ = request.GET.get('next')
    next_post = request.POST.get('next')
    redirect_path = next_ or next_post or None
    if form.is_valid():
        print(form.cleaned_data)
        email = form.cleaned_data.get('email')
        new_guest_email = GuestEmail.objects.create(email=email)
        request.session['guest_email_id'] = new_guest_email.email
        if is_safe_url(redirect_path, request.get_host()):
            return redirect(redirect_path)
        else:
            return redirect("/register/")

    return redirect("/register/")


class LoginView(FormView):
    form_class = LoginForm
    template_name = 'accounts/login.html'
    success_url = '/'

    def form_valid(self, form):
        request = self.request
        next_ = request.GET.get('next')
        next_post = request.POST.get('next')
        redirect_path = next_ or next_post or None
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']
        user = authenticate(request, username=email, password=password)
        print("User logged in: ", request.user.is_authenticated())
        if user is not None:
            print("User logged in: ", request.user.is_authenticated())
            login(request, user)
            print("User logged in: ", request.user.is_authenticated())
            user_logged_in.send(user.__class__, instance=user, request=request)
            try:
                del request.session['guest_email_id']
            except:
                pass
            # Redirect to a success page.
            # context['form'] = LoginForm()
            if is_safe_url(redirect_path, request.get_host()):
                return redirect(redirect_path)
            else:
                return redirect("/")

        return super(LoginView, self).form_invalid(form)


class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'accounts/register.html'
    success_url = '/login/'

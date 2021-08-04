from django.shortcuts import render
from .forms import UserRegisterForm, UserUpdateForm
from django.contrib.auth.decorators import login_required

def register(request):

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            # messages.success(request, f'Пользователь {username} был успешно создан!')
            return redirect('home')
    else:
        form = UserRegisterForm()

    form  = UserRegisterForm()
    return render(
    request,
    'users/registration.html',
    {
        'title':'Страница регистрации',
        'form':form
    }
    )

@login_required
def profile(request):
    if request.method == "POST":
        updateUserForm = UserUpdateForm(request.POST, instance=request.user)

        if updateUserForm.is_valid():
            updateUserForm.save()

            messages.success(request, f'Ваш аккаунт был успешно обновлен')
            return redirect('profile')
    else:
        updateUserForm = UserUpdateForm(instance=request.user)

    data = {
        'updateUserForm': updateUserForm,
    }

    return render(request, 'users/profile.html', data)

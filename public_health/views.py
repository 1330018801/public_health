# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.contrib import auth
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

import logging
debug = logging.getLogger('debug')


def login(request):
    message = ''
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        if user and user.is_active:
            auth.login(request, user)
            if user.is_superuser:
                return render(request, 'admin_page.html', {'role': u'超级管理员'})
            if user.is_staff:
                role = user.userprofile.role.name
                debug.info(role)
                return render(request, 'admin_page.html', {'role': role})
            else:
                return render(request, 'user_page.html')
        else:
            message = u'用户不存在或者密码错误'

    return render(request, 'login.html', {'message': message})


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('login'))


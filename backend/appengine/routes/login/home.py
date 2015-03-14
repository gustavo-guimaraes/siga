# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from google.appengine.api import users
from gaecookie.decorator import no_csrf
from gaepermission import facade
from gaepermission.decorator import login_not_required
from tekton import router
from config.template_middleware import TemplateResponse


@login_not_required
@no_csrf
def index():
    return TemplateResponse()

@login_not_required
@no_csrf
def temp1():
    return TemplateResponse(template_path='/login/temp1.html')

@login_not_required
@no_csrf
def temp2():
    return TemplateResponse(template_path='/login/temp2.html')
# -*- coding: utf-8 -*-

from contact import contact_router
from db import admin_router
from essay import essay_router

routers = (
    (contact_router, '/about'),
    (admin_router, '/wqnmlgb'),
    (essay_router, '')
)
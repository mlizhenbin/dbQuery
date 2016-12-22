#!/usr/bin/env python
# coding: utf-8
import web

render = web.template.render('templates/', cache=False)
web.config.debug = True

config = web.storage(
    email='lizhenbin08@sina.com',
    site_name='dbQuery',
    site_desc='',
    static='/static',
)

web.template.Template.globals['config'] = config
web.template.Template.globals['render'] = render

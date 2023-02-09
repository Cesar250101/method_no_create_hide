# -*- coding: utf-8 -*-
from odoo import http

# class MethodNoCreateHide(http.Controller):
#     @http.route('/method_no_create_hide/method_no_create_hide/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/method_no_create_hide/method_no_create_hide/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('method_no_create_hide.listing', {
#             'root': '/method_no_create_hide/method_no_create_hide',
#             'objects': http.request.env['method_no_create_hide.method_no_create_hide'].search([]),
#         })

#     @http.route('/method_no_create_hide/method_no_create_hide/objects/<model("method_no_create_hide.method_no_create_hide"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('method_no_create_hide.object', {
#             'object': obj
#         })
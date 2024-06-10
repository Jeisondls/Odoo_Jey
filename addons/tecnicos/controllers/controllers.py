# -*- coding: utf-8 -*-
# from odoo import http


# class Tecnicos(http.Controller):
#     @http.route('/tecnicos/tecnicos', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/tecnicos/tecnicos/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('tecnicos.listing', {
#             'root': '/tecnicos/tecnicos',
#             'objects': http.request.env['tecnicos.tecnicos'].search([]),
#         })

#     @http.route('/tecnicos/tecnicos/objects/<model("tecnicos.tecnicos"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('tecnicos.object', {
#             'object': obj
#         })


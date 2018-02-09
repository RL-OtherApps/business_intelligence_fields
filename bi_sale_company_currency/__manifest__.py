# -*- encoding: utf-8 -*-
##############################################################################
#
#    bi_sale_company_currency module for Odoo
#    Copyright (C) 2011-2015 Akretion (http://www.akretion.com)
#    @author Alexis de Lattre <alexis.delattre@akretion.com>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################


{
    'name': 'Business intelligence - Sale Order in company currency',
    'version': '0.2',
    'category': 'Sales Management',
    'license': 'AGPL-3',
    'description': """This module adds some fields required to do business intelligence :
it adds the amount in company currency on the sale order lines.""",
    'author': 'Akretion',
    'website': 'http://www.akretion.com/',
    'depends': ['sale'],
    'data': [
        'sale_view.xml',
        'report/sale_report_view.xml',
        'security/ir.model.access.csv',
        ],
    'installable': False,
}

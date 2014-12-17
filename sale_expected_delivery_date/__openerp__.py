# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
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
    'name': "Sale's Expected Delivery Date",
    'version': '0.1',
    'author': 'Ecosoft',
    'summary': "Force using SO's Expected Deivery Date in DO",
    'description': """
This module provides "Expected Delivery Date" in Sales Order.
This date will be used for DO's Scheduled Time instead of standard use of
Product's customer lead time (will be ignored).
""",
    'category': 'Sales Management',
    'website': 'http://ecosoft.co.th',
    'images': [],
    'depends': [
        'delivery',
        'sale',
        'sale_stock',
    ],
    'demo': [],
    'data': [
        'sale_view.xml',
    ],
    'test': [
        'test/test_date_expected.yml',
    ],
    'auto_install': False,
    'application': True,
    'installable': True,
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:

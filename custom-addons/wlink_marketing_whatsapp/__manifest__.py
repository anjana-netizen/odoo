# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Odoo WhatsApp Integration',
    'version': '19.0.1.0',
    'category': 'Marketing',
    'summary': 'Full WhatsApp messaging integration for Odoo with marketing and scheduling features.',
    'description': """
This module integrates Odoo with WhatsApp to enable messaging services, including
message templates, campaign management, scheduling, and advanced marketing features.
""",
    'author': 'WLink',
    'license': 'LGPL-3',
    'images': ['static/description/maketing_banner.jpg'],
    'depends': ['mail', 'contacts', 'phone_validation', 'wlink_whatsapp'],
    'data': [
        'data/whatsapp_templates_preview.xml',
        'security/res_groups.xml',
        'security/ir_rules.xml',
        'security/ir.model.access.csv',
        'wizard/whatsapp_preview_views.xml',
        'wizard/whatsapp_message_schedule_date_views.xml',
        'views/whatsapp_marketing_view.xml',
        'views/whatsapp_marketing_scheduler.xml',
        'views/whatsapp_message_view.xml',
        'views/whatsapp_template_views.xml',
        'views/campaign_list_views.xml',
        'views/whatsapp_menus.xml',
    ],
    'external_dependencies': {
        'python': ['phonenumbers'],
    },
    'assets': {
        'web.assets_backend': [
            'wlink_marketing_whatsapp/static/src/**/*',
            ('remove', 'wlink_marketing_whatsapp/static/src/**/*.dark.scss'),
        ],
        'web.assets_web_dark': [
            'wlink_marketing_whatsapp/static/src/**/*.dark.scss',
        ],
    },
    'application': True,
    'installable': True,
}

{
    'name': 'WhatsApp API Handler',
    'author': 'WLink',
    'license': 'LGPL-3',
    'version': '19.0.1.0',
    'sequence': 1,
    'images': ['static/description/base_banner.jpg'],
    'summary': 'Manage WhatsApp API connections, templates, and synchronization.',
    'description': """
Base module to manage WhatsApp API configurations, template synchronization,
and connection status within Odoo.
""",
    'category': 'Tools',
    'depends': ['mail', 'web', 'contacts'],
    'data': [
        'security/wlink_security.xml',
        'security/ir.model.access.csv',
        'wizard/base_url_editor.xml',
        'wizard/templates_editor.xml',
        'wizard/login_menu.xml',
        'wizard/sync_editor.xml',
        'views/connections.xml',
        'views/menu.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'wlink_whatsapp/static/src/scss/style.scss',
            'wlink_whatsapp/static/src/js/connection_auto_status.js',
        ],
    },
    'installable': True,
    'application': False,
}

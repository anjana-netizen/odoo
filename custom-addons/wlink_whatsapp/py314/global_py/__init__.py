import shelve
from platformdirs import user_config_dir
from pathlib import Path


def generate_payload(self, model='whatsapp_contacts.messaging_menu', template_mode=True, template_name=None, document_name=None):
    payload = {
        'type': 'ir.actions.act_window',
        'name': 'Send Whatsapp Message',
        'res_model': model,
        'target': 'new',
        'view_mode': 'form'
    }

    if template_mode:
        payload['context'] = {  # noqa
            'order': (self.id, self._name),
            'send_to': self.partner_id.phone,
            'template_name': template_name,
            'document_name': document_name,
            'variables': {'(slip-reference)': self.name, '(recipient-name)': self.partner_id.name, '(my-name)': self.env.user.name}
        }
    else:
        phone = self.phone if self._name == 'res.partner' else self.partner_id.phone
        payload['context'] = {'order': (self.id, self._name), 'send_to': phone}

    return payload


class Config:
    def __init__(self, you):  # You is self for the class that instantiated this class
        self.you = you

        with shelve.open(self.config_file) as db:
            db['pos_connection'] = db.get('pos_connection')
            db['default_connection'] = db.get('default_connection')
            db['base_url'] = db.get('base_url')

            if db.get('base_url') is None:
                db['base_url'] = 'https://wlink.geektechsol.com'

            if db.get('templates_text') is None:
                db['templates_text'] = {
                    'sales_quotations': "Hello,\nYour quotation (slip-reference) is ready for review.\n\nDo not hesitate to contact us if you have any questions.\n\n--\n(my-name)",
                    'invoice': "Hello,\nYour invoice (slip-reference) is ready for review.\n\nDo not hesitate to contact us if you have any questions.\n\n--\n(my-name)",
                    'purchase_quotation': "Hello,\nYour quotation (slip-reference) is ready for review.\n\nDo not hesitate to contact us if you have any questions.\n\n--\n(my-name)",
                    'stock.action_report_delivery': "Hello,\nYour delivery slip (slip-reference) is ready for review.\n\nDo not hesitate to contact us if you have any questions.\n\n--\n(my-name)",
                    'stock.action_report_picking': "Hello,\nYour picking operations slip (slip-reference) is ready for review.\n\nDo not hesitate to contact us if you have any questions.\n\n--\n(my-name)"
                }

    @property
    def config_file(self):
        config_dir = Path(user_config_dir("GeekTechSol"))
        config_dir.mkdir(parents=True, exist_ok=True)

        return str(config_dir / f'wlink_config_{self.you.env.cr.dbname}')

    def get_template_text(self, template):
        return self.get('templates_text').get(template, '')

    def set_template_text(self, template, text):
        new_templates_text = self.get('templates_text')
        new_templates_text[template] = text
        return self.set('templates_text', new_templates_text)

    def get(self, name):
        with shelve.open(self.config_file) as db:
            return db[name]

    def set(self, name, value):
        with shelve.open(self.config_file) as db:
            db[name] = value


def fill_text(self, text):
    if self.document_name:
        for variable_name, value in self.env.context['variables'].items():
            if value:
                text = text.replace(variable_name, value)

    return text


def get_from_id(self, model_name, record_id):
    record = self.env[model_name].search([('id', '=', record_id)], limit=1)  # noqa

    if record:
        return record

    return False


def get_default_connection(self, dbname='default_connection'):
    default_connection = Config(self).get(dbname)
    return get_from_id(self, 'whatsapp.connection', default_connection)


def get_phone(phone_c: str) -> str:
    phone_splitted = phone_c.split('@')

    if len(phone_splitted) >= 2:
        phone_splitted.remove(phone_splitted[-1])

    return ''.join(phone_splitted)


def remove_filextension(filename):
    return '.'.join(filename.split('.')[:-1])


def get_filextension(filename):
    return filename.split('.')[-1]


def get_reopen(self, title='Odoo'):
    return {
        'name': title,
        'type': 'ir.actions.act_window',
        'view_mode': 'form',
        'target': 'new',
        'res_model': self._name,
        'res_id': self.id
    }


def get_order(self):
    return get_from_id(self, self.env.context['order'][1], self.env.context['order'][0])

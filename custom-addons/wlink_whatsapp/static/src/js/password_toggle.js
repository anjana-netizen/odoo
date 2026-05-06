odoo.define('wlink_whatsapp.password_toggle', function (require) {
    "use strict";
    var fieldRegistry = require('web.field_registry');
    var AbstractField = require('web.AbstractField');
    var core = require('web.core');

    var PasswordToggle = AbstractField.extend({
        template: 'PasswordToggleWidget',
        supportedFieldTypes: ['char'],
        events: {
            'click .o_password_toggle_eye': '_onTogglePassword',
        },
        init: function () {
            this._super.apply(this, arguments);
            this.showPassword = false;
        },
        _onTogglePassword: function (ev) {
            ev.preventDefault();
            this.showPassword = !this.showPassword;
            this.renderElement();
        },
        _render: function () {
            var self = this;
            this.$el.empty();
            var inputType = this.showPassword ? 'text' : 'password';
            var $input = $('<input>', {
                type: inputType,
                class: 'form-control',
                value: this.value || '',
                readonly: this.mode === 'readonly',
                placeholder: this.attrs.placeholder || '',
                style: 'width: 100%;',
            });
            $input.on('input', function () {
                self._setValue($input.val());
            });
            this.$el.append($input);
            var $eye = $('<span>', {
                class: 'o_password_toggle_eye',
                style: 'margin-left: -30px; cursor: pointer; position: relative; z-index: 2;',
                html: '<i class="fa ' + (this.showPassword ? 'fa-eye-slash' : 'fa-eye') + '"></i>'
            });
            this.$el.append($eye);
        },
    });

    fieldRegistry.add('password_toggle', PasswordToggle);
    return PasswordToggle;
}); 
/** @odoo-module **/

import { patch } from "@web/core/utils/patch";
import { FormController } from "@web/views/form/form_controller";
import { rpc } from "@web/core/network/rpc";

patch(FormController.prototype, {
    async setup() {
        await super.setup(...arguments);

        console.log("[DEBUG] FormController.setup called", {
            resModel: this.props.resModel,
            props: this.props,
        });

        if (this.props.resModel === "whatsapp.connection" && this.props.resId) {
            console.log("[DEBUG] Auto status check: calling check_status for", this.props.resId);

            try {
                await rpc("/web/dataset/call_kw", {
                    model: "whatsapp.connection",
                    method: "check_status",
                    args: [[this.props.resId]],
                    kwargs: {},
                });

                // ✅ Proper way to refresh the form
                await this.model.load();
                this.render();

            } catch (err) {
                console.error("[ERROR] check_status failed:", err);
            }
        }
    },
});

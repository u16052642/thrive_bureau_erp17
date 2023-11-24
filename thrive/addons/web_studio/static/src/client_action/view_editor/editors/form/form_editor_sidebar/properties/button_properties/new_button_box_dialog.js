/** @thrive-module */

import { Component, useState } from "@thrive/owl";
import { Dialog } from "@web/core/dialog/dialog";
import { Many2XAutocomplete } from "@web/views/fields/relational_utils";
import { _t } from "@web/core/l10n/translation";
import { useService } from "@web/core/utils/hooks";
import { ICONS } from "@web_studio/utils";

export class NewButtonBoxDialog extends Component {
    static template = "web_studio.NewButtonBoxDialog";
    static components = {
        Dialog,
        Many2XAutocomplete,
    };
    static props = {
        isAddingButtonBox: { type: Boolean },
        model: { type: Object },
        close: { type: Function },
    };
    setup() {
        this.notification = useService("notification");
        this.state = useState({
            icon: "fa-diamond",
            field: undefined,
        });
        this.text = undefined;
    }
    get icons() {
        return ICONS;
    }
    get title() {
        return _t("Add a Button");
    }
    getDomain() {
        return [
            ["relation", "=", this.props.model.resModel],
            ["ttype", "in", ["many2one", "many2many"]],
            ["store", "=", true],
        ];
    }
    onConfirm() {
        if (!this.state.field?.id) {
            return this.notification.add(_t("Select a related field."));
        }
        if (this.props.isAddingButtonBox) {
            this.props.model.pushOperation({ type: "buttonbox" });
        }
        this.props.model.doOperation({
            type: "add",
            target: {
                tag: "div",
                attrs: {
                    class: "oe_button_box",
                },
            },
            position: "inside",
            node: {
                tag: "button",
                field: this.state.field.id,
                string: this.text || _t("New button"),
                attrs: {
                    class: "oe_stat_button",
                    icon: this.state.icon,
                },
            },
        });
        this.props.close();
    }
}

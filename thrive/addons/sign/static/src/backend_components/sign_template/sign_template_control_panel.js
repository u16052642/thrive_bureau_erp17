/** @thrive-module **/

import { _t } from "@web/core/l10n/translation";
import { useService } from "@web/core/utils/hooks";
import { Component } from "@thrive/owl";
import { ControlPanel } from "@web/search/control_panel/control_panel";
import { multiFileUpload } from "@sign/backend_components/multi_file_upload";

export class SignTemplateControlPanel extends Component {
    setup() {
        this.controlPanelDisplay = {};
        this.nextTemplate = multiFileUpload.getNext() ?? false;
        this.action = useService("action");
        this.orm = useService("orm");
    }

    get showDuplicateButton() {
        return this.props.hasSignRequests && this.props.isPDF;
    }

    get showShareButton() {
        return this.props.actionType !== "sign_send_request" && this.props.responsibleCount <= 1;
    }

    onSendClick() {
        this.action.doAction("sign.action_sign_send_request", {
            additionalContext: {
                active_id: this.props.signTemplate.id,
                sign_directly_without_mail: false,
            },
        });
    }

    onSignNowClick() {
        this.action.doAction("sign.action_sign_send_request", {
            additionalContext: {
                active_id: this.props.signTemplate.id,
                sign_directly_without_mail: true,
            },
        });
    }

    async onShareClick() {
        const action = await this.orm.call("sign.template", "open_shared_sign_request", [
            this.props.signTemplate.id,
        ]);
        this.action.doAction(action);
    }

    async duplicateTemplate() {
        const duplicatedTemplateId = await this.orm.call("sign.template", "copy", [
            this.props.signTemplate.id,
        ]);

        this.action.doAction({
            type: "ir.actions.client",
            tag: "sign.Template",
            name: _t("Duplicated Template"),
            params: {
                id: duplicatedTemplateId,
            },
        });
    }

    onNextDocumentClick() {
        const templateName = this.nextTemplate.name;
        const templateId = parseInt(this.nextTemplate.template);
        multiFileUpload.removeFile(templateId);
        this.action.doAction({
            type: "ir.actions.client",
            tag: "sign.Template",
            name: _t("Template %s", templateName),
            params: {
                sign_edit_call: "sign_template_edit",
                id: templateId,
                sign_directly_without_mail: false,
            },
        });
    }
}

SignTemplateControlPanel.template = "sign.SignTemplateControlPanel";
SignTemplateControlPanel.components = {
    ControlPanel,
};

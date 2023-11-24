/** @thrive-module */

import { registry } from "@web/core/registry";
import { endKnowledgeTour, openCommandBar } from '../knowledge_tour_utils.js';
import { stepUtils } from "@web_tour/tour_service/tour_utils";


registry.category("web_tour.tours").add('knowledge_file_command_tour', {
    url: '/web',
    test: true,
    steps: () => [stepUtils.showAppsMenuItem(), {
    // open the Knowledge App
    trigger: '.o_app[data-menu-xmlid="knowledge.knowledge_menu_root"]',
}, { // open the command bar
    trigger: '.thrive-editor-editable > p',
    run: function () {
        openCommandBar(this.$anchor[0]);
    },
}, { // click on the /file command
    trigger: '.oe-powerbox-commandName:contains("File")',
    run: 'click',
}, { // wait for the media dialog to open
    trigger: '.o_select_media_dialog',
}, { // click on the first item of the modal
    trigger: '.o_existing_attachment_cell:contains(Onboarding)',
    run: 'click'
}, { // wait for the block to appear in the editor
    trigger: '.o_knowledge_behavior_type_file a.o_image',
    run: 'click',
}, {
    trigger: '.o-FileViewer-headerButton[aria-label="Close"]',
    extra_trigger: 'iframe.o-FileViewer-view body:contains(Content)',
    run: 'click',
}, {
    trigger: '.o_knowledge_file_name:contains(Onboarding)',
    run: function() {
        this.$anchor[0].dispatchEvent(new Event('focus'));
    }
}, {
    trigger: 'input[placeholder="Onboarding.txt"]',
    run: function (helpers) {
        helpers.text("Renamed");
        this.$anchor[0].dispatchEvent(new Event('blur'));
    }
}, {
    trigger: '.o_knowledge_file_name > div:contains(Renamed)',
    run: () => {},
}, ...endKnowledgeTour()
]});

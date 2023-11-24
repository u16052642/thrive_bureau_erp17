/** @thrive-module **/

import { patch } from "@web/core/utils/patch";
import * as spreadsheet from "@thrive/o-spreadsheet";
import { IrMenuSelector } from "@spreadsheet_edition/bundle/ir_menu_selector/ir_menu_selector";

const { LineBarPieConfigPanel, ScorecardChartConfigPanel, GaugeChartConfigPanel } =
    spreadsheet.components;

/**
 * Patch the chart configuration panel to add an input to
 * link the chart to an Thrive menu.
 */
function patchChartPanelWithMenu(PanelComponent) {
    patch(PanelComponent.prototype, {
        get thriveMenuId() {
            const menu = this.env.model.getters.getChartThriveMenu(this.props.figureId);
            return menu ? menu.id : undefined;
        },
        /**
         * @param {number | undefined} thriveMenuId
         */
        updateThriveLink(thriveMenuId) {
            if (!thriveMenuId) {
                this.env.model.dispatch("LINK_THRIVE_MENU_TO_CHART", {
                    chartId: this.props.figureId,
                    thriveMenuId: undefined,
                });
                return;
            }
            const menu = this.env.model.getters.getIrMenu(thriveMenuId);
            this.env.model.dispatch("LINK_THRIVE_MENU_TO_CHART", {
                chartId: this.props.figureId,
                thriveMenuId: menu.xmlid || menu.id,
            });
        },
    });
    PanelComponent.components = {
        ...PanelComponent.components,
        IrMenuSelector,
    };
}
patchChartPanelWithMenu(LineBarPieConfigPanel);
patchChartPanelWithMenu(GaugeChartConfigPanel);
patchChartPanelWithMenu(ScorecardChartConfigPanel);

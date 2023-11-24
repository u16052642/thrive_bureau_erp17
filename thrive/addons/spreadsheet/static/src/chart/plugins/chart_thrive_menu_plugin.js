/** @thrive-module */

import { coreTypes, CorePlugin } from "@thrive/o-spreadsheet";

/** Plugin that link charts with Thrive menus. It can contain either the Id of the thrive menu, or its xml id. */
export class ChartThriveMenuPlugin extends CorePlugin {
    constructor(config) {
        super(config);
        this.thriveMenuReference = {};
    }

    /**
     * Handle a spreadsheet command
     * @param {Object} cmd Command
     */
    handle(cmd) {
        switch (cmd.type) {
            case "LINK_THRIVE_MENU_TO_CHART":
                this.history.update("thriveMenuReference", cmd.chartId, cmd.thriveMenuId);
                break;
            case "DELETE_FIGURE":
                this.history.update("thriveMenuReference", cmd.id, undefined);
                break;
        }
    }

    /**
     * Get thrive menu linked to the chart
     *
     * @param {string} chartId
     * @returns {object | undefined}
     */
    getChartThriveMenu(chartId) {
        const menuId = this.thriveMenuReference[chartId];
        return menuId ? this.getters.getIrMenu(menuId) : undefined;
    }

    import(data) {
        if (data.chartThriveMenusReferences) {
            this.thriveMenuReference = data.chartThriveMenusReferences;
        }
    }

    export(data) {
        data.chartThriveMenusReferences = this.thriveMenuReference;
    }
}
ChartThriveMenuPlugin.getters = ["getChartThriveMenu"];

coreTypes.add("LINK_THRIVE_MENU_TO_CHART");

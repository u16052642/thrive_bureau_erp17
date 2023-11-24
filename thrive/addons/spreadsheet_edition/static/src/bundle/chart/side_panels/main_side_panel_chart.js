/** @thrive-module **/

import { patch } from "@web/core/utils/patch";
import * as spreadsheet from "@thrive/o-spreadsheet";

const { chartRegistry } = spreadsheet.registries;
const { ChartPanel } = spreadsheet.components;

/**
 * This patch is necessary to ensure that the chart type cannot be changed
 * between thrive charts and spreadsheet charts.
 */

patch(ChartPanel.prototype, {
    get chartTypes() {
        const definition = this.getChartDefinition();
        const isThrive = definition.type.startsWith("thrive_");
        return this.getChartTypes(isThrive);
    },

    /**
     * @param {boolean} isThrive
     */
    getChartTypes(isThrive) {
        const result = {};
        for (const key of chartRegistry.getKeys()) {
            if ((isThrive && key.startsWith("thrive_")) || (!isThrive && !key.startsWith("thrive_"))) {
                result[key] = chartRegistry.get(key).name;
            }
        }
        return result;
    },

    onTypeChange(type) {
        if (this.getChartDefinition().type.startsWith("thrive_")) {
            const definition = {
                stacked: false,
                verticalAxisPosition: "left",
                ...this.env.model.getters.getChartDefinition(this.figureId),
                type,
            };
            this.env.model.dispatch("UPDATE_CHART", {
                definition,
                id: this.figureId,
                sheetId: this.env.model.getters.getActiveSheetId(),
            });
        } else {
            super.onTypeChange(type);
        }
    },
});

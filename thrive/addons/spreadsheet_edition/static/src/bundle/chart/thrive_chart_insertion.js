/** @thrive-module **/

import * as spreadsheet from "@thrive/o-spreadsheet";
import { initCallbackRegistry } from "@spreadsheet/o_spreadsheet/init_callbacks";
import { Domain } from "@web/core/domain";

const uuidGenerator = new spreadsheet.helpers.UuidGenerator();

export function insertChart(chartData) {
    const definition = {
        metaData: {
            groupBy: chartData.metaData.groupBy,
            measure: chartData.metaData.measure,
            order: chartData.metaData.order,
            resModel: chartData.metaData.resModel,
        },
        searchParams: {
            ...chartData.searchParams,
            domain: new Domain(chartData.searchParams.domain).toJson(),
        },
        stacked: chartData.metaData.stacked,
        cumulative: chartData.metaData.cumulated,
        title: chartData.name,
        background: "#FFFFFF",
        legendPosition: "top",
        verticalAxisPosition: "left",
        type: `thrive_${chartData.metaData.mode}`,
        dataSourceId: uuidGenerator.uuidv4(),
        id: uuidGenerator.uuidv4(),
    };
    return (model) => {
        model.dispatch("CREATE_CHART", {
            sheetId: model.getters.getActiveSheetId(),
            id: definition.id,
            position: {
                x: 10,
                y: 10,
            },
            definition,
        });
        if (chartData.menuXMLId) {
            model.dispatch("LINK_THRIVE_MENU_TO_CHART", {
                chartId: definition.id,
                thriveMenuId: chartData.menuXMLId,
            });
        }
    };
}

initCallbackRegistry.add("insertChart", insertChart);

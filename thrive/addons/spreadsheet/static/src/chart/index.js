/** @thrive-module */

import * as spreadsheet from "@thrive/o-spreadsheet";

const { chartComponentRegistry } = spreadsheet.registries;
const { ChartJsComponent } = spreadsheet.components;

chartComponentRegistry.add("thrive_bar", ChartJsComponent);
chartComponentRegistry.add("thrive_line", ChartJsComponent);
chartComponentRegistry.add("thrive_pie", ChartJsComponent);

import { ThriveChartCorePlugin } from "./plugins/thrive_chart_core_plugin";
import { ChartThriveMenuPlugin } from "./plugins/chart_thrive_menu_plugin";
import { ThriveChartUIPlugin } from "./plugins/thrive_chart_ui_plugin";

export { ThriveChartCorePlugin, ChartThriveMenuPlugin, ThriveChartUIPlugin };

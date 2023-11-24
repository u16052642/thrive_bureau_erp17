/** @thrive-module */

import * as spreadsheet from "@thrive/o-spreadsheet";
import { CommonThriveChartConfigPanel } from "./common/config_panel";
import { ThriveBarChartConfigPanel } from "./thrive_bar/thrive_bar_config_panel";
import { ThriveLineChartConfigPanel } from "./thrive_line/thrive_line_config_panel";

const { chartSidePanelComponentRegistry } = spreadsheet.registries;
const { LineBarPieDesignPanel } = spreadsheet.components;

chartSidePanelComponentRegistry
    .add("thrive_line", {
        configuration: ThriveLineChartConfigPanel,
        design: LineBarPieDesignPanel,
    })
    .add("thrive_bar", {
        configuration: ThriveBarChartConfigPanel,
        design: LineBarPieDesignPanel,
    })
    .add("thrive_pie", {
        configuration: CommonThriveChartConfigPanel,
        design: LineBarPieDesignPanel,
    });

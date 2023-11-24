/** @thrive-module */

import { CommonThriveChartConfigPanel } from "../common/config_panel";

export class ThriveBarChartConfigPanel extends CommonThriveChartConfigPanel {
    onUpdateStacked(ev) {
        this.props.updateChart(this.props.figureId, {
            stacked: ev.target.checked,
        });
    }
}

ThriveBarChartConfigPanel.template = "spreadsheet_edition.ThriveBarChartConfigPanel";

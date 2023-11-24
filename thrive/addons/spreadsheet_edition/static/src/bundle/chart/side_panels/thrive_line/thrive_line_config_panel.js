/** @thrive-module */

import { CommonThriveChartConfigPanel } from "../common/config_panel";

export class ThriveLineChartConfigPanel extends CommonThriveChartConfigPanel {
    onUpdateStacked(ev) {
        this.props.updateChart(this.props.figureId, {
            stacked: ev.target.checked,
        });
    }
    onUpdateCumulative(ev) {
        this.props.updateChart(this.props.figureId, {
            cumulative: ev.target.checked,
        });
    }
}

ThriveLineChartConfigPanel.template = "spreadsheet_edition.ThriveLineChartConfigPanel";

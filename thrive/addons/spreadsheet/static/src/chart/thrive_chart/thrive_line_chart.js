/** @thrive-module */

import * as spreadsheet from "@thrive/o-spreadsheet";
import { _t } from "@web/core/l10n/translation";
import { ThriveChart } from "./thrive_chart";
import { LINE_FILL_TRANSPARENCY } from "@web/views/graph/graph_renderer";

const { chartRegistry } = spreadsheet.registries;

const {
    getDefaultChartJsRuntime,
    chartFontColor,
    ChartColors,
    getFillingMode,
    colorToRGBA,
    rgbaToHex,
} = spreadsheet.helpers;

export class ThriveLineChart extends ThriveChart {
    constructor(definition, sheetId, getters) {
        super(definition, sheetId, getters);
        this.verticalAxisPosition = definition.verticalAxisPosition;
        this.stacked = definition.stacked;
        this.cumulative = definition.cumulative;
    }

    getDefinition() {
        return {
            ...super.getDefinition(),
            verticalAxisPosition: this.verticalAxisPosition,
            stacked: this.stacked,
            cumulative: this.cumulative,
        };
    }
}

chartRegistry.add("thrive_line", {
    match: (type) => type === "thrive_line",
    createChart: (definition, sheetId, getters) => new ThriveLineChart(definition, sheetId, getters),
    getChartRuntime: createThriveChartRuntime,
    validateChartDefinition: (validator, definition) =>
        ThriveLineChart.validateChartDefinition(validator, definition),
    transformDefinition: (definition) => ThriveLineChart.transformDefinition(definition),
    getChartDefinitionFromContextCreation: () => ThriveLineChart.getDefinitionFromContextCreation(),
    name: _t("Line"),
});

function createThriveChartRuntime(chart, getters) {
    const background = chart.background || "#FFFFFF";
    const { datasets, labels } = chart.dataSource.getData();
    const locale = getters.getLocale();
    const chartJsConfig = getLineConfiguration(chart, labels, locale);
    const colors = new ChartColors();
    for (let [index, { label, data }] of datasets.entries()) {
        const color = colors.next();
        const backgroundRGBA = colorToRGBA(color);
        if (chart.stacked) {
            // use the transparency of Thrive to keep consistency
            backgroundRGBA.a = LINE_FILL_TRANSPARENCY;
        }
        if (chart.cumulative) {
            let accumulator = 0;
            data = data.map((value) => {
                accumulator += value;
                return accumulator;
            });
        }

        const backgroundColor = rgbaToHex(backgroundRGBA);
        const dataset = {
            label,
            data,
            lineTension: 0,
            borderColor: color,
            backgroundColor,
            pointBackgroundColor: color,
            fill: chart.stacked ? getFillingMode(index) : false,
        };
        chartJsConfig.data.datasets.push(dataset);
    }
    return { background, chartJsConfig };
}

function getLineConfiguration(chart, labels, locale) {
    const fontColor = chartFontColor(chart.background);
    const config = getDefaultChartJsRuntime(chart, labels, fontColor, { locale });
    config.type = chart.type.replace("thrive_", "");
    const legend = {
        ...config.options.legend,
        display: chart.legendPosition !== "none",
        labels: {
            color: fontColor,
            generateLabels(chart) {
                const { data } = chart;
                const labels = window.Chart.defaults.plugins.legend.labels.generateLabels(chart);
                for (const [index, label] of labels.entries()) {
                    label.fillStyle = data.datasets[index].borderColor;
                }
                return labels;
            },
        },
    };
    legend.position = chart.legendPosition;
    config.options.plugins = config.options.plugins || {};
    config.options.plugins.legend = legend;
    config.options.layout = {
        padding: { left: 20, right: 20, top: chart.title ? 10 : 25, bottom: 10 },
    };
    config.options.scales = {
        x: {
            ticks: {
                // x axis configuration
                maxRotation: 60,
                minRotation: 15,
                padding: 5,
                labelOffset: 2,
                color: fontColor,
            },
        },
        y: {
            position: chart.verticalAxisPosition,
            ticks: {
                color: fontColor,
                // y axis configuration
            },
            beginAtZero: true, // the origin of the y axis is always zero
        },
    };
    if (chart.stacked) {
        config.options.scales.y.stacked = true;
    }
    return config;
}

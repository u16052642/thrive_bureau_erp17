 /** @thrive-module **/

import { serializeDateTime } from "@web/core/l10n/dates";
import { GanttModel, parseServerValues } from "@web_gantt/gantt_model";
import {_t} from "@web/core/l10n/translation";
import { Domain } from "@web/core/domain";

export class AttendanceGanttModel extends GanttModel {
    //-------------------------------------------------------------------------
    // Protected
    //-------------------------------------------------------------------------

    /**
     * @override
     */
     _getDomain(metaData) {
        const { dateStartField, dateStopField, startDate, stopDate } = metaData;
        const dateNow = luxon.DateTime.now()
        if (dateNow >= startDate) {
            const domain = Domain.and([
                this.searchParams.domain,
                [
                    "|",
                    '&',
                    [dateStartField, "<=", serializeDateTime(dateNow)],
                    [dateStopField, "=", false],
                    "&",
                    [dateStartField, "<=", serializeDateTime(stopDate)],
                    [dateStopField, ">=", serializeDateTime(startDate)],
                ],
            ])
            return domain.toList()
        }
        else {
            return super._getDomain(...arguments);
        }
    }

    _addProgressBarInfo(_, rows) {
        super._addProgressBarInfo(...arguments);
        for (const row of rows) {
            if (row.progressBar) {
                if (row.progressBar.value_formatted) {
                    row.progressBar.value_formatted += _t(" h");
                }
                if (row.progressBar.max_value_formatted) {
                    row.progressBar.max_value_formatted += _t(" h");
                }
            }
        }
    }

    async _fetchData(metaData) {
        const startDate = metaData.startDate.toISODate();
        const context = {
            gantt_start_date: startDate,
            user_domain: this.searchParams.domain
        };
        await super._fetchData(metaData, context);
    }

    _parseServerData(metaData, records) {
        const {
            dateStartField,
            dateStopField,
            fields,
        } = metaData;
        /** @type {Record<string, any>[]} */
        const parsedRecords = super._parseServerData(...arguments);
        for (const record of records) {
            const parsedRecord = parseServerValues(fields, record);
            const dateStart = parsedRecord[dateStartField];
            const dateStop = parsedRecord[dateStopField];
            if (!this.orm.isSample && dateStart && !dateStop) {
                parsedRecord[dateStopField] = luxon.DateTime.now();
                parsedRecords.push(parsedRecord);
            }
        }
        return parsedRecords;
    }
}

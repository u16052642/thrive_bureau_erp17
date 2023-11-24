/** @thrive-module **/

import { _t } from "@web/core/l10n/translation";
import { getThriveFunctions } from "../helpers/thrive_functions_helpers";

export const pivotFormulaRegex = /^=.*PIVOT/;

//--------------------------------------------------------------------------
// Public
//--------------------------------------------------------------------------

/**
 * Parse a spreadsheet formula and detect the number of PIVOT functions that are
 * present in the given formula.
 *
 * @param {string} formula
 *
 * @returns {number}
 */
export function getNumberOfPivotFormulas(formula) {
    return getThriveFunctions(formula, [
        "THRIVE.PIVOT",
        "THRIVE.PIVOT.HEADER",
        "THRIVE.PIVOT.POSITION",
        "THRIVE.PIVOT.TABLE",
    ]).length;
}

/**
 * Get the first Pivot function description of the given formula.
 *
 * @param {string} formula
 *
 * @returns {import("../helpers/thrive_functions_helpers").ThriveFunctionDescription|undefined}
 */
export function getFirstPivotFunction(formula) {
    return getThriveFunctions(formula, [
        "THRIVE.PIVOT",
        "THRIVE.PIVOT.HEADER",
        "THRIVE.PIVOT.POSITION",
        "THRIVE.PIVOT.TABLE",
    ])[0];
}

/**
 * Build a pivot formula expression
 *
 * @param {string} formula formula to be used (PIVOT or PIVOT.HEADER)
 * @param {*} args arguments of the formula
 *
 * @returns {string}
 */
export function makePivotFormula(formula, args) {
    return `=${formula}(${args
        .map((arg) =>
            typeof arg == "number" || (typeof arg == "string" && !isNaN(arg))
                ? `${arg}`
                : `"${arg.toString().replace(/"/g, '\\"')}"`
        )
        .join(",")})`;
}

export const PERIODS = {
    day: _t("Day"),
    week: _t("Week"),
    month: _t("Month"),
    quarter: _t("Quarter"),
    year: _t("Year"),
};

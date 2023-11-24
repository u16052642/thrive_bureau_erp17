/** @thrive-module */

import { getThriveFunctions } from "../helpers/thrive_functions_helpers";

/**
 * Parse a spreadsheet formula and detect the number of LIST functions that are
 * present in the given formula.
 *
 * @param {string} formula
 *
 * @returns {number}
 */
export function getNumberOfListFormulas(formula) {
    return getThriveFunctions(formula, ["THRIVE.LIST", "THRIVE.LIST.HEADER"]).length;
}

/**
 * Get the first List function description of the given formula.
 *
 * @param {string} formula
 *
 * @returns {import("../helpers/thrive_functions_helpers").ThriveFunctionDescription|undefined}
 */
export function getFirstListFunction(formula) {
    return getThriveFunctions(formula, ["THRIVE.LIST", "THRIVE.LIST.HEADER"])[0];
}

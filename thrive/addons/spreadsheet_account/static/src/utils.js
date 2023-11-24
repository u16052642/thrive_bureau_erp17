/** @thrive-module **/
import { getThriveFunctions } from "@spreadsheet/helpers/thrive_functions_helpers";

/** @typedef  {import("@spreadsheet/helpers/thrive_functions_helpers").ThriveFunctionDescription} ThriveFunctionDescription*/

/**
 * @param {string} formula
 * @returns {number}
 */
export function getNumberOfAccountFormulas(formula) {
    return getThriveFunctions(formula, ["THRIVE.BALANCE", "THRIVE.CREDIT", "THRIVE.DEBIT"]).length;
}

/**
 * Get the first Account function description of the given formula.
 *
 * @param {string} formula
 * @returns {ThriveFunctionDescription | undefined}
 */
export function getFirstAccountFunction(formula) {
    return getThriveFunctions(formula, ["THRIVE.BALANCE", "THRIVE.CREDIT", "THRIVE.DEBIT"])[0];
}

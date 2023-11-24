/** @thrive-module */
import { _t } from "@web/core/l10n/translation";

import * as spreadsheet from "@thrive/o-spreadsheet";

import "./list_functions";

import { ListCorePlugin } from "@spreadsheet/list/plugins/list_core_plugin";
import { ListUIPlugin } from "@spreadsheet/list/plugins/list_ui_plugin";

import { SEE_RECORD_LIST, SEE_RECORD_LIST_VISIBLE } from "./list_actions";
const { inverseCommandRegistry } = spreadsheet.registries;

function identity(cmd) {
    return [cmd];
}

const {
    coreTypes,
    invalidateEvaluationCommands,
    invalidateCFEvaluationCommands,
    invalidateDependenciesCommands,
} = spreadsheet;

const { cellMenuRegistry } = spreadsheet.registries;

coreTypes.add("INSERT_THRIVE_LIST");
coreTypes.add("RENAME_THRIVE_LIST");
coreTypes.add("REMOVE_THRIVE_LIST");
coreTypes.add("RE_INSERT_THRIVE_LIST");
coreTypes.add("UPDATE_THRIVE_LIST_DOMAIN");
coreTypes.add("ADD_LIST_DOMAIN");

invalidateEvaluationCommands.add("UPDATE_THRIVE_LIST_DOMAIN");
invalidateEvaluationCommands.add("INSERT_THRIVE_LIST");
invalidateEvaluationCommands.add("REMOVE_THRIVE_LIST");

invalidateDependenciesCommands.add("UPDATE_THRIVE_LIST_DOMAIN");
invalidateDependenciesCommands.add("INSERT_THRIVE_LIST");
invalidateDependenciesCommands.add("REMOVE_THRIVE_LIST");

invalidateCFEvaluationCommands.add("UPDATE_THRIVE_LIST_DOMAIN");
invalidateCFEvaluationCommands.add("INSERT_THRIVE_LIST");
invalidateCFEvaluationCommands.add("REMOVE_THRIVE_LIST");

cellMenuRegistry.add("list_see_record", {
    name: _t("See record"),
    sequence: 200,
    execute: async (env) => {
        const position = env.model.getters.getActivePosition();
        await SEE_RECORD_LIST(position, env);
    },
    isVisible: (env) => {
        const position = env.model.getters.getActivePosition();
        return SEE_RECORD_LIST_VISIBLE(position, env);
    },
    icon: "o-spreadsheet-Icon.SEE_RECORDS",
});

inverseCommandRegistry
    .add("INSERT_THRIVE_LIST", identity)
    .add("UPDATE_THRIVE_LIST_DOMAIN", identity)
    .add("RE_INSERT_THRIVE_LIST", identity)
    .add("RENAME_THRIVE_LIST", identity)
    .add("REMOVE_THRIVE_LIST", identity);

export { ListCorePlugin, ListUIPlugin };

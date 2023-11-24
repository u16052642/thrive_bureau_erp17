/** @thrive-module */

import * as spreadsheet from "@thrive/o-spreadsheet";
import { registry } from "@web/core/registry";
import { actionService } from "@web/webclient/actions/action_service";
import { menuService } from "@web/webclient/menus/menu_service";
import { spreadsheetLinkMenuCellService } from "@spreadsheet/ir_ui_menu/index";
import { makeTestEnv } from "@web/../tests/helpers/mock_env";
import { getMenuServerData } from "@spreadsheet/../tests/links/menu_data_utils";
import { patchWithCleanup } from "@web/../tests/helpers/utils";
import { getEvaluatedCell } from "../utils/getters";

const { Model } = spreadsheet;
const { urlRepresentation, openLink } = spreadsheet.links;

function beforeEach() {
    registry
        .category("services")
        .add("menu", menuService)
        .add("action", actionService)
        .add("spreadsheetLinkMenuCell", spreadsheetLinkMenuCellService);
}

QUnit.module("spreadsheet > link", { beforeEach });

QUnit.test("click a web link", async (assert) => {
    patchWithCleanup(window, {
        open: (href) => {
            assert.step(href.toString());
        },
    });
    const env = await makeTestEnv();
    const data = {
        sheets: [
            {
                cells: { A1: { content: "[Thrive](https://thrivebureau.com)" } },
            },
        ],
    };
    const model = new Model(data, { custom: { env } });
    const cell = getEvaluatedCell(model, "A1");
    assert.strictEqual(urlRepresentation(cell.link, model.getters), "https://thrivebureau.com");
    openLink(cell.link, env);
    assert.verifySteps(["https://thrivebureau.com"]);
});

QUnit.test("click a menu link", async (assert) => {
    const fakeActionService = {
        name: "action",
        start() {
            return {
                doAction(action) {
                    assert.step(action);
                },
            };
        },
    };
    registry.category("services").add("action", fakeActionService, { force: true });
    const env = await makeTestEnv({ serverData: getMenuServerData() });
    const data = {
        sheets: [
            {
                cells: { A1: { content: "[label](thrive://ir_menu_xml_id/test_menu)" } },
            },
        ],
    };
    const model = new Model(data, { custom: { env } });
    const cell = getEvaluatedCell(model, "A1");
    assert.strictEqual(urlRepresentation(cell.link, model.getters), "menu with xmlid");
    openLink(cell.link, env);
    assert.verifySteps(["action1"]);
});

QUnit.test("click a menu link", async (assert) => {
    const fakeActionService = {
        name: "action",
        start() {
            return {
                doAction(action) {
                    assert.step("do-action");
                    assert.deepEqual(action, {
                        context: undefined,
                        domain: undefined,
                        name: "an thrive view",
                        res_model: "partner",
                        target: "current",
                        type: "ir.actions.act_window",
                        views: [[false, "list"]],
                    });
                },
            };
        },
    };
    registry.category("services").add("action", fakeActionService, { force: true });
    const env = await makeTestEnv({ serverData: getMenuServerData() });
    const view = {
        name: "an thrive view",
        viewType: "list",
        action: {
            modelName: "partner",
            views: [[false, "list"]],
        },
    };
    const data = {
        sheets: [
            {
                cells: { A1: { content: `[a view](thrive://view/${JSON.stringify(view)})` } },
            },
        ],
    };
    const model = new Model(data, { custom: { env } });
    const cell = getEvaluatedCell(model, "A1");
    assert.strictEqual(urlRepresentation(cell.link, model.getters), "an thrive view");
    openLink(cell.link, env);
    assert.verifySteps(["do-action"]);
});

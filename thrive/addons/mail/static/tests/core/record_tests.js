/* @thrive-module */

import { Record, modelRegistry } from "@mail/core/common/record";
import { BaseStore, makeStore } from "@mail/core/common/store_service";

import { registry } from "@web/core/registry";
import { clearRegistryWithCleanup, makeTestEnv } from "@web/../tests/helpers/mock_env";
import { markup } from "@thrive/owl";

const serviceRegistry = registry.category("services");

let start;
QUnit.module("record", {
    beforeEach() {
        serviceRegistry.add("store", { start: (env) => makeStore(env) });
        clearRegistryWithCleanup(modelRegistry);
        Record.register();
        ({ Store: class extends BaseStore {} }).Store.register();
        start = async () => {
            const env = await makeTestEnv();
            return env.services.store;
        };
    },
});

QUnit.test("Insert by passing only single-id value (non-relational)", async (assert) => {
    (class Persona extends Record {
        static id = "name";
        name;
    }).register();
    const store = await start();
    const john = store.Persona.insert("John");
    assert.strictEqual(john.name, "John");
});

QUnit.test("Can pass object as data for relational field with inverse as id", async (assert) => {
    (class Thread extends Record {
        static id = "name";
        name;
        composer = Record.one("Composer", { inverse: "thread" });
    }).register();
    (class Composer extends Record {
        static id = "thread";
        thread = Record.one("Thread");
    }).register();
    const store = await start();
    const thread = store.Thread.insert("General");
    Object.assign(thread, { composer: {} });
    assert.ok(thread.composer);
    assert.ok(thread.composer.thread.eq(thread));
});

QUnit.test("Assign & Delete on fields with inverses", async (assert) => {
    (class Thread extends Record {
        static id = "name";
        name;
        composer = Record.one("Composer", { inverse: "thread" });
        members = Record.many("Member", { inverse: "thread" });
        messages = Record.many("Message", { inverse: "threads" });
    }).register();
    (class Composer extends Record {
        static id = "thread";
        thread = Record.one("Thread");
    }).register();
    (class Member extends Record {
        static id = "name";
        name;
        thread = Record.one("Thread");
    }).register();
    (class Message extends Record {
        static id = "content";
        content;
        threads = Record.many("Thread");
    }).register();
    const store = await start();
    const thread = store.Thread.insert("General");
    const [john, marc] = store.Member.insert(["John", "Marc"]);
    const [hello, world] = store.Message.insert(["hello", "world"]);
    // Assign on fields should adapt inverses
    Object.assign(thread, { composer: {}, members: [["ADD", john]], messages: [hello, world] });
    assert.ok(thread.composer);
    assert.ok(thread.composer.thread.eq(thread));
    assert.ok(john.thread.eq(thread));
    assert.ok(john.in(thread.members));
    assert.ok(hello.in(thread.messages));
    assert.ok(world.in(thread.messages));
    assert.ok(thread.in(hello.threads));
    assert.ok(thread.in(world.threads));
    // add() should adapt inverses
    thread.members.add(marc);
    assert.ok(marc.in(thread.members));
    assert.ok(marc.thread.eq(thread));
    // delete should adapt inverses
    thread.members.delete(john);
    assert.notOk(john.in(thread.members));
    assert.notOk(john.thread);
    // can delete with command
    thread.messages = [["DELETE", world]];
    assert.notOk(world.in(thread.messages));
    assert.notOk(thread.in(world.threads));
    assert.ok(thread.messages.length === 1);
    assert.ok(hello.in(thread.messages));
    assert.ok(thread.in(hello.threads));
    // Deletion removes all relations
    const composer = thread.composer;
    thread.delete();
    assert.notOk(thread.composer);
    assert.notOk(composer.thread);
    assert.notOk(marc.in(thread.members));
    assert.ok(thread.members.length === 0);
    assert.notOk(hello.in(thread.messages));
    assert.notOk(thread.in(hello.threads));
    assert.ok(thread.messages.length === 0);
});

QUnit.test("Computed relational field", async (assert) => {
    (class Thread extends Record {
        static id = "name";
        name;
        admin = Record.one("Persona", {
            compute() {
                return this.members[0];
            },
        });
        members = Record.many("Persona");
    }).register();
    (class Persona extends Record {
        static id = "name";
        name;
    }).register();
    const store = await start();
    const thread = store.Thread.insert("General");
    const [john, marc] = store.Persona.insert(["John", "Marc"]);
    Object.assign(thread, { members: [john, marc] });
    assert.ok(thread.admin.eq(john));
    thread.members.delete(john);
    assert.ok(thread.admin.eq(marc));
});

QUnit.test("Trusted insert on html field with { html: true }", async (assert) => {
    (class Message extends Record {
        static id = "body";
        body = Record.attr("", { html: true });
    }).register();
    const store = await start();
    const hello = store.Message.insert("<p>hello</p>", { html: true });
    const world = store.Message.insert("<p>world</p>");
    assert.ok(hello.body instanceof markup("").constructor);
    assert.strictEqual(hello.body.toString(), "<p>hello</p>");
    assert.strictEqual(world.body, "<p>world</p>");
});

QUnit.test("Unshift preserves order", async (assert) => {
    (class Message extends Record {
        static id = "id";
        id;
    }).register();
    (class Thread extends Record {
        static id = "name";
        name;
        messages = Record.many("Message");
    }).register();
    const store = await start();
    const thread = store.Thread.insert({ name: "General" });
    thread.messages.unshift({ id: 3 }, { id: 2 }, { id: 1 });
    assert.deepEqual(
        thread.messages.map((msg) => msg.id),
        [3, 2, 1]
    );
    thread.messages.unshift({ id: 6 }, { id: 5 }, { id: 4 });
    assert.deepEqual(
        thread.messages.map((msg) => msg.id),
        [6, 5, 4, 3, 2, 1]
    );
    thread.messages.unshift({ id: 7 });
    assert.deepEqual(
        thread.messages.map((msg) => msg.id),
        [7, 6, 5, 4, 3, 2, 1]
    );
});

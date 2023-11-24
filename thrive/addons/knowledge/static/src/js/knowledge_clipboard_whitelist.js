/** @thrive-module */

import { CLIPBOARD_WHITELISTS } from '@web_editor/js/editor/thrive-editor/src/ThriveEditor';

/**
 * Allow @see o_knowledge_ classes to be preserved in the editor on paste.
 */
CLIPBOARD_WHITELISTS.classes.push(/^o_knowledge_/);

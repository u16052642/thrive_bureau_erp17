/** @thrive-module **/

    import publicWidget from "@web/legacy/js/public/public_widget";
    import { loadJS } from "@web/core/assets";
    /* global ThriveFin */

    publicWidget.registry.OnlineSyncPortal = publicWidget.Widget.extend({
        selector: '.oe_online_sync',
        events: Object.assign({}, {
            'click #renew_consent_button': '_onRenewConsent',
        }),

        ThriveFinConnector: function (parent, action) {
            // Ensure that the proxyMode is valid
            const modeRegexp = /^[a-z0-9-_]+$/i;
            if (!modeRegexp.test(action.params.proxyMode)) {
                return;
            }
            const url = 'https://' + action.params.proxyMode + '.thrivefin.com/proxy/v1/thrivefin_link';

            loadJS(url)
                .then(() => {
                    // Create and open the iframe
                    const params = {
                        data: action.params,
                        proxyMode: action.params.proxyMode,
                        onEvent: function (event, data) {
                            switch (event) {
                                case 'success':
                                    const processUrl = window.location.pathname + '/complete' + window.location.search;
                                    $('.js_reconnect').toggleClass('d-none');
                                    $.post(processUrl, {csrf_token: thrive.csrf_token});
                                default:
                                    return;
                            }
                        },
                    };
                    ThriveFin.create(params);
                    ThriveFin.open();
                });
            return;
        },

        /**
         * @private
         * @param {Event} ev
         */
        _onRenewConsent: async function (ev) {
            ev.preventDefault();
            const action = JSON.parse($(ev.currentTarget).attr('iframe-params'));
            return this.ThriveFinConnector(this, action);
        },
    });

    export default {
        OnlineSyncPortal: publicWidget.registry.OnlineSyncPortal,
    };

/** @thrive-module **/

import { Component } from "@thrive/owl";

export class Navbar extends Component {}

Navbar.template = "frontdesk.Navbar";
Navbar.props = {
    companyInfo: Object,
    currentComponent: String,
    isMobile: Boolean,
    isPlannedVisitors: Boolean,
    showScreen: Function,
    onChangeLang: Function,
    theme: String,
    langs: [Object, Boolean],
    currentLang: String,
};

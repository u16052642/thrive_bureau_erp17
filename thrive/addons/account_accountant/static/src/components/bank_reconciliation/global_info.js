/** @thrive-module **/
import { Component } from "@thrive/owl";

export class BankRecGlobalInfo extends Component {
    static template = "account_accountant.BankRecGlobalInfo";
    static props = {
        journalId: { type: Number },
        journalBalanceAmount: { type: String },
    };

    /** Open the bank reconciliation report. **/
    actionOpenBankGL() {
        this.env.methods.actionOpenBankGL(this.props.journalId);
    }

}

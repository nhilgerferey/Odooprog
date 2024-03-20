/** @odoo-module */

import { Component } from "@odoo/owl";


export class StudentLine extends Component {
    static template = "tetras_school_management.StudentLine";

    static props = {
        name: String,
        studentId: Number,
        onClick: { type: Function, optional: true },
    };
}


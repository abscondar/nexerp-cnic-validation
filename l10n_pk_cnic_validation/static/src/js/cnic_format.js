/** @odoo-module **/

import { registry } from "@web/core/registry";

const CNIC_DIGITS_PATTERN = /^\d{13}$/;

function formatCnic(value) {
    if (!value) {
        return value;
    }
    const trimmed = value.trim();
    const digitsOnly = trimmed.replace(/\D/g, "");
    if (!CNIC_DIGITS_PATTERN.test(digitsOnly)) {
        return trimmed;
    }
    return `${digitsOnly.slice(0, 5)}-${digitsOnly.slice(5, 12)}-${digitsOnly.slice(12)}`;
}

function shouldHandleTarget(target) {
    return (
        target instanceof HTMLInputElement
        && target.name === "cnic"
        && target.type === "text"
    );
}

function applyFormatting(event) {
    const target = event.target;
    if (!shouldHandleTarget(target)) {
        return;
    }

    const formatted = formatCnic(target.value);
    if (formatted !== target.value) {
        const selectionStart = target.selectionStart;
        target.value = formatted;
        if (selectionStart !== null) {
            target.setSelectionRange(formatted.length, formatted.length);
        }
    }
}

const cnicFormatService = {
    start() {
        document.addEventListener("input", applyFormatting, true);
        document.addEventListener("change", applyFormatting, true);
    },
};

registry.category("services").add("l10n_pk_cnic_format_service", cnicFormatService);

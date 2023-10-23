"use strict";
console.log("Hello world");
class PlantationAccordion {
    constructor(_elements) {
        this._elements = _elements;
        this.bindAccordions();
    }
    bindAccordions() {
        for (const accordion of this._elements) {
            const header = this.$(accordion, '.plantation-options_header');
            if (!header)
                continue;
            header.addEventListener("mouseup", () => {
                accordion.classList.toggle('plantation-active');
            });
        }
    }
    $(element, selector) {
        return element.querySelector(selector);
    }
}
const accordions = Array.from(document.querySelectorAll('.plantation-options_item'));
new PlantationAccordion(accordions);

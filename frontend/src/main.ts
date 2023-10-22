console.log("Hello world");


class PlantationAccordion {
    constructor(private _elements: HTMLElement[]) {

        this.bindAccordions();
    }

    bindAccordions () {
        for(const accordion of this._elements) {
            const header = this.$(accordion, '.plantation-options_header');
            if(!header) continue;

            header.addEventListener("mouseup", () => {
                accordion.classList.toggle('plantation-active');
            });
        }
    }

    $(element: HTMLElement, selector: string) {
        return element.querySelector(selector) as HTMLElement  | null;
    }
}

const accordions = Array.from(document.querySelectorAll('.plantation-options_item')) as HTMLElement[];
new PlantationAccordion(accordions);
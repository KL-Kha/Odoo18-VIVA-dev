/** @odoo-module **/

import publicWidget from '@web/legacy/js/public/public_widget';

publicWidget.registry.ReviewCarousel = publicWidget.Widget.extend({
    selector: '.carousel-wrapper',

    start() {
        this._super(...arguments);
        this._initSwiper();
    },

    _initSwiper() {
        const root = this.el;
        const swiperEl = root.querySelector('.splide');
        const prevBtn = root.querySelector(".btn-prev");
        const nextBtn = root.querySelector(".btn-next");
        this.splide = new Splide(swiperEl, {
            fixedWidth: "clamp(432px, 400px, 432px)",
            gap: "20px",
            arrows: false,
            pagination: false,
            breakpoints: {
                768: { perPage: 1 },
                1024: { perPage: 2 },
            },
        })
        this.splide.mount();
        prevBtn.addEventListener("click", () => this.splide.go("<"));
        nextBtn.addEventListener("click", () => this.splide.go(">"));
    },

    destroy() {
        if (this.splide) this.splide.destroy();
        this._super(...arguments);
    },
});

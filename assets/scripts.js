$(document).ready(function () {
	$('.gallery').mauGallery({
		columns: {
			xs: 1,
			sm: 2,
			md: 3,
			lg: 3,
			xl: 3
		},
		lightBox: true,
		lightboxId: 'myAwesomeLightbox',
		showTags: true,
		tagsPosition: 'top'
	});

	const carouselElement = document.querySelector('#carouselExampleIndicators');

	if (carouselElement && window.bootstrap?.Carousel) {
		const prefersReducedMotion = window.matchMedia
			? window.matchMedia('(prefers-reduced-motion: reduce)')
			: null;

		if (!prefersReducedMotion || !prefersReducedMotion.matches) {
			const carousel = window.bootstrap.Carousel.getOrCreateInstance(carouselElement, {
				interval: 5000,
				pause: false,
				ride: 'carousel'
			});

			carousel.cycle();
		}
	}
});

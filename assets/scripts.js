function applyWebpFallback() {
    if (!document.documentElement.classList.contains('no-webp')) {
        return;
    }
    document.querySelectorAll('img[data-fallback-src]').forEach(function (img) {
        var fallback = img.getAttribute('data-fallback-src');
        if (fallback && img.getAttribute('src') !== fallback) {
            img.setAttribute('src', fallback);
        }
    });
}

document.addEventListener('DOMContentLoaded', applyWebpFallback);

$(document).ready(function() {
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
    applyWebpFallback();
});


document.addEventListener('DOMContentLoaded', function() {
    // Load saved language preference
    const savedLang = localStorage.getItem('language') || 'en';
    if (window.location.search.indexOf('lang=') === -1) {
        window.location.href = `?lang=${savedLang}`;
    }

    // Save language preference when changed
    document.querySelectorAll('.language-switcher a').forEach(link => {
        link.addEventListener('click', function(e) {
            const lang = this.href.split('lang=')[1];
            localStorage.setItem('language', lang);
        });
    });
});

document.addEventListener("DOMContentLoaded", function() {
    const toggleBtn = document.getElementById("menu-btn"); // Hamburger icon
    const menu = document.getElementById("mobile-menu"); // Collapsible menu

    if (toggleBtn && menu) {
        toggleBtn.addEventListener("click", function() {
            menu.classList.toggle("hidden"); // Show/hide menu
        });
    } else {
        console.error("Toggle button or menu not found in the DOM.");
    }
});
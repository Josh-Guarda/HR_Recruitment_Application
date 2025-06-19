document.addEventListener("DOMContentLoaded", function () {
    const toastEl = document.getElementById("toastMessage");
    if (toastEl) {
        const toast = new bootstrap.Toast(toastEl);
        toast.show();
    }
});




// Side bar Menu
document.addEventListener('DOMContentLoaded', function () {
    const offcanvasEl = document.getElementById('offcanvasScrolling');
    const offcanvas = new bootstrap.Offcanvas(offcanvasEl);

    // Manually add class on initial load
    document.body.classList.add('sidebar-open');
    offcanvas.show();

    // Handle class when opened/closed via buttons
    offcanvasEl.addEventListener('show.bs.offcanvas', function () {
        document.body.classList.add('sidebar-open');
    });

    offcanvasEl.addEventListener('hidden.bs.offcanvas', function () {
        document.body.classList.remove('sidebar-open');
    });
});


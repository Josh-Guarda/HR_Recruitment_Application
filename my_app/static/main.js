document.addEventListener("DOMContentLoaded", function () {
    const toastEl = document.getElementById("toastMessage");
    if (toastEl) {
        const toast = new bootstrap.Toast(toastEl);
        toast.show();
    }
});




document.addEventListener('DOMContentLoaded', function () {
        const offcanvasEl = document.getElementById('offcanvasScrolling');
        
        offcanvasEl.addEventListener('show.bs.offcanvas', function () {
            document.body.classList.add('sidebar-open');
        });

        offcanvasEl.addEventListener('hidden.bs.offcanvas', function () {
            document.body.classList.remove('sidebar-open');
        });
    });
document.addEventListener("DOMContentLoaded", function () {
    const toastEl = document.getElementById("toastMessage");
    if (toastEl) {
        const toast = new bootstrap.Toast(toastEl);
        toast.show();
    }
});
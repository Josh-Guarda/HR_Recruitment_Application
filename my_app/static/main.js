document.addEventListener("DOMContentLoaded", function () {

    // TOAST MESSAGE
    const toastEl = document.getElementById("toastMessage");
    if (toastEl) {
        const toast = new bootstrap.Toast(toastEl);
        toast.show();
    }

    // TOOL TIP
    var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    tooltipTriggerList.forEach(function (tooltipTriggerEl) {
      new bootstrap.Tooltip(tooltipTriggerEl);
    });
});



// ADMIN OFF-Canvass Sidebar Menu
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




// Toggle Controller for public dashboard profile settings and My Application button group
document.addEventListener("DOMContentLoaded", function () {
    const btnPersonal = document.getElementById("btn-personal");
    const btnJob = document.getElementById("btn-application");
    const sectionPersonal = document.getElementById("section-personal");
    const sectionPersonalNav= document.getElementById("profile-nav");

    const sectionJob = document.getElementById("section-job");

    btnPersonal.addEventListener("click", function () {
        btnPersonal.classList.add("active");
        btnJob.classList.remove("active");
        sectionPersonal.classList.remove("d-none");
        sectionPersonalNav.classList.remove("d-none");
        sectionJob.classList.add("d-none");
    });

    btnJob.addEventListener("click", function () {
        btnJob.classList.add("active");
        btnPersonal.classList.remove("active");
        
        sectionJob.classList.remove("d-none");
        sectionPersonal.classList.add("d-none");
        sectionPersonalNav.classList.add("d-none");
    });



    // SIDEBAR HIDE/SHOW OPTIONS
    const btnDocuments =document.getElementById('Documents')
    const btnSecurityPassword =document.getElementById('SecurityPassword')
    const sectionDocuments = document.getElementById("section-documents");
    const sectionSecurityPassword= document.getElementById("section-change-password");

    
    btnDocuments.addEventListener("click", function () {
        sectionPersonal.classList.add("d-none");
        sectionSecurityPassword.classList.add("d-none");
        sectionDocuments.classList.remove("d-none");
    });

    btnSecurityPassword.addEventListener("click", function () {
        sectionPersonal.classList.add("d-none");
        sectionSecurityPassword.classList.remove("d-none");
        sectionDocuments.classList.add("d-none");
    });




    // LOAD AVATAR to CONTAINER WHEN UPLOADED
    let profilePicture= document.getElementById('avatar-preview');
    let inputPicture = document.getElementById('avatar-upload');

    inputPicture.onchange=function() {
        profilePicture.src = URL.createObjectURL(inputPicture.files[0]);
    }


    // BARANGAY SHOW AS INPUT WITH DYNAMIC SELECTION
    document.getElementById("prov_id").addEventListener("change", function () {
    const provCode = this.value;
    fetch(`/get_municipalities?prov_code=${provCode}`)
        .then(res => res.json())
        .then(data => {
            const muniSelect = document.getElementById("munci_id");
            muniSelect.innerHTML = '<option value="">-- Select Municipality --</option>';
            data.data.forEach(muni => {
                muniSelect.innerHTML += `<option value="${muni.code}">${muni.name}</option>`;
            });

            // Clear barangay
            document.getElementById("brgy_id").innerHTML = '<option value="">-- Select Barangay --</option>';
        });
    });

    document.getElementById("munci_id").addEventListener("change", function () {
        const muniCode = this.value;
        fetch(`/get_barangays?muni_code=${muniCode}`)
            .then(res => res.json())
            .then(data => {
                const brgySelect = document.getElementById("brgy_id");
                brgySelect.innerHTML = '<option value="">-- Select Barangay --</option>';
                data.data.forEach(brgy => {
                    brgySelect.innerHTML += `<option value="${brgy.code}">${brgy.name}</option>`;
                });
            });
    });

});

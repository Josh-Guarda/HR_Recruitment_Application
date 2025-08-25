


//**** GLOBAL FUNCTIONALITY ****//
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

    const tooltipTrigger = document.querySelectorAll('.custom-tooltip');
    const tooltip = new bootstrap.Tooltip(tooltipTrigger, {
    delay: { show: 100, hide: 2000 } // Show after 100ms, hide after 2000ms
    });
});






// ****DASHBOARDS SCRIPTS ****//

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





//**** ADMIN DASHBOARD SCRIPTS ****//
document.addEventListener("DOMContentLoaded", function () {
    
    //*****/ USERS MANAGEMENT ****//

    // SWITCH VIEW OF KANBAN AND TREEVIEW SCRIPT
    const btnUsersTreeView = document.getElementById("btn-UsersTreeView");
    const btnUsersKanbanView = document.getElementById("btn-UsersKanbanView");
    const sectionUsersTreeView= document.getElementById("UsersManagementTreeView");
    const sectionKanbanView = document.getElementById("UsersManagementKanbanView");
    
    btnUsersTreeView.addEventListener("click", function () {
        btnUsersTreeView.classList.add("active");
        btnUsersKanbanView.classList.remove("active");
        sectionUsersTreeView.classList.remove("d-none");
        sectionKanbanView.classList.add("d-none");
    });

    btnUsersKanbanView.addEventListener("click", function () {
        btnUsersKanbanView.classList.add("active");
        btnUsersTreeView.classList.remove("active");
        sectionKanbanView.classList.remove("d-none");
        sectionUsersTreeView.classList.add("d-none");
    });



    // ADMIN KANBAN SCRIPTS
    // document.querySelectorAll('.btn-edit-user').forEach(btn => {
    //     btn.addEventListener('click', () => {
    //         const userId = btn.getAttribute('data-user-id');
    //         console.log("User ID:", userId);
    //         // You can even trigger an AJAX call here to fetch user data
    //     });
    // });





    // ADMIN TREEVIEW SCRIPTS

    $(document).ready(function(){
    var dataTable = $('#users_data').DataTable({
        // dom: 'lrtip'  // removes the default search bar (the 'f' option)
        
        dom:
            // Each letter stands for a feature:
            // l – Length changing (entries per page)
            // f – Filtering (search bar) 
            // t – The actual table
            // i – Table info text (e.g., “Showing 1 to 10 of 50 entries”)
            // p – Pagination
            // r – Processing display element (shows loading)

            // So dom: 'lrtip' means:
            // Length menu (l)
            // No search bar
            // Table (t)
            // Info (i)
            // Pagination (p)


            // TABLE SPACING DESIGN
            // top row
            '<"row mb-3 "<"col-md-12 text-end"l>>' +
            // table
            'rt' +
            // bottom row
            '<"row mt-2 py-5"<"col-md-6"i><"col-md-6 text-end"p>>',

        pagingType: 'simple_numbers',
        language: { emptyTable: 'No users found – please add one.' ,lengthMenu: 'Show _MENU_ entries'},
        columnDefs: [
            { orderable: false, targets: 0 },
            { targets: '_all', className: 'text-center' }
        ],
        select: {
            style: 'multi',
            selector: 'td:first-child'   // clicking this cell selects the row
        },
        
    });

    // clicking this cell selects all the inside the Tree
    $('#checkAll').on('click', function () {
    $('.row-check').prop('checked', this.checked);
    });

    $('#users_data').editable({
        container:'body',
        selector:'td.firstname',
        url:'/admin-users-management/',
        title:'Name',
        type:'POST',
        validate:function(value){
            if($.trim(value) == '')
            {
                return 'This field is required';
            }
        }
    });

    $('#users_data').editable({
        container:'body',
        selector:'td.lastname',
        url:'/admin-users-management/',
        title:'Name',
        type:'POST',
        validate:function(value){
            if($.trim(value) == '')
            {
                return 'This field is required';
            }
        }
    });
 
    $('#users_data').editable({
        container:'body',
        selector:'td.email_address',
        url:'/admin-users-management/',
        title:'Email',
        type:'POST',
        validate:function(value){
            if($.trim(value) == '')
            {
                return 'This field is required';
            }
        }
    });

    $('#users_data').editable({
        container:'body',
        selector:'td.mobile_number',
        url:'/admin-users-management/',
        title:'Email',
        type:'POST',
        validate:function(value){
            if($.trim(value) == '')
            {
                return 'This field is required';
            }
        }
    });
    
    $('#users_data').editable({
        container:'body',
        selector:'td.phone_number',
        url:'/admin-users-management/',
        title:'Phone',
        type:'POST',
        validate:function(value){
            if($.trim(value) == '')
            {
                return 'This field is required';
            }
        }
    });
    
    $('#users_data').editable({
        container:'body',
        selector:'td.department',
        url:'/admin-users-management/',
        title:'Phone',
        type:'POST',
        validate:function(value){
            if($.trim(value) == '')
            {
                return 'This field is required';
            }
        }
    });

    $('#users_data').editable({
        container:'body',
        selector:'td.user_type',
        url:'/admin-users-management/',
        title:'Phone',
        type:'POST',
        validate:function(value){
            if($.trim(value) == '')
            {
                return 'This field is required';
            }
        }
    });
}); 
});













//**** PUBLIC USER DASHBOARD SCRIPTS: ****//

document.addEventListener("DOMContentLoaded", function () {
    //Toggle Controller for public dashboard profile settings and My Application button group
    const btnPersonal = document.getElementById("btn-personal");
    const btnJob = document.getElementById("btn-application");
    const sectionPersonal = document.getElementById("section-personal");
    const sectionPersonalNav= document.getElementById("profile-nav");
    const sectionChangePass = document.getElementById("section-change-password");
    const sectionJob = document.getElementById("section-job");
    
    btnPersonal.addEventListener("click", function () {
        btnPersonal.classList.add("active");
        btnJob.classList.remove("active");
        sectionPersonal.classList.remove("d-none");
        sectionPersonalNav.classList.remove("d-none");
        sectionJob.classList.add("d-none");
        sectionChangePass.classList.add("d-none");
    });

    btnJob.addEventListener("click", function () {
        btnJob.classList.add("active");
        btnPersonal.classList.remove("active");
        
        sectionJob.classList.remove("d-none");
        sectionPersonal.classList.add("d-none");
        sectionPersonalNav.classList.add("d-none");
    });



    // SIDEBAR HIDE/SHOW OPTIONS PUBLIC DASHBOARD
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
    const provSelect = document.getElementById('prov_id');
    const munciSelect = document.getElementById('munci_id');
    const brgySelect = document.getElementById('brgy_id');
    
    console.log(provSelect.value)
    // Function to update municipality dropdown based on province selection
    provSelect.addEventListener('change', function() {
        const provCode = this.value;
        
        // Clear municipality and barangay dropdowns
        munciSelect.innerHTML = '<option value="">-- Select Municipality --</option>';
        brgySelect.innerHTML = '<option value="">-- Select Barangay --</option>';
        
        if (provCode) {
            // Make AJAX request to get municipalities
            fetch(`/get_municipalities/${provCode}`)
                .then(response => response.json())
                .then(data => {
                    data.forEach(muni => {
                        const option = document.createElement('option');
                        option.value = muni.code;
                        option.textContent = muni.name;
                        munciSelect.appendChild(option);
                    });
                });
        }
    });
    
    // Function to update barangay dropdown based on municipality selection
    munciSelect.addEventListener('change', function() {
        const munciCode = this.value;
        
        // Clear barangay dropdown
        brgySelect.innerHTML = '<option value="">-- Select Barangay --</option>';
        
        if (munciCode) {
            // Make AJAX request to get barangays
            fetch(`/get_barangays/${munciCode}`)
                .then(response => response.json())
                .then(data => {
                    data.forEach(brgy => {
                        const option = document.createElement('option');
                        option.value = brgy.code;
                        option.textContent = brgy.name;
                        brgySelect.appendChild(option);
                    });
                });
        }
    });
});


// document.addEventListener('click', function (event) {
//     const modal = document.getElementById('userEditModal');
//     const modalContent = modal.querySelector('.modal-content');
//     const isModalVisible = modal.classList.contains('show');

//     if (isModalVisible && !modalContent.contains(event.target)) {
//       const beep = document.getElementById('modal-beep');
//       beep.currentTime = 0;
//       beep.play();
//     }
//   });




    
function openUserModal(userId) {

    // Update the modal title
    document.getElementById("userEditModalLabel").innerText = `Edit User Profile - ${userId}`;

    // Initialize and show the modal
    const modalElement = document.getElementById("userEditModal");
    const modal = new bootstrap.Modal(modalElement);
    modal.show();

    // (Optional: load user inside the modal and input data dynamically via user_id)
    loadUserData(userId);
}


function loadUserData(userId) {
    const contentDiv = document.getElementById("modalContent");

    // Show loading spinner while fetching
    contentDiv.innerHTML = `
        <div class="text-center py-5">
            <div class="spinner-border text-primary" role="status">
                <span class="visually-hidden">Loading...</span>
            </div>
            <p class="mt-2 text-muted">Loading user data...</p>
        </div>
    `;

    fetch(`/get-user-form/${userId}`)
        .then(response => response.json())
        .then(data => {
            
            contentDiv.innerHTML = `
                <form id="userEditForm" method="POST" enctype="multipart/form-data">
                    <input type="hidden" name="user_id" value="{{ user.id }}">
                    <!--{{user_info_form.user_id(value=user.id)}}-->
                    <div class="container d-none d-sm-block">
                        <div class="avatar pb-5 ">
                            <div id="avatar-container">
                                
                                <img id="avatar-preview" src="
                                    {% if user.profile_picture %}
                                    {{ url_for('static', filename='uploads/avatars/'~ value="${data.profile_pic})}}
                                    {% else %}
                                    {{ url_for('static', filename='builtin/icons/person.png')}}
                                    {% endif %}" 
                                    alt="Avatar"
                                    onerror="this.onerror=null; this.src='{{ url_for('static', filename='builtin/icons/person.png') }}'">
                            </div>
                            <label for="avatar-upload" class="upload-label">
                                    <span class="upload-icon">+</span>
                            </label>
                            <input type="file" id="avatar-upload" name="avatar" accept="image/png,image/jpeg"/>
                        </div>
                    </div>
                    
                    <div class="row row-cols-1 row-cols-lg-2 mb-3 text-muted">
                        <div class="col text-center">
                            <label class="form-label">First Name</label>
                            <input type="text" name="firstname" placeholder="Juan" class="form-control" value="${data.firstname}">
                        </div>
                        <div class="col text-center">
                            <label class="form-label">Last Name</label>
                            <input type="text" name="lastname" class="form-control" placeholder="Dela Cruz" value="${data.lastname}">
                        </div>
                    </div>
                    
                    <div class="row">
                        <div class="col text-center text-muted py-5 ps-lg-3">
                            <h6 class="mb-4">Address Details</h6>
                            
                            <div class="row row-cols-1 row-cols-lg-2 mb-5 text-muted">
                                <div class="col text-center">
                                    <label class="form-label">Address 1</label>
                                    <input type="text" name="address_1" class="form-control" id="address1_{{user.id}}" placeholder="Block # / Lot #" value="${data.address_1}">
                                </div>
                                <div class="col text-center">
                                    <label class="form-label">Address 2</label>
                                    <input type="text" name="address_1" class="form-control", id="address2_{{user.id}}" placeholder="Street / Phase " value="${data.address_1}">
                                </div>
                            </div>
                            <div class="row row-cols-1 row-cols-lg-4 mb-5 text-muted">
                                <div class="col text-center">
                                    <label class="form-label">Province</label>
                                    <select name="province" class="form-control text-center" id="dynamic_prov_id"></select>
                                </div>

                                <div class="col text-center">
                                    <label class="form-label">Municipality</label>
                                    <select name="province" class="form-control text-center" id="dynamic_munci_id"></select>
                                </div>

                                <div class="col text-center">
                                    <label class="form-label">Barangay</label>
                                    <select name="province" class="form-control text-center" id="dynamic_brgy_id"></select>

                                </div>
                                
                                <div class="col text-center">
                                    <label class="form-label">Zipcode</label> 
                                    <input type="text" class="form-control" id="zipcode" value="${data.zipcode}">
                                    
                                </div>
                                
                            </div>
                        </div>
                    </div>

                    
                    <div class="row">
                        <div class="col-12 col-lg-6 text-center text-muted py-2 pe-lg-3">
                            <h6 class="mb-4">Contact Details</h6>
                            <div class="mb-3">
                                <label class="form-label">Email</label>
                                <input type="email" class="form-control" placeholder="your@email.com" value="${data.email_address}">
                            </div>
                            <div class="mb-3">
                                <label class="form-label">Mobile Number</label>
                                <input type="text" class="form-control" placeholder="+63*" value="${data.mobile_number}">
                            </div>
                            <div>
                                <label class="form-label">Phone Number</label>
                                <input type="text" class="form-control" placeholder="0000-0000" value="${data.phone_number}">
                            </div>
                        </div>
                    </div>

                    <div class="my-5">
                        <input type="submit" value="Save Changes" class="btn btn-md btn-primary px-5 w-100" />

                    </div>
                </form>
            `;

            const provSelect = document.getElementById("dynamic_prov_id");
            const munciSelect = document.getElementById("dynamic_munci_id");
            const brgySelect = document.getElementById("dynamic_brgy_id");

            // 1. Load provinces
            fetch(`/get_provinces`)
                .then(res => res.json())
                .then(provinces => {
                    provSelect.innerHTML = '<option value="">-- Select Province --</option>';
                    provinces.forEach(prov => {
                        const option = document.createElement("option");
                        option.value = prov.code;
                        option.textContent = prov.name;
                        provSelect.appendChild(option);
                    });

                    if (data.prov_id) {
                        provSelect.value = data.prov_id;
                        loadMunicipalities(data.prov_id, data.munci_id, data.brgy_id);
                    }
                });

            // 2. Province change handler
            provSelect.addEventListener("change", () => {
                loadMunicipalities(provSelect.value, null, null);
            });

            // Helper: Load municipalities
            function loadMunicipalities(provCode, preselectMuni, preselectBrgy) {
                munciSelect.innerHTML = '<option value="">-- Select Municipality --</option>';
                brgySelect.innerHTML = '<option value="">-- Select Barangay --</option>';

                if (!provCode) return;

                fetch(`/get_municipalities/${provCode}`)
                .then(res => res.json())
                .then(munis => {
                    munis.forEach(muni => {
                        const option = document.createElement("option");
                        option.value = muni.code;
                        option.textContent = muni.name;
                        munciSelect.appendChild(option);
                    });

                    if (preselectMuni) {
                        munciSelect.value = preselectMuni;
                        loadBarangays(preselectMuni, preselectBrgy);
                    }
                });
            }

            // 3. Municipality change handler
            munciSelect.addEventListener("change", () => {
                loadBarangays(munciSelect.value, null);
            });

            // Helper: Load barangays
            function loadBarangays(munciCode, preselectBrgy) {
                brgySelect.innerHTML = '<option value="">-- Select Barangay --</option>';
                if (!munciCode) return;

                fetch(`/get_barangays/${munciCode}`)
                .then(res => res.json())
                .then(brgys => {
                    brgys.forEach(brgy => {
                        const option = document.createElement("option");
                        option.value = brgy.code;
                        option.textContent = brgy.name;
                        brgySelect.appendChild(option);
                    });

                    if (preselectBrgy) {
                        brgySelect.value = preselectBrgy;
                    }
                });
            }


            // Attach submit handler
            document.getElementById("userEditForm").addEventListener("submit", function(e) {
                console.log('POGI AKO')
                e.preventDefault();

                // Collect form data
                const formData = new FormData(this);
                const body = {};
                formData.forEach((value, key) => body[key] = value);

                fetch(`/update-user/${userId}`, {
                    method: "POST",   // or PATCH
                    headers: { "Content-Type": "application/json" },
                    body: JSON.stringify(body)
                })
                .then(res => res.json())
                .then(result => {
                    console.log("Update success:", result);
                    // Optional: close modal
                    bootstrap.Modal.getInstance(document.getElementById("userEditModal")).hide();
                })
                .catch(err => console.error("Update failed:", err));
            });
        })
        .catch(error => {
            console.error("Error fetching user data:", error);
            contentDiv.innerHTML = `<p class="text-danger">Failed to load user data.</p>`;
        });
}



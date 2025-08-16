


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
        
        console.log('Trace here')
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

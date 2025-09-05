


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
    const btnUsersTreeView = document.querySelectorAll(".list-view");
    const btnUsersKanbanView = document.querySelectorAll(".kanban-view");
    const sectionUsersTreeView = document.getElementById("UsersManagementTreeView");
    const sectionKanbanView = document.getElementById("UsersManagementKanbanView");
    
    // Add event listener to all list-view elements
    btnUsersTreeView.forEach(btn => {
        btn.addEventListener("click", function () {
            // Add active class to all list-view buttons
            btnUsersTreeView.forEach(item => item.classList.add("active"));
            // Remove active class from all kanban-view buttons
            btnUsersKanbanView.forEach(tag => tag.classList.remove("active"));
            sectionUsersTreeView.classList.remove("d-none");
            sectionKanbanView.classList.add("d-none");
        });
    });

    // Add event listener to all kanban-view elements
    btnUsersKanbanView.forEach(tag => {
        tag.addEventListener("click", function () {
            // Add active class to all kanban-view buttons
            btnUsersKanbanView.forEach(item => item.classList.add("active"));
            // Remove active class from all list-view buttons
            btnUsersTreeView.forEach(item => item.classList.remove("active"));
            sectionKanbanView.classList.remove("d-none");
            sectionUsersTreeView.classList.add("d-none");
        });
    });



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




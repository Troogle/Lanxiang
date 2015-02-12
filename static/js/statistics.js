$(document).ready(function () {
    $('#playerTable').DataTable({
        "lengthChange": false,
        "pageLength": 20,
        "columnDefs": [
            { "orderable": false, "targets": 1 }
        ]
    });
});
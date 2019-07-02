$(function(){
    var url = "https://crm.zoho.com/crm/private/json/Leads/getRecords?authtoken=4f86a4c7e8f1b2505ff9ba5ae58f3c53&scope=crmapi&selectColumns=Leads(First Name,Last Name,Email)&version=1"; //Solo te manda el nombre, last name y el correo
    //var myobj = JSON.parse();
    $("#grid").dxDataGrid({
        dataSource: DevExpress.data.AspNet.createStore({
            key: "no",
            loadUrl: url ,
            insertUrl: url ,
            updateUrl: url ,
            deleteUrl: url ,
            onBeforeSend: function(method, ajaxOptions) {
                ajaxOptions.xhrFields = { withCredentials: false };//true
            }
        }),
        editing: {
            allowUpdating: true,
            allowDeleting: true,
            allowAdding: false
        },
        remoteOperations: {
            sorting: true,
            paging: true
        },
        paging: {
            pageSize: 100
        },
        pager: {
            showPageSizeSelector: true,
            allowedPageSizes: [10, 20, 100]
        },
        columns: [{
            dataField: "no",
            dataType: "number",
            allowEditing: false
        }, {
            dataField:"First Name"
        }, {
            dataField: "Last Name"
        }, {
            dataField: "Email"
        }, ],
    }).dxDataGrid("instance");
});
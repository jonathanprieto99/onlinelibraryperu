$(function(){
    var url = "https://js.devexpress.com/Demos/Mvc/api/DataGridWebApi";
    $("#grid").dxDataGrid({
        dataSource: DevExpress.data.AspNet.createStore({
            key: "OrderID",
            loadUrl: url + "/Orders",
            insertUrl: url + "/InsertOrder",
            updateUrl: url + "/UpdateOrder",
            deleteUrl: url + "/DeleteOrder",
            onBeforeSend: function(method, ajaxOptions) {
                ajaxOptions.xhrFields = { withCredentials: true };
            }
        }),
        remoteOperations: true,
        columns: [{
                dataField: "CustomerID",
                caption: "Libro",
                validationRules: [{
                    type: "stringLength",
                    message: "The field Customer must be a string with a maximum length of 50.",
                    max: 50
                }],
                lookup: {
                    dataSource: DevExpress.data.AspNet.createStore({
                        key: "Value",
                        loadUrl: url + "/CustomersLookup",
                        onBeforeSend: function(method, ajaxOptions) {
                            ajaxOptions.xhrFields = { withCredentials: true };
                        }
                    }),
                    valueExpr: "Value",
                    displayExpr: "Text"
                }
            },{
                dataField: "Autor",
                validationRules: [{
                    type: "stringLength",
                    message: "The field ShipCountry must be a string with a maximum length of 50.",
                    max: 50
                }]
            },{
                dataField: "Genero",
                validationRules: [{
                    type: "stringLength",
                    message: "The field ShipCountry must be a string with a maximum length of 15.",
                    max: 15
                }]
            }, {
                dataField: "Descripcion",
                validationRules: [{
                    type: "stringLength",
                    message: "The field ShipCountry must be a string with a maximum length of 500.",
                    max: 500
                }]
            }, {
                dataField: "Archivo",
                validationRules: [{
                    type: "file",
                    message: "The field ShipCountry must be a string with a maximum length of 15.",
                    max: 15
                }]
            },{
                dataField: "Imagen",
                validationRules: [{
                    type: "image",
                    message: "The field ShipCountry must be a string with a maximum length of 15.",
                    max: 15
                }]
            },{
                dataField: "Foto Autor",
                validationRules: [{
                    type: "image",
                    message: "The field ShipCountry must be a string with a maximum length of 15.",
                    max: 15
                }]
            }


        ],
        filterRow: {
            visible: true
        },
        headerFilter: {
            visible: true
        },
        groupPanel: {
            visible: true
        },
        scrolling: {
            mode: "virtual"
        },
        height: 600,
        showBorders: true,
        masterDetail: {
            enabled: true,
            template: function(container, options) {
                $("<div>")
                    .dxDataGrid({
                        dataSource: DevExpress.data.AspNet.createStore({
                            loadUrl: url + "/OrderDetails",
                            loadParams: { orderID : options.data.OrderID },
                            onBeforeSend: function(method, ajaxOptions) {
                                ajaxOptions.xhrFields = { withCredentials: true };
                            }
                        }),
                        showBorders: true
                    }).appendTo(container);
            }
        },
        editing: {
            allowAdding: true,
            allowUpdating: true,
            allowDeleting: true
        },
        grouping: {
            autoExpandAll: false
        },
        summary: {
            totalItems: [{
                column: "Freight",
                summaryType: "sum"
            }],
            groupItems: [{
                    column: "Freight",
                    summaryType: "sum"
                }, {
                    summaryType: "count"
                }
            ]
        }
    });
});
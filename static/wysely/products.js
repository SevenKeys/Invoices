wysely.products = {
    selectedProduct: '',

    init: function() {
        wysely.products.bindUIHandlers();
    },

    bindUIHandlers: function () {
        $("#search-bar").on('input', wysely.products.searchProduct);
        $("#create-group").on('input', wysely.products.showGroupPopup);
        $("#delete-product").on('click', wysely.products.removeProduct);
        $("#save-product").on('click', wysely.products.saveProduct);
        $("#create-product").on('click', wysely.products.createProduct);
        $(".product-selector").on('click', wysely.products.selectProduct);

        $('#product-form').on('submit', function(event) {
            event.preventDefault();
            console.log("form submitted!");  // sanity check
            alert($(event.target).data('method'));
        });
    },

    ajaxOp: function(path, method, data) {
       $.ajax({
            url: path ,
            type: method,
            data: data,

            // handle a successful response
            success : function(json) {
                console.log(json); // log the returned json to the console
                console.log("success"); // another sanity check
            },

            // handle a non-successful response
            error : function(xhr,errmsg,err) {
                $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: "+errmsg+
                    " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
                console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
        }
        })
    },

    showGroupPopup: function(ev) {
        $('#popup1').w2popup();
    },

    removeProduct: function(ev) {
        console.log('removing product: ' + wysely.products.selectedProduct);
    },

    selectProduct: function(ev) {
        console.log('product selected, loading form');
        wysely.products.selectedProduct = $(ev.target).data('value');
        alert($(ev.target).data('value'));
        /// TODO: load properties, show form
    },

    saveProduct: function(ev) {
        console.log('saving product: ' + wysely.products.selectedProduct);
    },

    createProduct: function(ev) {
        console.log('adding product');
        wysely.products.selectedProduct = '_new';
        wysely.products.ajaxOp('create_new/', "POST");
    },

    searchProduct:function (ev) {
        var searchval = $("#search-bar").val();
        $("#foldable-container li").each(function(obj) {
            if (searchval) {
                if ($(this).data('value').indexOf(searchval) >= 0) {
                    $(this).show();
                }
                else {
                    $(this).hide();
                }
            }
            else {
                $(this).show();
            }
        });
        return true;
    }
};



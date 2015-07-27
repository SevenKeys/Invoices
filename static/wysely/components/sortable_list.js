wysely.components.sortable_list = {
    init: function() {
        $("#sortable1, #sortable2, #sortable3").sortable({
            connectWith: ".connectedSortable"
        }).disableSelection();

        $('#foldable-container h3').on('click', function() {
            $(this).next('.display-group').slideToggle();
        });
    }
};

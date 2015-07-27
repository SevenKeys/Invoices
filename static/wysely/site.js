var gridster;

/**
 * Start the grid.
 */
$(function() {

	gridster = $(".gridster ul").gridster({
		widget_margins: [10, 10],
		widget_base_dimensions: [140, 140],
		max_cols: 6,
		draggable: {
			handle: 'span'
		},
		serialize_params: function($w, wgd) {
			return {
				id: $($w).attr('id'),
				col: wgd.col,
				row: wgd.row,
				size_x: wgd.size_x,
				size_y: wgd.size_y,
				htmlContent : CKEDITOR.instances["editable_" + $($w).attr('id')].getData()
			};
		}
	}).data("gridster");

	$(".draggable-element").draggable({
		helper: "clone"
	});

	$(".gridster").droppable({
		drop: function(event, ui) {
			var widget_id = uuid();
			var id = "editable_" + widget_id;
            gridster.add_widget(
                '<li id="' + widget_id + '" style="border: 2px solid red;" class="element-added"><span class="glyphicon glyphicon-move" aria-hidden="true"></span><button type="button" class="btn btn-default remove" aria-label="Left Align"><span class="glyphicon glyphicon-remove" aria-hidden="true"</span></button><div id="' + id + '" name="' + id + '" class="editable" contenteditable="true" style="width:100%;height:100%">' + ui.draggable.data('text') +  '</div></li>', ui.draggable.data('x-size'), ui.draggable.data('y-size'), ui.draggable.data('x'), ui.draggable.data('y'));
            CKEDITOR.disableAutoInline = true;
            CKEDITOR.inline(id);
            $(document).on('click', '.remove', function() {
				gridster.remove_widget( $(this).parent());
			});
        }
	});

	$('#save').on('click', function() {
		alert(JSON.stringify(gridster.serialize()));
	});

	CKEDITOR.disableAutoInline = true;
	CKEDITOR.inline("editable_widget_first");
});

/**
 * Generate a specific uuid, a unique id
 * for each auto-generated element.
 */
function uuid(){
    var d = new Date().getTime();
    var uuid = 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, function(c) {
        var r = (d + Math.random()*16)%16 | 0;
        d = Math.floor(d/16);
        return (c=='x' ? r : (r&0x3|0x8)).toString(16);
    });
    return uuid;
};

/**
 * Parse the String to a JSON list.
 */
function widgetsJson(jsonList) {
	return JSON.parse(jsonList);
}
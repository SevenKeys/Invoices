/**
 * Start the grid.
 */
$(function() {
	$.fn.extend({
		template: function(initialData) {

			var gridster = $(".gridster ul").gridster({
				widget_margins: [10, 10],
				widget_base_dimensions: [140, 140],
				max_cols: 6,
				draggable: {
					handle: 'span'
				},
				serialize_params: function($w, wgd) {
					return {
						reference: $($w).attr('id'),
						position_y: wgd.col,
						position_x: wgd.row,
						component: {
						    id: $($w).data('component')
						}
					};
				}
			}).data("gridster");

			if (initialData != undefined && initialData != null && "" != initialData) {
				gridster.remove_all_widgets();
				$.each(Gridster.sort_by_row_and_col_asc(JSON.parse(initialData)), function() {
					gridster.add_widget('<li id="' + this.id + '" style="border: 2px solid red;" class="element-added"><span class="glyphicon glyphicon-move" aria-hidden="true"></span><button type="button" class="btn btn-default remove" aria-label="Left Align"><span class="glyphicon glyphicon-remove" aria-hidden="true"</span></button><div id="editable_' + this.id + '" name="editable_' + this.id + '" class="editable" style="width:100%;height:100%"></div></li>', this.position_x, this.position_y, this.col, this.row);
					$(document).on('click', '.remove', function() {
						gridster.remove_widget( $(this).parent());
					});
					CKEDITOR.disableAutoInline = true;
					CKEDITOR.inline("editable_" + this.id);
					CKEDITOR.instances["editable_" + this.id].setData(this.content.toString().replace("_salto_", "\n"));
				});
			}

			CKEDITOR.replace("widget-content");
			$("#add-element").on('click', function() {
				$("#add-widget").modal();
			});

			$('.addable-element').on('click', function() {
				var widget_id = uuid();
				var id = "editable_" + widget_id;
				gridster.add_widget(
				'<li id="' + widget_id + '" style="border: 2px solid red;" class="element" data-component="' + $(this).attr("id") + '"><span class="glyphicon glyphicon-move" aria-hidden="true"></span><button type="button" class="btn btn-default remove" aria-label="Left Align"><span class="glyphicon glyphicon-remove" aria-hidden="true"</span></button><div id="' + id + '" name="' + id + '" class="editable" style="width:100%;height:100%">' + $(this).data("content") +  '</div></li>', $(this).data("x-size"), $(this).data("y-size"), 1, 1);
				$(document).on('click', '.remove', function() {
					gridster.remove_widget( $(this).parent());
				});
				CKEDITOR.disableAutoInline = true;
				CKEDITOR.inline(id);
			});

			$('#save').on('click', function() {
				CKEDITOR.instances["widget-content"].destroy();
				alert(JSON.stringify(gridster.serialize()));
			});
		}
	});
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
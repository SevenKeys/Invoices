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
						id: $($w).attr('id'),
						col: wgd.col,
						row: wgd.row,
						size_x: wgd.size_x,
						size_y: wgd.size_y,
						htmlContent : CKEDITOR.instances["editable_" + $($w).attr('id')].getData().toString().replace("\n", "_salto_")
					};
				}
			}).data("gridster");

			if (initialData != undefined && initialData != null && "" != initialData) {
				gridster.remove_all_widgets();
				$.each(Gridster.sort_by_row_and_col_asc(JSON.parse(initialData)), function() {
					gridster.add_widget('<li id="' + this.id + '" style="border: 2px solid red;" class="element-added"><span class="glyphicon glyphicon-move" aria-hidden="true"></span><button type="button" class="btn btn-default remove" aria-label="Left Align"><span class="glyphicon glyphicon-remove" aria-hidden="true"</span></button><div id="editable_' + this.id + '" name="editable_' + this.id + '" class="editable" style="width:100%;height:100%"></div></li>', this.size_x, this.size_y, this.col, this.row);
					$(document).on('click', '.remove', function() {
						gridster.remove_widget( $(this).parent());
					});
					CKEDITOR.disableAutoInline = true;
					CKEDITOR.inline("editable_" + this.id);
					CKEDITOR.instances["editable_" + this.id].setData(this.htmlContent.toString().replace("_salto_", "\n"));
				});
			}

			$(".draggable-element").draggable({
				helper: "clone"
			});

			$(".gridster").droppable({
				drop: function(event, ui) {
					$("#add-widget").modal();
					CKEDITOR.replace("widget-content");
					$('#create-widget').on('click', function() {
						var widget_id = uuid();
						var id = "editable_" + widget_id;
						gridster.add_widget(
						'<li id="' + widget_id + '" style="border: 2px solid red;" class="element-added"><span class="glyphicon glyphicon-move" aria-hidden="true"></span><button type="button" class="btn btn-default remove" aria-label="Left Align"><span class="glyphicon glyphicon-remove" aria-hidden="true"</span></button><div id="' + id + '" name="' + id + '" class="editable" style="width:100%;height:100%">' + CKEDITOR.instances["widget-content"].getData() +  '</div></li>', document.getElementById("x-size").value, document.getElementById("y-size").value, 1, 1);
						$(document).on('click', '.remove', function() {
							gridster.remove_widget( $(this).parent());
						});
						$("#add-widget").modal('hide');
					});
				}
			});

			$('#save').on('click', function() {
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
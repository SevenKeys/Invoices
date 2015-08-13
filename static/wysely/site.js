var gridster;

/**
 * Start the grid.
 */
$(function() {
	$.fn.extend({
		template: function(id_template) {
			prepareAjax();
			gridster = $(this).gridster({
				widget_margins: [10, 10],
				widget_base_dimensions: [130, 130],
				max_cols: 6,
				min_cols: 6,
				min_rows: 10,
				draggable: {
					handle: 'span'
				},
				serialize_params: function($w, wgd) {
					return {
						reference: $($w).attr('id'),
						position_y: wgd.row,
						position_x: wgd.col,
						size_x: wgd.size_x,
						size_y: wgd.size_y,
						id_component: $($w).data('component'),
						content: $('#editable_' + $($w).attr('id')).html(),
						type: $($w).data('type')
					};
				}
			}).data("gridster");

			if (id_template != undefined && id_template != null && "" != id_template) {
				loadTemplate(id_template);
			}

			CKEDITOR.replace("widget-content");
			$("#add-component").on('click', function() {
			    document.getElementById("id_component").value = null
			    $("#create-component").show();
                $("#update-component").hide();
			    document.getElementById("x-size").readOnly = false;
                document.getElementById("y-size").readOnly = false;
				$("#add-widget").modal();

			});

			editableEvent(".edit-component");
			addableEvent();

			$('#save').on('click', function() {
				if (CKEDITOR.instances['widget-content']) {
					CKEDITOR.instances["widget-content"].destroy();
				}
				document.getElementById("instances_template").value = JSON.stringify(gridster.serialize());
				saveTemplate(
					document.getElementById('id_template').value,
					document.getElementById('title_template').value,
					document.getElementById('description_template').value,
					document.getElementById('instances_template').value);
				CKEDITOR.replace("widget-content");
			});

			$('#show-preview').on('click', function() {
				if (CKEDITOR.instances['widget-content']) {
					CKEDITOR.instances["widget-content"].destroy();
				}
				document.getElementById("instances_template").value = JSON.stringify(gridster.serialize());
				CKEDITOR.replace("widget-content");
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
 * Save a custom component.
 * @param title Title of the component
 * @param sizex Horizontal size of the component
 * @param sizey Vertical size of the component
 * @param cont Content of the component in html
 */
function saveComponent(title, sizex, sizey, cnt) {
    $(document).ready(function(){
        $.ajax({
            url: '/templates/customcomponents/',
            data: {
                    title: title,
                    size_x: sizex,
                    size_y: sizey,
                    content: cnt
            },
            dataType: "json",
            error: function(data) {
                console.error(data);
            },
            success: function(data) {
            	var customcomponent = '<li role="presentation" class="list-group-item"><a>' + title + '</a><a id="' + JSON.stringify(data) + '" class="addable-element" data-x-size="' + sizex + '" data-y-size="' + sizey + '" data-content="' + cnt + '"><span class="glyphicon glyphicon-plus" aria-hidden="true"></span></a><a class="edit-component"><span class="glyphicon glyphicon-pencil" aria-hidden="true"></span></a><a class="delete-component" onclick="deleteComponent(' + JSON.stringify(data) + ')"><span class="glyphicon glyphicon-trash" aria-hidden="true"></span></a></li></li>';
            	$("#custom-components").append(customcomponent);
            	$("#add-widget").modal('hide');
            	addableEvent();
            	editableEvent(".edit-component");
            },
            type: 'POST'
        });
    });
}

/**
 * Update the custom component.
 * Only allow edit the title and content,
 * because the component can be used for other
 * templates and can break the grids.
 * @param id_component Id of the component to edit
 * @param title Title of the component to edit
 * @param content New content of the component
 */
function updateComponent(id_component, title, content) {
    $(document).ready(function(){
        $.ajax({
            url: '/templates/customcomponents/update/',
            data: {
                    id_component: id_component,
                    title: title,
                    content: content
            },
            dataType: "json",
            error: function(data) {
                console.error(data);
            },
            success: function(data) {
                $('#' + id_component).prev().text(title);
                $('#' + id_component).data("content", content);
                $("#add-widget").modal('hide');
            },
            type: 'POST'
        });
    });
}

/**
 * Save a complete template, creating or editing it.
 * @param id_template If is editing the template, can be null if is new
 * @param title Title of the template
 * @param description Description of the template
 * @param component_instances List of widgets of the template
 */
function saveTemplate(id_template, title, description, component_instances) {
    $(document).ready(function() {
        $.ajax({
            url: '/templates/save/',
            data: {
                    title_template: title,
                    description_template: description,
                    id_template: id_template,
                    instances_template: component_instances
            },
            dataType: "json",
            error: function(data) {

            },
            success: function(data) {
            	$("#saved").show();
            	document.getElementById("id_template").value = JSON.stringify(data)
            },
            type: 'POST'
        });
    });
}

/**
 * Delete the component.
 * @param id_component id of the component to delete
 */
function deleteComponent(id_component) {
    $(document).ready(function() {
        $.ajax({
            url: '/templates/customcomponents/delete/',
            data: {
                    id_component: id_component
            },
            dataType: "json",
            error: function(data) {
             	if (data.responseText == "ok") {
            	    $("#success-delete-component").show();
            	    $("#error-delete-component").alert('close');
            	    $("#" + id_component).parent().remove();
            	} else {
            	    $("#error-delete-component").show();
            	    $("#success-delete-component").alert('close');
            	}
            },
            success: function(data) {
            	if (data.responseText == "ok") {
            	    $("#success-delete-component").show();
            	    $("#error-delete-component").alert('close');
            	    $("#" + id_component).parent().remove();
            	} else {
            	    $("#error-delete-component").show();
            	    $("#success-delete-component").alert('close');
            	}
            },
            type: 'GET'
        });
    });
}

/**
 * Delete the component.
 * @param id_component id of the component to delete
 */
function loadTemplate(id_template) {
    $(document).ready(function() {
        $.ajax({
            url: '/templates/get/',
            data: {
                    id_template: id_template
            },
            dataType: "json",
            error: function(data) {
             	console.error(data);
            },
            success: function(data) {
            	gridster.remove_all_widgets();
            	$.each(Gridster.sort_by_row_and_col_asc(data), function() {
					addComponentInstance(this.id, this.component, this.content, this.size_x, this.size_y, this.position_x, this.position_y, this.removable, this.type);
				});
            },
            type: 'GET'
        });
    });
}

/**
 * Add the "click" event to addables elements.
 */
function addableEvent() {
	$(document).ready(function() {
		$('.addable-element').on('click', function() {
			addComponentInstance(uuid(), $(this).attr("id"), $(this).data("content"), $(this).data("x-size"), $(this).data("y-size"), 1, 1, true, $(this).data("type"));
		});
	});
}

/**
 * Add the editable functionality.
 * @param element Element to make editable
 */
function editableEvent(element) {
	$(element).on('click', function() {
		document.getElementById("x-size").readOnly = true;
		document.getElementById("y-size").readOnly = true;
		$("#create-component").hide();
		$("#update-component").show();
		document.getElementById("title").value = $(this).prev().prev().text();
		CKEDITOR.instances['widget-content'].setData($(this).prev().data("content"));
		document.getElementById("id_component").value = $(this).prev().attr("id");
		$("#add-widget").modal();
	});
}

/**
 * Get the cookie of the browser.
 * @param name Name of the cookie to get
 */
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

/**
 * Check the csrf safe method.
 * @param method Method to check
 */
function csrfSafeMethod(method) {
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

/**
 * Return the widget, removable or not.
 * @param id Id of the element
 * @param component component
 * @param removable if is removable or
 * @param type Type of the widget
 */
function getWidget(id, component, removable, type) {
	var widget = '<li id="' + id + '" class="element" data-component="' + component + '" data-type="' + type + '"><span class="move-component"> --- </span>';
	if (removable) {
		widget = widget + '<a class="remove"><span class="glyphicon glyphicon-remove" aria-hidden="true"</span></a>';
	}
	widget = widget + '<div id="editable_' + id + '" name="editable_' + id + '" class="editable"></div></li>';
	return widget;
}

/**
 * Prepare the csrf for
 * ajax calls.
 */
function prepareAjax() {
	$(document).ready(function(){
		$.ajaxSetup({
			beforeSend: function(xhr, settings) {
				if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
					xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
				}
			}
		});
	});
}

/**
 * Add a component to the template.
 * @param component Id of the template component
 * @param content Content of the widget
 * @param x_size Horizontal size of the widget
 * @param y_size Vertical size of the widget
 * @param x_position Horizontal position
 * @param y_position Vertical position
 * @param type Type of the component
 */
function addComponentInstance(id, component, content, x_size, y_size, x_position, y_position, removable, type) {
	var ck_id = "editable_" + id;
	gridster.add_widget(getWidget(id, component, removable, type), x_size, y_size, x_position, y_position);
	$(document).on('click', '.remove', function() {
		gridster.remove_widget($(this).parent());
	});
	inlineEdition(ck_id, content)
}

/**
 * Activate the inline editor.
 * @param id Id
 * @param content Content to set
 */
function inlineEdition(id, content) {

	$('#' + id).html(content);
}
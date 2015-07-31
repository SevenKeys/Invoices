var gridster;

/**
 * Start the grid.
 */
$(function() {
	$.fn.extend({
		template: function(initialData) {

			gridster = $(this).gridster({
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
						id_component: $($w).data('component')
					};
				}
			}).data("gridster");

			if (initialData != undefined && initialData != null && "" != initialData) {
				gridster.remove_all_widgets();
				$.each(Gridster.sort_by_row_and_col_asc(JSON.parse(encrypt(initialData))), function() {
					gridster.add_widget(getWidget(this.id, this.component, this.removable), this.size_x, this.size_y, this.position_y, this.position_x);
					$(document).on('click', '.remove', function() {
						gridster.remove_widget( $(this).parent());
					});
					CKEDITOR.disableAutoInline = true;
					CKEDITOR.inline("editable_" + this.id);
					CKEDITOR.instances["editable_" + this.id].setData(decrypt(this.content));
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

function saveComponent(title, sizex, sizey, cnt) {
    $(document).ready(function(){
		$.ajaxSetup({
			beforeSend: function(xhr, settings) {
				if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
					xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
				}
			}
		});
        $.ajax({
            url: '/invoices/templates/customcomponents/new/',
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
            	var customcomponent = '<li role="presentation"><a id="' + JSON.stringify(data) + '" class="addable-element" data-x-size="' + sizex + '" data-y-size="' + sizey + '" data-content="' + cnt + '">' + title + '</a><span class="glyphicon glyphicon-add"></span></li>';
            	$("#custom-components").append(customcomponent);
            	$("#add-widget").modal('hide');
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
            },
            type: 'POST'
        });
    });
}

function saveTemplate(id_template, title, description, component_instances) {
    $(document).ready(function(){
		$.ajaxSetup({
			beforeSend: function(xhr, settings) {
				if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
					xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
				}
			}
		});
        $.ajax({
            url: '/invoices/templates/save/',
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

function csrfSafeMethod(method) {
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

/**
 * Encryp the message.
 */
function encrypt(toEncrypt) {
	var Re = new RegExp('&quot;', "g");
	var formated = toEncrypt.replace(Re, '"');
	Re = new RegExp('\n', "g");
	formated = formated.replace(Re, '__jump__');
	Re = new RegExp("\t", "g");
	formated = formated.replace(Re, '__tab__')
	Re = new RegExp("\r", "g");
	formated = formated.replace(Re, '__return__')
	return formated;
}

function decrypt(toDecrypt) {
	Re = new RegExp("__jump__", "g");
	formated = toDecrypt.replace(Re, '\n')
	Re = new RegExp("__tab__", "g");
	formated = formated.replace(Re, '\t')
	Re = new RegExp("__return__", "g");
	formated = formated.replace(Re, '\r')
	return formated;
}

/**
 * Return the widget, removable or not.
 * @param id Id of the element
 * @param component component
 * @param removable if is removable or not
 */
function getWidget(id, component, removable) {
	var widget = '<li id="' + id + '" style="border: 2px solid red;" class="element" data-component="' + component + '"><span class="glyphicon glyphicon-move" aria-hidden="true"></span>';
	if (removable) {
		widget = widget + '<button type="button" class="btn btn-default remove" aria-label="Left Align"><span class="glyphicon glyphicon-remove" aria-hidden="true"</span></button>';
	}
	widget = widget + '<div id="editable_' + id + '" name="editable_' + id + '" class="editable" style="width:100%;height:100%"></div></li>';
	return widget;
}
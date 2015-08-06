$(function(){
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
var csrftoken = getCookie('csrftoken');

    $('#search_customers').keyup(function(){
    	if ($('#search_customers').val() != ''){
	    	$.ajax({
	    		type: 'POST',
	    		url: '/customers/search/',
	    		data: {
	    			'search_text':$('#search_customers').val(),
	    			'csrfmiddlewaretoken':$('input[name=csrfmiddlewaretoken]').val()
	    		},
	    		success: searchSuccessCust,
	    		dataType: 'html'
	    	});
	    }else{
	    	$('#search_customers_results').html('');
	    }
    });

    function searchSuccessCust(data, textStatus, jqXHR){
    	$('#search_customers_results').attr('display','block !important');
    	$('#search_customers_results').html(data);
    }

    $('#search_products').keyup(function(){
    	if ($('#search_products').val() != ''){
	    	$.ajax({
	    		type: 'POST',
	    		url: '/products/search/',
	    		data: {
	    			'search_text':$('#search_products').val(),
	    			'csrfmiddlewaretoken':$('input[name=csrfmiddlewaretoken]').val()
	    		},
	    		success: searchSuccessProd,
	    		dataType: 'html'
	    	});
	    }else{
	    	$('#search_products_results').html('');
	    }
    });

    function searchSuccessProd(data, textStatus, jqXHR){
    	$('#search_products_results').attr('display','block');
    	$('#search_products_results').html(data);
    };
});
	

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

    $('#search').keyup(function(){
    	$.ajax({
    		type: 'POST',
    		url: '/customers/search/',
    		data: {
    			'search_text':$('search').val(),
    			'csrfmiddlewaretoken':$('input[name=csrfmiddlewaretoken]')
    		},
    		success: searchSuccess,
    		dataType: 'html'
    	});
    });
    
    function searchSuccess(data, textStatus, jqXHR){
    	$('#search-results').html(data);
    }
});
	

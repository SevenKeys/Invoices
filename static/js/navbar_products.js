$(function(){
	$menu = $('#products-dropdown-menu');
	$menu.hide();
	$('#navbar_products').mouseover(function(){
		$menu.show();
	})
	$menu.mouseleave(function(){
		$(this).hide();
	})
});
$(function(){
	$menu = $('#products-dropdown-menu');
	$nav = $('#navbar_products');
	$menu.hide();
	$nav.mouseover(function(){
		$menu.show();
	});
	$menu.mouseleave(function(){
		$(this).hide();
	})
});
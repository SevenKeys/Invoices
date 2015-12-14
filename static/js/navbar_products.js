$(function(){
	$menu = $('#products-dropdown-menu');
	$menu_group = $('#product-group-dropdown-menu');
	$nav = $('#navbar_products');
	$nav_group = $('#navbar-product-groups');
	$menu.hide();
	$menu_group.hide();

	$nav.hover(
		function(){
			$menu.show();
		},
		function(){
			$menu.hide();
		}
	);
	$nav_group.hover(
		function(){
			$menu_group.show();
		},
		function(){
			$menu_group.hide();
		}
	);
});
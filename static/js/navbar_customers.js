$(function(){
	$menu = $('#customers-dropdown-menu');
	$menu_group = $('#customer-group-dropdown-menu');
	$nav = $('#navbar-customers');
	$nav_group = $('#navbar-customer-groups');
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
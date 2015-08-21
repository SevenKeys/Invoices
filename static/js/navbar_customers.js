$(function(){
	$menu_cust = $('#customers-dropdown-menu');
	$nav_cust = $('#navbar-customers');
	$menu_cust.hide();
	$nav_cust.hover(
		function(){
			$menu_cust.show();
		},
		function(){
			$menu_cust.hide();
		}
	);
});
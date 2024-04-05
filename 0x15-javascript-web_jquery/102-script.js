$(document).ready( function () {
	$('btn_translate').click( function (){
		var id = $('btn_translate').val();
	});

$.get( 'https://www.fourtonfish.com/hellosalut/hello/', function (data) {
	var result = data.hello;
	$('#hello').text(result);
});
});

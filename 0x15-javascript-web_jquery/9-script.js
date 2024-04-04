$.get('https://hellosalut.stefanbohacek.dev/?lang=fr', function(data) {
	var val = data.hello;
	$('#hello').text(val)
});

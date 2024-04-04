$.get('https://swapi-api.alx-tools.com/api/people/5/?format=json', function(data) {
	var charName = data.name;
	$('character').text(charName)
});

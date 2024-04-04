$.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (data) {
	var titles;
	$.each(data.results, function(index, movie){
	var LiatIte = $('<li>'),text(movie.title);
	$('#list_movies').append(listItem);
});
});

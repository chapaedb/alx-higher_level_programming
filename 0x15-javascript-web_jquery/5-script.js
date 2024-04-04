$('#add_item').click( function ()  {
	const new_item = $('<li>Item</li>');
	$('UL.my_list').append(new_item)
});

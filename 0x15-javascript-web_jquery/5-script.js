$('#add_item').click(function () {
  $('my_list').add('<li>Item</li>').add('').appendTo('ul.my_list');
});

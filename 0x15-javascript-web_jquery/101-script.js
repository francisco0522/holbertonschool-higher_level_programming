$(document).ready(() => {
  $('#add_item').click(function () {
    $('.my_list').append('<li>Item</li>');
  });
  $('#remove_item').click(function () {
    $('.my_list LI').slice(-1).remove();
  });
  $('#clear_list').click(function () {
    $('.my_list LI').remove();
  });
});

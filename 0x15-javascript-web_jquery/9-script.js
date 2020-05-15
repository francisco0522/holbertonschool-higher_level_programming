$.get('https://fourtonfish.com/hellosalut/?lang=fr', function (data) {
  $('.result').html(data);
  $('#hello').text(data.hello);
});

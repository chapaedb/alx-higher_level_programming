$(document).ready(function() {
    $('#btn_translate').click(fetchTranslation);
    $('#language_code').keypress(function(event) {
      if (event.keyCode === 13) {
        fetchTranslation();
      }
    });
  
    function fetchTranslation() {
      var languageCode = $('#language_code').val();
      var apiUrl = 'https://hellosalut.stefanbohacek.dev/?lang=' + languageCode;
  
      $.get(apiUrl, function(data) {
        var translation = data.hello;
        alert(translation);
      });
    }
  });

$(() => {
  $.ajax({
    type: 'GET',
    url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
    success: (data) => {
      $.each(data.results, (indexInArray, valueOfElement) => {
        $('ul#list_movies').append('<li>' + valueOfElement.title + '</li>');
      });
    }
  });
});

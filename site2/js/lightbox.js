/* Lightbox JS */

document.addEventListener('DOMContentLoaded', function() {
  let images = document.querySelectorAll('.lightbox-image');
  images.forEach(function(image) {
    image.addEventListener('click', function(event) {
      event.preventDefault();
      let href = image.getAttribute('href');
      let lightbox = document.createElement('div');
      lightbox.setAttribute('id', 'lightbox');
      lightbox.innerHTML = '<img src="' + href + '">' +
                           '<a href="#" class="close">&times;</a>';
      document.body.appendChild(lightbox);
      let closeButton = document.querySelector('.close');
      closeButton.addEventListener('click', function(event) {
        event.preventDefault();
        lightbox.remove();
      });
    });
  });
});

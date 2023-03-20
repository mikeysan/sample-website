/* Lightbox JS */
// Lightbox functionality
var $lightbox = $("<div id='lightbox'></div>");
var $img = $("<img>");
var $caption = $("<p></p>");

// Add image and caption to lightbox
$lightbox.append($img);
$lightbox.append($caption);

// Add lightbox to the document
$('body').append($lightbox);

// Hide lightbox on click
$lightbox.click(function() {
  $lightbox.hide();
});

// Show the previous image in the lightbox
function showPrevImage() {
  var $prev = $('.lightbox-image.active').prev('.lightbox-image');
  if ($prev.length) {
    var src = $prev.data('src');
    var caption = $prev.data('caption');
    $img.attr('src', src);
    $caption.text(caption);
    $('.lightbox-image.active').removeClass('active');
    $prev.addClass('active');
  }
}

// Show the next image in the lightbox
function showNextImage() {
  var $next = $('.lightbox-image.active').next('.lightbox-image');
  if ($next.length) {
    var src = $next.data('src');
    var caption = $next.data('caption');
    $img.attr('src', src);
    $caption.text(caption);
    $('.lightbox-image.active').removeClass('active');
    $next.addClass('active');
  }
}

// Add click events to each image in the gallery
$('.gallery-image').click(function() {
  var src = $(this).attr('src');
  var caption = $(this).data('caption');
  $img.attr('src', src);
  $caption.text(caption);
  $lightbox.show();
  $('.lightbox-image').removeClass('active');
  $(this).addClass('active');
});

// Add click events to the prev and next buttons in the light
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

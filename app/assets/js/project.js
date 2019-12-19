/* Project specific Javascript. */

// Set Copyright date to current year
const date = new Date();
document.querySelector('.year').innerHTML = date.getFullYear();

// Set fade timing on any messages
setTimeout(function() {
  $('#message').fadeOut('slow');
}, 3000);


/* Template JS */
(function($) {
  "use strict";

  // Page Scroll
  var page_scroll = $('a.page-scroll');
  page_scroll.on('click', function(event) {
    var $anchor = $(this);
    $('html, body').stop().animate({
      scrollTop: $($anchor.attr('href')).offset().top - 55
    }, 1500, 'easeInOutExpo');
    event.preventDefault();
  });

  // Back to top button
  $(window).scroll(function() {
    if ($(this).scrollTop() > 100) {
      $('.back-to-top').fadeIn('slow');
    } else {
      $('.back-to-top').fadeOut('slow');
    }
  });

  $('.back-to-top').click(function(){
    $('html, body').animate({scrollTop : 0},1500, 'easeInOutExpo');
    return false;
  });

})(jQuery);


// Activate tab panels
$('#prodTab li:first-child a').tab('show') // Select first tab

$('#prodTab a').on('click', function (e) {
  e.preventDefault()
  $(this).tab('show')
})



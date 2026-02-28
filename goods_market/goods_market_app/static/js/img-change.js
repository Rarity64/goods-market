$(document).ready(function() {
  $(".good-img").hover(function() {
    let img = $(this);
    let src = img.attr('src');
    $(this).attr("src", src.replace('1.png', '2.png'));
  }, 
  function() {
    let img = $(this);
    let src = img.attr('src');
    $(this).attr("src", src.replace('2.png', '1.png'))
  });
});
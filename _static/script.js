var colWidth = $(".grid-item").width();

window.onresize = function () {
  var colWidth = $(".grid-item").width();
};
console.log(colWidth);

var $grid = $(".masonry").masonry({
  // options
  itemSelector: ".grid-item",
  columnWidth: ".grid-item",
  // percentPosition: true,
  gutter: 10,
  fitWidth: true,
});

$grid.imagesLoaded().progress(function () {
  $grid.masonry("layout");
});

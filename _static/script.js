var colWidth = $(".grid-item").width();

window.onresize = function () {
  colWidth = $(".grid-item").width();
};

var $grid = $(".masonry").masonry({
  itemSelector: ".grid-item",
  columnWidth: ".grid-item",
  percentPosition: true,
  gutter: 10,
  fitWidth: true,
});

toastr.options = {
  closeButton: true,
  debug: false,
  newestOnTop: false,
  progressBar: false,
  positionClass: "toast-top-right",
  preventDuplicates: false,
  onclick: null,
  showDuration: "300",
  hideDuration: "1000",
  timeOut: "5000",
  extendedTimeOut: "1000",
  showEasing: "swing",
  hideEasing: "linear",
  showMethod: "fadeIn",
  hideMethod: "fadeOut",
};

$(function () {
    $(".logo").draggable().resizable();
    $(".logo").each(function() {
        $(this).prepend('<span class="drag">&nbsp;</span>')
    })
});


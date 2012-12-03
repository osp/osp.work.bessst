var storePositions = function() {
    $('.logo').each(function() {
        positions.push( $(this).offset() );
    });
}

var retrievePositions = function() {
    for (var i=0; i < positions.length; i++) {
        $($('.logo')[i]).offset(positions[i]);
    };
}

$(function () {
    $(".logo").draggable().resizable();
    $(".logo").each(function() {
        $(this).prepend('<span class="drag">&nbsp;</span>')
    })

    retrievePositions();
});

(function($)
{
    $.fn.tailing=function()
    {
        return this.each(function(){
            height = $(this).height();
            width = $(this).width();
            lineheight = parseInt($(this).css("line-height"));
            lines = height/lineheight;
            step = 20;
            tail_lines = (width/2)/step;
            keep_lines = lines - tail_lines + 8
            // console.log($(this))
            // console.log("height = " + height)
            // console.log("width = " + width)
            // console.log("lineheight = " + lineheight)
            // console.log("lines = " + lines)
            // console.log("tail_lines = " + tail_lines)
            wraps = "<div style='clear: left; float: left; width: 0px; height: " + keep_lines * lineheight + "px'></div> <div style='clear: right; float: right; width: 0px; height: " + keep_lines * lineheight + "px'></div>";
            for (i=step; i<width/2; i+=step) {
                wraps += "<div style='clear: left; float: left; width:"+ i +"px; height: " + lineheight + "px'></div> <div style='clear: right; float: right; width:"+ i +"px; height: " + lineheight + "px'></div>";
            }
                $(this).prepend(wraps);
                $(this).append("<div style='clear: both;'></div>");
        });
    };
})(jQuery);

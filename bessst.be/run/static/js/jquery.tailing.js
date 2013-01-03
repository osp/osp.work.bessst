(function($)
{
    $.fn.tailing=function()
    {
        return this.each(function(){
            height = $(this).height();
            width = $(this).width();
            lineheight = parseInt($(this).css("line-height"));
            lines = height/lineheight;
            step = Math.floor(width/20);
            tail_lines = Math.floor((width/2)/step);

            base_surface = height*width
            tail_blank_surface = width * (tail_lines*lineheight) /2
            remaining_surface = base_surface - tail_blank_surface

            keep_lines = Math.round((base_surface - tail_blank_surface) / (width * lineheight)) + 1

            //console.log($(this))
            //console.log("height = " + height)
            //console.log("width = " + width)
            //console.log("base-surface = " + height*width)

            //console.log("lineheight = " + lineheight)
            //console.log("lines = " + lines)
            //console.log("step = " + step)

            //console.log("tail_lines = " + tail_lines)
            //console.log("lines - tail_lines = " + (lines - tail_lines))
            //console.log("keep_lines = " + keep_lines)

            //console.log("tail_blank_surface = " + width * (tail_lines*lineheight)/2)
            //console.log("remaining_surface = " + remaining_surface)
            //console.log("keep_surface = " + keep_surface)

            wraps = "<div style='clear: left; float: left; width: 0px; height: " + keep_lines * lineheight + "px'></div> <div style='clear: right; float: right; width: 0px; height: " + keep_lines * lineheight + "px'></div>";
            for (i=step; i<width/2; i+=step) {
                wraps += "<div style='clear: left; float: left; width:"+ i +"px; height: " + lineheight + "px'></div> <div style='clear: right; float: right; width:"+ i +"px; height: " + lineheight + "px'></div>";
            }
                $(this).prepend(wraps);
                //console.log("new number of lines = " + $(this).height()/lineheight)
                $(this).append("<div style='clear: both;'></div>");
        });
    };
})(jQuery);

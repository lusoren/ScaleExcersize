var id= 0;
var im= 0;

var timeout= $("body");

$(document).ready(function(){
    
    timeout = setInterval(function(){
            addDiv();
            id++;
            }, 0);

    return false;
});

function addDiv() {
            
    var w = window.innerWidth;
    var h = window.innerHeight;
    
    var opacity = h/1000;
    
    var width = 1500 - w;
    var height = 1500 - h;
    
    $("#width").html(w);
    $("#height").html(h);
    
    $("#circle").css("width", width);
    $("#circle").css("height", width);
    
    $("#circle").css("opacity", opacity);
    
    if (w >700 && w <900 ) {
        $("body").css("background-color", "cyan");
    }
    
    else {
        $("body").css("background-color", "blue");      
    }
}


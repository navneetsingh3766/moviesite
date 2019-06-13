$(document).ready(function(){
	var isTouch = (('ontouchstart' in window) || (navigator.msMaxTouchPoints > 0));
	if (isTouch == false){
	$(".movie-image").hover(function(){
		$(this).find(".play").show();

	},
	function()
	{
		$(this).find(".play").hide();
	});


	$(".blink").focus(function() {
            if(this.title==this.value) {
                this.value = '';
            }
        })
        .blur(function(){
            if(this.value=='') {
                this.value = this.title;                    
			}
		});
	}
	else{
		$("span").remove();
	}
});

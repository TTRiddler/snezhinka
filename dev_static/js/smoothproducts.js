!function(d){d.fn.extend({deleteSmoothProducts:function(){d(document.body).off("click",".sp-large a"),d(document.body).off("click",".sp-noff-touch .sp-zoom"),d(document.body).off("click",".sp-tb-active a"),d(document.body).off("click",".sp-thumbs")},smoothproducts:function(){d(".sp-loading").hide(),d(".sp-wrap").each(function(){if(d(this).addClass("sp-touch"),1<d("a",this).length){var p,i,n=!!d("a.sp-default",this)[0];d(this).append('<div class="sp-large"></div><div class="sp-thumbs sp-tb-active"></div>'),d("a",this).each(function(s){var t=d("img",this).attr("src"),e=d(this).attr("href"),a="";(0===s&&!n||d(this).hasClass("sp-default"))&&(a=' class="sp-current"',p=e,i=d("img",this)[0].src),d(this).parents(".sp-wrap").find(".sp-thumbs").append('<a href="'+e+'" style="background-image:url('+t+')"'+a+"></a>"),d(this).remove()}),d(".sp-large",this).append('<a href="'+p+'" class="sp-current-big"><img src="'+i+'" alt="" /></a>'),d(".sp-wrap").css("display","inline-block")}else d(this).append('<div class="sp-large"></div>'),d("a",this).appendTo(d(".sp-large",this)).addClass(".sp-current-big"),d(".sp-wrap").css("display","inline-block")}),d(document.body).on("click",".sp-thumbs",function(s){s.preventDefault()}),d(document.body).on("mouseover",function(s){d(".sp-wrap").removeClass("sp-touch").addClass("sp-non-touch"),s.preventDefault()}),d(document.body).on("touchstart",function(){d(".sp-wrap").removeClass("sp-non-touch").addClass("sp-touch")}),d(document.body).on("click",".sp-tb-active a",function(s){s.preventDefault(),d(this).parent().find(".sp-current").removeClass(),d(this).addClass("sp-current"),d(this).parents(".sp-wrap").find(".sp-thumbs").removeClass("sp-tb-active"),d(this).parents(".sp-wrap").find(".sp-zoom").remove();var t=d(this).parents(".sp-wrap").find(".sp-large").height(),e=d(this).parents(".sp-wrap").find(".sp-large").width();d(this).parents(".sp-wrap").find(".sp-large").css({overflow:"hidden",height:t+"px",width:e+"px"}),d(this).addClass("sp-current").parents(".sp-wrap").find(".sp-large a").remove();var a=d(this).parent().find(".sp-current").attr("href"),p=d(this).parent().find(".sp-current").css("backgroundImage").match(/url\([\"\']{0,1}(.+)[\"\']{0,1}\)+/i)[1];d(this).parents(".sp-wrap").find(".sp-large").html('<a href="'+a+'" class="sp-current-big"><img src="'+p+'"/></a>'),d(this).parents(".sp-wrap").find(".sp-large").hide().fadeIn(250,function(){var s=d(this).parents(".sp-wrap").find(".sp-large img").height();d(this).parents(".sp-wrap").find(".sp-large").animate({height:s},"fast",function(){d(".sp-large").css({height:"auto",width:"auto"})}),d(this).parents(".sp-wrap").find(".sp-thumbs").addClass("sp-tb-active")})}),d(document.body).on("mouseenter",".sp-non-touch .sp-large",function(s){var t=d("a",this).attr("href");d(this).append('<div class="sp-zoom"><img src="'+t+'"/></div>'),d(this).find(".sp-zoom").fadeIn(250),s.preventDefault()}),d(document.body).on("mouseleave",".sp-non-touch .sp-large",function(s){d(this).find(".sp-zoom").fadeOut(250,function(){d(this).remove()}),s.preventDefault()}),d(".sp-large").mousemove(function(s){var t=d(this).width(),e=d(this).height(),a=d(this).offset(),p=d(this).find(".sp-zoom").width(),i=d(this).find(".sp-zoom").height(),n=s.pageX-a.left,r=s.pageY-a.top,o=Math.floor(n*(t-p)/t),h=Math.floor(r*(e-i)/e);d(this).find(".sp-zoom").css({left:o,top:h})})}})}(jQuery);

   $('.case-item .swiper-container').swiper({
        pagination: '.swiper-pagination',
        slidesPerView: 4,
        paginationClickable: '.swiper-pagination',
        nextButton: '.swiper-button-next',
        prevButton: '.swiper-button-prev',
        spaceBetween: 27


    });
    $('.js_topping').on('click',function(){       
        $('html,body').animate({scrollTop: '0px'}, 600);
    });

    $('.features-con').find('img:first').show();
    $('.features-menu a').on('mouseover',function(){       
         var index=$(this).index(); 
         $('.features-con').find('img').hide().eq(index).show();           
         $(this).addClass('active').siblings().removeClass('active');  
         return false;
    }); 
    $('.js_menu_pro .weui-cell__ft').find('img:first').show();
    $('.js_menu_pro a').on('click',function(){       
         var index=$(this).index(); 
         $('.js_menu_pro .weui-cell__ft').find('img').hide().eq(index).show();           
         $(this).addClass('active').siblings().removeClass('active');  
         return false;
    }); 
    jQuery.scrollto = function(scrolldom,scrolltime) {

        $(scrolldom).click( function(){
            var scrolltodom = $(this).attr('date-scroll');
            $(this).addClass('active').siblings().removeClass('active');
           
            $('html,body').animate({
                    scrollTop:$(scrolltodom).offset().top-90},scrolltime
            );
            
            return false;
        });

    };

    $.scrollto(".job-list li",600);          

    $('.menu li').each(function(i,o){     
        $(o).on('click',function(){
            $(o).addClass('active').siblings().removeClass('active');           
          
        });
    });  
    if(!$('.menu li').hasClass('active')){
        $('.menu li:first').addClass('active');
    }

  $('.js_sales_qrcode').each(function(i,o){     
        $(o).on('click',function(e){
        if($(o).next().css('display')=='none'){
            $(o).parent().parent().parent().addClass('active').siblings().removeClass('active');                
            $(o).next().show();                

        }else{  
            $(o).next().hide();  
        }
        e.stopPropagation();
               
          
        });
    });   
    $(document).click(function(){
        $('.sales-desc').removeClass('active');
    });

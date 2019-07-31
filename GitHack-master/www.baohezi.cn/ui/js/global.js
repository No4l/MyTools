//js模仿hover属性
$(function(){
    $("#tabs li").mouseenter(function(){
        //给li添加下横线
        $(this).addClass('active').siblings('li').removeClass('active');
        var index = $(this).index();
        console.log(index);
        //显示对应的div
        $('.news-box-company').eq(index).addClass('news-box-active').siblings('div').removeClass('news-box-active');
    })
});
$(function() {
    $(".standard-box").hover(function () {
        $(this).addClass('hover');
    }, function () {
        $(this).removeClass('hover');
    })
});
//咨询弹框
$(".close-global").click(function(){
    $(".fixed-frame-box").hide();
});
$(".catact-box-global").click(function(){
    $(".fixed-frame-box").show();
});
// 案列选项卡切换
$(function(){
    $("#caseTabs li").click(function(){
        //给li添加下横线
        $(this).addClass('active').siblings('li').removeClass('active');
        var index = $(this).index();
        console.log(index);
        //显示对应的div
        $('.case-content-box').eq(index).addClass('case-content-box-active').siblings('div').removeClass('case-content-box-active');
    })
});
<div class="footer-container box-container pt-50">
    <div class="footer-area-box">
        <div class="link-text-box">
            <div class="footer-logo"><img src="<?php echo HTTP_UI ;?>img/bottom-logo.png"></div>
            <div class="link-text">
                <a class="mr-50" href="#" >网站首页</a>
                <a class="mr-50" href="#">产品服务</a>
                <a class="mr-50" href="#">新闻动态</a>
                <a class="mr-50" href="#">招商加盟</a>
                <a class="mr-50" href="#">关于我们</a>
                <a href="#">联系我们</a>
            </div>
            <ul>
                <li class="mr-20 mt-23"><span class="iconfont icon-facebook"></span></li>
                <li class="mr-20 mt-23"><span class="iconfont icon-telegram active"></span></li>
                <li class="mr-20 mt-23"><span class="iconfont icon-weibiaoti504"></span></li>
                <li class="mr-20 mt-23"><span class="iconfont icon-twitter0"></span></li>
                <li class=" mt-23"><span class="iconfont icon-github"></span></li>
            </ul>
        </div>
        <em></em>
        <div class="address-box">
            <p>
                <span class="pr-22">客服电话：133-0716-6750</span>
                <span>公司地址：武汉市洪山区光谷168号</span>
                <span class="pl-40 pr-20 iconfont icon-weibo red"></span>
                <span class="iconfont icon-weixin green"></span>
            </p>
        </div>
        <div class="copyright-box">
            <p>武汉宝盒子科技有限公司 © 2011-2013 baohezi.cn鄂ICP备12004378号
                <span class="pl-40 pr-10">
                    <a target="_blank" href="http://www.beian.gov.cn/portal/registerSystemInfo?recordcode=42011102001245" style="display:inline-block;text-decoration:none;height:20px;line-height:20px;">
                        <img class="mr-10" src="<?php echo HTTP_UI ;?>img/check.png" style="float:left;"/>
                        鄂公网安备 42011102001245号
                    </a>
                </span>
            </p>
        </div>
    </div>
</div>
<div class="fixed-frame-box">
    <h1>在线咨询<span class="iconfont icon-guanbi pl-65 close-global"></span></h1>
    <ul class="catact-way-list">
        <li class="qq" >
            <span class="iconfont icon-QQ pr-10"></span>
            <span class="text">点击咨询</span>
        </li>
        <li class="phone" href="#">
            <span class="iconfont icon-dianhua"></span>
            <p><span>联系电话</span><br><span class="bottom">133-0716-6750</span></p>
        </li>
    </ul>
</div>
<!-- Swiper JS -->
<script src="<?php echo HTTP_UI ;?>/js/jquery-3.2.1.min.js"></script>
<script src="<?php echo HTTP_UI ;?>/js/swiper.min.js"></script>
<!-- Initialize Swiper -->

<script src="<?php echo HTTP_UI ;?>/js/global.js"></script>
<script>
    //首页幻灯片
    var swiper = new Swiper('.swiper-container', {
        slidesPerView: 1,
        spaceBetween: 30,
        loop: true,
        pagination: {
            el: '.swiper-pagination',
            clickable: true,
        },
        navigation: {
            nextEl: '.swiper-button-next',
            prevEl: '.swiper-button-prev',
        },
    });
</script>
</body>
</html>

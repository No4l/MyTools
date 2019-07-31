<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title><?php echo $SEO['title']; ?></title>
    <meta name="keywords" content="<?php echo $SEO['keywords']; ?>" />
    <meta name="description" content="<?php echo $SEO['description']; ?>" />
    <meta name="viewport" content="width=device-width, initial-scale=1, minimum-scale=1, maximum-scale=1">
    <link rel="stylesheet" href="//at.alicdn.com/t/font_891541_kgenfl1t63m.css" media="all" />
    <link href="<?php echo HTTP_UI; ?>css/swiper.min.css" rel="stylesheet" type="text/css"/>
    <link href="<?php echo HTTP_UI; ?>css/global.css?v=<?=time();?>" rel="stylesheet" type="text/css"/>
    <link href="<?php echo HTTP_UI; ?>css/common.css?v=<?=time();?>" rel="stylesheet" type="text/css"/>
    <script type="text/javascript">
    try {
    var urlhash = window.location.hash;
    if (!urlhash.match("fromapp"))
    {
    if ((navigator.userAgent.match(/(iPhone|iPod|Android|ios|iPad)/i)))
    {
    window.location="http://www.baohezi.cn/wap";
    }
    }
    }
    catch(err)
    {}
</script>
</head>
<body>
<header class="header">
    <div class="container">
        <a href="<?php echo DOMAIN_NAME_WWW;?>" class="logo"><img src="<?php echo HTTP_UI ;?>img/head-logo.png"></a>
        <div class="menu">
            <div class="index-nav-frame-line active" tabindex="-1">
                <a href="<?php echo DOMAIN_NAME_WWW;?>">网站首页</a>
            </div>
            <div class="index-nav-frame-line" tabindex="-1">
                产品服务<img class="pl-5" src="<?php echo HTTP_UI ;?>img/xl.jpg">
                <div class="index-nav-frame-line-center">
                    <div class="index-nav-frame-line-li">
                        <a href="today_news">今日快讯</a>
                    </div>
                    <div class="index-nav-frame-line-li">
                        <a href="chain_news">链讯</a>
                    </div>
                    <div class="index-nav-frame-line-li">
                        <a href="net_chain">互联网产品开发</a>
                    </div>
                    <div class="index-nav-frame-line-li">
                        <a href="block_chain">区快链开发</a>
                    </div>
                    <div class="index-nav-frame-line-li">
                        <a href="network_marketing">网络营销服务</a>
                    </div>
                    <div class="index-nav-frame-line-li">
                        <a href="advert">网络广告服务</a>
                    </div>
                    <div class="index-nav-frame-line-li">
                        <a href="case_show">案列展示</a>
                    </div>
                </div>
                <div class="index-nav-frame-line-focus" tabindex="-1"></div>
            </div>
            <div class="index-nav-frame-line" tabindex="-1">
                新闻动态<img class="pl-5" src="<?php echo HTTP_UI ;?>img/xl.jpg">
                <div class="index-nav-frame-line-center">
                    <div class="index-nav-frame-line-li">
                        <a href="company_news">公司新闻</a>
                    </div>
                    <div class="index-nav-frame-line-li">
                        <a href="industry_news">行业新闻</a>
                    </div>
                </div>
                <div class="index-nav-frame-line-focus" tabindex="-1"></div>
            </div>
            <div class="index-nav-frame-line" tabindex="-1">
                关于我们<img class="pl-5" src="<?php echo HTTP_UI ;?>img/xl.jpg">
                <div class="index-nav-frame-line-center ">
                    <div class="index-nav-frame-line-li">
                        <a href="about">公司介绍</a>
                    </div>
                    <div class="index-nav-frame-line-li">
                        <a href="teams">精英团队</a>
                    </div>
                    <div class="index-nav-frame-line-li">
                        <a href="culture">企业文化</a>
                    </div>
                    <div class="index-nav-frame-line-li">
                        <a href="vision">企业愿景</a>
                    </div>
                    <div class="index-nav-frame-line-li">
                        <a href="history">发展历程</a>
                    </div>
                </div>
                <div class="index-nav-frame-line-focus" tabindex="-1"></div>
            </div>
            <div class="index-nav-frame-line " tabindex="-1">
                联系我们<img class="pl-5" src="<?php echo HTTP_UI ;?>img/xl.jpg">
                <div class="index-nav-frame-line-center">
                    <div class="index-nav-frame-line-li ">
                        <a href="contact">联系方式</a>
                    </div>
                    <div class="index-nav-frame-line-li">
                        <a href="recruit">人才招聘</a>
                    </div>
                </div>
                <div class="index-nav-frame-line-focus" tabindex="-1"></div>
            </div>
        </div>
    </div>
</header>

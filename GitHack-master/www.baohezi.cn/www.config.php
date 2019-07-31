<?php
//时区设置
date_default_timezone_set('PRC');
//开启数据库报错机制
define('MYSQL_DEBUG', true);
//开启框架报错机制
define('YSP_DEBUG', true);
//数据库连接信息

$db_config = array(
    'host' => '182.92.102.87',
    'port' => 3306,
    'user' => 'ubaohezi',
    'pwd' => 'TzQ5DqcTm8EpdQR5',
    'dbname' => 'dwwwbhzdb'
);

define('WEBSITE_ROOT_BASE', rtrim(str_replace('\\', '/', dirname(__FILE__)), '\/'));

define('DOMAIN_NAME', '.baohezi.cn');
define('DOMAIN_NAME_WWW', 'http://www' . DOMAIN_NAME);
//以下配置主要用于单域名配置
define('HTTP_UI', DOMAIN_NAME_WWW . '/ui/');
define('HTTP_UPLOAD', DOMAIN_NAME_WWW . '/upload/');
//物理路径
//网站上传目录
define('PATH_UPLOAD', WEBSITE_ROOT_BASE . '/upload/');
//本模块控制层的目层，每个模块应单独修改下面的控制层的路径
define('PATH_CONTROLLERS', WEBSITE_ROOT_BASE . '/controllers/');
//本域名下的插件目录
define('HTTP_EXTENDS', DOMAIN_NAME_WWW . '/extends/');
//COOKIE KEY
define('COOKIE_KEY', 'aksdfj9234df32@#!$%dxkj');

//开发目录
define('PATH_VIEW', WEBSITE_ROOT_BASE . '/view/');

<?php
//时区设置
date_default_timezone_set('PRC');
//开启数据库报错机制
define('MYSQL_DEBUG', true);
//数据库连接信息

$db_config = array(
    'host' => '182.92.102.87',
    'port' => 3306,
    'user' => 'ubaohezi',
    'pwd' => 'TzQ5DqcTm8EpdQR5',
    'dbname' => 'dwwwbhzdb'
);

define('ADMIN_FOLDER', 'admin');
define('WEBSITE_ROOT_BASE', rtrim(str_replace('\\', '/', str_replace(ADMIN_FOLDER, '', dirname(__FILE__))), '\/'));
//网站上传目录
define('PATH_UPLOAD', WEBSITE_ROOT_BASE . '/upload/');

//总后台控制层的目录
define('PATH_CONTROLLERS', WEBSITE_ROOT_BASE . '/' . ADMIN_FOLDER . '/controllers/');
//公共文件夹的目录
define('PATH_COMMON', WEBSITE_ROOT_BASE . '/' . ADMIN_FOLDER . '/common/');

//项级域名，不带www的域名，下面是举的例子，应以正式项目的域名为主
define('DOMAIN_NAME', '.baohezi.cn');
/**
 * 以下网站的upload文件夹对应的文件，有多域名配置权限的可以按以下方案做。
 * 如果没有多域名权限的，则应该更改为单域名模式，以保证ui和upload的中的文件能被正确调用到。
 * 主要用于多域名架构的网站
 */
//define('HTTP_UPLOAD', 'http://upload.' . DOMAIN_NAME);
//以下配置主要用于单域名配置
//后台域名前缀
define('DOMAIN_NAME_ADMIN', 'http://www' . DOMAIN_NAME . '/' . ADMIN_FOLDER);
define('HTTP_UI', DOMAIN_NAME_ADMIN. '/ui/');
//以下是主域名配置，如果有其它域名，后台需要调用，则依次在下面列出来
define('DOMAIN_NAME_WWW', 'http://www' . DOMAIN_NAME);
define('HTTP_UPLOAD', DOMAIN_NAME_WWW . '/upload/');
//本域名下的插件目录
define('HTTP_EXTENDS', DOMAIN_NAME_ADMIN . '/extends/');

//COOKIE KEY
define('COOKIE_KEY', 'sa@#$^%kfjh3@543sdsh4eq9pm');

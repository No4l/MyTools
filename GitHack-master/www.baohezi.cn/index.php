<?php
// error_reporting(E_ALL^E_NOTICE);
// require 'ysp/YspFramework/ysp.config.php';
require 'ysp.config.php';
require 'www.config.php';
$controller = isset($_GET['C']) ? trim($_GET['C']) : 'Index';
$controller .= 'Page';
$action = isset($_GET['A']) ? trim($_GET['A']) : 'index';
require PATH_CONTROLLERS . 'BasePage.php';
require_once PATH_CONTROLLERS . "$controller.php";
$obj = new $controller();
if (method_exists($obj, $action)) {
    $obj->$action();
}
unset($obj);

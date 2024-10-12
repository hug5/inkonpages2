<?php
namespace mooHtml\inkonpages;

class Contact implements ArticleInterface {

    private $html;
    private $config;

    //private $showBillboard = true;
    //private $showSidebar = false;

    public function getHtml()
    {
        return $this->html;
    }

    public function getConfig()
    {
        return $this->config;
    }

    //public function getShowSidebar() {
    //        return $this->showSidebar;
    // }
    //public function getShowBillboard() {
    //        return $this->showBillboard;
    //}

    public function doConfig()
    {

        $logoTitle = F::json("config", "siteName");

        $title = "Contact Us | $logoTitle";

        $description = F::json("config", "siteDescription");
        $keywords    = "Contact Us, " . F::json("config", "siteKeywords");


        $this->config = [
            //"showBillboard"  => false,
            //"showSidebar"    => false,
            "title"          => $title,
            "description"    => $description,
            "keywords"       => $keywords
        ];

    }

    private function doContactHtml()
    {
        $oContactHtml = new ContactHtml();
        $this->html = $oContactHtml->getHtml();
    }


    private function doAction($action)
    {
        // //if bad url under /book/, then just go to /book/theswine/ url
        // if (!$action) F::goUrl($this->swh); //url should be /book/xyz/

        // if ($action == "theswines") {
        //    $this->doBook_TheSwines();
        //    // $this->doBookHtml($action);
        // } else {
        //     // echo "test3"; exit;
        //     F::goUrl($this->swh);
        // }

    }

    private function readUrl()
    {
        $arr = G::$urlParams; // get url params
        $moreParam = $arr[1] ?? false;

        //there should be no other params after /contact/
        if ($moreParam) {
            F::goUrl("/contact/");
        }

    }

    private function init()
    {

        // $this->swh = G::$baseUrl . "/book/theswines/";
        // $this->swh = "/book/theswines/";
    }

    private function start()
    {

        $action = $this->readUrl();
        $this->doContactHtml();
        $this->doConfig();

        // $this->init();

        // $this->doAction($action);
    }

    public function __construct()
    {
        $this->start();
    }
}

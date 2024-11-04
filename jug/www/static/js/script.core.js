
import { G, lib } from "./script.lib.js";
// import "./script.lib.js";
// import * as script_libx from "./script.lib.js";

$(function() {
//////////////////////////////////



function setHomeSection() {

    if ( $("#homeSection").length < 1 ) return false;
    //if ( $("#homeTest").length < 1 ) return false;



}

function setContactSection() {

    if ( $("#contactSection").length < 1 ) return false;

    var this_btn; //set later

    var doAjax = function(name, email, msg) {

        var p_action  = "contactUsMsg",
            p_name    = lib.ajaxencode(name),
            p_email   = lib.ajaxencode(email),
            p_msg     = lib.ajaxencode(msg),

            param     = "action=" + p_action +
                        "&name=" + p_name +
                        "&email=" + p_email +
                        "&msg=" + p_msg;
// alert(param);
        $.post(G.ajaxUrl, param, function(result) {

            $(this_btn).removeClass("disabled");

            // alert(result)

            if (result == "ok") {
                $("#msgForm").slideUp(400, function() {
                    $("#formSection p").fadeIn(300).html("YOUR MESSAGE WAS SENT!");
                });
            }

            else {
                $("#formSection p").fadeIn(300).html("Oops! There was an error.");
            }
        });
    };

    //init events
    $("#sendBtn").on("click", function() {

        if ( !lib.formInputCheck("msgForm") || $(this).hasClass("disabled") ) return false;


        var name  = $("#nameField").val(),
            email = $("#emailField").val(),
            msg   = $("#msgField").val();
        this_btn = $(this); //not part of var inititialization above

        doAjax(name, email, msg);

        return false;
    });

}

function doDelayload() {
//anything we want to delay doing in order to help speed up page load;


   //Using delayload to change from jpg to apng background; but not replacing but
   //using #pageDiv to replace over the old body bg; this prevent jerky effect;
   (function doChangePreloadBG() {

       if ( $("#homeSection").length < 1 ) return false;

       var bg = "url(\"/static/img/victory-web-press.jpg\")";

       // the bg is not shared by all pages; so load via js for home page only
       $("body").css("background-image", bg);

       //#1 timed event
       var loadApngImg = setTimeout(function() {
           //after 1sec, preload the new apng into image object
           var newImg = new Image();
           newImg.src = "/static/img/victory-web-press.apng";

           //#2 timed event
           var replaceWithApngImg = setTimeout(function() {
               //after 2 seconds, add apng image to #pageDiv element

               var bg = "url(\"/static/img/victory-web-press.apng\")";
               // $("#pageDiv").css("background-image", bg);
               $("#pageDiv").css({
                   "background-image":bg
                   // "background-repeat": "repeat-y",
                   // "background-size": "cover",
                   // "height": "100vh"
               });
               newImg = null; //destroy our original image object

               //#3 timed event
               var destroyOldImg = setTimeout(function() {
                   //not sure if it's necessary to remove body image;
                   //$("body").css("background-image", "none");

               }, 300);

           }, 700);

       }, 500); //1000

   })(); //doChangeBG


}

function setRankSection() {
    if ( $("#rankSection").length < 1 ) return false;

    lib.imgRowCellRndMove(); //randomize position of our cells;

    //We want to change the z-index of the parent of the element we hover over
    (function setCellHoverEffect() {
        $(".bookcellDiv").on("mouseenter", ".bookcellInnerDiv", function() {
            $(this).parent(".bookcellDiv").css({
                "z-index": 500
            });
        });
        $(".bookcellDiv").on("mouseleave", ".bookcellInnerDiv", function() {
            $(this).parent(".bookcellDiv").css({
                "z-index": "auto"
            });
        });

    })();

    // ----------------------------------

    // let ajaxencode = (str) => encodeURIComponent(str);
    // let ajaxdecode = (str) => decodeURIComponent(str);
    // let ajaxUrl = "https://ww2.inkonpages.com/ajax/";


    let data = {
        "action" : "get_rank",
    }

    $.ajax({
        type: "POST",
        url: ajaxUrl,
        url: G.ajaxUrl,
        async: true,
        data: JSON.stringify(data),
        cache: true,
        processData: false,
        contentType: "application/json; charset=UTF-8",
        // most settings above are the default;
    })

    .done(function(data, textStatus, jqXHR) {
        // data: This is the data returned from the server
        // textStatus: A string describing the status of the response (e.g., "success").
        // jqXHR: The jQuery XMLHttpRequest (jqXHR) object, which contains
        // information about the request and response.

        console.log("Status Code: " + jqXHR.status + ", textStatus: " + textStatus);

        let status = data["status"];
        if (status != "ok") {
            msg = data["message"]
            console.log("200, but failed request: " + msg);
            return
        }


        $("#bookCellContainer").html() = data["rank_result"];

        ////
          // let location = data["title"];
          // let url = data["url"];
          // let description = data["description"];
          // let imageUrl = data["imageUrl"];

          // $("#location_img").attr("src", imageUrl);
          // $("#location_description_box a").each(function(){
          //     $(this).attr("href", url);
          // })
          // $("#location_description span:first-child").html(description);

          // $("#location_box").fadeIn(500)

    })

    .fail(function(jqXHR, textStatus, errorThrown) {
        console.log("Status Code: " + jqXHR.status + ", textStatus: " + textStatus + ", errorThrown: " + errorThrown);
        // jqXHR: The jqXHR object representing the failed request.
        // textStatus: A string categorizing the type of error that occurred
        // (e.g., "timeout", "error", "abort", or "parsererror").
        // errorThrown: An optional exception object, if one occurred.
    });




}

function setCommons() {

    //universal input behavior; press esc, then erase content
    $("#pageDiv").on("keyup", "input", function(event) {
        // pressed escape key
        if (event.which == 27)  {
            $(this).val("");
            return false;
        }
    });

    //not sure if this is a good universal behavior to remove error styling
    // $("input, textarea").on("focus", function() {
    $("#pageDiv").on("focus", "input, textarea", function() {
        if ($(this).hasClass("error")) {
            $(this).removeClass("error");
        }
    });

}

function initEvents() {
    setCommons();
    setHomeSection();
    setContactSection();
    setRankSection();
    doDelayload();
}

function initVars() {
    G.baseUrl = "https://" + document.location.host;
    G.viewportal_width = $(window).width(); //browser width
    G.ajaxUrl = G.baseUrl + "/ajax/";
}

(function start() {
    initVars();     // initialize global variables
    initEvents();   // initialize events
    //setGreeting();
    // checkUser();

})();


///////////////////////////////////
});
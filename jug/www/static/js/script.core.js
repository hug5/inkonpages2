
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

        let data = {
            "action" : "contact_us",
            "name" : lib.ajaxencode(name),
            "email" : lib.ajaxencode(email),
            "msg" : lib.ajaxencode(msg),
        }
        let settings = {
            type: "POST",
            url: G.ajaxUrl,
            // async: true,
            // cache: true,
            processData: false,
            data: JSON.stringify(data),
            contentType: "application/json; charset=UTF-8",
        }

        $.ajax(settings)
        .done(function(data, textStatus, jqXHR) {

            console.log("Status Code: " + jqXHR.status + ", textStatus: " + textStatus);

            let status = data["status"];
            if (status != "ok") {
                msg = data["message"]
                console.log("200, but failed request: " + msg);
                return
            }

            $("#msgForm").slideUp(400, function() {
                $("#formSection p").fadeIn(300).html("YOUR MESSAGE WAS SENT!");
            });
        })
        .fail(function(jqXHR, textStatus, errorThrown) {
            $("#formSection p").fadeIn(300).html("Oops! There was an error.");
            console.log("Status Code: " + jqXHR.status + ", textStatus: " + textStatus + ", errorThrown: " + errorThrown);
        });

        $(this_btn).removeClass("disabled");


    };





    //init events
    $("#sendBtn").on("click", function() {

        // if ( $(this).hasClass("disabled") )
        if ( !lib.formInputCheck("msgForm") || $(this).hasClass("disabled") )
            return false;

        let name  = $("#nameField").val(),
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

    // lib.imgRowCellRndMove(); //randomize position of our cells;
    // put the ajax call into a self-calling function;
    (function() {

        // let ajaxencode = (str) => encodeURIComponent(str);
        // let ajaxdecode = (str) => decodeURIComponent(str);
        // let ajaxUrl = "https://ww2.inkonpages.com/ajax/";

        let data = {
            "action" : "get_rank",
            "category" : $("#categoryTabDiv").attr("category")
              // fiction, nonfiction, alltime
        }

        let settings = {
            type: "POST",
            // url: ajaxUrl,
            url: G.ajaxUrl,
            // async: true,  //default
            // cache: true,  //default
            data: JSON.stringify(data),
            processData: false,
              // default true; don't urlencode;
              // true: raw data, eg. json
              // false: 'name=John+Doe&age=30&hobby=reading'
            contentType: "application/json; charset=UTF-8"
              // default: 'application/x-www-form-urlencoded; charset=UTF-8')
            // dataType: Intelligent guess
              // expected return type: xml, json, script, text, html.
        }

        $.ajax(settings)
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

            // alert(data["rank_result"]);
            $("#bookCellContainer")
                .html(data["rank_result"])
                .fadeTo(700, 1,
                // move the cells after finish fadeTo;
                function(){
                    lib.imgRowCellRndMove();
                });

            // $("#bookCellContainer").fadeIn(450);

            // create an effect of movement post fadein;
            // let move = setTimeout(function() {
                // lib.imgRowCellRndMove();
            // }, 700);

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
        // .always(function() {
        //     alert( "finished" );
        // });

    })();

    // post( url [, data ] [, success ] [, dataType ] )
    // $.post( "example.php",, data, function() {
    //     alert( "success" );
    // })
    // .done(function() {
    //     alert( "second success" ); #<--- redundant
    // })
    // .fail(function() {
    //     alert( "error" );
    // })
    // .always(function() {
    //     alert( "finished" );
    // });


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
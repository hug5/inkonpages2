/* Common Library functions */

    var G = {
        // is_ssl : null,
        // baseUrl : null,
        // baseUrlS : null,
        // viewportal_width : null

    };

    var lib = {

        hasAttr: function(ths, name) {
            // alert(ths);
            // alert(name);
            //pass in $(this) and attr name (eg, required)
            // if attr exists, then typeof should be "string"; if not exist, then "undefined"
            let result = typeof( $(ths).attr(name) ) != "undefined" ? true : false;
            return result;

        },

        formInputCheck : function(domParent) {
            //pass in the dom parent; this method checks all child input and textarea fields
            //that it has a value;  if not, adds "error" class;
            //only checks elements where display is not NONE and has attr REQUIRED
            //domParent should be an ID; tried passing in #formSection, but passing in #
            //doesn't seem to work

            let allGood = true,
                password = false;

            $("#" + domParent + " input, #" + domParent + " textarea").each(function() {

                if ( $(this).css("display") != "none" && lib.hasAttr($(this), "required") ) {

                    // //note: this method doesn't check for spaces before and after text

                    //check for blank
                    if (!$(this).val().trim()) {
                        $(this).addClass("error");
                        allGood = false;
                    }

                    //do email checks on input type email
                    if ($(this).attr("type") == "email") {
                        let result = lib.checkEmail( $(this).val() );
                        if (!result) {
                            allGood = false;
                            $(this).addClass("error");
                        }
                    }

                    if ($(this).attr("type") == "password" && !password) {
                        //store our first password; then check if
                        //there's another that we must check against
                        password = $(this).val();
                    }
                    //if we already have a prior stored password
                    else if ($(this).attr("type") == "password" && password)  {
                        let password2 = $(this).val(); //this is our 2nd password
                        if (password !== password2) {
                            $(this).addClass("error");
                            allGood = false;
                        }
                    }
                }
            });
            return allGood;
        },

        refreshMain : function(url) {

            (function doAjax() {

                //var url = getBaseUrl() + "/ajax/";
                //var url = G.ajaxUrl;

                var p_action  = "refreshMainFiles";
                var param     = "action=" + p_action;

                $.post(url, param, function(result) {

                    var marr = result.split(";");
                    if (marr[0] != "ok") {
                        //document.body.style.cursor = "wait";
                        return; //there was an error...
                    }

                    //our new main files
                    var $html = lib.ajaxdecode( marr[1] );

                    $("#contentSection").hide();
                    // $("#contentSection").html($html).fadeIn(0);
                    $("#contentSection").html($html).show(0);
                    //$("#contentSection").html($html).slideDown();
                }).fail(function(request, status, err) {
                    //status: "timeout", "error", "abort", and "parsererror"
                    //error: textual portion of the HTTP status
                    alert(request);
                    alert(status);
                    alert(err);
                });

            })();

        },

        checkEmail : function(str) {
          /// check for invalid email; called by signin and register
                /// S = non white character
                /// + = match 1 or more
                var pattern = /\S+@\S+\.\S+/;

                var result = pattern.test(str); /// return true/false

                return result;
        },

        lcFirst : function(str) {
        // converts first letter of string to lowercase

                var newStr = str.charAt(0).toLowerCase() + str.substr(1);
                return newStr;
        },

        ucFirst: function(str) {
          /// converts first letter of string to uppcase

                var newStr = str.charAt(0).toUpperCase() + str.substr(1);
                return newStr;

        },

        tab_to_next_input : function(elemInput, thisName) {
        // elemInput = the element to loop over with .each
        // thisName = name of input element we keyed down

            var name0 = thisName;
            var name1;
            var found = false;
            var arr = new Array();
            var inputFilled = true;

            $(elemInput).each(function() {  //$(".formInputDiv :input").each(function() {
                    if ( $(this).is(":visible") ) {
                            var iValue = $.trim( $(this).val() );
                            if (iValue == "") {
                                    inputFilled = false;
                            }

                            name1 = $(this).attr("name");
                            arr.push(name1);
                    }
            });

            if (inputFilled == true)    return true;

            for (var i = 0; i < arr.length; i++) {
                    name1 = arr[i];
                    if (found) {
                            // the small delay will allow the default behavior
                            // to take place before we tab; the default might be autofill;
                            setTimeout(function() {
                                    $("input[name=" + name1 + "]").focus();
                            }, 50);
                            return false;
                    }

                    found = (name1 == name0) ? true : false;
                    i = (i == arr.length - 1) ? -1 : i;
            };

        },

        ///////////////////////////////////////////
        imgRowCell : function() {

        },

        imgRowCellRndMove : function() {

                // if ( $(".productRowDiv").length < 1 ) return false;
                if ( $(".bookcellDiv").length < 1 ) return false;

                // $(".productListCellDiv").each(function() {
                $(".bookcellDiv").each(function() {

                        var hOffset = 17;
                        var vOffset = 25;
                        var l = Math.floor( Math.random() * hOffset ); //horizontal offset
                        var t = Math.floor( Math.random() * vOffset ); //vertical offset
                        var z = Math.floor(Math.random() * 50); // set random z-index for cells
                        var sign_l = Math.floor(Math.random() * 2 + 1); //1 or 2
                        var sign_t = Math.floor(Math.random() * 2 + 1); //1 or 2

                        //sign_l = sign_l == 1 && count != 0 ? -1 : 1;
                        sign_l = sign_l == 1 ? -1 : 1;
                        sign_t = sign_t == 1 ? -1 : 1;
                        //z = z == 1 ? 10 : "default"; //randomize z-dinex; some on top; some bottom
                        //z = "default"; //randomize z-dinex; some on top; some bottom

                        l = l * sign_l;
                        t = t * sign_t;

                        $(this).css({
                                "position": "relative",
                                "left": l,
                                "top": t,
                                "z-index" : z
                        });
                });
        },

        imgFadeTo : function(i, run_imgRowCellRndMove) {
        //i=0 or 1; 0=fadeTo 0; 1= fadeTo 1
        // fadeTo images effect for all images between header and footer;
        // all images within #contentSection (excludes header, footer generally; but depends
        // on one's html design in schema html) are by default opacity < 1 in css; and only
        // by js do we make all images appear visible, creating that affect; and preventin
        // long load time affect for larger images or firs time visitors;

        // ** Note: since I put the billboards outside contentSEction, it's no longer
        // relevant to banenrs; and maybe I'll just keep it this way for now;

                // if i isn't passed, then assume 1;
                i = i === undefined ? 1 : i;
                // below, creating effect where images will load at
                //different speeds; not all at the same time;
                var n = 0;
                $("#mainDiv img").each(function() {
                //$("#contentSection img").each(function() {
                        //I want to get a random number, but not too big or small;
                        do {
                               n = Math.random() * 10; //.200 * 10
                        }
                        while (n < 2 || n > 8); // 3 and 6

                        Math.floor(n); //make # an integer between 3 and 6; //7;
                        n = n * 100 + 50; // will be number between 350 and 550; //750;
                        $(this).fadeTo(n, i);
                });


                // whether to run this method; if undefined, then run; only if user
                //explicitly states FALSE do we not run this; will not run it when
                // "setProductCatSearchWidth" and lig.imgFadeTo methods are run
                // within same method or process; so don't want to repeat;
                if (run_imgRowCellRndMove !== false) {

                        lib.imgRowCellRndMove();
                }


                // **note: this js operation will actually insert a style="opacity: 1" attribute into all img elements
        },

        doMsgBox : function(title, msg, buttonsArr) {
        // title of the dialog box, msg=message to display, buttons=buttons to display

                var show = function() {
                        var doButtons = function() {
                        // accepted buttons are: okay, cancel
                                var okay_btn = "<div class=\"dBtn\" id=\"msgBox_okay_btn\">Okay</div>";
                                var cancel_btn = "<div class=\"dBtn\" id=\"msgBox_cancel_btn\">Cancel</div>";


                                var html = "";
                                if ( buttonsArr instanceof Array && buttonsArr.length > 0 ) {
                                        for (var i = 0; i < buttonsArr.length; i++) {
                                                if ( buttonsArr[i] == "okay" ) {
                                                        html += okay_btn;
                                                }
                                                else if ( buttonsArr[i] == "cancel" ) {
                                                        html += cancel_btn;
                                                }
                                                //We could also allow custom buttons...
                                        };
                                }

                                // if not array, or user put in no accepted parameters, then use default;
                                if ( html == "" ) {
                                        html = okay_btn;
                                }
                                return html;

                        };

                        var attach_events = function() {

                                $("#msgBox").on("click", "#msgBox_cancel_btn, #msgBox_okay_btn", function() {

                                        if ( $(this).attr("id") == "msgBox_cancel_btn" ) {
                                                ///alert("cancel");
                                        }
                                        else if ( $(this).attr("id") == "msgBox_okay_btn" ) {

                                        }

                                        lib.doMsgBox(); //toggle msgBox and background
                                });

                        };


                        var h = "";
                        h += "<div id=\"msgBox\">";
                                h += "<h4>" + title + "</h4>";
                                h += "<div id=\"msgBox_msg\">" + msg + "</div>";
                                h += "<div id=\"msgBox_btns\">" + doButtons() + "</div>";
                        h += "</div>";

                        $("body").append(h);
                        lib.getViewportCenter("#msgBox", true);
                        attach_events();
                        $("#msgBox").fadeIn();

                };

                var hide = function() {
                        $("#msgBox").remove();
                };

                if ( $("#msgBox").length > 0 ) {
                        hide();
                } else {
                        show();
                }

                lib.dobg(); // show or hide background

        },

        dobg : function() {
        //Call to this background function will toggle it, creating or removing it from the dom

                if ( $("#bgDiv").length > 0 ) {
                        $("#bgDiv").remove();
                } else {
                         var bg = "<div id=\"bgDiv\"></div>";
                         $("body").append(bg);
                }
        },

        getViewportCenter : function(element, setCss) {
        // center passed element on viewable browser port or screen

                var h = $(window).height(); // returns height of browser viewport
                var t = $(document).scrollTop(); // get top position relative to browser
                var center = t + Math.round( h * .5 ); // calculate vertical middle of browser screen
                // if element is passed, then get height of element and calc center of this element relative to screen coordinates;
                var top = ( typeof element === "undefined" ) ? center : center - ( $(element).height() / 2 );
                top = top < 0 ? 0 : top; // if screen height is shorter than image height, then make top of image 0; don't let go into negative

                // whether to set css; if this is not set or false, then false; otherwise, true
                setCss = ( typeof setCss === "undefined" || setCss === false ) ? false : true;

                // vertically and horizontally center element;
                // better to put here? or all in CSS file????
                if ( setCss && typeof element !== "undefined" ) {
                        $(element).css({
                            "top":top,
                            "position":"absolute",
                            "left":0,
                            "right":0,
                            "margin-left":"auto",
                            "margin-right":"auto",
                            "z-index": 100
                        });
                        return false;
                } else {
                        return top;
                }

        },

        //doSpinner : function(element, t_offset, l_offset, w) {
        doSpinner : function(obj) {
        // with the spinner, we can either pass in no parameter, and this function will center the spinner with default size;
        // or we can pass in a size; or we can also pass in an element with offsets top and left offset values
                // if spinner exists, then remove it and exit;
                if ( $("#spinnerContainer").length > 0 ) {
                        $("#spinnerContainer").remove();
                        $("#bgtDiv").remove(); //remove transparent background
                        lib.doCursor("default");
                        return false;
                }


                lib.doCursor("wait");
                // create transparent background; do this to prevent user from clicking on anything
                var bg = "<div id=\"bgtDiv\"></div>";
                $("body").append(bg);

                var element  = false; // if not set, then center on screen
                var size     = ""; // if not set, then us css default
                var t_offset = 0; // if element set, then see if top offset is given; other, zero
                var l_offset = 0; // left offset, or zero; if element not set, then not applicable;

                var spinner = "<div id=\"spinnerContainer\"></div>";
                $("body").append(spinner);

                // check if parameter passed in; then use those values;
                // otehrwise, do default;
                if (typeof obj !== "undefined") {

                        // if passed in, callers should have passed in an object parameter like this:
                        // var obj = {
                        //         "pos": "center",
                        //         "element": (name of element),
                        //         "size" : "400px", //width/height
                        //         t_offset: "50",
                        //         l_offset: "50",
                        // };

                        element  = ( obj.element  === "undefined" ) ? element  : obj.element;  // relative to an element
                        t_offset = ( obj.t_offset === "undefined" ) ? t_offset : obj.t_offset; // vertical offset
                        l_offset = ( obj.l_offset === "undefined" ) ? l_offset : obj.l_offset; // horizontal offset
                        size     = ( obj.size     === "undefined" ) ? size     : obj.size;     // size: width, height
                }

                if (element) {
                        var pos = $(element).position();
                        var top = pos.top - t_offset;
                        var left = pos.left - l_offset;
                        $("#spinnerContainer").css({"left":left, "top":top, "width":size, "height":size}).toggle();
                }

                // center spinner
                else if (!element) {
                        // false: tell function not to set css
                        var top = lib.getViewportCenter("#spinnerContainer", false);
                        $("#spinnerContainer").css({"top":top, "width":size, "height":size}).toggle();
                }


        },


        currToNum: function(curr) {
                // make sure passed is being treated as string so we can do the replace procedure
                curr = curr.toString();
                curr = curr.replace("$", "");
                return curr;
        },

        numToCurr: function(num) {

                // make sure the num is being treated as a string; or else get error
                num = num.toString();

                num = num.replace("$", "");  //remove dollar

                var isNeg = num.indexOf("-") === 0 ? true : false; // check if neg sign exists
                num = num.replace("-", ""); //remove - sign
                var arr = num.split("."); //split integer portion and float portion
                var int = arr[0] == undefined || arr[0] == "" ? "0" : arr[0];
                var fl = arr[1] == undefined || arr[1] == ""  ? "00" : arr[1];

                var curr = int + "." + fl;

                // round float point to 2 digits

                curr = Number(curr).toFixed(2);


                curr = curr == "NaN" ? "0.00" : curr; // if result was "NaN", then make zero

                curr = "$" + curr;
                curr = isNeg ? "-" + curr : curr;
                return curr;


        },


        getGuid: function() {
        // returns our unique guid; should match our guid found in FunctionLib.php
        // Not using this for anything at the moment; used it before for ajax;

                //todo:: don't need this!
                var guid = "2E7CF555-AC8B-4780-B3FA-921E5A84B960";
                return guid;
        },


        doCursor: function(kind) {
        // kind = wait or default
                //document.body.style.cursor = kind;
                //if ( document.body.style.cursor === "default" ) {

                var c1 = document.body.style.cursor;
                var c2 = ( c1 == "" || c1 == "default" ) ? "wait" : "default";

                if (kind == "wait") {
                        document.body.style.cursor = "wait";
                } else {
                        document.body.style.cursor = "default";
                }

                return false;
        },


        hent: function(str) {
        // mimicking a little of php's htmlentities function;
        // Since I'm only doing the limited set below, it's equivalent
        // to PHP's htmlspecialchars

        // Note:
        // While text() will output the literal character as the screen renders it and html() will
        // output whatever the original html characters are; effectively, appear
        // the same when shown in an input field;
        // and for some reason, js seems to take the entity version
        // of " and ' and convert back to " and ', respectively; very strange!
        // So again, the hitch is that text() will not give me the literal text for " and ';
        // &quot; becomes --> ", rather than the original! this is a bug here!

                if ( str.indexOf("&amp;") == -1 && str.indexOf("&quot;") == -1 &&
                     str.indexOf("&#039") == -1 && str.indexOf("&lt;") == -1 &&
                     str.indexOf("&gt;") == -1 && str.indexOf("&") >= 0 ) {

                        str = str.replace(/&/g, "&amp;");
                }

                if ( str.indexOf("&lt;") == -1 && str.indexOf("<") >= 0 ) {
                         str = str.replace(/</g, "&lt;");
                }
                if ( str.indexOf("&gt;") == -1 && str.indexOf(">") >= 0 ) {
                        str = str.replace(/>/g, "&gt;");
                }
                //if ( str.indexOf("&quot;") == -1 && str.indexOf('"') >= 0 ) {
                if ( str.indexOf('"') >= 0 ) {
                //    alert("yes");
                //if ( str.indexOf("&quot;") == -1 ) {
                        str = str.replace(/"/g, "&quot;");
                //        alert(str);
                }
                if ( str.indexOf("&#039") == -1 && str.indexOf("'") >= 0 ) {
                        str = str.replace(/'/g, "&#039");
                }

                return str; //.replace(/"/g, "&quot;");


                // for " and ', we always do!
             /*   return str
                           //.replace(/&/g, "&amp;")
                           .replace(/"/g, "&quot;")
                           .replace(/'/g, "&#039")
                           .replace(/</g, "&lt;")
                           .replace(/>/g, "&gt;")
                           ;
            */


        },


        // #### Ajax Functions ####
        // encodeajax: function(str, exclude) {
        ajaxencode: function(str, exclude) {


                //return encodeURIComponent(str);
                var ns = encodeURIComponent(str);
                //substring
                //indexOf
// alert(ns);

                //if no value given for exclude, then will be "undefined";
                //if (exclude == "/") {

                // ***** 12/18 note: Should I really be removing this???? It screws up the url!
                //note: if user put / in string, then remove it; this, when
                //encoded, will throw an error with apache; see apache notes
                //for more info on this; there is a workaround but my version
                //of apache is not new enough;
                //  if ( ns.indexOf("%2F") > -1 ) {
                //         ns = ns.replace("%2F", "");
                //  }
                //*******************
// alert(ns);
                //}
                return ns;
        },
        // decodeajax: function(str) {
        ajaxdecode: function(str) {
                return decodeURIComponent(str);
        },


        // #### Cookie functions ####
        // * Modified from Nicholas Zakas *
        // js reads the entire cookie, which is a semicolon separated string; then we have to parse that string;
        // ex: alias=Aquaman2; idNo=%7B8%D; PHPSESSID=gmq11v1unankkbv0
        cookieget: function (name){
            var cookieName = encodeURIComponent(name) + "=",
                cookieStart = document.cookie.indexOf(cookieName),
                cookieValue = null,
                cookieEnd;

            if (cookieStart > -1) {
                    cookieEnd = document.cookie.indexOf(";", cookieStart);
                    if (cookieEnd == -1) {
                            cookieEnd = document.cookie.length;
                    }

                    // attempt to decode some character, like %, will result in error for whatever reason
                    try {
                            cookieValue = decodeURIComponent( document.cookie.substring(cookieStart + cookieName.length, cookieEnd) );
                    }
                    catch(e) {
                            cookieValue = "decodeError";
                    }
                    finally {
                            //var x = (x == undefined) ? "error" : x;
                    }

            }
            return cookieValue;
        },
        //set: function (name, value, expires, path, domain, secure) {
        cookieset: function (name, value, m) {
            // m = minutes till expiration

            //if (expires instanceof Date) { cookieText += "; expires=" + expires.toUTCString(); }
            //if (path) { cookieText += "; path=" + path; }
            //if (domain) { cookieText += "; domain=" + domain; }
            //// tells browser to only transmit if over ssl connection
            //if (secure) { cookieText += "; secure"; }
            //var now2 = now.getTime();       // convert date object to milliseconds
            //document.cookie = "searchSortBy=date;max-age=" + (60*60*24*365); // in seconds
            //if (expires instanceof Date == false) {
            //-----------------------------------------------------------------------------


            var cookieText = encodeURIComponent(name) + "=" + encodeURIComponent(value);
            cookieText += "; path=/"; // set path to root

            // assuming m is set, then set day and hrs to 1
            var d = 1;
            var h = 1;

            // if m is not set, then set default values: 180days
            if ( typeof m != "number" ) {
                    d = 180;
                    h = 24;
                    m = 60;
            }

            var offset = 1000 * 60 * m * h * d;         // time in milliseconds, in days
            var dateMs = Date.now() + offset;           // today's date in milliseconds + offset
            expires = new Date(dateMs);                 // translate our millisecond as a date object, standard date format

            expires = expires.toUTCString()             // convert local time to UTC time
            cookieText += "; expires=" + expires;       // add our exp. date to cookie;
            document.cookie = cookieText;               // save our unencrypted string to cookie
            return true;
        },
        //unset: function (name, path, domain, secure){
        cookieunset: function (name){
            //this.set(name, "", new Date(0), path, domain, secure);
            this.set(name, "", new Date(0));
            return true;
        }



    };


    // Can use this syntax:
    // export var G = {...
    // or this below:
    export { G, lib };
    // export { G };

    // Variables and functions must be exported if it wants to be imported

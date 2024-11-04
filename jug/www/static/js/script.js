// submit_btn.addEventListener("click", myScript);
// object.onclick = function(){myScript};

// const submit_btn = document.getElementById("submit_btn");
// submit_btn.addEventListener("click", function() {
//     document.getElementById("demo").innerHTML = "Hello World";
//     let val = document.getElementById("destination_input").value;
//     alert(val);

// });

$(function() {
// ----------------------------------------------------------


let ajaxencode = (str) => encodeURIComponent(str);
let ajaxdecode = (str) => decodeURIComponent(str);
let ajaxUrl = "https://ww2.inkonpages.com/ajax/";

function set_rank() {
    if ( $("#rankSection").length < 1 ) return false;

    alert("here");


    let data = {
        "action" : "get_rank",
    }

    $.ajax({
        type: "POST",
        url: ajaxUrl,
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

function set_news_result_box() {
    if ( $("#news_result_box").length < 1 ) return false;

    let data = {
        "action" : "get_news_result"
    }
    $.ajax({
        type: "POST",
        url: ajaxUrl,
        async: true,
        data: JSON.stringify(data),
        cache: true,
        processData: false,
        contentType: "application/json; charset=UTF-8",
        // most settings above are the default;
    })
    // .done(function(data, textStatus, errorThrown, xhr) {
    .done(function(data, textStatus, jqXHR) {
        // data: This is the data returned from the server
        // textStatus: A string describing the status of the response (e.g., "success").
        // jqXHR: The jQuery XMLHttpRequest (jqXHR) object, which contains
        // information about the request and response.

        console.log("Status Code: " + jqXHR.status + ", textStatus: " + textStatus);

        let status = data["status"];
        if (status != "ok") {
            msg = data["error_message"]
            console.log("200, but failed request: " + msg);
            return
        }

        // let news_result_arr = ajaxdecode( data["news_result"] );  // this results in plain string
        let news_result_arr = data["news_result"];                   // This results in array

        if (news_result_arr.length == 0) {
            return
        }

        let news_headlines = "";

        for (let i = 0; i < news_result_arr.length; i++) {
            // url = news_result_arr[1][i];
            // headline = news_result_arr[0][i];
            headline = news_result_arr[i][0];
            url = news_result_arr[i][1];

            news_headlines += (i == 0) ? "<span class='news_first'>" : "<span class='news_hide'>";
            news_headlines += "<a href=\"" + url + "\" tabindex=-1 target=\"_blank\">" + headline + "</a></span>";
        }

        // alert(news_headlines);

        // append headlines after news_headline_title, but before the button;
        $("#news_headline_title").after(news_headlines)
        $("#news_result_box").slideDown(400, "linear")

    })

    .fail(function(jqXHR, textStatus, errorThrown) {
        console.log("Status Code: " + jqXHR.status + ", textStatus: " + textStatus + ", errorThrown: " + errorThrown);
        // jqXHR: The jqXHR object representing the failed request.
        // textStatus: A string categorizing the type of error that occurred
        // (e.g., "timeout", "error", "abort", or "parsererror").
        // errorThrown: An optional exception object, if one occurred.
    });

}



(function start() {
    set_rank();

})();



// ----------------------------------------------------------
});



// { a: "bc", d: "e,f" } is converted to the string "a=bc&d=e%2Cf"

// data
// Type: PlainObject or String or Array
// Data to be sent to the server. If the HTTP method is one that cannot have an entity body, such as GET, the data is appended to the URL.
// When data is an object, jQuery generates the data string from the object's key/value pairs unless the processData option is set to false. For example, { a: "bc", d: "e,f" } is converted to the string "a=bc&d=e%2Cf". If the value is an array, jQuery serializes multiple values with same key based on the value of the traditional setting (described below). For example, { a: [1,2] } becomes the string "a%5B%5D=1&a%5B%5D=2" with the default traditional: false setting.
// When data is passed as a string it should already be encoded using the correct encoding for contentType, which by default is application/x-www-form-urlencoded.
// In requests with dataType: "json" or dataType: "jsonp", if the string contains a double question mark (??) anywhere in the URL or a single question mark (?) in the query string, it is replaced with a value generated by jQuery that is unique for each copy of the library on the page (e.g. jQuery21406515378922229067_1479880736745).


// $("#location_box img").fadeOut(0);
// $("#location_box img").fadeIn(400);


// var p_action  = "contactUsMsg",
//     p_name    = lib.ajaxencode(name),
//     p_email   = lib.ajaxencode(email),
//     p_msg     = lib.ajaxencode(msg),

//     param     = "action=" + p_action +
//                 "&name=" + p_name +
//                 "&email=" + p_email +
//                 "&msg=" + p_msg;
// $.post(G.ajaxUrl, param, function(result) {

//     $(this_btn).removeClass("disabled");

//     if (result == "ok") {

//         $("#msgForm").slideUp(400, function() {
//             $("#formSection p").fadeIn(300).html("YOUR MESSAGE WAS SENT!");
//         });
//     }

//     else {
//         $("#formSection p").fadeIn(300).html("Oops! There was an error.");
//     }
// });


// $("#submit").click(function (e) {
//     $.post("result.php",
//     {
//         firstName: $("#firstName").val(),
//         lastName: $("#lastName").val()
//     })
//     .done(function (result, status, xhr) {
//         $("#message").html(result)
//     })
//     .fail(function (xhr, status, error) {
//         $("#message").html("Result: " + status + " " + error + " " + xhr.status + " " + xhr.statusText)
//     });
// });

// var jqxhr = $.ajax( "example.php" )
//   .done(function() {
//     alert( "success" );
//   })
//   .fail(function() {
//     alert( "error" );
//   })
//   .always(function() {
//     alert( "complete" );
//   });


//    $.ajax({
//      url: 'https://jsonplaceholder.typicode.com/todos/1', // Sample API endpoint
//      method: 'GET',
//      dataType: 'json',
//      success: function(data) {
//      // Update the content on success
//      $("#dataContainer").text('Title: ' + data.title);
//      },
//      error: function(error) {
//      // Handle errors
//      console.error('Error:', error);
//      }
//  });

// $.ajax({
//     url: "geeks.txt",
//     success: function (result) {
//         $("#h11").html(result);
//     },
//     error: function (xhr, status, error) {
//         console.log(error);
//     }
// });



// $.ajax({
//   type: "POST",
//   url: url,
//   data: data,
//   success: success,
//   dataType: dataType
// });


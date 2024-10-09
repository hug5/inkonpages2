// submit_btn.addEventListener("click", myScript);
// object.onclick = function(){myScript};



// const submit_btn = document.getElementById("submit_btn");
// submit_btn.addEventListener("click", function() {
//     document.getElementById("demo").innerHTML = "Hello World";
//     let val = document.getElementById("destination_input").value;
//     alert(val);

// });


$(function() {

    // Focus by default;
    // $("#destination_input").focus();

    gotoCity = function() {
        let dest_val = $("#destination_input").val().toLowerCase();
        //
          // let dest_val = $("#destination_input").val();
          // let dest_val = "Big City";


          // Don't need to do this check anympore; just checking through python so can catch manual entry as well;
          // if (dest_val == "home" || dest_val == "paperdrift") {
          //     dest_val = "/";
          // }
          // else {
          //   dest_val = "/" + dest_val;
          // }
            // window.location.href = dest_val;

        // remove non-alphanumeric characters, but allow for space
        // all bad characters will be replaced with space;
        // then later we'll remove redundant spaces;
        dest_val = dest_val.replace(/[^0-9a-z\- ]/gi, ' ')

        // remove redundant spaces
        dest_val = dest_val.replace(/\s\s+/g, ' ')
        // s = s.replace(/ +/g, " ") // this should also work;

        window.location.href = "/" + dest_val + "/";

    }

    $("#submit_btn").on("click", gotoCity);
    $("#destination_input").on("keypress", function(event) {

        // press enter;
        if (event.which == 13)  {
            // $(this).val();
            gotoCity();
        }
    });

    $("#more_btn").on("click", function(event) {

        let btn_type = $(this).html();


        $(".news_hide").slideToggle(150);
        // $(".news_hide").fadeToggle(150);
        // $(".news_hide").show();
        // $(".news_hide").hide();

        if (btn_type == "+MORE"){
            $(this).html("-LESS");
        }
        else {
            $(this).html("+MORE")
        }

    });

    // $("#location_box img").fadeOut(0);
    // $("#location_box img").fadeIn(400);

});


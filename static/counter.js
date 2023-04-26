var counter1 = 0;
var counter2 = 0;

$("#btn1").click(function() {
   counter1++;
});
$("#btn2").click(function() {
   counter2++;
});
$("#add").click(function() {
    url = $(this).attr("to_java");
    $.ajax(
        {
            type:"GET",
            url:url,
            data:{
                counter1:counter1,
                counter2:counter2
            }
        }
    )
});


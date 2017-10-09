$(document).ready(function() {
    console.log("hello?????");

    $('#test').click(function() {
        console.log("okay good");
        $.ajax({
            url: "/findSummoner?name=" + $('#summonerName').val(),
            type: "get",
            success: function(response) {
                console.log("name is: " + response);
            },
            error: function(xhr) {
            //Do Something to handle error
            }
        });
    });
});
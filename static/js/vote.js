$(document).ready(function () {

    var ask_vote_url = $('.ask-vote-url').val();
    var csrf = $('input[name=csrfmiddlewaretoken]').val();

    function vote_ask(id, delta, type) {
        var data = {
            ask_id: id,
            delta: delta,
            csrfmiddlewaretoken: csrf
        };
        var url;
        if(type == 'ask'){
            url = ask_vote_url;
        }
        $.ajax({
            url: url,
            method: 'POST',
            data: data,
            success: function (response) {
                data = JSON.parse(response);
                if(data.error == false) {
                    lazy_success(data.message);
                }else{
                    lazy_danger(data.message);
                }
            }
        });
    }



    $(".vote-up").on("click", function (e) {
        e.preventDefault();
        vote_ask($(this).data('ask'), 1, 'ask');
    });

    $(".vote-down").on("click", function (e) {
        e.preventDefault();
        vote_ask($(this).data('ask'), -1, 'ask');
    });
});


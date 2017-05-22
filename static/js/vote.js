$(document).ready(function () {

    var ask_vote_url = $('.ask-vote-url').val();
    var answer_vote_url = $('.answer-vote-url').val();
    var csrf = $('input[name=csrfmiddlewaretoken]').val();

    function vote(id, delta, type, $item) {
        var data = {
            id: id,
            delta: delta,
            csrfmiddlewaretoken: csrf
        };
        var url;
        if (type == 'ask') {
            url = ask_vote_url;
        }else{
            url = answer_vote_url;
        }
        $.ajax({
            url: url,
            method: 'POST',
            data: data,
            success: function (response) {
                data = JSON.parse(response);
                if (data.error == false) {
                    lazy_success(data.message);
                    var $vote_container = $item.parent();
                    if (delta > 0) {
                        $vote_container.find('.value').html(data.rating).addClass('voted-up');
                    } else {
                        $vote_container.find('.value').html(data.rating).addClass('voted-down');
                    }
                    $vote_container.find('a').hide();
                } else {
                    lazy_danger(data.message);
                }
            }
        });
    }


    $(".vote-up").on("click", function (e) {
        e.preventDefault();
        vote($(this).data('ask'), 1, 'ask', $(this));
    });

    $(".vote-down").on("click", function (e) {
        e.preventDefault();
        vote($(this).data('ask'), -1, 'ask', $(this));
    });

    $(".answer-vote-up").on("click" ,function (e) {
        e.preventDefault();
        vote($(this).data('answer'), 1, 'answer', $(this));
    })

    $(".answer-vote-down").on("click" ,function (e) {
        e.preventDefault();
        vote($(this).data('answer'), -1, 'answer', $(this));
    })


});


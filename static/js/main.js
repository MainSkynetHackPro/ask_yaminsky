function lazy_warning(text) {
    new Noty({
        type: 'warning',
        text: text,
        timeout: 1500
    }).show();
}

function lazy_danger(text) {
    new Noty({
        type: 'error',
        text: text,
        timeout: 1500
    }).show();
}

function lazy_success(text) {
    new Noty({
        type: 'success',
        text: text,
        timeout: 1500
    }).show();
}

$(document).ready(function () {

    $(function () {
        $("#search-box").autocomplete({
            source: '/autocomplete/asks',
            minLength: 2,
            select: function (e, ui) {
                $('#search-box').val(ui.item.label);
                $('#search-box').closest('form').submit();
            }
        });
    });

});
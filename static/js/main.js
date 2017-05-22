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


});
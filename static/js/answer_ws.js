$(document).ready(function () {

    var ws_path = "ws://localhost:8000/answers/" + currentid + "/";
    console.log(ws_path);
    var webSocketBridge = new channels.WebSocketBridge();
    webSocketBridge.connect(ws_path);
    webSocketBridge.listen(function (data) {
        lazy_success('New answer');
        $('#answers_block').append(data["html"]);
        console.log(data["html"]);
    });
});
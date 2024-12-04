var timeout = 15000;

window.setTimeout(poller, timeout);

function poller() {
    window.location = "https://wad18.pythonanywhere.com/kitchen/";

    window.setTimeout(poller, timeout);
}

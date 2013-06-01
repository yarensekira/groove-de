(function () {
    "use strict";

    function setBody(html) {
        document.close();
        document.open();
        document.write(html);
        document.close();
    }

    function removeTimers() {
        var handle = setTimeout(null, 1e9);
        while (handle) {
            clearTimeout(handle--);
        }
        handle = setInterval(null, 1e9);
        while (handle) {
            clearInterval(handle--);
        }
    }

    function getContentFromProxy(url, success, failure) {
        var xhr = new XMLHttpRequest(),
            callback;
        xhr.open('GET', url, true);
        xhr.onload = function () {
            success(xhr.responseText);
        };
        xhr.onerror = function () {
            failure(xhr.responseText || "");
        };
        xhr.setRequestHeader('X-Cookie', document.cookie);
        xhr.setRequestHeader('X-Requested-With', 'XMLHttpRequest');
        xhr.send();
    }

    // run once and only if website is blocked by GEMA
    if (!window._groovesharkRun &&
            document.querySelector('a[href="mailto:gema@gema.de"]')) {
        window._groovesharkRun = true;
        setBody('loading...');
        removeTimers();
        // local testing support
        getContentFromProxy(/[?&]test(=|$)/.test(location.search) ?
            'http://localhost:8080/' : 'https://PUT-YOUR-APPID-HERE.appspot.com/',
            function (responseText) {
                setBody(responseText);
            }, function (responseText) {
                setBody('<h1>Grooveshark Germany unlocker failed!</h1>' + responseText);
        });
    }
})();

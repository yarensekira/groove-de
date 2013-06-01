"use strict";
var permissions = chrome.runtime.getManifest().permissions,
    proxyDomain,
    proxyURL,
    match,
    i;

for (i = 0; i < permissions.length; i++) {
    match = /^https:\/\/([^.]+\.appspot.com)\/$/.exec(permissions[i]);
    if (match) {
        proxyURL = match[0];
        proxyDomain = match[1];
        break;
    }
}

chrome.cookies.onChanged.addListener(function (changeInfo) {
    var cookie = changeInfo.cookie,
        removed = changeInfo.removed;
    if (/grooveshark\.com$/.test(cookie.domain)) {
        if (removed) {
            chrome.cookies.remove({
                url: proxyURL,
                name: cookie.name
            });
        } else {
            chrome.cookies.set({
                url: proxyURL,
                name: cookie.name,
                value: cookie.value,
                domain: proxyDomain,
                path: '/',
                secure: true,
                httpOnly: true,
                expirationDate: cookie.expirationDate
            });
        }
    }

});

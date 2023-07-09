function getCookie(key) {
    let cookies = document.cookie.split(';');
    for (let i = 0; i < cookies.length; i++) {
        let cookie = cookies[i];
        let a = cookie.split('=');
        if (a[0].trim() == key) {
            return a[1];
        }
    }
    return null;
}

function sendEvent(id, event) {
    fetch("/api/v1/tcar/" + id, {
        method: "PUT",
        headers: {
            'X-CSRFToken' : getCookie('csrftoken'),
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({next_state: event})
    })
    .then(function(response) {
    })
    .catch(function(error) {
        alert("失敗");
    });
}
function checkStatus(requestId) {
    fetch(`/check_status/${requestId}/`)
        .then(response => response.json())
        .then(data => {
            if (data.status === 'done') {
                window.location.href = `/result/${requestId}/`;
            } else {
                setTimeout(() => checkStatus(requestId), 2000);
            }
        });
}
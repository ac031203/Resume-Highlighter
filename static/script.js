document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('uploadForm').addEventListener('submit', function(event) {
        event.preventDefault();
        
        var form = this;
        var formData = new FormData(form);

        var xhr = new XMLHttpRequest();
        xhr.open('POST', '/convert');
        xhr.onload = function() {
            if (xhr.status === 200) {
                document.getElementById('output').innerHTML = xhr.responseText;
            } else {
                document.getElementById('output').innerHTML = 'Error occurred. Please try again.';
            }
        };
        xhr.send(formData);
    });
});

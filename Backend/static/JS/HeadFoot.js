let pathDepth = window.location.pathname.split('/').length - 2;
let basePath = '../'.repeat(pathDepth);

document.addEventListener("DOMContentLoaded", function() {
//Headbar
    fetch(`${basePath}9_HeadFoot/headbar.html`)
            .then(response => response.text())
            .then(data => {
                document.getElementById("header-placeholder").innerHTML = data;
            });

// Footer
    fetch(`${basePath}9_HeadFoot/footer.html`)
        .then(response => response.text())
        .then(data => {
            document.getElementById("footer-placeholder").innerHTML = data;
        });
});

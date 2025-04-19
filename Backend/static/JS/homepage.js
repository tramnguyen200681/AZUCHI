document.addEventListener("DOMContentLoaded", function () {
    let slides = document.querySelectorAll(".slide");
    let index = 0; // first slide

    // First image appears immediately
    slides[index].style.opacity = 1; // style: take all styles from css

    function showSlide() {
        let previousIndex = index;
        index = (index + 1) % slides.length; 

        slides[previousIndex].style.opacity = 0;

        // Appear after 5s -> delay apperance
        setTimeout(() => {
            slides[index].style.opacity = 1;
        }, 500);
    }

    // Make sure the 1st img appears in only 5s
    setTimeout(() => {
        setInterval(showSlide, 5000); //Change evry after 5s.
        showSlide(); //Move to 2nd img
    }, 5000);
});

document.addEventListener("DOMContentLoaded", function () {
    const togglePassword = document.querySelector("#togglePassword");
    const passwordInput = document.querySelector("#password");

    togglePassword.addEventListener("click", function () {
        // Toggle between type="password" and type="text"
        // const type = passwordInput.getAttribute("type") === "password" ? "text" : "password";
        // passwordInput.setAttribute("type", type);

        let newType;
        if(pastwordInput.getAttribute("type") === "password"){ // hiding
            newType = "text"; // show
        } else{ //showing
            newType = "password"; //hide
        }
        passwordInput.setAttribute("type", newType);

        // Toggle icon between fa-eye and fa-eye-slash
        this.classList.toggle("fa-eye");
        this.classList.toggle("fa-eye-slash"); 
        // -> Like if-else statement
    });
});


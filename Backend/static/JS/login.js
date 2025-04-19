document.addEventListener("DOMContentLoaded", () => {
    let BACKEND_URL;
    if(location.hostname ==="localhost" || location.hostname === "127.0.0.1"){
        BACKEND_URL = `http://${location.hostname}:5000`;
    } else{
        BACKEND_URL = "https://your-api-domain.com"; //Change after but domain
    }

    const registerForm = document.querySelector(".register-form");
    const loginForm = document.querySelector(".login-place form");

    //REGISTER:
    registerForm.addEventListener("submit", async (e) => {
        e.preventDefault();

        const username = document.getElementById("username").ariaValueMax;
        const password = document.getElementById("password").value;
        const confirmPassword = document.getElementById("confirm-password").value;

        if (username === "" || password === "") {
            alert("Vui lòng nhập đầy đủ thông tin.");
            return;
        }

        if (password !== confirmPassword) {
            alert("Mật khẩu không khớp.");
            return;
        }

        try {
            const res = await fetch(`${BACKEND_URL}/register`, {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({ username, password }),
            });

            const data = await res.json();

            if (data.success) {
                alert("Đăng ký thành công! Hãy đăng nhập.");
                registerForm.reset();
            } else {
                alert(data.message);
            }
        } catch (err) {
            console.error("Lỗi khi gọi API đăng ký:", err);
            alert("Đã xảy ra lỗi khi đăng ký.");
        }
    });

    loginForm.addEventListener("submit", async (e) => {
        e.preventDefault();

        const username = document.getElementById("login-username").value;
        const password = document.getElementById("login-password").value;

        if (username === "" || password === "") {
            alert("Vui lòng nhập tài khoản và mật khẩu.");
            return;
        }

        try {
            const res = await fetch(`${BACKEND_URL}/login`, {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({ username, password }),
            });

            const data = await res.json();

            if (data.success) {
                alert("Đăng nhập thành công!");
                
            } else {
                alert(data.message);
            }
        } catch (err) {
            console.error("Lỗi khi gọi API đăng nhập:", err);
            alert("Đã xảy ra lỗi khi đăng nhập.");
        }
    });
});
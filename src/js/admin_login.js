// admin_login.js
(function () {
    fetch('/api/login')
        .then((response) => {
            return response.json();
        })
        .then((myjson) => {
            // Проверяем, есть ли метка аутентификации в sessionStorage
            var isAuthenticated = sessionStorage.getItem("authenticated");

            // Если пользователь уже авторизован, перенаправляем на страницу /admin
            if (isAuthenticated) {
                console.log("Пользователь уже авторизован");
                window.location.href = "/admin";
                return;
            }

            document.getElementById("login").addEventListener("submit", function (event) {
                event.preventDefault();
                let login = document.querySelector('.login-form').value;
                let password = document.querySelector('.password-form').value;

                if (myjson.login == login && myjson.password == password) {
                    // Устанавливаем метку аутентификации в sessionStorage
                    sessionStorage.setItem("authenticated", "true");
                    window.location.href = "/admin";
                    console.log("Ура!");
                } else {
                    console.log("Неверный логин или пароль!");
                }
            });
            console.log(myjson);
        });
})();

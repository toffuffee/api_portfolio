// admin.js
(function () {
    function redirectToLogin() {
        window.location.href = '/admin/login';
    }

    function hideLogoutButton() {
        var exitButton = document.querySelector('.exit');
        exitButton.style.display = 'none';
    }

    function initialize() {
        // Проверяем, есть ли метка аутентификации в sessionStorage
        var isAuthenticated = sessionStorage.getItem("authenticated");

        if (!isAuthenticated) {
            // Если пользователя нет в sessionStorage, перенаправляем на страницу /admin/login
            redirectToLogin();
            return;
        }

        // Если мы здесь, значит пользователь успешно аутентифицирован
        console.log("Пользователь вошел");

        // Обработка кнопки "Выйти"
        var exitButton = document.querySelector('.exit');
        exitButton.addEventListener('click', function () {
            // Удаляем метку аутентификации из sessionStorage
            sessionStorage.removeItem("authenticated");
            console.log("Пользователь вышел");
            // Перенаправляем на страницу /admin/login после выхода
            redirectToLogin();
        });
    }

    // Вызываем функцию при загрузке страницы
    document.addEventListener('DOMContentLoaded', initialize);

})();

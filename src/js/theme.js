(function () {
    document.getElementById("themeToggleBtn").addEventListener("click", toggleTheme);

    // Получаем текущую тему из куки
    const currentTheme = getCookie("theme");
    if (currentTheme === "dark") {
        document.body.classList.add("dark-theme");
    }

    // Обновляем иконку в зависимости от текущей темы
    updateThemeIcon();

    function toggleTheme() {
        // Добавляем/удаляем класс темы
        document.body.classList.toggle("dark-theme");

        // Сохраняем текущую тему в куки
        const isDarkTheme = document.body.classList.contains("dark-theme");
        setCookie("theme", isDarkTheme ? "dark" : "light", 365);

        // Обновляем иконку в зависимости от текущей темы
        updateThemeIcon();
    }

    function updateThemeIcon() {
        // Заменяем иконку в зависимости от текущей темы
        const icon = document.getElementById("themeToggleBtn").querySelector("i");
        icon.classList.toggle("fa-sun", !document.body.classList.contains("dark-theme"));
        icon.classList.toggle("fa-moon", document.body.classList.contains("dark-theme"));
    }

    // Функция для установки значения в куки
    function setCookie(name, value, days) {
        const date = new Date();
        date.setTime(date.getTime() + (days * 24 * 60 * 60 * 1000));
        const expires = "expires=" + date.toUTCString();
        document.cookie = name + "=" + value + ";" + expires + ";path=/";
    }

    // Функция для получения значения из куки
    function getCookie(name) {
        const cname = name + "=";
        const decodedCookie = decodeURIComponent(document.cookie);
        const ca = decodedCookie.split(';');
        for (let i = 0; i < ca.length; i++) {
            let c = ca[i];
            while (c.charAt(0) === ' ') {
                c = c.substring(1);
            }
            if (c.indexOf(cname) === 0) {
                return c.substring(cname.length, c.length);
            }
        }
        return "";
    }
})();

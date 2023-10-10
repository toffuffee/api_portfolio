(function () {
    document.querySelector(".header-logo").addEventListener("click", function (e) {
        e.preventDefault();
        document.querySelector(".menu").classList.toggle("open");
    });

    document.querySelector(".logo-menu").addEventListener("click", function (e) {
        e.preventDefault();
        document.querySelector(".menu").classList.toggle("open");
    });
})();
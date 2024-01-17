(function () {
    fetch('/api/images')
        .then((response) => {
            return response.json();
        })
        .then((myjson) => {
            let container = document.getElementById("images");
            for (let key in myjson) {
                let div = document.createElement("div");
                let img = document.createElement("img");
                let cardTitle = document.createElement("div");
                let cardDesc = document.createElement("div");

                img.classList.add("image");
                div.classList.add("card");
                div.setAttribute("id", myjson[key].id);
                cardTitle.classList.add("card-title");

                cardTitle.innerHTML = myjson[key].image_name;
                img.src = myjson[key].image;

                container.appendChild(div);
                div.appendChild(img);
                div.appendChild(cardTitle);

                // Добавим обработчик событий для наведения на карточку
                div.addEventListener("mouseover", function () {
                    cardDesc.style.display = "block";
                });

                // Добавим обработчик событий для ухода с карточки
                div.addEventListener("mouseout", function () {
                    cardDesc.style.display = "none";
                });
            }

            // Инициализация Masonry
            var masonry = new Masonry(container, {
                itemSelector: '.card',
                columnWidth: 300,
                fitWidth: true
            });

            let cards = document.querySelectorAll(".card");
            for (let i = 0; i < cards.length; i++) {
                cards[i].addEventListener("click", function () {
                    window.location.replace("/image/" + cards[i].id);
                    console.log(cards[i]);
                });
            }
            for (let i = 0; i < cards.length; i++) {
                cards[i].addEventListener("mouseover", function () {
                    cards[i].style.zIndex = "2"; // Устанавливаем более высокий z-index при наведении
                });

                cards[i].addEventListener("mouseout", function () {
                    cards[i].style.zIndex = "1"; // Восстанавливаем обычный z-index при уходе
                });

                cards[i].addEventListener("click", function () {
                    window.location.replace("/image/" + cards[i].id);
                    console.log(cards[i]);
                });
            }
        });
})();

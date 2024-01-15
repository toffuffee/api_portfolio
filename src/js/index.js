(function () {
    fetch('/api/images')
        .then((response) => {
            return response.json();
        })
        .then((myjson) => {
            let container = document.getElementById("images");
            for (let key in myjson) {
                let div = document.createElement("div");
                let img = document.createElement("div");
                let divContent = document.createElement("div");
                let cardTitle = document.createElement("div");
                let cardPrice = document.createElement("div");

                img.classList.add("image")
                div.classList.add("card");
                div.setAttribute("id", myjson[key].id)
                divContent.classList.add("card-content");
                cardTitle.classList.add("card-title");
                cardPrice.classList.add("card-price");

                cardTitle.innerHTML = myjson[key].image_name;
                cardPrice.innerHTML = myjson[key].image_country;
                img.style = `background-image: url(${myjson[key].image})`;

                container.appendChild(div);
                div.appendChild(img);
                div.appendChild(divContent);
                divContent.appendChild(cardTitle);
                divContent.appendChild(cardPrice);
            }
            let cards = document.querySelectorAll(".card");
            for (let i = 0; i < cards.length; i++) {
                cards[i].addEventListener("click", function () {
                    window.location.replace("/image/" + cards[i].id);
                    console.log(cards[i]);
                })
            }
        });
})();

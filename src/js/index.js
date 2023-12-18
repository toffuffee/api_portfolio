(function () {
    fetch('/api/products')
        .then((response) => {
            return response.json();
        })
        .then((myjson) => {
            let container = document.querySelector(".container");
            for (let key in myjson) {
                let div = document.createElement("div");
                let img = document.createElement("img");
                let divContent = document.createElement("div");
                let cardTitle = document.createElement("div");
                let cardDescription = document.createElement("p");
                let cardPrice = document.createElement("div");
                let btn = document.createElement("a");

                div.classList.add("card");
                div.setAttribute("id", myjson[key].id)
                divContent.classList.add("card-content");
                cardTitle.classList.add("card-title");
                cardDescription.classList.add("card-description");
                cardPrice.classList.add("card-price");
                btn.classList.add("btn");

                cardTitle.innerHTML = myjson[key].name;
                cardDescription.innerHTML = myjson[key].description;
                cardPrice.innerHTML = myjson[key].cost;
                btn.innerHTML = "В корзину";
                btn.style = "cursor: pointer;";
                img.src = myjson[key].image;

                container.appendChild(div);
                div.appendChild(img);
                div.appendChild(divContent);
                divContent.appendChild(cardTitle);
                divContent.appendChild(cardDescription);
                divContent.appendChild(cardPrice);
                divContent.appendChild(btn);

                console.log(myjson[key])
                console.log(myjson[key].image)
            }
        });
})()
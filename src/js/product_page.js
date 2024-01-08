(function () {
    fetch('/api/products')
        .then((response) => {
            return response.json();
        })
        .then((myjson) => {
            let path = window.location.href;
            let productId = new URL(path).pathname.split('/').pop();
            productId = parseInt(productId, 10);
            let productWithId = myjson.find(product => product.id === productId);
            if (productWithId) {
                document.querySelector(".name").innerHTML = productWithId.name;
                document.querySelector(".desc").innerHTML = productWithId.description;
                document.querySelector(".cost").innerHTML = productWithId.cost;
                document.querySelector(".img-product").src = productWithId.image;
            }
            else {
                alert("Такого продукта нет!")
            }

            console.log(productWithId);
        });
})();

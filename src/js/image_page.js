(function () {
    fetch('/api/images')
        .then((response) => {
            return response.json();
        })
        .then((myjson) => {
            let path = window.location.href;
            let productId = new URL(path).pathname.split('/').pop();
            productId = parseInt(productId, 10);
            let productWithId = myjson.find(product => product.id === productId);
            if (productWithId) {
                document.querySelector(".image-name").innerHTML = productWithId.image_name;
                document.querySelector(".image-desc").innerHTML = productWithId.image_desc;
                document.querySelector(".image-country").innerHTML = productWithId.image_country;
                document.querySelector(".image").src = productWithId.image;
            }
            else {
                alert("Такого продукта нет!")
            }

            console.log(productWithId);
        });
})();

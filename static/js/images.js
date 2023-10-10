(function () {
    lightbox.option({
        'resizeDuration': 300,
        'wrapAround': true,
        'albumLabel': "Изображение %1 / %2"
    })
    fetch('/api/photos')
        .then((response) => {
            return response.json();
        })
        .then((myjson) => {
            for (let key in myjson) {
                let link = document.createElement("a")
                link.href = '../static/db/images/' + key;
                link.setAttribute('data-lightbox', 'roadtrip')

                let image = document.createElement('img');
                image.classList.add('element-item')
                image.classList.add('persent-size')
                image.src = `data:image/jpg;base64,${myjson[key]}`;
                link.appendChild(image)

                document.querySelector(".elements-gride").appendChild(link)
            }
            jQuery(document).ready(function ($) {
                $('.elements-gride').masonry({
                    itemSelector: '.element-item',
                    columnWidth: '.persent-size',
                    percentPosition: true,
                });
            });

        });
})();
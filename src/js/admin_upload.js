(function () {
    const form = document.getElementById('imageUploadForm');
    const imageInput = document.getElementById('imageInput');
    const imageNameInput = document.getElementById('imageName');
    const imageDescTextarea = document.getElementById('imageDesc');
    const imageCountryInput = document.getElementById('imageCountry');

    form.addEventListener('submit', function (event) {
        event.preventDefault();
        const formData = new FormData();
        formData.append('image', imageInput.files[0]);
        formData.append('image_name', imageNameInput.value);
        formData.append('image_desc', imageDescTextarea.value);
        formData.append('image_country', imageCountryInput.value);
        console.log(formData)
        uploadImage(formData);
    });

    async function uploadImage(formData) {
        const url = '/api/upload_image';

        try {
            const response = await fetch(url, {
                method: 'POST',
                body: formData,
            });

            if (response.ok) {
                const result = await response.json();
                window.location.href = "/"
                console.log(result);
            } else {
                console.error('Ошибка при отправке изображения на сервер');
            }
        } catch (error) {
            console.error('Ошибка:', error);
        }
    }
})()
(function () {
    console.log("blog")
    fetch('/api/blog')
        .then((response) => {
            return response.json();
        })
        .then((myjson) => {
            for (let key in myjson) {
                let postRedirect = document.createElement('a');
                postRedirect.classList.add('post-redirect')
                postRedirect.href = '/blog/' + key;
                document.querySelector(".blog").appendChild(postRedirect);

                let post = document.createElement('div');
                post.classList.add('post');
                postRedirect.appendChild(post);

                let title = document.createElement('div');
                title.classList.add('post-title');
                title.innerHTML = myjson[key]['title'];
                post.appendChild(title);

                let subtitle = document.createElement('div');
                subtitle.classList.add('post-subtitle');
                subtitle.innerHTML = myjson[key]['subtitle'];
                post.appendChild(subtitle)
            }
        })
})();
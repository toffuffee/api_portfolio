// (function () {
//     let url = new URL(document.URL)
//     let href = url.href
//     const segments = new URL(href).pathname.split('/');
//     const last = segments.pop() || segments.pop();
//     fetch("/api/blog/" + last)
//         .then((response) => {
//             return response.json();
//         })
//         .then((myjson) => {
//             if (Object.keys(myjson).length === 0) {
//                 document.title = "Error: 404";
//                 let divError = document.createElement('div');
//                 divError.classList.add('error');
//                 divError.innerHTML = "Error: 404<br>Post not founded!";
//                 document.querySelector('.container').appendChild(divError);
//             }
//             else {
//                 document.title = myjson[last]['title'];

//                 let divTitle = document.createElement('div');
//                 divTitle.classList.add('title');
//                 divTitle.innerHTML = myjson[last]['title'];

//                 let divSubtitle = document.createElement('div');
//                 divSubtitle.classList.add('subtitle');
//                 divSubtitle.innerHTML = myjson[last]['subtitle'];

//                 let divContent = document.createElement('div');
//                 divContent.classList.add('content');
//                 divContent.innerHTML = myjson[last]['content'];

//                 document.querySelector('.post').appendChild(divTitle);
//                 document.querySelector('.post').appendChild(divSubtitle);
//                 document.querySelector('.post').appendChild(divContent);
//             }

//         });
// })();
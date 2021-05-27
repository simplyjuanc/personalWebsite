if ('attachShadow' in document.createElement('div')) {
    templateContent = document.querySelector('template').content;
    article = document.querySelector('article').cloneNode(true);
    article.querySelectorAll('*[id]').forEach((ele) => { ele.removeAttribute('id') });
    article.attachShadow({ mode: 'closed' }).appendChild(templateContent.cloneNode(true));
    document.querySelector('#toc').appendChild(article);
} else
    console.warn('attachShadow not supported');
async function getName () {
    const response = await fetch('https://swapi-api.hbtn.io/api/films/?format=json');
    const nameCollect = await response.json();
    const nameList = document.getElementById('list_movies');


    nameCollect.results.forEach(function (title) {
        const li = document.createElement('li');
        li.textContent = title.title;
        nameList.appendChild(li);
    });
}

getName();
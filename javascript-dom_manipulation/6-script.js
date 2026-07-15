async function getName () {
    const response = await fetch('https://swapi-api.hbtn.io/api/people/5/?format=json');
    const nameCollect = await response.json();
    document.getElementById('character').innerHTML = nameCollect.name;
}

getName();
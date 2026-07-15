async function translate() {
    const response = await fetch('https://hellosalut.stefanbohacek.com/?lang=fr');
    const transCollect = await response.json();
    document.getElementById('hello').innerHTML = transCollect.hello
}

translate();
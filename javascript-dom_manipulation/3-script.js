#!/usr/bin/node

document.getElementById('toggle_header').onclick = function () {
  const header = document.querySelector('header');
  let colour;

  if (header.classList.contains('red')) {
    colour = 'green';
  } else {
    colour = 'red';
  }

  header.classList.remove('red', 'green');
  header.classList.add(colour);
};
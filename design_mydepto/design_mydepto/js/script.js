let menu = document.querySelector('.header .menu');

document.querySelector('#menu-btn').onclick = () =>{
   menu.classList.toggle('active');
}

window.onscroll = () =>{
   menu.classList.remove('active');
}

document.querySelectorAll('input[type="number"]').forEach(inputNumber => {
   inputNumber.oninput = () =>{
      if(inputNumber.value.length > inputNumber.maxLength) inputNumber.value = inputNumber.value.slice(0, inputNumber.maxLength);
   };
});

document.querySelectorAll('.view-property .details .thumb .small-images img').forEach(images =>{
   images.onclick = () =>{
      src = images.getAttribute('src');
      document.querySelector('.view-property .details .thumb .big-image img').src = src;
   }
});

document.querySelectorAll('.faq .box-container .box h3').forEach(headings =>{
   headings.onclick = () =>{
      headings.parentElement.classList.toggle('active');
   }
});

document.addEventListener('DOMContentLoaded', function() {
   const favoriteListings = document.querySelector('.favorite-listings');

   // Aquí se puede agregar lógica para cargar y mostrar los departamentos favoritos desde una fuente de datos (como una API o una base de datos)
   const departamentosFavoritos = [
       {
           id: 1,
           title: 'Apartamento de Lujo en el Centro',
           image: 'img/pile 3.jpg',
           price: '$2000/mes'
       },
       {
           id: 2,
           title: 'Penthouse con Vista al Mar',
           image: 'img/apartamento2.jpg',
           price: '$3000/mes'
       },
       {
           id: 3,
           title: 'Loft Moderno en la Ciudad',
           image: 'img/apartamento3.jpg',
           price: '$2500/mes'
       }
   ];

   departamentosFavoritos.forEach(departamento => {
       const listingDiv = document.createElement('div');
       listingDiv.classList.add('favorite-listing');

       const image = document.createElement('img');
       image.src = departamento.image;
       image.alt = departamento.title;

       const title = document.createElement('h2');
       title.textContent = departamento.title;

       const price = document.createElement('p');
       price.textContent = `Precio: ${departamento.price}`;

       listingDiv.appendChild(image);
       listingDiv.appendChild(title);
      listingDiv.appendChild(price);

      favoriteListings.appendChild(listingDiv);
   });
});



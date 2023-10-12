 // Variables para el manejo de la paginación
 const itemsPerPage = 5; // Cambia esto al número deseado de elementos por página
 const paginationList = document.getElementById('pagination-list');
 const tableBody = document.getElementById('order-table-body');
 const ordersData = []; // Aquí se almacenarán todos los datos de pedidos
 let currentPage = 1;

 // Función para cargar y mostrar los datos de pedidos
 function loadOrderData(pageNumber) {
     const startIndex = (pageNumber - 1) * itemsPerPage;
     const endIndex = startIndex + itemsPerPage;
     const ordersToDisplay = ordersData.slice(startIndex, endIndex);

     // Limpiar la tabla antes de cargar nuevos datos
     tableBody.innerHTML = '';

     // Iterar a través de los datos y crear las filas de la tabla
     ordersToDisplay.forEach(order => {
         const row = tableBody.insertRow();
         row.insertCell(0).textContent = order.table;
         row.insertCell(1).textContent = order.nameFood;
         row.insertCell(2).textContent = order.quantity;
         row.insertCell(3).textContent = order.description;
         row.insertCell(4).textContent = new Date(order.date).toLocaleDateString();
         row.insertCell(5).textContent = `$${order.total}`;
         row.insertCell(6).textContent = order.served ? 'Served' : 'Pending';
     });
 }

 // Llama a loadOrderData con la página inicial (por ejemplo, 1)
 loadOrderData(currentPage);

 // Función para crear elementos de paginación
 function createPagination(totalPages) {
     paginationList.innerHTML = '';

     if (currentPage > 1) {
         createPaginationItem('Previous', currentPage - 1);
     }

     for (let i = 1; i <= totalPages; i++) {
         createPaginationItem(i, i);
     }

     if (currentPage < totalPages) {
         createPaginationItem('Next', currentPage + 1);
     }
 }

 // Función para crear un elemento de paginación
 function createPaginationItem(text, page) {
     const li = document.createElement('li');
     li.classList.add('page-item');
     if (page === currentPage) {
         li.classList.add('active');
     }

     const a = document.createElement('a');
     a.href = '#';
     a.classList.add('page-link');
     a.textContent = text;
     li.appendChild(a);

     // Agrega un manejador de eventos para cargar los datos de la página correspondiente
     a.addEventListener('click', () => {
         if (page !== currentPage) {
             currentPage = page;
             loadOrderData(currentPage);
             createPagination(Math.ceil(ordersData.length / itemsPerPage));
         }
     });

     paginationList.appendChild(li);
 }

 // Actualiza los datos de pedidos
 function updateOrderData() {
     // Hacer una solicitud para obtener los datos de pedidos
     fetch('/get_orders')
         .then(response => response.json())
         .then(data => {
             ordersData.length = 0; // Limpia los datos existentes
             ordersData.push(...data);
             createPagination(Math.ceil(ordersData.length / itemsPerPage));

             // Cargar la primera página de datos
             loadOrderData(currentPage);
         })
         .catch(error => {
             console.error('Error al obtener los datos de pedidos:', error);
         });
 }

 // Llama a updateOrderData una vez al cargar la página
 updateOrderData();

 // Actualizar los datos de pedidos cada 10 segundos (puedes ajustar el intervalo según tus necesidades)
 setInterval(updateOrderData, 10000);
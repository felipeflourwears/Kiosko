 // Actualiza los datos de pedidos
 function updateOrderData() {
    // Hacer una solicitud para obtener los datos de pedidos
    fetch('/get_orders_all')
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
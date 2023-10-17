document.getElementById('search-icon').addEventListener('click', function() {
    let searchTerm = document.querySelector('.search-product').value;
    redirectToSearchPage(searchTerm);
});

document.getElementById('search-input').addEventListener('keyup', function(event) {
    if (event.key === 'Enter') {
        let searchTerm = document.querySelector('.search-product').value;
        redirectToSearchPage(searchTerm);
    }
});

function redirectToSearchPage(searchTerm) {
    window.location.href = `/products?search=${searchTerm}`;
}

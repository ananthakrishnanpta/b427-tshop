const productSection = document.querySelector('#product-section');

productSection.addEventListener('click', async function (event){
    const btn = event.target;
    if (btn.classList.contains('add-to-cart')){
        let productId;
        const product_card = btn.closest('.product-card');

        productId = product_card.dataset.productId;
        alert(productId);
    }

})
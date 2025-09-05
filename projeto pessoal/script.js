let cart = [];
let total = 0;

function addToCart(button) {
  const productElement = button.closest('.product');
  const name = productElement.getAttribute('data-name');
  const price = parseFloat(productElement.getAttribute('data-price'));

  cart.push({ name, price });
  total += price;

  document.getElementById('cart-count').innerText = cart.length;
  document.getElementById('cart-total').innerText = total.toFixed(2);
}

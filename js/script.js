const cupcakes = [
    {
        name: "Cupcake de Morango",
        price: 8.99,
    },
    {
        name: "Cupcake de Chocolate",
        price: 8.99,
    },
    {
        name: "Cupcake de Baunilha",
        price: 7.99,
    },
    {
        name: "Cupcake de Caramelo",
        price: 7.99,
    },
    {
        name: "Cupcake de Doce de Leite",
        price: 7.99,
    },
];

document.addEventListener("DOMContentLoaded", function () {
    const orderList = document.getElementById("order-list");
    const totalPrice = document.getElementById("total-price");
    const checkoutButton = document.getElementById("checkout-button");
    const removeItemButton = document.getElementById("remove-item-button");

    cupcakes.forEach((cupcake, index) => {
        const orderButton = document.querySelectorAll(".order-button")[index];

        orderButton.addEventListener("click", () => {
            const listItem = document.createElement("li");
            listItem.textContent = cupcake.name + " - R$ " + cupcake.price.toFixed(2);
            orderList.appendChild(listItem);

            const currentTotal = parseFloat(totalPrice.textContent);
            totalPrice.textContent = (currentTotal + cupcake.price).toFixed(2);
        });
    });

    checkoutButton.addEventListener("click", () => {
        orderList.innerHTML = "";
        totalPrice.textContent = "0.00";
        window.location.href = "login.html"; // Redirecionar para a página "login.html"
    });
});

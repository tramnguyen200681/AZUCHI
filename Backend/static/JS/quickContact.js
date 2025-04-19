// Create container for Zalo and Call buttons
const floatingButtons = document.createElement("div");
floatingButtons.classList.add("floating-buttons");

floatingButtons.innerHTML = `
    <a href="https://zalo.me/0903827465" target="_blank" class="button zalo">
        <img src="${zaloImg}" alt="Zalo">
    </a>
    <a href="tel:0903827465" class="button call">
        <img src="${phoneImg}" alt="Gọi điện">
    </a>
`;

// Add it in the end of the body
document.body.appendChild(floatingButtons);

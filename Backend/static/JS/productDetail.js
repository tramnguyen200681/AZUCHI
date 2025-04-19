const zoomContainer = document.querySelector('.zoom-container');
const zoomImage = document.getElementById('zoom-image');

zoomContainer.addEventListener('mousemove', function(e) {
    const bounds = zoomContainer.getBoundingClientRect();
    const x = ((e.clientX - bounds.left) / bounds.width) * 100;
    const y = ((e.clientY - bounds.top) / bounds.height) * 100;

    zoomImage.style.transformOrigin = `${x}% ${y}%`;
    zoomImage.style.transform = 'scale(2)';
});

zoomContainer.addEventListener('mouseleave', function () {
    zoomImage.style.transform = 'scale(1)';
});



function showTab(tabId, event) {
    const tabs = document.querySelectorAll('.tab-content');
    const buttons = document.querySelectorAll('.tab-btn');
  
    tabs.forEach(tab => {
      tab.classList.remove('active');
    });
  
    buttons.forEach(btn => {
      btn.classList.remove('active');
    });
  
    document.getElementById(tabId).classList.add('active');
    event.target.classList.add('active');
  }


// ===== Price update based on size =====
let selectedWidth = null;
let selectedHeight = null;

document.addEventListener("DOMContentLoaded", () => {
  const widthBtns = document.querySelectorAll(".size-badge.width");
  const heightBtns = document.querySelectorAll(".size-badge.height");

  widthBtns.forEach(btn => {
      btn.addEventListener("click", () => {
          widthBtns.forEach(b => b.classList.remove("selected"));
          btn.classList.add("selected");
          selectedWidth = btn.dataset.width;
          updatePrice();
      });
  });

  heightBtns.forEach(btn => {
      btn.addEventListener("click", () => {
          heightBtns.forEach(b => b.classList.remove("selected"));
          btn.classList.add("selected");
          selectedHeight = btn.dataset.height;
          updatePrice();
      });
  });
});

function updatePrice() {
  const key = `${selectedWidth}x${selectedHeight}`;
  const price = priceMap[key]; // priceMap được truyền từ template

  const priceEl = document.getElementById("dynamic-price");
  if (price) {
      priceEl.textContent = `${parseInt(price).toLocaleString()} đ`;
  } else {
      priceEl.textContent = "Kích thước không khả dụng";
  }
}

  
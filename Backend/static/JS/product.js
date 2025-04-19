
// document.addEventListener("DOMContentLoaded", function () {
//     // --- DROPDOWN SORT ---
//     const sortSelect = document.getElementById('sort');

//     if (sortSelect) {
//         sortSelect.addEventListener('change', function () {
//             const selectedSort = this.value;
//             const url = new URL(window.location.href);
//             url.searchParams.set('sort', selectedSort);
//             window.location.href = url.toString();
//         });
//     }

//     // --- RANGE KÉO 2 ĐẦU GIÁ ---
//     const rangeMin = document.querySelector(".range-min");
//     const rangeMax = document.querySelector(".range-max");
//     const display = document.getElementById("price-display");
//     const progress = document.querySelector(".slider .progress");

//     let priceGap = 50000;

//     function updatePriceDisplay(e) {
//         let minVal = parseInt(rangeMin.value);
//         let maxVal = parseInt(rangeMax.value);

//         if (maxVal - minVal < priceGap) {
//             if (e.target === rangeMin) {
//                 rangeMin.value = maxVal - priceGap;
//             } else {
//                 rangeMax.value = minVal + priceGap;
//             }
//         } else {
//             display.textContent = `${minVal.toLocaleString()}đ - ${maxVal.toLocaleString()}đ`;
//             progress.style.left = (minVal / parseInt(rangeMax.max)) * 100 + "%";
//             progress.style.right = 100 - (maxVal / parseInt(rangeMax.max)) * 100 + "%";
//         }
//     }

//     if (rangeMin && rangeMax && display && progress) {
//         rangeMin.addEventListener("input", updatePriceDisplay);
//         rangeMax.addEventListener("input", updatePriceDisplay);
//         updatePriceDisplay({ target: rangeMax }); // hiển thị lúc đầu
//     }
// });


// 1) Catalog

// 2) Min_Max
const inputMin = document.querySelector(".input-min");
const inputMax = document.querySelector(".input-max");
const priceGap = 50000;

inputMin.addEventListener("input", () => {
  let minVal = parseInt(inputMin.value);
  let maxVal = parseInt(inputMax.value);

  if (minVal + priceGap > maxVal) {
    inputMax.value = minVal + priceGap;
  }

  // update min for max input
  inputMax.min = minVal + priceGap;
});

inputMax.addEventListener("input", () => {
  let minVal = parseInt(inputMin.value);
  let maxVal = parseInt(inputMax.value);

  if (maxVal - priceGap < minVal) {
    inputMin.value = maxVal - priceGap;
  }

  // update max for min input
  inputMin.max = maxVal - priceGap;
});
